from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from mock_data import MOCK_RESOURCES, MOCK_SCANS, MOCK_INCIDENTS

app = FastAPI(title="Security Compliance Dashboard")

class Resource(BaseModel):
    id: str
    type: str
    name: str
    compliance_status: str

class ScanResult(BaseModel):
    id: str
    resource_id: str
    tool: str
    severity: str
    finding: str
    status: str

class Incident(BaseModel):
    id: str
    title: str
    status: str
    description: Optional[str] = None

@app.get("/resources", response_model=List[Resource])
def list_resources():
    return MOCK_RESOURCES

@app.get("/scans", response_model=List[ScanResult])
def list_scans():
    return MOCK_SCANS

@app.get("/incidents", response_model=List[Incident])
def list_incidents():
    return MOCK_INCIDENTS

@app.get("/report/summary")
def ai_report_summary():
    # Stub: Replace with OpenAI/Copilot integration if desired
    return {"summary": "All systems nominal. 2 critical findings. 1 open incident."}