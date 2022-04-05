from typing import Literal
from pydantic import BaseModel, Field

IsCorrect = Literal[1, -1]

class Word(BaseModel):
    id: str
    word: str
    meaning: str
    book_name: str = Field("Basic Words 早稲田アカデミー")
    word_num: int
    is_correct: IsCorrect

class PostIsCorrectInput(BaseModel):
    id: str
    is_correct: IsCorrect