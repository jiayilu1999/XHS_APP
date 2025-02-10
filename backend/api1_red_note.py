from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
import uvicorn

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Initial link ...")
    yield
    print(f"user service:{__file__} shutdown ... ...")


app = FastAPI(
    title="MS RedNote Service",
    version="1.0.0",
    lifespan=lifespan)



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
