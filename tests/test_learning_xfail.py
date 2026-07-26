"""Learning demonstration of the pytest xfail marker (not a core sanity check).

xfail = "expected to fail". It documents a known unmet target inside the test
suite: hitting an acceptable ESI-1 recall. The current best model does not reach
it, so this test is expected to fail. If a future model DOES reach the target,
pytest reports an unexpected pass (xpass), signalling the target is now met.
"""
import pytest


@pytest.mark.xfail(reason="Known limitation: ESI-1 recall target not yet met by any model")
def test_esi1_recall_meets_clinical_target():
    achieved_esi1_recall = 0.313  # best so far: Gradient Boosting, full dataset
    clinical_target = 0.80
    assert achieved_esi1_recall >= clinical_target