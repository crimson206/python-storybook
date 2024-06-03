from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from python_storybook.core import StoryHub
from python_storybook.autodocs import AutoDocsAPI, AutoDocs
from typing import List
from pydantic import BaseModel

app = FastAPI()


class Titles(BaseModel):
    body: List[str]


class AutoDocsInput(BaseModel):
    title: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=[
        "*"
    ],
    allow_headers=["*"],
)


@app.get("/")
async def welcome():
    return {"message": "Welcome to the Python Storybook!"}


@app.get("/get_titles", response_model=Titles)
async def get_titles():
    try:
        titles = StoryHub.get_titles()
        return Titles(body=titles)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate_auto_docs", response_model=AutoDocs)
async def generate_auto_docs(input_data: AutoDocsInput):
    try:
        stories = AutoDocsAPI.generate_auto_docs(input_data.title)
        return stories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
