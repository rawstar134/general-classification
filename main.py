import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from webScraping.NDTV.handler import trending_handler, page_handler
import json
import os
app = FastAPI()


@app.get("/pageNews")
async def NDTV_pageHandler():
    response = page_handler()
    return response


@app.get("/trendingNews")
async def NDTV_trendingHandler():
    response = trending_handler()

    return response


@app.get("/home")
async def homepage():
    print("Inside the home class")
    with open('index.html', 'r') as fh:
        data = fh.read()
    print(data)
    return HTMLResponse(content=data, status_code=200)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
