from dash import html, register_page, callback, Input, Output, no_update
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from flask_login import current_user
from dash_iconify import DashIconify
from controllers import db_connection, users_controllers

register_page(
    __name__,
    path="/account",
)

USERDATA = ''

def layout(l="y"):
    global USERDATA

    if not current_user.is_authenticated or l == "y" or not db_connection.test_conn():
        return html.Div()
    else:
        username = current_user.get_id()
        USERDATA = users_controllers.get_user_info(username=username)

        return dbc.Row(
            [
                dbc.Col(className="adaptive-hide", width=1),
                dbc.Col(
                    dmc.Card(
                        [
                            dmc.Stack(
                                [
                                    DashIconify(
                                        icon="codicon:account",
                                        width=85,
                                        color="var(--bs-primary)",
                                        className="pb-3",
                                    ),
                                    dmc.Group(
                                        [
                                            dmc.Text(label, fw=500)
                                            for label in [
                                                f"{USERDATA['last_name']}",
                                                f"{USERDATA['first_name']}",
                                                f"{USERDATA['middle_name']}",
                                            ]
                                        ],
                                        gap=5,
                                        justify="center",
                                    ),
                                    dmc.Text(f"{USERDATA['position_name']}", c="gray"),
                                    html.Div(
                                        "",
                                        className="border-top mt-3 pb-3 w-100",
                                    ),
                                    html.Table(
                                        [
                                            html.Tr(
                                                [
                                                    html.Td(
                                                        dmc.Text(
                                                            label,
                                                            c="var(--mantine-color-gray-text)",
                                                        )
                                                    ),
                                                    html.Td(dmc.Text(content)),
                                                ]
                                            )
                                            for label, content in [
                                                [
                                                    "Табельный номер",
                                                    f"{USERDATA['employee_id']}",
                                                ],
                                                [
                                                    "Электронная почта",
                                                    f"{USERDATA['email']}",
                                                ],
                                                [
                                                    "Отдел",
                                                    f"{USERDATA['department_name']}",
                                                ],
                                                [
                                                    "Уровень доступа",
                                                    f"{USERDATA['level_name']} ({USERDATA['access_level']})",
                                                ],
                                            ]
                                        ],
                                        className="w-100",
                                    ),
                                ],
                                align="center",
                                w="100%",
                                gap=0,
                            )
                        ],
                        shadow="sm",
                        radius="md",
                        withBorder=True,
                    ),
                    width=3,
                    class_name="m-1 p-1",
                ),
                dbc.Col(
                    dmc.Accordion(
                        id="account-accordion-data",
                        disableChevronRotation=True,
                        children=[
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        dmc.Text(
                                            "Отправленные обращения",
                                            className="p-1",
                                        ),
                                        icon=dmc.Indicator(
                                            DashIconify(
                                                icon="iconoir:send-diagonal",
                                                color=dmc.DEFAULT_THEME["colors"][
                                                    "gray"
                                                ][6],
                                                width=30,
                                            ),
                                            inline=True,
                                            color="red",
                                            size=10,
                                            processing=True,
                                            id="account-tickets-sents_indicator",
                                            disabled=True,
                                        ),
                                    ),
                                    dmc.AccordionPanel(
                                        "account-tickets-sents_data",
                                        id="account-tickets-sents_data",
                                    ),
                                ],
                                value="account-tickets-sents",
                            ),
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        dmc.Text(
                                            "Завершенные обращения", className="p-1"
                                        ),
                                        icon=dmc.Indicator(
                                            DashIconify(
                                                icon="tabler:circle-check",
                                                color=dmc.DEFAULT_THEME["colors"][
                                                    "green"
                                                ][6],
                                                width=30,
                                            ),
                                            inline=True,
                                            color="red",
                                            size=10,
                                            processing=True,
                                            id="account-tickets-ended_indicator",
                                            disabled=True,
                                        ),
                                    ),
                                    dmc.AccordionPanel(
                                        "account-tickets-ended_data",
                                        id="account-tickets-ended_data",
                                    ),
                                ],
                                value="account-tickets-ended",
                            ),
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        dmc.Text(
                                            "Обращения, ожидающие уточнения",
                                            className="p-1",
                                        ),
                                        icon=dmc.Indicator(
                                            DashIconify(
                                                icon="material-symbols:info-outline",
                                                color=dmc.DEFAULT_THEME["colors"][
                                                    "blue"
                                                ][6],
                                                width=30,
                                            ),
                                            inline=True,
                                            color="red",
                                            size=10,
                                            processing=True,
                                            id="account-tickets-awaiting_indicator",
                                            disabled=True,
                                        ),
                                    ),
                                    dmc.AccordionPanel(
                                        "account-tickets-awaiting_data",
                                        id="account-tickets-awaiting_data",
                                    ),
                                ],
                                value="account-tickets-awaiting",
                            ),
                        ],
                    ),
                    # style={"background-color": "cyan"},
                    class_name="m-1 p-1",
                ),
                dbc.Col(className="adaptive-hide", width=1),
            ],
            style={"paddingTop": "6dvh"},
        )


@callback(
    Output("account-tickets-sents_indicator", "disabled"),
    Output("account-tickets-sents_data", "children"),
    Output("account-tickets-ended_indicator", "disabled"),
    Output("account-tickets-ended_data", "children"),
    Output("account-tickets-awaiting_indicator", "disabled"),
    Output("account-tickets-awaiting_data", "children"),
    Input("account-accordion-data", "value"),
)
def test_controller_for_accordion(value):
    if value == None:
        return [True, no_update] * 3
    elif "sents" in value:
        return [False, no_update] + [True, no_update] * 2
    elif "ended" in value:
        return [True, no_update] + [False, no_update] + [True, no_update]
    elif "awaiting" in value:
        return [True, no_update] * 2 + [False, no_update]
