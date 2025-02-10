from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# 允许前端访问的源（origin）
origins = [
    "http://localhost:5173",  # 你的 Vite 前端地址
    "http://127.0.0.1:5173"   # 可能的本地变体
]

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Initial link ...")
    yield
    print(f"user service:{__file__} shutdown ... ...")


app = FastAPI(
    title="MS RedNote Service",
    version="1.0.0",
    reload=True,
    lifespan=lifespan)

# 启用 CORS 让前端访问后端
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许的前端地址
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法（GET, POST, PUT, DELETE）
    allow_headers=["*"],  # 允许所有请求头
)


@app.post("/api1_red_note_sharing")
async def api1_red_note_sharing(sharing_link, style, max_words, token=None):
    print("server has get sharing link:", sharing_link)
    # todo : invoke LLM api
    # res = from LLm
    return {"code": 1, "message": "success"}

@app.post("/api1_red_note_rewrite")
async def api1_red_note_copy_rewrite(content, style, max_words, token=None):
    print("server has get copy:", content)
    return {"code": 1, "message": "success"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
