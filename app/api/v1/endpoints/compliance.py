from fastapi import APIRouter, Depends
from app.api.dependencies import verificar_api_key
from app.schemas.report_schema import ReportRequest, ReportAnonymizedResponse
from app.services.anonymization_service import anonymization_service

router = APIRouter()

@router.post("/anonimizar", response_model=ReportAnonymizedResponse, dependencies=[Depends(verificar_api_key)])
async def anonimizar_manifestacao(payload: ReportRequest):

    return await anonymization_service.process_report(payload)