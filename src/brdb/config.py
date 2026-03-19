from oracledb import Connection, Cursor
import oracledb
from dataclasses import dataclass, field

@dataclass
class Config:
    dsn: str|None = None
    host: str|None = None
    port: int|None = None
    service: str|None = None
    user: str|None = None
    password: str|None = None
    domain: str|None = None 
    conn: Connection|None = None
    cur: Cursor|None = None
    shopid: int|None = None
    debug: bool = False

    def __post_init__(self, *args, **kwargs):
        pass
        

if __name__ == "__main__":
    config = Config()
    