"""Load, clean, and split the CariSurg triage dataset. Target: esi (1-5)."""
from __future__ import annotations

from typing import List, Tuple

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

TARGET: str = "esi"

VITALS: List[str] = [
    "triage_vital_hr", "triage_vital_sbp", "triage_vital_dbp", "triage_vital_rr",
    "triage_vital_o2", "triage_vital_temp", "triage_glucose",
]
DEMOGRAPHICS: List[str] = [
    "age", "gender", "ethnicity", "race", "lang", "religion",
    "maritalstatus", "employstatus", "insurance_status",
]
ADMIN: List[str] = [
    "dep_name", "arrivalmode", "arrivalmonth", "arrivalday", "arrivalhour_bin",
]
LEAKAGE: List[str] = ["disposition", "previousdispo"]


def load_raw_data(path: str) -> pd.DataFrame:
    """Read the raw triage CSV export from disk."""
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame, vitals: List[str] = VITALS) -> pd.DataFrame:
    """Turn the raw export into a modelling-ready table (Week 5 cleaning, compact)."""
    out = df.copy()
    out = out.drop(columns=[c for c in out.columns if c.startswith("Unnamed")],
                   errors="ignore")
    for col in vitals:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    out[TARGET] = pd.to_numeric(out[TARGET], errors="coerce")
    out = out[out[TARGET].isin([1, 2, 3, 4, 5])].copy()
    if "triage_vital_temp" in out.columns:
        bad_temp = (out["triage_vital_temp"] < 90) | (out["triage_vital_temp"] > 110)
        out.loc[bad_temp, "triage_vital_temp"] = np.nan
    if "triage_vital_o2" in out.columns:
        out.loc[out["triage_vital_o2"] > 100, "triage_vital_o2"] = np.nan
    if "gender" in out.columns:
        out["gender"] = (
            out["gender"].astype(str).str.strip().str.lower()
            .map({"male": 0, "m": 0, "female": 1, "f": 1})
        )
    for col in vitals + ["age", "gender"]:
        if col in out.columns:
            out[col] = out[col].fillna(out[col].median())
    out[TARGET] = out[TARGET].astype(int)
    return out


def select_features(
    df: pd.DataFrame,
    drop_demographics: bool = True,
    drop_admin: bool = True,
) -> Tuple[pd.DataFrame, pd.Series, List[str]]:
    """Split a cleaned table into features X and target y (excludes leakage)."""
    exclude = set(LEAKAGE)
    if drop_admin:
        exclude |= set(ADMIN)
    if drop_demographics:
        exclude |= set(DEMOGRAPHICS)
    feature_names = [c for c in df.columns if c != TARGET and c not in exclude]
    return df[feature_names], df[TARGET], feature_names


def split_data(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    seed: int = 42,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Stratified train/test split (reproduces the Week 6 split with seed=42)."""
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=seed)