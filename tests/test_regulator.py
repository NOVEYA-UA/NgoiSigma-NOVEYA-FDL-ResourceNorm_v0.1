from norm_engine import NormEngine, ResourceSignal

def test_audit_triggers():
    eng = NormEngine()
    eng.ingest(ResourceSignal("X","energy","daily_consumption", 100,"t"))
    eng.ingest(ResourceSignal("X","energy","consumption", 125,"t"))
    out = eng.audit("X","energy")
    assert any(code.startswith("T1") for code,_ in out)
