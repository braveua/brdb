from oracledb import Connection, Cursor
from dataclasses import dataclass

@dataclass
class Config:
    host: str|None = None
    service: str|None = None
    user: str|None = None
    password: str|None = None
    domain: str|None = None 
    conn: Connection|None = None
    cur: Cursor|None = None
    shopid: int|None = None


