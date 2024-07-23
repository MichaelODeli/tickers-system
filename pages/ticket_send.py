from dash import html, register_page, callback, Input, Output, State, no_update, dcc
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
from uuid_extensions import uuid7str
from controllers import db_connection
import re

register_page(
    __name__,
    path=f"/ticket_send",
)


def layout():
    return dbc.Row(
        [
            dbc.Col(className="adaptive-hide", width=3),
            dbc.Col(
                [
                    html.H3("Создание нового обращения"),
                    dmc.Stack(
                        [
                            dmc.TextInput(
                                label="Электронная почта для связи",
                                w=300,
                                placeholder="Электронная почта",
                                leftSection=DashIconify(
                                    icon="ic:round-alternate-email"
                                ),
                                id="ticket-email",
                            ),
                            dmc.Select(
                                label="Ваш отдел",
                                data=[
                                    {"value": "economic", "label": "Экономический"},
                                    {"value": "tech", "label": "Технический"},
                                    {"value": "ohs", "label": "Охрана труда"},
                                ],
                                searchable=True,
                                w=300,
                                rightSection=DashIconify(
                                    icon="radix-icons:chevron-down"
                                ),
                                id="ticket-district",
                            ),
                            dmc.NumberInput(
                                label="Ваш табельный номер",
                                w=300,
                                hideControls=True,
                                placeholder="Введите 8 цифр",
                                id="ticket-userid",
                            ),
                            dmc.Select(
                                label="Срочность",
                                data=[
                                    {"value": "high", "label": "Высокая"},
                                    {"value": "medium", "label": "Средняя"},
                                    {"value": "low", "label": "Низкая"},
                                ],
                                searchable=True,
                                w=300,
                                rightSection=DashIconify(
                                    icon="radix-icons:chevron-down"
                                ),
                                placeholder="Не завышайте приоритет",
                                id="ticket-priority",
                            ),
                            dmc.Textarea(
                                label="Что случилось?",
                                placeholder="Опишите проблему как можно подробнее. "
                                "Что вы делали до возникновения ошибки? При каких обстоятельствах она возникла?",
                                w=500,
                                autosize=True,
                                minRows=3,
                                maxRows=7,
                                id="ticket-text",
                            ),
                            dmc.Text("", c="red", id="ticket-send-status", fw=500),
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
                                                    "Ваше обращение успешно передано. Его уникальный номер: ",
                                                    dmc.Code(id="ticket-uuid7"),
                                                ]
                                            ),
                                            dmc.Text(
                                                "Сохраните этот номер для дальнейших обращений."
                                            ),
                                        ]
                                    ),
                                    dmc.Space(h=20),
                                    dmc.Group(
                                        [
                                            dmc.Button("OK", id="modal-submit-button"),
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
    State("ticket-email", "value"),
    State("ticket-district", "value"),
    State("ticket-userid", "value"),
    State("ticket-priority", "value"),
    State("ticket-text", "value"),
    State("ticket-send-modal", "opened"),
    prevent_initial_call=True,
)
def send_ticket(n_clicks, avaliablity, email, district, userid, priority, text, opened):
    if avaliablity:
        if (
            None in [email, district, userid, priority, text]
            or "" in [email, district, userid, priority, text]
            or not re.match(r"[^@]+@[^@]+\.[^@]+", email)
        ):
            return "Не все поля правильно заполнены", no_update, no_update
        elif len(text) > 1024:
            return "Максимальное количество символов - 1024", no_update, no_update
        elif len(str(userid)) != 8:
            return "Табельный номер состоит из 8 цифр", no_update, no_update
        else:
            try:
                ticket_uuid = uuid7str()
                conn = db_connection.get_conn()
                with conn.cursor() as cursor:
                    cursor.execute(
                        'INSERT INTO "tickets_simple" ("uuid", "user_id", "email", "district", "priority", "text") values (%(uuid)s, %(user_id)s, %(email)s, %(district)s, %(priority)s, %(text)s)',
                        {
                            "uuid": ticket_uuid,
                            "user_id": userid,
                            "email": email,
                            "district": district,
                            "priority": priority,
                            "text": text,
                        },
                    )
                conn.commit()
                conn.close()
                return "", ticket_uuid, not opened
            except:
                return "Ошибка отправки. Повторите позднее.", no_update, no_update
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
