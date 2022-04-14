from gettext import translation
from typing import Literal, Optional
from pydantic import BaseModel, Field

IsCorrect = Literal[1, -1]

class Word(BaseModel):
    id: str
    word: str
    example: str
    translation: str
    meaning: Optional[str]
    book_name: str = Field("Basic Words 早稲田アカデミー")
    word_num: int
    is_correct: IsCorrect

class PostIsCorrectInput(BaseModel):
    id: str
    is_correct: IsCorrect