from pydantic import BaseModel

class TextAnalysisResponse(BaseModel):
    original_text: str
    errors: list
    grade: float
    suggestions: list
