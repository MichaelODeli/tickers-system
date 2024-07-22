import os
import psycopg2

DBNAME="tickets_system"
USER="postgres"
PASSWORD="postgres"
HOST="localhost" if not os.environ.get("AM_I_IN_A_DOCKER_CONTAINER", False) else "db"
PORT="5432"

def test_conn(
    dbname=DBNAME,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        conn.close()
        return True
    except:
        return False


def get_conn(
    dbname=DBNAME,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
):
    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port,
        connect_timeout=2,
    ) if test_conn() else None
