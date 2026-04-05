from pydantic import BaseModel

class ReportRequest(BaseModel):
    report_id: int
    title: str
    description: str

class ReportAnonymizedResponse(BaseModel):
    report_id: int
    anonymized_title: str
    anonymized_description: str