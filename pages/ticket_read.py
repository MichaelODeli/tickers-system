from dash import html, register_page

register_page(
    __name__,
    path=f"/ticket_read",
)


def layout():
    return html.Div(html.H3("Tickets read"))
