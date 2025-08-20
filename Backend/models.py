from pydantic import BaseModel
from typing import List

class ComplianceReport(BaseModel):
    id: int
    cloud_provider: str
    service: str
    compliance_status: str
    last_checked: str
    issues: List[str]
