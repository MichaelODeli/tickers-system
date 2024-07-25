from controllers import db_connection

def check_creditnals(username, password_hash):
    conn = db_connection.get_conn()
    with conn.cursor() as cursor:
        conn.autocommit = True
        cursor.execute(
            "SELECT id FROM users WHERE username=%(username)s and password=%(password)s;",
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
            (SELECT id as u_id, employee_id, first_name, middle_name, last_name, username, 
            email, department_id FROM users WHERE username = %(username)s) u 
            left join departments d on u.department_id = d.id;""",
            {"username": username},
        )
        desc = cursor.description
        column_names = [col[0] for col in desc]
        basic_user_data = [dict(zip(column_names, row)) for row in cursor.fetchall()][0]

        cursor.execute(
            "SELECT * FROM access_levels WHERE id = %(level_id)s;",
            {"level_id": basic_user_data['access_level']},
        )
        desc = cursor.description
        column_names = [col[0] for col in desc]
        access_data = [dict(zip(column_names, row)) for row in cursor.fetchall()][0]

        data = dict(list(basic_user_data.items()) + list(access_data.items()))
    
    return data