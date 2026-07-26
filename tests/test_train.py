"""Sanity check (b): the pipeline runs end-to-end on ~50 rows.

A smoke test — proves the pieces connect, not that the model is good.
"""
import numpy as np
import pandas as pd

from src.data import clean_data, select_features, split_data
from src.features import add_clinical_features
from src.model import build_model, train_model, evaluate_model


def _synthetic_raw(n: int = 50) -> pd.DataFrame:
    rng = np.random.default_rng(1)
    return pd.DataFrame({
        "triage_vital_hr": rng.integers(50, 130, n).astype(float),
        "triage_vital_sbp": rng.integers(90, 180, n).astype(float),
        "triage_vital_dbp": rng.integers(50, 110, n).astype(float),
        "triage_vital_rr": rng.integers(10, 30, n).astype(float),
        "triage_vital_o2": rng.integers(85, 100, n).astype(float),
        "triage_vital_temp": rng.uniform(97, 103, n),
        "triage_glucose": rng.integers(70, 200, n).astype(float),
        "age": rng.integers(18, 90, n),
        "gender": rng.choice(["M", "F"], n),
        "cc_chest_pain": rng.integers(0, 2, n),
        "esi": rng.choice([2, 3], n),
    })


def test_training_smoke():
    df = clean_data(_synthetic_raw())
    X, y, _ = select_features(df)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.3, seed=42)
    X_train = add_clinical_features(X_train)
    X_test = add_clinical_features(X_test)

    model = build_model("gradient_boosting", {"max_iter": 20})
    train_model(model, X_train, y_train)
    metrics = evaluate_model(model, X_test, y_test)

    for key in ("accuracy", "precision", "recall", "f1", "recall_esi1"):
        assert key in metrics
        assert 0.0 <= metrics[key] <= 1.0