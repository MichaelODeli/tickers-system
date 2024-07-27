from controllers import db_connection
import pandas as pd


def get_query_string(all=False, limit=None, offset=None, ticket_uuid=''):
    table_name = "tickets" if all else f"(select * from tickets where uuid = '{ticket_uuid}')"
    limits = f"LIMIT {limit} OFFSET {offset}" if all  else ""

    query_string = f"""SELECT * FROM {table_name} t 
    left join (select id as probl_id, problem_name from problems_list) p on t.problem_id = p.probl_id 
    left join (select id as prior_id, priority_name from priority_list) d on d.prior_id = t.priority_id 
    left join (select id as rep_id, username from users) u on u.rep_id = t.reporter_id 
    ORDER BY priority_id DESC, created_at DESC 
    {limits};""".replace('\n', '')

    return query_string


def get_tickets_info(return_df=True, limit=None, offset=None, ticket_uuid=None):
    conn = db_connection.get_conn()

    # query only needed data
    if return_df:
        df = pd.read_sql_query(
            get_query_string(all=True, limit=limit, offset=offset), conn
        )
    else:
        df = pd.read_sql_query(
            get_query_string(ticket_uuid=ticket_uuid), conn
        )

    # prepare, rename and delete columns
    df["id"] = df["uuid"]
    df["created_at"] = df["created_at"].dt.strftime("%H:%M:%S %d.%m.%Y")
    df.drop(columns=['prior_id', 'priority_id', 'probl_id', 'problem_id', 'rep_id', 'reporter_id'], inplace=True)


    # return only needed data
    if return_df:
        df["text"] = df["text"].apply(
            lambda x: x[:15] + "..." if len(x) > 15 else x
        )
        return df
    else:
        return df.to_dict('records')[0]


# print(get_query_string(all=True, limit=PAGE_SIZE, offset=start_record))
