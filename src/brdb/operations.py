import os
from .config import Config

config = Config()

def init():
    config.host = os.getenv("ORA_HOST")
    config.service = os.getenv("ORA_SERVICE")
    config.user = os.getenv("ORA_CR_USER")
    config.password = os.getenv("ORA_CR_PASSWORD")


def connect(domain: str|None = None):
    config.domain = domain
    try:
        config.conn = oracledb.connect(
            host=config.host,
            service_name=config.service,
            user=config.user,
            password=config.password
        )
        config.cur = config.conn.cursor()
        config.shopid = config.cur.callfunc("sh.get_shopid", int, (config.domain,))
    except Exception as err:
        print(f"Shop: Error connect to DB. {err}")
        exit(f"Ошибка подключения к базе данных. {err}")
    return config.conn, config.cur, config.shopid

def save_shop_rec(rec: dict):
    config.cur.callproc(
        "sh.insert_price",
        (
            config.shopid,
            rec["akc"],
            rec["name"],
            rec["url"],
            rec["price"],
            rec["old_price"],
            rec["unit"],
        ),
    )
