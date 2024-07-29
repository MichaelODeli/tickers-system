from controllers import db_connection
import pandas as pd


def get_query_strings(
    mode, query_filter, limit=5, offset=0, ticket_uuid="", user_id=None
):
    limits = f"LIMIT {limit} OFFSET {offset}"
    orderby = "ORDER BY priority_id DESC, created_at DESC"
    if mode == "multi":
        if query_filter == "unanswered":
            table_name = f"(select * from tickets where status_id = 0)"
        elif query_filter == "this_reviewer":
            table_name = "tickets"  # for future releases
        else:
            table_name = "tickets"
    if mode == "account_last5sended":
        table_name = f"(select * from tickets where reporter_id = {user_id})"
        orderby = "ORDER BY created_at DESC"
    if mode == "single":
        table_name = f"(select * from tickets where uuid = '{ticket_uuid}')"

    query_string = f"""SELECT * FROM {table_name} t 
    left join (select id as probl_id, problem_name from problems_list) p on t.problem_id = p.probl_id 
    left join (select id as prior_id, priority_name from priority_list) pi on pi.prior_id = t.priority_id 
    left join (select id as rep_id, username, first_name, middle_name, last_name, position_id, email from users) u on u.rep_id = t.reporter_id 
    left join (select id as pos_id, department_id, position_name from positions) po on u.position_id = po.pos_id
    left join (select id as dep_id, department_name from departments) d on d.dep_id = po.department_id
    left join (select id as stat_id, status_name from status_list) s on s.stat_id = t.status_id
    {orderby} 
    {limits};""".replace(
        "\n", ""
    )
    len_query_string = f"SELECT count(*) FROM {table_name};"

    return query_string, len_query_string


def filter_and_rename_df(
    df,
    mode="milti",
    multi_reports_columns=[
        "id",
        "Дата и время создания",
        "ФИО",
        "Название проблемы",
        "Приоритет",
        "Содержание отчета (сокр.)",
        "Текущий статус обращения",
    ],
    single_report_columns=[
        "id",
        "Дата и время создания",
        "ФИО (полное)",
        "Должность",
        "Отдел",
        "Приоритет",
        "Название проблемы",
        "Содержание отчета (полн.)",
        "Почта для связи",
        "Текущий статус обращения",
    ],
):
    if len(df) == 0:
        return df
    df["id"] = df["uuid"]
    df["created_at"] = df["created_at"].dt.strftime("%d.%m.%Y %H:%M:%S")

    # удаление ненужных колонок
    df.drop(
        columns=(
            [
                "prior_id",
                "priority_id",
                "probl_id",
                "problem_id",
                "rep_id",
                "reporter_id",
                "pos_id",
                "position_id",
                "dep_id",
                "department_id",
                "stat_id",
                "status_id",
                "username",
                "uuid",
            ]
        ),
        inplace=True,
    )
    # переименование
    df.rename(
        columns={
            "created_at": "Дата и время создания",
            "priority_name": "Приоритет",
            "problem_name": "Название проблемы",
            "text": "Содержание отчета (полн.)",
            "username": "Пользователь",
            "last_name": "Фамилия",
            "first_name": "Имя",
            "middle_name": "Отчество",
            "department_name": "Отдел",
            "position_name": "Должность",
            "email": "Почта для связи",
            "status_name": "Текущий статус обращения",
        },
        inplace=True,
    )
    df["Содержание отчета (сокр.)"] = df["Содержание отчета (полн.)"].apply(
        lambda x: x[:25] + "..." if len(x) > 25 else x
    )
    df["ФИО"] = (
        df["Фамилия"]
        + " "
        + df["Имя"].str.slice(0, 1)
        + ". "
        + df["Отчество"].str.slice(0, 1)
        + ". "
    )
    df["ФИО (полное)"] = df["Фамилия"] + " " + df["Имя"] + " " + df["Отчество"]
    df.drop(columns=["Фамилия", "Имя", "Отчество"], inplace=True)

    if mode == "single":
        return df[single_report_columns]
    if mode == "multi":
        return df[multi_reports_columns]


def get_tickets_info(
    return_df=True,
    mode="multi",
    query_filter="all",
    limit=5,
    offset=0,
    ticket_uuid=None,
    user_id=None,
):
    conn = db_connection.get_conn()
    query_string, len_query_string = get_query_strings(
        mode=mode,
        limit=limit,
        offset=offset,
        user_id=user_id,
        ticket_uuid=ticket_uuid,
        query_filter=query_filter,
    )

    records = pd.read_sql(len_query_string, conn)["count"].tolist()[0]

    # print(query_string)

    df = pd.read_sql_query(
        query_string,
        conn,
    )

    if len(df) == 0:
        df = pd.DataFrame(columns=["id", "По данному запросу нет данных"])

    # return only needed data
    if return_df:
        return filter_and_rename_df(df, mode="multi"), records
    else:
        return filter_and_rename_df(df, mode="single").to_dict("records")[0]
