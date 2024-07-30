from dash import html, register_page, callback, Input, Output, no_update, dash_table, State
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from flask_login import current_user
from dash_iconify import DashIconify
from controllers import db_connection, users_controllers, tickets_controllers, modal_render
from assets import datatable_style

register_page(
    __name__,
    path="/account",
)

USERDATA = ""


def layout(l="y", **kwargs):
    global USERDATA

    if not current_user.is_authenticated or l == "y" or not db_connection.test_conn():
        return html.Div()
    else:
        username = current_user.get_id()
        USERDATA = users_controllers.get_user_info(username=username)

        return dbc.Row(
            [
                dmc.Modal(
                    title=html.H4("Просмотр отчета"),
                    id="ticket-read-modal-account",
                    zIndex=201,
                    size="75%",
                    trapFocus=False,
                    className='adaptive-modal'
                ),
                dbc.Col(className="adaptive-hide", width=1),
                dbc.Col(
                    children=dmc.Card(
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
                    class_name="m-1 p-1 adaptive-width",
                ),
                dbc.Col(
                    dmc.Accordion(
                        id="account-accordion-data",
                        disableChevronRotation=True,
                        variant="separated",
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
                                        
                                        id="account-tickets-sents_data",
                                    ),
                                ],
                                value="account-tickets-sents",
                            ),
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        children=dmc.Text(
                                            "Обращения в работе",
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
                                        id="account-tickets-awaiting_data",
                                    ),
                                ],
                                value="account-tickets-awaiting",
                            ),
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        children=dmc.Text(
                                            "Завершенные обращения",
                                            className="p-1",
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
                                        id="account-tickets-ended_data",
                                    ),
                                ],
                                value="account-tickets-ended",
                            ),
                            
                        ],
                    ),
                    class_name="m-1 p-1 adaptive-width",
                ),
                dbc.Col(className="adaptive-hide", width=1),
            ],
            style={"paddingTop": "6dvh"},
            class_name='adaptive-block'
        )


@callback(
    Output("account-tickets-sents_indicator", "disabled"),
    Output("account-tickets-sents_data", "children"),
    Output("account-tickets-ended_indicator", "disabled"),
    Output("account-tickets-ended_data", "children"),
    Output("account-tickets-awaiting_indicator", "disabled"),
    Output("account-tickets-awaiting_data", "children"),
    Input("account-accordion-data", "value"),
    # prevent_initial_call=True,
)
def test_controller_for_accordion(value):
    global USERDATA

    sents, ended, awaiting = [False]*3
    noupdate_return = [True, no_update]

    if value == None: return noupdate_return * 3

    if "sents" in value:
        df, records = tickets_controllers.get_tickets_info(mode='multi', query_filter = 'account_last5sended', user_id=USERDATA["user_id"], return_df=True,)
        sents = True
    if 'ended' in value:
        df, records = tickets_controllers.get_tickets_info(mode='multi', query_filter = 'account_last5ended', user_id=USERDATA["user_id"], return_df=True,)
        ended = True
    if 'awaiting' in value:
        df, records = tickets_controllers.get_tickets_info(mode='multi', query_filter = 'account_last5awaiting', user_id=USERDATA["user_id"], return_df=True,)
        awaiting = True

    return_list = [
        False,
        dmc.Stack(
            [
                dmc.Text("Отображаются 5 последних обращений"),
                html.Div(
                    dash_table.DataTable(
                        id="tickets-datatable-user",
                        css=datatable_style.datatable_list,
                        hidden_columns=["id", "uuid"],
                        data=df.to_dict("records"),
                        columns=[{"name": i, "id": i} for i in sorted(df.columns)],
                        style_data_conditional=datatable_style.styles_data_conditional,
                    ),
                    className="table table-hover shadow-none w-100",
                ),
            ],
            w="100%",
        )
    ]

    return (return_list if sents else noupdate_return) + (return_list if ended else noupdate_return) +  (return_list if awaiting else noupdate_return)
    
@callback(
    Output("ticket-read-modal-account", "children"),
    Output("ticket-read-modal-account", "opened"),
    Input("tickets-datatable-user", "active_cell"),
    State("ticket-read-modal-account", "opened"),
    # running=[
    #     (Output("loading-overlay-read", "visible"), True, False),
    # ],
    # prevent_initial_call=True,
)
def view_ticket(active_cell, opened):
    if active_cell is not None:
        t_uuid = active_cell["row_id"]
        try:
            modal_content = modal_render.get_modal_content_by_uuid(ticket_uuid=t_uuid, userdata=USERDATA, source='account')

            return modal_content, not opened
        except Exception:
            return "Ошибка получения данных. Попробуйте позднее", not opened
    else:
        return [no_update] * 2