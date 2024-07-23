from controllers import db_connection
from dash import html, no_update

def checker_conn(style):
    """
    Функция checker_conn проверяет соединение с базой данных и возвращает результат в виде компонентов Dash.

    :param style: стиль отображения сообщения об ошибке.
    :return: кортеж, содержащий сообщение об ошибке и флаг успешности соединения.
    """
    if db_connection.test_conn():
        """
        Если соединение с базой данных успешно, функция возвращает no_update и флаг True.
        """
        return no_update, True
    else:
        """
        Если соединение с базой данных не установлено, функция возвращает сообщение об ошибке и флаг False.
        """
        return (
            html.Center(
                [
                    html.H6(
                        "Сервер техподдержки недоступен. Обратитесь за помощью по внутреннему телефону или через мессенджер."
                    )
                ],
                style={"margin-top": "70px"},
            ),
            False,
        )