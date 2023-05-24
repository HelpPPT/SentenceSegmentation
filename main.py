from typing import List

from fastapi import FastAPI
from kss import split_sentences
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

# pip install "fastapi[all]"

# start dev server with `uvicorn main:app --reload`
# start prod server with `uvicorn --host 0.0.0.0 --port 8080 --workers 4 main:app`
app = FastAPI()

origins = [
    '*',
    # 'https://localhost',
    # 'https://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


class SlideText(BaseModel):
    slideId: str
    slideIndex: int
    text: str


class SlideTexts(BaseModel):
    slideTexts: List[SlideText]


@app.post('/sentence-split')
def read_item(slide_texts: SlideTexts) -> SlideTexts:
    kss_split_result: List[SlideText] = [
        SlideText(
            slideId=slideText.slideId,
            slideIndex=slideText.slideIndex,
            text=sentence
        )
        for slideText in slide_texts.slideTexts
        for sentence in split_sentences(slideText.text)
    ]
    return SlideTexts(slideTexts=kss_split_result)
