import dash_mantine_components as dmc
from dash_iconify import DashIconify

def db_error():
    return dmc.Notification(
        title="Ошибка получения данных",
        # id="simple-notify",
        action="show",
        message="Произошла ошибка. Попробуйте позднее.",
        icon=DashIconify(icon="material-symbols:error-outline"),
        color='red'
    ) 