from dash import html, register_page, clientside_callback, Input, Output
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from flask_login import current_user
from controllers import users_controllers

register_page(
    __name__,
    path="/",
)


def layout():
    if not current_user.is_authenticated:
        return html.Div()
    else:
        username = current_user.get_id()
        userdata = users_controllers.get_user_info(username=username)

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
                                        "Перейти" if userdata['can_create_reports'] else 'Недоступно',
                                        mt="md",
                                        radius="md",
                                        fullWidth=True,
                                        disabled = not userdata['can_create_reports']
                                    ),
                                    href="/tickets/send?l=n",
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
                                        fullWidth=True
                                    ),
                                    href="/tickets/read?l=n",
                                    className="a-no-decoration",
                                ),
                            ],
                            w="max-content",
                            m="auto",
                        )
                    ],
                    md=3,
                    xs=6
                ) if userdata['can_read_reports'] else None,
                dbc.Col(className="adaptive-hide", width=3),
            ],
            style={"paddingTop": "33dvh"},
        )
