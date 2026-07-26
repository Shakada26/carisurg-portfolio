"""Train the pinned triage model from a single config file.

Usage: python scripts/train.py --config config.yaml
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import joblib

# Make 'src' importable when run from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src import data as data_mod
from src import features as feat_mod
from src import model as model_mod
from src.utils import load_config, set_seed, timed


def main(config_path: str) -> None:
    cfg = load_config(config_path)
    set_seed(cfg.get("seed", 42))

    df_raw = data_mod.load_raw_data(cfg["data"]["raw_path"])
    df = data_mod.clean_data(df_raw)

    X, y, feature_names = data_mod.select_features(
        df,
        drop_demographics=cfg["data"].get("drop_demographics", True),
        drop_admin=cfg["data"].get("drop_admin", True),
    )
    print(f"Loaded {len(df)} rows; {len(feature_names)} base features.")

    X_train, X_test, y_train, y_test = data_mod.split_data(
        X, y,
        test_size=cfg["data"].get("test_size", 0.2),
        seed=cfg.get("seed", 42),
    )

    if cfg["features"].get("add_clinical_features", True):
        X_train = feat_mod.add_clinical_features(X_train)
        X_test = feat_mod.add_clinical_features(X_test)
    if cfg["features"].get("add_demographics", False):
        X_train = feat_mod.add_demographics(X_train, df)
        X_test = feat_mod.add_demographics(X_test, df)

    mdl = model_mod.build_model(cfg["model"]["name"], cfg["model"].get("params"))
    with timed() as t:
        model_mod.train_model(mdl, X_train, y_train)
    print(f"Trained {cfg['model']['name']} in {t['elapsed_s']:.2f}s.")

    metrics = model_mod.evaluate_model(mdl, X_test, y_test)
    print("Test metrics:")
    for k, v in metrics.items():
        print(f"  {k:12s}: {v}")

    out_path = Path(cfg["output"]["model_path"])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(mdl, out_path)
    print(f"Saved model -> {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train the pinned triage model.")
    parser.add_argument("--config", default="config.yaml", help="Path to config.yaml")
    args = parser.parse_args()
    main(args.config)