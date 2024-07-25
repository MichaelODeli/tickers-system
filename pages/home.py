from dash import html, register_page, clientside_callback, Input, Output
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from flask_login import current_user

register_page(
    __name__,
    path="/",
)


def layout():
    if not current_user.is_authenticated:
        return html.Div()
    else:
        return dbc.Row(
            [
                dbc.Col(className="adaptive-hide", width=3),
                dbc.Col(
                    [
                        dmc.Card(
                            children=[
                                dmc.Text("Создать обращение", fw=500),
                                dmc.Text(
                                    "Перейдите, чтобы сообщить о возникшей проблеме",
                                    size="sm",
                                    c="dimmed",
                                ),
                                html.A(
                                    dmc.Button(
                                        "Перейти",
                                        mt="md",
                                        radius="md",
                                        fullWidth=True,
                                    ),
                                    href="/ticket_send?l=n",
                                    className="a-no-decoration",
                                ),
                            ],
                            w="max-content",
                            m="auto",
                        )
                    ],
                    md=3,
                    xs=6,
                ),
                dbc.Col(
                    [
                        dmc.Card(
                            children=[
                                dmc.Text("Просмотр обращений", fw=500),
                                dmc.Text(
                                    "Перейдите для просмотра имеющихся обращений",
                                    size="sm",
                                    c="dimmed",
                                ),
                                html.A(
                                    dmc.Button(
                                        "Перейти",
                                        mt="md",
                                        radius="md",
                                        fullWidth=True,
                                    ),
                                    href="/ticket_read?l=n",
                                    className="a-no-decoration",
                                ),
                            ],
                            w="max-content",
                            m="auto",
                        )
                    ],
                    md=3,
                    xs=6,
                ),
                dbc.Col(className="adaptive-hide", width=3),
            ],
            style={"paddingTop": "33dvh"},
        )
