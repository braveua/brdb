from dataclasses import dataclass

@dataclass
class Config:
    host: str|None = None
    service: str|None = None
    user: str|None = None
    password: str|None = None
    domain: str|None = None 
    conn: bool|None = None
    cur: str|None = None
    shopid: int|None = None


