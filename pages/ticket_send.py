from dash import (
    html,
    register_page,
    callback,
    Input,
    Output,
    State,
    no_update,
)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
from uuid import uuid4
from controllers import db_connection
from flask_login import current_user
import re
from controllers import users_controllers
from templates.templates_user_roles import user_has_no_access_template

register_page(
    __name__,
    path="/tickets/send",
)

USERDATA = ''

def layout(l='y'):

    if not current_user.is_authenticated or l=='y':
        return html.Div()
    
    global USERDATA
    
    username = current_user.get_id()
    USERDATA = users_controllers.get_user_info(username=username)
    # проверка доступа к отправке тикетов
    if not USERDATA['can_create_reports']:
        return user_has_no_access_template()
    else:
        return dbc.Row(
            [
                dbc.Col(className="adaptive-hide", width=3),
                dbc.Col(
                    [
                        html.H3("Создание нового обращения"),
                        dmc.Stack(
                            [
                                dmc.TextInput(
                                    label="Электронная почта, на которую придет ответ",
                                    w=400,
                                    leftSection=DashIconify(
                                        icon="ic:round-alternate-email"
                                    ),
                                    value=USERDATA['email'],
                                    disabled=True
                                ),
                                dmc.Select(
                                    label="Срочность",
                                    data=users_controllers.get_priority_list(),
                                    searchable=True,
                                    w=300,
                                    rightSection=DashIconify(
                                        icon="radix-icons:chevron-down"
                                    ),
                                    placeholder="Не завышайте приоритет",
                                    id="ticket-priority",
                                ),
                                dmc.Select(
                                    label="Категория проблемы",
                                    data=users_controllers.get_problems_list(),
                                    searchable=True,
                                    w=300,
                                    rightSection=DashIconify(
                                        icon="radix-icons:chevron-down"
                                    ),
                                    placeholder="Укажите категорию",
                                    id="ticket-problem",
                                ),
                                dmc.Textarea(
                                    label="Что случилось?",
                                    placeholder="Опишите проблему как можно подробнее. "
                                    "Что вы делали до возникновения ошибки? "
                                    "При каких обстоятельствах она возникла?",
                                    w=500,
                                    autosize=True,
                                    minRows=3,
                                    maxRows=7,
                                    id="ticket-text",
                                ),
                                dmc.Text(
                                    "",
                                    c="red",
                                    id="ticket-send-status",
                                    fw=500,
                                ),
                                dmc.Button("Отправить", id="ticket-send"),
                                dmc.Modal(
                                    title="Подтверждение отправки",
                                    id="ticket-send-modal",
                                    zIndex=10000,
                                    children=[
                                        dmc.Stack(
                                            [
                                                dmc.Text(
                                                    [
                                                        "Ваше обращение "
                                                        "успешно передано. Его"
                                                        " уникальный номер: ",
                                                        dmc.Code(
                                                            id="ticket-uuid7"
                                                        ),
                                                    ]
                                                ),
                                                dmc.Text(
                                                    "Сохраните этот номер "
                                                    "для дальнейших обращений."
                                                ),
                                            ]
                                        ),
                                        dmc.Space(h=20),
                                        dmc.Group(
                                            [
                                                dmc.Button(
                                                    "OK",
                                                    id="modal-submit-button",
                                                ),
                                            ],
                                            justify="flex-end",
                                        ),
                                    ],
                                ),
                            ],
                            id="send-form",
                        ),
                    ]
                ),
                dbc.Col(className="adaptive-hide", width=3),
            ],
            style={"paddingTop": "10dvh"},
        )


@callback(
    Output("ticket-send-status", "children"),
    Output("ticket-uuid7", "children"),
    Output("ticket-send-modal", "opened", allow_duplicate=True),
    Input("ticket-send", "n_clicks"),
    State("server-avaliablity", "data"),
    State("ticket-text", "value"),
    State("ticket-problem", "value"),
    State("ticket-priority", "value"),
    State("ticket-send-modal", "opened"),
    prevent_initial_call=True,
)
def send_ticket(
    n_clicks, avaliablity, text, problem, priority, opened
):
    if avaliablity:
        if (
            None in [text, problem, priority]
            or "" in [text, problem, priority]
        ):
            return "Не все поля правильно заполнены", no_update, no_update
        elif len(text) > 1024:
            return (
                "Максимальное количество символов - 1024",
                no_update,
                no_update,
            )
        else:
            try:
                global USERDATA

                # ticket_uuid = uuid7str()
                ticket_uuid = str(uuid4)
                conn = db_connection.get_conn()
                with conn.cursor() as cursor:
                    cursor.execute(
                        'INSERT INTO "tickets" '
                        '("uuid", "reporter_id", "priority_id", "problem_id", "text") '
                        'values (%(uuid)s, %(reporter_id)s, %(priority_id)s, %(problem_id)s, %(text)s);',
                        {
                            "uuid": ticket_uuid,
                            "reporter_id": USERDATA['user_id'],
                            "priority_id": int(priority),
                            "problem_id": int(problem),
                            "text": text
                        },
                    )
                conn.commit()
                conn.close()
                return "", ticket_uuid, not opened
            except Exception:
                return (
                    "Ошибка отправки. Повторите позднее.",
                    no_update,
                    no_update,
                )
    else:
        return no_update


@callback(
    Output("ticket-send-modal", "opened"),
    Input("modal-submit-button", "n_clicks"),
    State("ticket-send-modal", "opened"),
    prevent_initial_call=True,
)
def close_modal(n_clicks, opened):
    return not opened
