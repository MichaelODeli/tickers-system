from dash import html, register_page
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

register_page(
    __name__,
    path="/",
)


def layout():
    return dbc.Row(
        [
            dbc.Col(className='adaptive-hide', width=3),
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
                                    color="blue",
                                    mt="md",
                                    radius="md",
                                    fullWidth=True
                                ),
                                href="/ticket_send",
                                className='a-no-decoration'
                            ),
                        ],
                        w='max-content',
                        m='auto'
                    )
                ],
                md=3,
                xs=6
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
                                    color="blue",
                                    mt="md",
                                    radius="md",
                                    fullWidth=True
                                ),
                                href="/ticket_read",
                                className='a-no-decoration'
                            ),
                        ],
                        w='max-content',
                        m='auto'
                    )
                ],
                md=3,
                xs=6
            ),
            dbc.Col(className='adaptive-hide', width=3),
        ],
        style={'padding-top': '33dvh'}
    )
