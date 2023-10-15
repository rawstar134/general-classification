import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from webScraping.NDTV.handler import handler
import json
import os
app = FastAPI()


@app.get("/")
async def index():
    response = handler()
    return response


@app.get("/home")
async  def homepage():
    with open('index.html','r') as fh:
        data = fh.read()
    return HTMLResponse(content=data,status_code=200)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
