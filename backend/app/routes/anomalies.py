#anomalies.py has the same pattern of insights.py -> goes to the service

from fastapi import APIRouter
from ..services import anomaly

router = APIRouter()

@router.get("/anomalies") 
def get_anomalies():
    return anomaly.dectect_anomalies()