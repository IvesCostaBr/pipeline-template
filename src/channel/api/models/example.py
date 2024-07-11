from pydantic import BaseModel

class InExample(BaseModel):
    anyway : str



class OutExampleCreate(BaseModel):
    id: str