import dash
from dash import (
    html,
    Output,
    Input,
    State,
    callback,
    dcc,
    no_update,
    page_container,
)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_extensions.pages import setup_page_components
import os
from controllers import db_connection
import flask
from flask_login import (
    login_user,
    LoginManager,
    UserMixin,
    logout_user,
    current_user,
)


# mantine configuration
dash._dash_renderer._set_react_version("18.2.0")
mantine_stylesheets = [
    # "https://unpkg.com/@mantine/dates@7/styles.css",
    # "https://unpkg.com/@mantine/code-highlight@7/styles.css",
    # "https://unpkg.com/@mantine/charts@7/styles.css",
    # "https://unpkg.com/@mantine/carousel@7/styles.css",
    "https://unpkg.com/@mantine/notifications@7/styles.css",
    # "https://unpkg.com/@mantine/nprogress@7/styles.css",
]

# flask and dash configuration
server = flask.Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.ZEPHYR,
        "assets/offline/bootstrap.min.css",
    ]
    + mantine_stylesheets,
    title="Tickets System",
    update_title="Tickets System 🔄️",
    suppress_callback_exceptions=True,
)

# password protection config
# Updating the Flask Server configuration with Secret Key
# to encrypt the user session cookie
server.config.update(SECRET_KEY=os.getenv("SECRET_KEY"))

# Login manager object will be used to login / logout users
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = "/login"

# User data model. It has to have at least self.id as a minimum


class User(UserMixin):
    def __init__(self, username):
        self.id = username


@login_manager.user_loader
def load_user(username):
    """This function loads the user by user id. Typically this looks up
    the user from a user database.
    We won't be registering or looking up users in this example, since
    we'll just login using LDAP server.
    So we'll simply return a User object with the passed in username.
    """
    return User(username)


# app layout
app.layout = dmc.MantineProvider(
    [
        dmc.Container(
            [
                dbc.NavbarSimple(
                    brand="TicketsSystem",
                    brand_href="/",
                    color="primary",
                    dark=True,
                    id="navbar",
                ),
                page_container,
                setup_page_components(),
                dmc.LoadingOverlay(
                    visible=True,
                    id="loading-overlay",
                    zIndex=1000,
                    overlayProps={"radius": "sm", "blur": 5},
                    loaderProps={"size": "lg"},
                ),
                dcc.Store(id="server-avaliablity"),
                dcc.Location(id="url", refresh=False),
                dcc.Location(id="redirect", refresh=True),
                html.Div(id="user-status-div"),
            ],
            miw="100%",
            mih="100%",
            id="server-blocker",
            p=0,
        ),
        dmc.NotificationProvider(),
    ],
    id="mantine_theme",
    defaultColorScheme="light",
    theme={
        "primaryColor": "indigo",
        "fontFamily": 'system-ui, -apple-system, "Segoe UI", Roboto,'
        '"Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif,'
        '"Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol",'
        '"Noto Color Emoji"',
    },
)


# standart callback for connection checking
@app.callback(
    Output("server-avaliablity", "data"),
    Output("server-blocker", "children"),
    Input("server-blocker", "style"),
    running=[
        (Output("loading-overlay", "visible"), True, False),
    ],
)
def server_blocker(style):
    if db_connection.test_conn():
        return True, no_update
    else:
        return False, html.Center(
            [
                html.H5(
                    "Сервис технической поддержки недоступен. "
                    "Обратитесь за помощью по внутреннему телефону "
                    "или через мессенджер."
                )
            ],
            style={"margin-top": "70px"},
        )


# draw navbar buttons
@app.callback(
    Output("navbar", "children"),
    Input("url", "pathname"),
)
def navbar_drawer(pathname):
    return [
        (
            dbc.DropdownMenu(
                children=[
                    # dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem(
                        "Личный кабинет", href="/account", disabled=True
                    ),
                    dbc.DropdownMenuItem("Выйти", href="/logout"),
                ],
                nav=True,
                in_navbar=True,
                label=f"Привет, {current_user.get_id()}!",
                style={"color": "rgb(255 255 255 / 85%)"},
            )
            if current_user.is_authenticated and pathname != "/logout"
            else dbc.NavLink("Войти", href="/login")
        )
    ]


@app.callback(
    Output("redirect", "pathname"),
    Input("url", "pathname"),
    State("server-avaliablity", "data"),
)
def redirector(current_path, avaliablity):
    if not avaliablity:
        return no_update

    url = dash.no_update

    if current_path == "/login":
        return no_update
    elif current_path == "/logout":
        if current_user.is_authenticated:
            logout_user()
        else:
            url = "/login"
    else:
        if current_user.is_authenticated:
            url = current_path
        else:
            url = "/login"
    return url


@callback(
    [Output("url_login", "pathname")],
    [Input("login-button", "n_clicks")],
    [
        State("uname-box", "value"),
        State("pwd-box", "value"),
        State("login-remember", "checked"),
    ],
)
def login_button_click(n_clicks, username, password, remember):
    if n_clicks > 0:
        if username == "test" and password == "test":
            user = User(username)
            login_user(user, remember=remember)
            return ["/"]
        else:
            return ["/login"]
    return [no_update]  # Return a placeholder to indicate no update


dev = (
    True if not os.environ.get("AM_I_IN_A_DOCKER_CONTAINER", False) else False
)

if __name__ == "__main__":
    if dev:
        app.run_server(debug=True, host="0.0.0.0", port=82)
    else:
        from waitress import serve

        serve(app.server, host="0.0.0.0", port=82)
