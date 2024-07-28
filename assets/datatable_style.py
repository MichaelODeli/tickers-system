datatable_list = [
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
]

styles_data_conditional = [
    {
        "if": {"state": "selected"},
        "border": "1px !important",
    },
    {
        "if": {
            "filter_query": '{Приоритет} contains "Высокий"',
        },
        "fontWeight": "600",
        "color": "red",
    },
]
