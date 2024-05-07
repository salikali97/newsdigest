from fastapi import FastAPI, Depends, Request,APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routes.newsaggregator import router as newsrouter


app = FastAPI()


# app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2Templates to load HTML templates
templates = Jinja2Templates(directory="templates")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins if origins not defined
    allow_credentials=True,  # Set to True if cookies or authorization headers are sent
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all HTTP headers
)


@app.get("/", response_class=HTMLResponse)
async def render_index(request: Request):
    # Pass the name of the HTML template file to the TemplateResponse constructor
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(newsrouter)