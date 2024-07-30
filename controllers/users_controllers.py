from controllers import db_connection

def check_creditnals(username, password_hash):
    conn = db_connection.get_conn()
    with conn.cursor() as cursor:
        conn.autocommit = True
        cursor.execute(
            "SELECT id FROM users WHERE username=%(username)s and password=%(password)s AND active;",
            {"username": username, "password": password_hash},
        )
        result = cursor.fetchone()
        if result != None:
            cursor.execute(
                "UPDATE users SET updated_at = NOW() + interval '2 hour' WHERE username=%(username)s;",
                {"username": username},
            )
            return True
        else:
            return False


def get_user_info(username):
    conn = db_connection.get_conn()
    with conn.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM 
                (
                    SELECT id as user_id, employee_id, first_name, middle_name, last_name, username, email, position_id 
                    FROM users WHERE username = %(username)s 
                ) u
                left join (select id as pos_id, department_id, access_level, position_name from positions) p on u.position_id = p.pos_id
                left join (select id as dep_id, department_name from departments) d on d.dep_id = p.department_id
                left join access_levels al on al.id = p.access_level;""",
            {"username": username},
        )
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in cursor.fetchall()][0]
    
    return data

def get_priority_list():
    conn = db_connection.get_conn()
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id::text as value, priority_name as label FROM priority_list WHERE active;"
        )
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in cursor.fetchall()]
    return data

def get_problems_list():
    conn = db_connection.get_conn()
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id::text as value, problem_name as label FROM problems_list WHERE active;"
        )
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in cursor.fetchall()]
    return data

def get_status_list():
    conn = db_connection.get_conn()
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id::text as value, status_name as label FROM status_list WHERE active;"
        )
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in cursor.fetchall()]
    return data