from fastapi import FastAPI
import os, asyncio

app = FastAPI(title="Hermes Ari AI Cloud Agent")

@app.get("/")
@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "Hermes Ari AI Cloud Agent",
        "council": "Multi-Model Groq & Gemini",
        "cloud": "Render Singapore Node"
    }

@app.on_event("startup")
async def startup_event():
    print("Hermes Ari AI Agent starting up...")
    try:
        import autonomous_cloud_agent
        asyncio.create_task(autonomous_cloud_agent.main())
    except Exception as e:
        print("Startup warning:", e)
