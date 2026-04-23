import logging
from fastapi import APIRouter, Depends
from app.api.dependencies import verificar_api_key
from app.schemas.report_schema import ReportRequest, ReportAnonymizedResponse
from app.services.anonymization_service import anonymization_service

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/anonimizar", response_model=ReportAnonymizedResponse, dependencies=[Depends(verificar_api_key)])
async def anonimizar_manifestacao(payload: ReportRequest):
    resposta = await anonymization_service.process_report(payload)
    logger.info(
        "[/anonimizar] report_id=%s | title=%s | description=%s",
        resposta.report_id,
        resposta.anonymized_title,
        resposta.anonymized_description,
    )
    return resposta