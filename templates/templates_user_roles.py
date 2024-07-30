from dash import html


def user_has_no_access_template(service_div_children: list = None):
    return html.Center(
        [
            html.H5("У вас нет прав для просмотра данной страницы."),
            html.Div(children=service_div_children)
        ],
        style={"margin-top": "70px"},
    )
