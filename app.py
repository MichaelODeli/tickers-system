import dash
from dash import (
    html,
    Output,
    Input,
    State,
    callback,
    dcc,
    clientside_callback,
    no_update,
    page_container,
    page_registry,
)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_extensions.pages import setup_page_components

dash._dash_renderer._set_react_version("18.2.0")
app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.ZEPHYR, 'assets/offline/bootstrap.min.css'],
    title="Tickets System",
    update_title="Tickets System 🔄️",
)

app.layout = dmc.MantineProvider(
    dmc.Container(
        [page_container, setup_page_components()],
        miw="100%",
        mih='100%'
    ),
    id="mantine_theme",
    defaultColorScheme="light",
)

# app.css.config.serve_locally = True
# app.scripts.config.serve_locally = True


# @callback(
#     Output("mantine_theme", "forceColorScheme"), Input("color-mode-switch", "value")
# )
# def make_mantine_theme(value):
#     return "dark" if value == False else "light"

# clientside_callback(
#     """
#     (switchOn) => {
#        document.documentElement.setAttribute('data-bs-theme', switchOn ? 'light' : 'dark');
#        return window.dash_clientside.no_update
#     }
#     """,
#     Output("color-mode-switch", "id"),
#     Input("color-mode-switch", "value"),
# )

server = app.server
app.config.suppress_callback_exceptions = True

dev = True

if __name__ == "__main__":
    if dev:
        app.run_server(debug=True, host="0.0.0.0", port=82)
    else:
        from waitress import serve

        serve(app.server, host="0.0.0.0", port=82)
