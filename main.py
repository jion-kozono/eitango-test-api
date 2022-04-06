from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import word

app = FastAPI()

origins = [
    "http://localhost",
    "https://simple-eitango-test-app.web.app"
]

origin_regex = "http://localhost:.*"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=origin_regex,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(word.router)