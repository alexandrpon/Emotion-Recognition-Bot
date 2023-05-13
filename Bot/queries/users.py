from dbs.queries import execute_query, execute_read_query
from dbs.dbs_connect import connections


async def add_id_to_bd(id):
    if "users" in connections:
        connection = connections["users"]

        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE
        );
        """
        execute_query(connection, create_users_table)

        select_user_id = f"""
        SELECT user_id FROM users
        WHERE user_id = {id};
        """
        users_id = execute_read_query(connection, select_user_id)

        if users_id:
            pass
        else:
            create_users = f"""
            INSERT INTO users (user_id)
            VALUES ({id});
            """
            execute_query(connection, create_users)
