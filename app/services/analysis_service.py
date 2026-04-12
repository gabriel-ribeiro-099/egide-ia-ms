import asyncio
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from app.core.config import settings
from app.schemas.analysis_schema import AnalysisRequest, AnalysisResponse, ReportCategory, ReportRisk
from app.ai_agents.prompts import CATEGORY_SYSTEM_PROMPT, RISK_SYSTEM_PROMPT

class CategoryOutput(BaseModel):
    category: ReportCategory

class RiskOutput(BaseModel):
    risk_level: ReportRisk

class AnalysisService:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=0.1
        )
        
    def _montar_mensagem_multimodal(self, payload: AnalysisRequest, system_prompt: str) -> list:
        conteudo = [{"type": "text", "text": f"{system_prompt}\n\nTÍTULO: {payload.title}\nDESCRIÇÃO: {payload.description}"}]
        
        for f in payload.files:
            conteudo.append({
                "type": "image_url",
                "image_url": {"url": f"data:{f.mime_type};base64,{f.base64_data}"}
            })
            
        return [HumanMessage(content=conteudo)]

    async def _analisar_categoria(self, mensagens: list) -> CategoryOutput:
        llm_cat = self.llm.with_structured_output(CategoryOutput)
        return await llm_cat.ainvoke(mensagens)

    async def _analisar_risco(self, mensagens: list) -> RiskOutput:
        llm_risk = self.llm.with_structured_output(RiskOutput)
        return await llm_risk.ainvoke(mensagens)

    async def analyze_report(self, payload: AnalysisRequest) -> AnalysisResponse:
        msg_categoria = self._montar_mensagem_multimodal(payload, CATEGORY_SYSTEM_PROMPT)
        msg_risco = self._montar_mensagem_multimodal(payload, RISK_SYSTEM_PROMPT)
        
        resultado_cat, resultado_risco = await asyncio.gather(
            self._analisar_categoria(msg_categoria),
            self._analisar_risco(msg_risco)
        )
        
        return AnalysisResponse(
            report_id=payload.report_id,
            category=resultado_cat.category,
            risk_level=resultado_risco.risk_level
        )

analysis_service = AnalysisService()