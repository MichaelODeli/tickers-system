from dash import html


def user_has_no_access_template():
    return html.Center(
        [
            html.H5("У вас нет доступа на просмотр этой страницы."),
        ],
        style={"margin-top": "70px"},
    )
