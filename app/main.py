import os
import platform
import socket
import time

from fastapi import FastAPI

START_TIME = time.time()
APP_VERSION = os.getenv("APP_VERSION", "dev")

app = FastAPI(title="healthcheck-api", version=APP_VERSION)

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

@app.get("/info")
def info() -> dict:
    return {
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "uptime_seconds": round(time.time() - START_TIME, 1),
        "version": APP_VERSION
    }

