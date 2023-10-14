import uvicorn
from fastapi import FastAPI
from webScraping.NDTV.handler import handler
app = FastAPI()


@app.get("/")
async def index():
    handler()
    return {"status": "sucess"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
