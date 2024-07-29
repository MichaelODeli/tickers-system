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
                    zIndex=100,
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
    if active_cell is not None or "ticket_uuid" in href:
        if active_cell is not None:
            t_uuid = active_cell["row_id"]
        else:
            parsed_url = urlparse(href)
            t_uuid = parse_qs(parsed_url.query)["ticket_uuid"][0]

        try:
            ticket_details = tickets_controllers.get_tickets_info(
                return_df=False,
                ticket_uuid=t_uuid,
                mode="single",
                user_id=USERDATA["user_id"],
            )

            ticket_table = dbc.Table(
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

            modal_content = dmc.Stack(
                [
                    dmc.Accordion(
                        id="review-ticket_accordion",
                        disableChevronRotation=True,
                        value=[
                            "ticket_table",
                        ],
                        variant="separated",
                        multiple=True,
                        children=[
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        "Информация о тикете",
                                        icon=DashIconify(
                                            icon="material-symbols:info-outline",
                                            color=dmc.DEFAULT_THEME["colors"]["blue"][
                                                6
                                            ],
                                            width=30,
                                        ),
                                    ),
                                    dmc.AccordionPanel(ticket_table),
                                ],
                                value="ticket_table",
                            ),
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        "История рассмотрения тикета",
                                        icon=DashIconify(
                                            icon="material-symbols:history",
                                            color=dmc.DEFAULT_THEME["colors"]["red"][6],
                                            width=30,
                                        ),
                                    ),
                                    dmc.AccordionPanel(
                                        "Загрузка...", id="review-ticket_history"
                                    ),
                                ],
                                value="ticket_history",
                            ),
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        "Ответ на тикет",
                                        icon=DashIconify(
                                            icon="ic:outline-question-answer",
                                            color=dmc.DEFAULT_THEME["colors"]["green"][
                                                6
                                            ],
                                            width=30,
                                        ),
                                    ),
                                    dmc.AccordionPanel(
                                        "Загрузка...", id="review-ticket_answer"
                                    ),
                                ],
                                value="ticket_answer",
                            ),
                        ],
                    )
                ],
                className="w-100",
            )

            return modal_content, not opened
        except Exception:
            return "Ошибка получения данных. Попробуйте позднее", not opened
    else:
        return [no_update] * 2


@callback(
    Output("review-ticket_history", "children"),
    Output("review-ticket_answer", "children"),
    Input("review-ticket_accordion", "value"),
    prevent_initial_call=True,
)
def output_fields(accordion_value):
    history_data = no_update
    answer_data = no_update

    if "ticket_history" in accordion_value:
        history_data = dmc.Timeline(
            active=2,
            bulletSize=15,
            lineWidth=2,
            children=[
                dmc.TimelineItem(
                    title="Получен",
                    children=[
                        dmc.Text(
                            ["01/01/2024 08:00"],
                            c="dimmed",
                            size="sm",
                        ),
                    ],
                ),
                dmc.TimelineItem(
                    title="На рассмотрении",
                    children=dmc.Stack(
                        [
                            dmc.Text(
                                "02/01/2024 08:00",
                                c="dimmed",
                                size="sm",
                            ),
                            dmc.Space(h="xs"),
                            dmc.Text(
                                "Ответ: {ответ}",
                                c="dimmed",
                                size="sm",
                            ),
                            dmc.Text(
                                "Исполнитель: {должность} {ФИО}",
                                c="dimmed",
                                size="sm",
                            ),
                        ],
                        gap=0,
                    ),
                ),
                dmc.TimelineItem(
                    title="В работе",
                    children=dmc.Stack(
                        [
                            dmc.Text(
                                "03/01/2024 08:00",
                                c="dimmed",
                                size="sm",
                            ),
                            dmc.Space(h="xs"),
                            dmc.Text(
                                "Ответ: {ответ}",
                                c="dimmed",
                                size="sm",
                            ),
                            dmc.Text(
                                "Исполнитель: {должность} {ФИО}",
                                c="dimmed",
                                size="sm",
                            ),
                        ],
                        gap=0,
                    ),
                ),
                dmc.TimelineItem(
                    title="Завершен",
                    lineVariant="dashed",
                ),
            ],
        )
    if "ticket_answer" in accordion_value:
        answer_data = dmc.Stack(
            [
                dmc.Select(
                    label="Присвойте статус отчету",
                    data=users_controllers.get_status_list(),
                    searchable=True,
                    w=300,
                    rightSection=DashIconify(icon="radix-icons:chevron-down"),
                    placeholder="Статус",
                    id="ticket-status-select",
                ),
                dmc.Textarea(
                    label="Введите ответ",
                    placeholder="До 1024 символов",
                    w=500,
                    autosize=True,
                    minRows=3,
                    maxRows=7,
                ),
                dmc.Button("Отправить"),
            ]
        )
    return history_data, answer_data
