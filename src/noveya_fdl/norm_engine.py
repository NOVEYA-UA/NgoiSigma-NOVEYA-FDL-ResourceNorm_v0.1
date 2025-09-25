from dataclasses import dataclass
from typing import Dict, List, Tuple
import math

@dataclass
class ResourceSignal:
    site_id: str
    resource: str  # e.g., "energy", "raw_material"
    metric: str    # e.g., "daily_consumption", "lead_time_var"
    value: float
    ts: str

@dataclass
class NormParams:
    alpha: float = 0.6
    beta: float = 1.2
    z: float = 1.65  # ≈95% service level

class NormEngine:
    def __init__(self, params: NormParams = NormParams()):
        self.params = params
        self.state: Dict[tuple, Dict[str, float]] = {}

    def ingest(self, s: ResourceSignal):
        key = (s.site_id, s.resource)
        if key not in self.state:
            self.state[key] = {}
        self.state[key][s.metric] = s.value

    def safe_stock(self, site_id: str, resource: str) -> float:
        st = self.state.get((site_id, resource), {})
        dc = st.get("daily_consumption", 0.0)
        ltv = st.get("lead_time_var", 0.0)
        return max(self.params.alpha * dc, self.params.beta * ltv)

    def reorder_point(self, avg_demand: float, lead_time: float, demand_std: float) -> float:
        return avg_demand * lead_time + self.params.z * demand_std * math.sqrt(max(lead_time, 0.0))

    def audit(self, site_id: str, resource: str) -> List[Tuple[str, float]]:
        st = self.state.get((site_id, resource), {})
        out: List[Tuple[str, float]] = []
        ss = self.safe_stock(site_id, resource)
        cons = st.get("consumption", st.get("daily_consumption", 0.0))
        norm = st.get("norm", ss)
        if cons > 1.10 * norm:
            out.append(("T1:throttle_supply", cons - norm))
        if st.get("lead_time_var", 0.0) > st.get("ltv_threshold", 1.0):
            out.append(("T2:reallocate_local", st.get("lead_time_var", 0.0)))
        return out

if __name__ == "__main__":
    eng = NormEngine()
    eng.ingest(ResourceSignal("OLVIA-PORT","energy","daily_consumption", 1200,"2025-09-25T10:00Z"))
    eng.ingest(ResourceSignal("OLVIA-PORT","energy","lead_time_var", 15,"2025-09-25T10:00Z"))
    eng.ingest(ResourceSignal("OLVIA-PORT","energy","ltv_threshold", 10,"2025-09-25T10:00Z"))
    eng.ingest(ResourceSignal("OLVIA-PORT","energy","consumption", 1500,"2025-09-25T10:00Z"))
    ss = eng.safe_stock("OLVIA-PORT","energy")
    print("safe_stock:", ss)
    print("audit:", eng.audit("OLVIA-PORT","energy"))
