import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator

from llama_index.llms import LlamaCPP
from llama_index.llms.llama_utils import messages_to_prompt, completion_to_prompt

llms = {}

@asynccontextmanager
async def lifespan(app: FastAPI):    
    # Make sure the model path is correct for your system!
    llms["llama"] = LlamaCPP(
        model_path="../models/llama-2-7b-chat.Q8_0.gguf", 
        temperature=0.1,
        max_new_tokens=256,
        # llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
        context_window=3900,
        # kwargs to pass to __call__()
        generate_kwargs={},
        # transform inputs into Llama2 format
        messages_to_prompt=messages_to_prompt,
        completion_to_prompt=completion_to_prompt,
        verbose=True,
    )
    yield    

app = FastAPI(lifespan=lifespan) 

def run_llm(question: str) -> AsyncGenerator:
    llm : LlamaCPP = llms["llama"]
    response_iter = llm.stream_complete(question)
    for response in response_iter:
        yield f"data: {response.delta}\n\n"

@app.get("/")
async def root(question: str) -> StreamingResponse:
    return StreamingResponse(run_llm(question), media_type="text/event-stream")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)