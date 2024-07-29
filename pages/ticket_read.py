from dash import (
    html,
    register_page,
    callback,
    Input,
    Output,
    State,
    no_update,
    dash_table,
    dcc,
)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import pandas as pd
import math
import warnings
from flask_login import current_user
from controllers import (
    users_controllers,
    tickets_controllers,
    db_connection,
    notifications,
    modal_render
)
from templates.templates_user_roles import user_has_no_access_template
from assets import datatable_style
from dash_iconify import DashIconify
from urllib.parse import urlparse
from urllib.parse import parse_qs

warnings.filterwarnings("ignore")

register_page(
    __name__,
    path="/tickets/read",
)
PAGE_SIZE = 17
USERDATA = ""
GLOBAL_TICKET_UUID = None


# @login_required
def layout(l="y", ticket_uuid=None, **kwargs):
    global PAGE_SIZE
    global USERDATA
    global GLOBAL_TICKET_UUID
    GLOBAL_TICKET_UUID = ticket_uuid

    if not current_user.is_authenticated or l == "y":
        return html.Div()

    username = current_user.get_id()
    USERDATA = users_controllers.get_user_info(username=username)
    # проверка доступа к просмотру тикетов
    if not USERDATA["can_read_reports"]:
        return user_has_no_access_template()
    else:
        filter_values = [
            ["Все", "all"],
            ["Неотвеченные", "unanswered"],
            # ["Принятые Вами в работу", "this_reviewer"],
        ]

        return dbc.Row(
            [
                dmc.Modal(
                    title=html.H4("Просмотр отчета"),
                    id="ticket-read-modal",
                    zIndex=201,
                    size="75%",
                    trapFocus=False,
                ),
                dbc.Col(className="adaptive-hide", width=2),
                dbc.Col(
                    [
                        html.Div(id="notifications-container"),
                        dmc.Stack(
                            gap="xs",
                            children=[
                                html.H3(
                                    (
                                        "Просмотр обращений"
                                        if ticket_uuid == None
                                        else "Просмотр выбранного обращения"
                                    ),
                                    id="dummy",
                                ),
                                dmc.RadioGroup(
                                    children=dmc.Group(
                                        [
                                            dmc.Radio(l, value=k)
                                            for l, k in filter_values
                                        ],
                                        my=10,
                                    ),
                                    id="radiogroup-filter",
                                    value=(
                                        filter
                                        if any(filter in sl for sl in filter_values)
                                        else "all"
                                    ),
                                    label="Фильтрация отчетов",
                                    size="sm",
                                    mb=10,
                                    display="none" if ticket_uuid != None else "block",
                                ),
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
                                            css=datatable_style.datatable_list,
                                            style_data_conditional=datatable_style.styles_data_conditional,
                                            hidden_columns=["id", "uuid"],
                                        ),
                                    ],
                                    className="table table-hover shadow-none",
                                    id="output-read",
                                ),
                                html.A(
                                    dmc.Button(
                                        "Вернуться к просмотру всех обращений",
                                        radius="md",
                                    ),
                                    href="/tickets/read?l=n",
                                    className="a-no-decoration",
                                    style=(
                                        {"display": "none"}
                                        if ticket_uuid is None
                                        else {"display": "block"}
                                    ),
                                ),
                            ],
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
    Output("notifications-container", "children"),
    Input("tickets-datatable", "page_current"),
    Input("radiogroup-filter", "value"),
    State("server-avaliablity", "data"),
    running=[
        (Output("loading-overlay-read", "visible"), True, False),
    ],
)
def update_table(page_current, query_filter, avaliablity):
    global PAGE_SIZE
    global GLOBAL_TICKET_UUID
    global USERDATA
    page_current = 0 if page_current is None else page_current

    if avaliablity:

        start_record = page_current * PAGE_SIZE
        # end_record = (page_current + 1) * PAGE_SIZE

        if GLOBAL_TICKET_UUID == None:
            df, records = tickets_controllers.get_tickets_info(
                mode="multi",
                return_df=True,
                limit=PAGE_SIZE,
                offset=start_record,
                query_filter=query_filter,
                user_id=USERDATA["user_id"],
            )
        else:
            try:
                df, records = tickets_controllers.get_tickets_info(
                    mode="single",
                    return_df=True,
                    limit=1,
                    offset=0,
                    ticket_uuid=GLOBAL_TICKET_UUID,
                    query_filter='by_uuid'
                )
            except pd.errors.DatabaseError:
                return [no_update] * 3 + [notifications.db_error()]

        page_count = math.ceil(records / PAGE_SIZE) 
        
        return (
            df.to_dict("records"),
            [{"name": i, "id": i} for i in df.columns],
            page_count,
            no_update,
        )
    else:
        return [no_update] * 4


@callback(
    Output("ticket-read-modal", "children"),
    Output("ticket-read-modal", "opened"),
    Input("tickets-datatable", "active_cell"),
    Input("url", "href"),
    State("ticket-read-modal", "opened"),
    running=[
        (Output("loading-overlay-read", "visible"), True, False),
    ],
    # prevent_initial_call=True,
)
def view_ticket(active_cell, href, opened):
    global USERDATA

    if active_cell is not None or "ticket_uuid" in href:
        if active_cell is not None:
            t_uuid = active_cell["row_id"]
        else:
            parsed_url = urlparse(href)
            t_uuid = parse_qs(parsed_url.query)["ticket_uuid"][0]

        try:
            modal_content = modal_render.get_modal_content_by_uuid(ticket_uuid=t_uuid, userdata=USERDATA)

            return modal_content, not opened
        except Exception:
            return "Ошибка получения данных. Попробуйте позднее", not opened
    else:
        return [no_update] * 2
