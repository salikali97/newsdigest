import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
from application import app



if __name__ == "__main__":
    uvicorn.run(
        app, host="localhost", reload=False, port=8000
    )
