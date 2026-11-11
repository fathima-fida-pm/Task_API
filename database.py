import sqlite3

DB_PATH = "tasks.db"


def get_connection():

    connection = sqlite3.connect(DB_PATH)

    connection.row_factory = sqlite3.Row

    return connection


def create_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            description TEXT NOT NULL,

            priority TEXT NOT NULL
            CHECK(priority IN ('Low', 'Medium', 'High')),

            status TEXT NOT NULL
            CHECK(status IN ('Pending', 'In Progress', 'Completed'))

        )
    """)

    connection.commit()

    connection.close()