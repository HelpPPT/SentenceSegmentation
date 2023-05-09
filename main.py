from fastapi import FastAPI
from pydantic import BaseModel

from sentencesplitter import split_sentences

# start dev server with `uvicorn main:app --reload`
# start prod server with `uvicorn main:app`
app = FastAPI()


class Sentences(BaseModel):
    sentences: list[str]


@app.post("/sentence-split")
def read_item(sentences: Sentences):
    return {"sentences": split_sentences(sentences.sentences)}
