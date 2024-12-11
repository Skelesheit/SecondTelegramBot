from pydantic import BaseModel

class FrameworkLink(BaseModel):
    framework: str
    link: str

class TitleLink(BaseModel):
    title: str
    link: str