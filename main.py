from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from sentencesplitter import split_sentences

# pip install fastapi[all]

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


class Sentences(BaseModel):
    sentences: list[str]


@app.post('/sentence-split')
def read_item(sentences: Sentences):
    return {'sentences': split_sentences(sentences.sentences)}
