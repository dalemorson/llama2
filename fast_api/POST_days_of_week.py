import uvicorn
from fastapi import Request, FastAPI
from llama_cpp import Llama

app = FastAPI()
LLM = Llama(model_path="../models/llama-2-7b-chat.Q8_0.gguf")

@app.get("/")
async def index():
   return {"message": "Hello World"}

@app.get("/health")
async def health():
   return {"Health": "Up"}

@app.post("/ask")
async def prompt(req: Request):
   body = await req.json()
   prompt = body['question']
   answer = LLM(prompt)["choices"][0]["text"]
   return {"answer": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)