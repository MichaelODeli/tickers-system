from controllers import db_connection
import pandas as pd


def get_query_string(all=False, limit=None, offset=None, ticket_uuid="", user_id=None):
    table_name = (
        "tickets" if all else f"(select * from tickets where uuid = '{ticket_uuid}')"
    )
    limits = f"LIMIT {limit} OFFSET {offset}" if all else ""
    where_userid = f"WHERE reporter_id = {user_id}" if user_id != None else ""

    query_string = f"""SELECT * FROM (SELECT * FROM {table_name} {where_userid}) t 
    left join (select id as probl_id, problem_name from problems_list) p on t.problem_id = p.probl_id 
    left join (select id as prior_id, priority_name from priority_list) pi on pi.prior_id = t.priority_id 
    left join (select id as rep_id, username, first_name, middle_name, last_name, position_id, email from users) u on u.rep_id = t.reporter_id 
    left join (select id as pos_id, department_id, position_name from positions) po on u.position_id = po.pos_id
    left join (select id as dep_id, department_name from departments) d on d.dep_id = po.department_id
    ORDER BY priority_id DESC, created_at DESC 
    {limits};""".replace(
        "\n", ""
    )

    return query_string


def get_tickets_info(return_df=True, limit=5, offset=0, ticket_uuid=None, user_id=None):
    conn = db_connection.get_conn()

    # query only needed data
    if return_df:
        df = pd.read_sql_query(
            get_query_string(all=True, limit=limit, offset=offset, user_id=user_id),
            conn,
        )
    else:
        df = pd.read_sql_query(get_query_string(ticket_uuid=ticket_uuid), conn)

    # prepare, rename and delete columns
    df["id"] = df["uuid"]
    df["created_at"] = df["created_at"].dt.strftime("%d.%m.%Y %H:%M:%S")
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
                "username",
                "uuid",
            ]
        ),
        inplace=True,
    )
    df.rename(
        columns={
            "created_at": "Дата и время создания",
            "priority_name": "Приоритет",
            "problem_name": "Название проблемы",
            "text": "Содержание отчета",
            "username": "Пользователь",
            "last_name": "Фамилия",
            "first_name": "Имя",
            "middle_name": "Отчество",
            "department_name": "Отдел",
            "position_name": "Должность",
            "email": "Почта для связи",
        },
        inplace=True,
    )


    # return only needed data
    if return_df:
        df["ФИО"] = (
            df["Фамилия"]
            + " "
            + df["Имя"].str.slice(0, 1)
            + ". "
            + df["Отчество"].str.slice(0, 1)
            + ". "
        )
        df.drop(
            columns=["Фамилия", "Имя", "Отчество", "Отдел", "Должность"], inplace=True
        )

        df["Содержание отчета"] = df["Содержание отчета"].apply(
            lambda x: x[:15] + "..." if len(x) > 15 else x
        )

        df = df[
            [
                'id',
                "Дата и время создания",
                "ФИО",
                "Название проблемы",
                "Приоритет",
                "Содержание отчета",
            ]
        ]

        return df
    else:
        df["ФИО"] = df["Фамилия"] + " " + df["Имя"] + " " + df["Отчество"]
        df.drop(columns=["Фамилия", "Имя", "Отчество"], inplace=True)

        df = df[
            [
                "id",
                "Дата и время создания",
                "ФИО",
                "Должность",
                "Отдел",
                "Приоритет",
                "Название проблемы",
                "Содержание отчета",
                'Почта для связи'
            ]
        ]

        return df.to_dict("records")[0]

