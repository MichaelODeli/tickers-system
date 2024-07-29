from dash import html, register_page, clientside_callback, Input, Output
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from flask_login import current_user
from controllers import users_controllers
from templates.templates_user_roles import user_has_no_access_template

register_page(
    __name__,
    path="/admin",
)


def layout(l='y'):
    global PAGE_SIZE

    if not current_user.is_authenticated or l=='y':
        return html.Div()
    
    username = current_user.get_id()
    userdata = users_controllers.get_user_info(username=username)
    # проверка доступа к просмотру тикетов
    if not userdata['admin_access']:
        return user_has_no_access_template()
    else:
        return 'Скоро...'