"""
шаблоны для REST Microservice_apples
"""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class DataApples(BaseModel):
    name: str
    sort: str
    region: str
    type: str
    description: str
    createTime: datetime
    removeTime: Optional[datetime] = Field(default=None)
