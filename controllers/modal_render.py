from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import html, callback, no_update, Output, Input
from controllers import tickets_controllers, users_controllers


def get_modal_content_by_uuid(ticket_uuid, userdata, source="unset"):
    ticket_details = tickets_controllers.get_tickets_info(
        return_df=False,
        ticket_uuid=ticket_uuid,
        mode="single",
        user_id=userdata["user_id"],
        query_filter="by_uuid",
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

    created, in_work, ended = tickets_controllers.get_ticket_history(
        ticket_uuid=ticket_uuid
    )
    active_num = 0
    created_item = [
        dmc.TimelineItem(
            title=created["status_name"],
            children=[
                dmc.Text(
                    created["created_at"],
                    c="dimmed",
                    size="sm",
                ),
            ],
        )
    ]
    if len(in_work) > 0:
        active_num += len(in_work)
        in_work_items = [
            dmc.TimelineItem(
                title=in_work_dict["status_name"],
                children=dmc.Stack(
                    [
                        dmc.Text(
                            in_work_dict["created_at"],
                            c="dimmed",
                            size="sm",
                        ),
                        dmc.Space(h="xs"),
                        dmc.Text(
                            f"Ответ: {in_work_dict['text']}",
                            c="dimmed",
                            size="sm",
                        ),
                        dmc.Text(
                            f"Исполнитель: {in_work_dict['position_name']} {in_work_dict['FIO']}",
                            c="dimmed",
                            size="sm",
                        ),
                    ],
                    gap=0,
                ),
            )
            for in_work_dict in in_work
        ]
    else:
        in_work_items = [
            dmc.TimelineItem(title="На рассмотрении", lineVariant="dashed")
        ]

    if len(ended) > 0:
        active_num =+ 1
        ended_item = [
            dmc.TimelineItem(
                title=ended["status_name"],
                children=dmc.Stack(
                    [
                        dmc.Text(
                            ended["created_at"],
                            c="dimmed",
                            size="sm",
                        ),
                        dmc.Space(h="xs"),
                        dmc.Text(
                            f"Ответ: {ended['text']}",
                            c="dimmed",
                            size="sm",
                        ),
                        dmc.Text(
                            f"Исполнитель: {ended['position_name']} {ended['FIO']}",
                            c="dimmed",
                            size="sm",
                        ),
                    ],
                    gap=0,
                ),
            )
        ]
    else:
        ended_item = [dmc.TimelineItem(title="Завершен", lineVariant="dashed")]

    history_data = dmc.Timeline(
        active=active_num,
        bulletSize=15,
        lineWidth=2,
        children=created_item + in_work_items + ended_item,
    )

    answer_data = (
        dmc.Stack(
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
        if source != "account"
        else None
    )

    return dmc.Stack(
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
                                    color=dmc.DEFAULT_THEME["colors"]["blue"][6],
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
                                history_data, id="review-ticket_history"
                            ),
                        ],
                        value="ticket_history",
                    ),
                    (
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl(
                                    "Ответ на тикет",
                                    icon=DashIconify(
                                        icon="ic:outline-question-answer",
                                        color=dmc.DEFAULT_THEME["colors"]["green"][6],
                                        width=30,
                                    ),
                                ),
                                dmc.AccordionPanel(
                                    answer_data, id="review-ticket_answer"
                                ),
                            ],
                            value="ticket_answer",
                        )
                        if (source != "account" and userdata["can_answer_reports"])
                        else html.Div()
                    ),
                ],
            )
        ],
        className="w-100",
    )


# @callback(
#     Output("review-ticket_history", "children"),
#     Output("review-ticket_answer", "children"),
#     Input("review-ticket_accordion", "value"),
#     prevent_initial_call=True,
# )
# def output_fields(accordion_value):
#     history_data = no_update
#     answer_data = no_update

#     if "ticket_history" in accordion_value:
#         history_data = dmc.Timeline(
#             active=2,
#             bulletSize=15,
#             lineWidth=2,
#             children=[
#                 dmc.TimelineItem(
#                     title="Получен",
#                     children=[
#                         dmc.Text(
#                             ["01/01/2024 08:00"],
#                             c="dimmed",
#                             size="sm",
#                         ),
#                     ],
#                 ),
#                 dmc.TimelineItem(
#                     title="На рассмотрении",
#                     children=dmc.Stack(
#                         [
#                             dmc.Text(
#                                 "02/01/2024 08:00",
#                                 c="dimmed",
#                                 size="sm",
#                             ),
#                             dmc.Space(h="xs"),
#                             dmc.Text(
#                                 "Ответ: {ответ}",
#                                 c="dimmed",
#                                 size="sm",
#                             ),
#                             dmc.Text(
#                                 "Исполнитель: {должность} {ФИО}",
#                                 c="dimmed",
#                                 size="sm",
#                             ),
#                         ],
#                         gap=0,
#                     ),
#                 ),
#                 dmc.TimelineItem(
#                     title="В работе",
#                     children=dmc.Stack(
#                         [
#                             dmc.Text(
#                                 "03/01/2024 08:00",
#                                 c="dimmed",
#                                 size="sm",
#                             ),
#                             dmc.Space(h="xs"),
#                             dmc.Text(
#                                 "Ответ: {ответ}",
#                                 c="dimmed",
#                                 size="sm",
#                             ),
#                             dmc.Text(
#                                 "Исполнитель: {должность} {ФИО}",
#                                 c="dimmed",
#                                 size="sm",
#                             ),
#                         ],
#                         gap=0,
#                     ),
#                 ),
#                 dmc.TimelineItem(
#                     title="Завершен",
#                     lineVariant="dashed",
#                 ),
#             ],
#         )
#     if "ticket_answer" in accordion_value:
#         answer_data = dmc.Stack(
#             [
#                 dmc.Select(
#                     label="Присвойте статус отчету",
#                     data=users_controllers.get_status_list(),
#                     searchable=True,
#                     w=300,
#                     rightSection=DashIconify(icon="radix-icons:chevron-down"),
#                     placeholder="Статус",
#                     id="ticket-status-select",
#                 ),
#                 dmc.Textarea(
#                     label="Введите ответ",
#                     placeholder="До 1024 символов",
#                     w=500,
#                     autosize=True,
#                     minRows=3,
#                     maxRows=7,
#                 ),
#                 dmc.Button("Отправить"),
#             ]
#         )
#     return history_data, answer_data
