from controllers import db_connection
from dash import html, no_update

def checker_conn(style):
    if db_connection.test_conn():
        return no_update, True
    else:
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