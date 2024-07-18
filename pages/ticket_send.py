from dash import html, register_page
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

register_page(
    __name__,
    path=f"/ticket_send",
)


def layout():
    return dbc.Row(
        [
            dbc.Col(className="adaptive-hide", width=3),
            dbc.Col(
                dmc.Stack(
                    [
                        html.H3("Создание нового обращения"),
                        dmc.TextInput(
                            label="Электронная почта для связи",
                            w=300,
                            placeholder="Электронная почта",
                            leftSection=DashIconify(icon="ic:round-alternate-email"),
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
                            rightSection=DashIconify(icon="radix-icons:chevron-down"),
                        ),
                        dmc.NumberInput(
                            label="Ваш табельный номер",
                            w=300,
                            hideControls=True,
                            placeholder='Введите 8 цифр'
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
                            rightSection=DashIconify(icon="radix-icons:chevron-down"),
                            placeholder='Не завышайте приоритет'
                        ),
                        dmc.Textarea(
                            label="Что случилось?",
                            placeholder="Опишите проблему как можно подробнее. Что вы делали до возникновения ошибки?",
                            w=500,
                            autosize=True,
                            minRows=2,
                        ),
                    ]
                ),
            ),
            dbc.Col(className="adaptive-hide", width=3),
        ],
        style={"padding-top": "10dvh"},
    )
