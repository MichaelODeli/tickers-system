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
import os

dash._dash_renderer._set_react_version("18.2.0")
mantine_stylesheets = [
    # "https://unpkg.com/@mantine/dates@7/styles.css",
    # "https://unpkg.com/@mantine/code-highlight@7/styles.css",
    # "https://unpkg.com/@mantine/charts@7/styles.css",
    # "https://unpkg.com/@mantine/carousel@7/styles.css",
    "https://unpkg.com/@mantine/notifications@7/styles.css",
    # "https://unpkg.com/@mantine/nprogress@7/styles.css",
]
app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.ZEPHYR, "assets/offline/bootstrap.min.css"]
    + mantine_stylesheets,
    title="Tickets System",
    update_title="Tickets System 🔄️",
)

app.layout = dmc.MantineProvider(
    [
        dmc.Container(
            [page_container, setup_page_components()], miw="100%", mih="100%"
        ),
        dmc.NotificationProvider()
    ],
    id="mantine_theme",
    defaultColorScheme="light",
)

# app.css.config.serve_locally = True
# app.scripts.config.serve_locally = True


server = app.server
app.config.suppress_callback_exceptions = True

dev = True if not os.environ.get("AM_I_IN_A_DOCKER_CONTAINER", False) else False

if __name__ == "__main__":
    if dev:
        app.run_server(debug=True, host="0.0.0.0", port=82)
    else:
        from waitress import serve

        serve(app.server, host="0.0.0.0", port=82)
