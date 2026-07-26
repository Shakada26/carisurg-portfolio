"""Regenerate the model-selection results table (docs/model-selection.md).

Trains every model tried in Weeks 6-7 on the same split and writes a markdown
table of accuracy / precision / recall / F1 plus training & inference time.

Usage: python scripts/benchmark.py --config config.yaml
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src import data as data_mod
from src import features as feat_mod
from src import model as model_mod
from src.utils import load_config, set_seed, timed

MODELS = [
    ("Dummy (stratified)", "dummy", {}),
    ("Logistic Regression", "logistic_regression", {"max_iter": 1000}),
    ("Decision Tree", "decision_tree", {"max_depth": 5}),
    ("Random Forest", "random_forest", {"n_estimators": 300}),
    ("Gradient Boosting", "gradient_boosting", {"max_iter": 300, "max_depth": 6}),
    ("Small MLP", "mlp", {"hidden_layer_sizes": (64, 32)}),
]
WINNER = "Gradient Boosting"


def main(config_path: str) -> None:
    cfg = load_config(config_path)
    set_seed(cfg.get("seed", 42))

    df = data_mod.clean_data(data_mod.load_raw_data(cfg["data"]["raw_path"]))
    X, y, _ = data_mod.select_features(df)
    X_train, X_test, y_train, y_test = data_mod.split_data(
        X, y, test_size=cfg["data"]["test_size"], seed=cfg["seed"]
    )
    X_train = feat_mod.add_clinical_features(X_train)
    X_test = feat_mod.add_clinical_features(X_test)

    rows = []
    for label, name, params in MODELS:
        mdl = model_mod.build_model(name, params)
        with timed() as t_train:
            model_mod.train_model(mdl, X_train, y_train)
        t0 = time.perf_counter()
        m = model_mod.evaluate_model(mdl, X_test, y_test)
        infer_ms = (time.perf_counter() - t0) * 1000
        rows.append({
            "model": label, "params": _fmt_params(params),
            **m, "train_s": round(t_train["elapsed_s"], 2),
            "infer_ms": round(infer_ms, 1),
        })

    _write_markdown(rows, Path("docs/model-selection.md"))
    print("Wrote docs/model-selection.md")


def _fmt_params(params: dict) -> str:
    return ", ".join(f"{k}={v}" for k, v in params.items()) or "defaults"


def _write_markdown(rows, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    head = ("| Model | Key hyperparameters | Accuracy | Precision | Recall | "
            "F1 | Recall ESI-1 | Train (s) | Infer (ms) |")
    sep = "|" + "---|" * 9
    lines = [head, sep]
    for r in rows:
        star = " *WINNER*" if r["model"] == WINNER else ""
        lines.append(
            f"| {r['model']}{star} | {r['params']} | {r['accuracy']} | "
            f"{r['precision']} | {r['recall']} | {r['f1']} | {r['recall_esi1']} | "
            f"{r['train_s']} | {r['infer_ms']} |"
        )
    path.write_text("# Model-selection results\n\n" + "\n".join(lines) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmark all Week 6-7 models.")
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()
    main(args.config)