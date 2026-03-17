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
    # conn: Connection = field(init=False)
    cur: Cursor|None = None
    # cur: Cursor = field(init=False)
    shopid: int|None = None
    debug: bool = False

    def __post_init__(self, *args, **kwargs):
        # def connect(*args, **kwargs):
        # init()    
        if not self.domain:
            self.domain = kwargs.get("domain")
        if not self.dsn:
            self.dsn = kwargs.get("dsn")
        if not self.host:
            self.host = kwargs.get("host")
        if not self.service:  
            self.service = kwargs.get("service")
        # if not config.user:
        if kwargs.get("user"):
            self.user = kwargs.get("user")
        # if not config.password:
        if kwargs.get("password"):
            self.password = kwargs.get("password")
        self.debug = kwargs.get("debug", False)
        try:
            # print(config)
            if self.dsn:
                if self.debug:
                    print("Connect by DSN")
                self.conn = oracledb.connect(
                    dsn=self.dsn,
                    user=self.user,
                    password=self.password
                )
            else:
                if self.debug:
                    print("Connect by HOST/SERVICE")    
                self.conn = oracledb.connect(
                    host=self.host,
                    service_name=self.service,
                    user=self.user,
                    password=self.password
            )
            self.cur = self.conn.cursor()
            if self.domain:
                self.shopid = self.cur.callfunc("sh.get_shopid", int, (self.domain,))
        except Exception as err:
            print(f"Shop: Error connect to DB. {err}")
            exit(f"Ошибка подключения к базе данных. {err}")
        return self.conn, self.cur, self.shopid

if __name__ == "__main__":
    config = Config()
    # config.__post_init__(debug=True)