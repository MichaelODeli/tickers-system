from dash import (
    html,
    register_page,
    callback,
    Input,
    Output,
    State,
    no_update,
    dash_table,
)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import pandas as pd
from controllers import db_connection
import math
import warnings
from flask_login import current_user
from controllers import users_controllers, tickets_controllers
from templates.templates_user_roles import user_has_no_access_template

warnings.filterwarnings("ignore")

register_page(
    __name__,
    path="/tickets/read",
)
PAGE_SIZE = 18

# @login_required
def layout(l='y'):
    global PAGE_SIZE

    if not current_user.is_authenticated or l=='y':
        return html.Div()
    
    username = current_user.get_id()
    userdata = users_controllers.get_user_info(username=username)
    # проверка доступа к просмотру тикетов
    if not userdata['can_read_reports']:
        return user_has_no_access_template()
    else:
        return dbc.Row(
            [
                dmc.Modal(
                    title="Информация об отчете",
                    id="ticket-read-modal",
                    zIndex=10000,
                    size="55%",
                ),
                dbc.Col(className="adaptive-hide", width=2),
                dbc.Col(
                    [
                        html.Div(id="notifications-container"),
                        dmc.Stack(
                            [
                                html.H3("Просмотр обращений", id="dummy"),
                                html.Div(
                                    [
                                        dmc.LoadingOverlay(
                                            id="loading-overlay-read",
                                            zIndex=1000,
                                            overlayProps={
                                                "radius": "sm",
                                                "blur": 2,
                                            },
                                        ),
                                        dash_table.DataTable(
                                            id="tickets-datatable",
                                            page_current=0,
                                            page_size=PAGE_SIZE,
                                            page_action="custom",
                                            css=[
                                                {
                                                    "selector": "tr:hover",
                                                    "rule": "background-color: var(--bs-table-hover-bg) !important",
                                                },
                                                {
                                                    "selector": "td",
                                                    "rule": "background-color: inherit !important",
                                                },
                                                {
                                                    "selector": "table",
                                                    "rule": "font-family: var(--bs-font-sans-serif) !important",
                                                },
                                                {
                                                    "selector": "th",
                                                    "rule": "font-weight: 600 !important",
                                                },
                                            ],
                                            hidden_columns=["id", "uuid"],
                                        ),
                                    ],
                                    className="table table-hover shadow-none",
                                    id="output-read",
                                ),
                            ]
                        ),
                    ]
                ),
                dbc.Col(className="adaptive-hide", width=2, id="dummy-1"),
            ],
            style={"paddingTop": "10dvh"},
        )


@callback(
    Output("tickets-datatable", "data"),
    Output("tickets-datatable", "columns"),
    Output("tickets-datatable", "page_count"),
    Output("tickets-datatable", "style_data_conditional"),
    Input("tickets-datatable", "page_current"),
    Input("tickets-datatable", "page_size"),
    Input("loading-overlay-read", "visible"),
    State("server-avaliablity", "data"),
)
def update_table(page_current, page_size, visible, avaliablity):
    global PAGE_SIZE
    page_current = 0 if page_current is None else page_current

    if avaliablity:
        conn = db_connection.get_conn()
        records = pd.read_sql("select count(*) from tickets;", conn)[
            "count"
        ].tolist()[0]

        start_record = page_current * PAGE_SIZE
        # end_record = (page_current + 1) * PAGE_SIZE
        page_count = math.ceil(records / PAGE_SIZE)

        df = tickets_controllers.get_tickets_info(limit=PAGE_SIZE, offset=start_record)

        conn.close()

        return (
            df.to_dict("records"),
            [{"name": i, "id": i} for i in sorted(df.columns)],
            page_count,
            [
                {
                    "if": {"state": "selected"},
                    "border": "1px !important",
                },
                {
                    "if": {
                        "filter_query": '{priority_name} contains "Высокий"',
                    },
                    "fontWeight": "600",
                    "color": "red",
                },
            ],
        )
    else:
        return [no_update] * 4


@callback(
    Output("ticket-read-modal", "children"),
    Output("ticket-read-modal", "opened"),
    Output("notifications-container", "children"),
    Input("tickets-datatable", "active_cell"),
    State("ticket-read-modal", "opened"),
    running=[
        (Output("loading-overlay-read", "visible"), True, False),
    ],
    prevent_initial_call=True,
)
def view_ticket(active_cell, opened):
    if active_cell is not None:
        # conn = db_connection.get_conn()
        # df = pd.read_sql(
        #     f"SELECT * FROM tickets WHERE uuid = '{active_cell['row_id']}';",
        #     conn,
        # )
        # conn.close()

        # ticket_details = df.to_dict("records")[0]

        ticket_details = tickets_controllers.get_tickets_info(return_df=False, ticket_uuid=active_cell['row_id'])

        modal_content = dbc.Table(
            [
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Td(key, className="p-2 fw-bold"),
                                html.Td(ticket_details[key], className="p-2"),
                            ],
                        )
                        for key in list(ticket_details.keys())
                    ]
                )
            ],
            class_name="shadow-none w-content",
            bordered=True,
            hover=True,
        )

        return modal_content, not opened, no_update
    else:
        return [no_update] * 3
