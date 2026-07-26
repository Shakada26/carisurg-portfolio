"""Model factory, training, and evaluation (Weeks 6-7). Nothing runs at import."""
from __future__ import annotations

from typing import Any, Dict, Optional

import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, f1_score, precision_score, recall_score,
)
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

_DEFAULTS: Dict[str, Dict[str, Any]] = {
    "dummy": {"strategy": "stratified", "random_state": 42},
    "logistic_regression": {"max_iter": 1000, "random_state": 42},
    "decision_tree": {"max_depth": 5, "random_state": 42},
    "random_forest": {
        "n_estimators": 300, "class_weight": "balanced",
        "random_state": 42, "n_jobs": -1,
    },
    "gradient_boosting": {
        "max_depth": 6, "learning_rate": 0.1, "max_iter": 300,
        "class_weight": "balanced", "random_state": 42,
    },
    "mlp": {
        "hidden_layer_sizes": (64, 32), "alpha": 1e-3,
        "max_iter": 500, "random_state": 42,
    },
}
_NEEDS_SCALING = {"logistic_regression", "mlp"}


def build_model(name: str, params: Optional[Dict[str, Any]] = None):
    """Return an untrained estimator (or Pipeline) for the given model name."""
    if name not in _DEFAULTS:
        raise ValueError(f"Unknown model '{name}'. Choose from {sorted(_DEFAULTS)}.")
    hp = {**_DEFAULTS[name], **(params or {})}
    builders = {
        "dummy": DummyClassifier,
        "logistic_regression": LogisticRegression,
        "decision_tree": DecisionTreeClassifier,
        "random_forest": RandomForestClassifier,
        "gradient_boosting": HistGradientBoostingClassifier,
        "mlp": MLPClassifier,
    }
    estimator = builders[name](**hp)
    if name in _NEEDS_SCALING:
        return make_pipeline(StandardScaler(), estimator)
    return estimator


def train_model(model, X_train: pd.DataFrame, y_train: pd.Series):
    """Fit model on the training data and return the fitted model."""
    model.fit(X_train, y_train)
    return model


def evaluate_model(
    model, X_test: pd.DataFrame, y_test: pd.Series, average: str = "macro"
) -> Dict[str, float]:
    """Score a fitted model: accuracy, precision, recall, f1 (macro), recall_esi1."""
    preds = model.predict(X_test)
    esi1 = recall_score(y_test, preds, labels=[1], average=None, zero_division=0)
    return {
        "accuracy": round(float(accuracy_score(y_test, preds)), 4),
        "precision": round(float(precision_score(y_test, preds, average=average, zero_division=0)), 4),
        "recall": round(float(recall_score(y_test, preds, average=average, zero_division=0)), 4),
        "f1": round(float(f1_score(y_test, preds, average=average, zero_division=0)), 4),
        "recall_esi1": round(float(esi1[0]) if len(esi1) else 0.0, 4),
    }