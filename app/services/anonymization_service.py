from app.schemas.report_schema import ReportRequest, ReportAnonymizedResponse
from app.ai_agents.graph import orquestrador

class AnonymizationService:
    async def process_report(self, payload: ReportRequest) -> ReportAnonymizedResponse:

        estado_inicial = {
            "title_original": payload.title,
            "description_original": payload.description,
            "tentativas": 0,
            "aprovado": False
        }
        
        resultado = await orquestrador.ainvoke(estado_inicial)
        
        return ReportAnonymizedResponse(
            report_id=payload.report_id,
            anonymized_title=resultado["title_anonimizado"],
            anonymized_description=resultado["description_anonimizada"]
        )

anonymization_service = AnonymizationService()