from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

convo_history = []

class ChatRequest(BaseModel):
    text : str

@app.post("/chat")
async def chat(req: ChatRequest):
    user_msg = {"role":"user","content":req.text}
    convo_history.append(user_msg)
    
    payload = {
        "model": "qwen2-7b-instruct",
        "messages": convo_history,
        "stream": False
    }
    
    async with httpx.AsyncClient(timeout=60.0) as client:  # 60 seconds timeout
        response = await client.post(
          "http://host.docker.internal:1234/v1/chat/completions",
            headers={"Content-Type":"application/json"},
            json=payload,
        )
        res_json = response.json()
        
    llm_res = res_json["choices"][0]["message"]
    convo_history.append(llm_res)
    
    return {"response":llm_res["content"]}
