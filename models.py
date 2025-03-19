from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional, Union

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str

class URLRequest(BaseModel):
    url: HttpUrl = Field(..., description="URL to process")
