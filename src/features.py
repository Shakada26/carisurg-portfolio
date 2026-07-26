"""Feature engineering for the triage models (Week 7)."""
from __future__ import annotations

import pandas as pd


def add_clinical_features(data: pd.DataFrame) -> pd.DataFrame:
    """Add derived clinical features (ratios plus red-flag indicators)."""
    out = data.copy()
    out["shock_index"] = out["triage_vital_hr"] / out["triage_vital_sbp"]
    out["pulse_pressure"] = out["triage_vital_sbp"] - out["triage_vital_dbp"]
    out["spo2_rr_ratio"] = out["triage_vital_o2"] / out["triage_vital_rr"]
    out["is_tachypneic"] = (out["triage_vital_rr"] > 20).astype(int)
    out["is_hypoxic"] = (out["triage_vital_o2"] < 92).astype(int)
    out["is_febrile"] = (out["triage_vital_temp"] >= 100.4).astype(int)
    out["red_flag_count"] = out[["is_tachypneic", "is_hypoxic", "is_febrile"]].sum(axis=1)
    return out


def encode_demographics(df: pd.DataFrame) -> pd.DataFrame:
    """One-hot encode ethnicity and race from the cleaned table."""
    return pd.get_dummies(df[["ethnicity", "race"]], prefix=["eth", "race"], dtype=int)


def add_demographics(X_fe: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
    """Bolt encoded demographics onto an engineered feature frame (aligned by index)."""
    rows = X_fe.index
    extra = encode_demographics(df).loc[rows].copy()
    extra["age"] = df.loc[rows, "age"]
    extra["gender"] = df.loc[rows, "gender"]
    return pd.concat([X_fe, extra], axis=1)