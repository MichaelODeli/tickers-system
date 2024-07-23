import os
import psycopg2

DBNAME="tickets_system"
USER="postgres"
PASSWORD="postgres"
HOST="localhost" if not os.environ.get("AM_I_IN_A_DOCKER_CONTAINER", False) else "db"
PORT="5432"

def test_conn(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT):
    """
    Функция test_conn проверяет соединение с базой данных.

    :param dbname: имя базы данных.
    :param user: имя пользователя базы данных.
    :param password: пароль пользователя базы данных.
    :param host: хост базы данных.
    :param port: порт базы данных.
    :return: True, если соединение установлено успешно, иначе False.
    """
    try:
        """
        Пытается установить соединение с базой данных.
        """
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        """
        Закрывает соединение с базой данных.
        """
        conn.close()
        return True
    except:
        """
        Если возникает ошибка при установке соединения, функция возвращает False.
        """
        return False



def get_conn(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT):
    """
    Функция get_conn возвращает соединение с базой данных, если оно установлено успешно, иначе None.

    :param dbname: имя базы данных.
    :param user: имя пользователя базы данных.
    :param password: пароль пользователя базы данных.
    :param host: хост базы данных.
    :param port: порт базы данных.
    :return: соединение с базой данных, если оно установлено успешно, иначе None.
    """
    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port,
        connect_timeout=2,
    ) if test_conn() else None

