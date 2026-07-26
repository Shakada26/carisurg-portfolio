"""Sanity check (a): data cleaning produces the expected schema.

Uses a tiny synthetic frame so it runs with no data file and no network.
"""
import numpy as np
import pandas as pd

from src.data import clean_data, select_features, TARGET, VITALS


def _synthetic_raw(n: int = 60) -> pd.DataFrame:
    rng = np.random.default_rng(0)
    return pd.DataFrame({
        "triage_vital_hr": rng.integers(50, 130, n).astype(float),
        "triage_vital_sbp": rng.integers(90, 180, n).astype(float),
        "triage_vital_dbp": rng.integers(50, 110, n).astype(float),
        "triage_vital_rr": rng.integers(10, 30, n).astype(float),
        "triage_vital_o2": rng.integers(85, 100, n).astype(float),
        "triage_vital_temp": rng.uniform(97, 103, n),
        "triage_glucose": rng.integers(70, 200, n).astype(float),
        "age": rng.integers(18, 90, n),
        "gender": rng.choice(["M", "female", "f", "MALE"], n),
        "ethnicity": rng.choice(["A", "B"], n),
        "race": rng.choice(["X", "Y"], n),
        "cc_chest_pain": rng.integers(0, 2, n),
        "disposition": rng.choice(["admit", "discharge"], n),
        "esi": rng.choice([1, 2, 3, 4, 5, 9], n),
    })


def test_clean_data_schema():
    clean = clean_data(_synthetic_raw())
    assert TARGET in clean.columns
    assert clean[TARGET].dtype.kind in "iu"
    assert set(clean[TARGET].unique()).issubset({1, 2, 3, 4, 5})
    for col in VITALS:
        assert col in clean.columns
        assert clean[col].isna().sum() == 0
    assert set(clean["gender"].unique()).issubset({0, 1})


def test_select_features_drops_leakage():
    clean = clean_data(_synthetic_raw())
    X, y, names = select_features(clean)
    assert "disposition" not in names
    assert TARGET not in names
    assert "cc_chest_pain" in names
    assert len(X) == len(y)