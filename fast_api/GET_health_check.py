import uvicorn
from fastapi import Request, FastAPI
app = FastAPI()

@app.get("/health")
async def health():
   return {"Health": "Up"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)