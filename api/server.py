from fastapi import FastAPI
from pydantic import BaseModel
from norm_engine import NormEngine, ResourceSignal

app = FastAPI(title="FDL Resource Norm API")
eng = NormEngine()

class NormRequest(BaseModel):
    type: str
    current: float
    expected: float
    context: str = "default"

@app.post("/regulate")
def regulate(req: NormRequest):
    # naive regulation recommendation
    delta = req.current - req.expected
    if delta <= 0:
        advice = "OK: within norm"
    elif delta <= 0.1 * req.expected:
        advice = "Slightly above norm: optimize schedule"
    else:
        advice = "Norm exceeded: throttle or reallocate"
    return {"status": "ok", "delta": delta, "advice": advice}

@app.get("/norms/{resource}/current")
def get_norm(resource: str):
    # demo: return placeholder norm
    return {"resource": resource, "norm_value": 100.0, "params": {"alpha": 0.6, "beta": 1.2, "z": 1.65}}
