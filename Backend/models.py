from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
	id: int
	username: str
	email: str
	is_active: bool = True

class ComplianceCheck(BaseModel):
	id: int
	name: str
	description: Optional[str] = None
	passed: bool
	checked_at: str  # ISO datetime string

class Report(BaseModel):
	id: int
	user_id: int
	checks: List[ComplianceCheck]
	generated_at: str  # ISO datetime string
