from dataclasses import dataclass 
from typing import Optional 

@dataclass 
class Movie: 
    id: Optional[int] 
    title: str 
    description: str 
    genre: Optional[str] 
    language: Optional[str] 
    embedding: Optional[str] 