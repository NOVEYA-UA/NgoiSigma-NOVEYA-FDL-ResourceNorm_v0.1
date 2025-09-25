from norm_engine import NormEngine, ResourceSignal

eng = NormEngine()
eng.ingest(ResourceSignal("PLANT-A","energy","daily_consumption", 900,"2025-09-25T10:00Z"))
eng.ingest(ResourceSignal("PLANT-A","energy","consumption", 1100,"2025-09-25T10:00Z"))
print("Audit:", eng.audit("PLANT-A","energy"))
