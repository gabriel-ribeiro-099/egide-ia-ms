from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api_router import api_router

def get_application() -> FastAPI:
    application = FastAPI(
        title="Égide.IA - Anonymization Service",
        description="Microsserviço multiagente para anonimização inteligente de denúncias.",
        version="1.0.0",
        docs_url="/docs", 
        redoc_url="/redoc"
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix="/api/v1")

    return application

app = get_application()

@app.get("/health", tags=["System"])
async def health_check():
    return {
        "status": "online", 
        "service": "Égide.IA NLP Engine", 
        "message": "Sistema operacional e aguardando manifestações."
    }