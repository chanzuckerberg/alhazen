# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_agent.ipynb.

# %% auto 0
__all__ = ['app', 'root']

# %% ../nbs/01_agent.ipynb 3
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}