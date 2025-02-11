from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import auth, anomaly  # Added anomaly import
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from app.routes.anomaly import router as anomaly_router

templates = Jinja2Templates(directory="app/templates")

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    # masukkan URL yang ingin menggunakan service
    allow_origins=["http://127.0.0.1:8000/", "https://finalyze.up.railway.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directly serve the index.html at the root route
@app.get("/", response_class=HTMLResponse)
def landing_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Dashboard route
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# Anomaly detection dashboard route
@app.get("/anomaly-dashboard", response_class=HTMLResponse)
def anomaly_dashboard(request: Request):
    return templates.TemplateResponse("anomaly.html", {"request": request})

# Register routers
app.include_router(auth.router, prefix="/auth")
app.include_router(anomaly_router)
