from fastapi import APIRouter, Depends
from app.api.dependencies import verificar_api_key
from app.schemas.analysis_schema import AnalysisRequest, AnalysisResponse
from app.services.analysis_service import analysis_service

router = APIRouter()

@router.post("/analisar", response_model=AnalysisResponse, dependencies=[Depends(verificar_api_key)])
async def analisar_risco_categoria(payload: AnalysisRequest):
    return await analysis_service.analyze_report(payload)