from database import get_connection

def create_task(task):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks
        (title, description, priority, status)

        VALUES (?, ?, ?, ?)
    """, (
        task.title,
        task.description,
        task.priority,
        task.status
    ))
    connection.commit()
    task_id = cursor.lastrowid
    connection.close()

    return get_task_by_id(task_id)

def get_all_tasks(status=None, priority=None):

    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM tasks"

    conditions = []
    values = []

    if status:
        conditions.append("status = ?")
        values.append(status)

    if priority:
        conditions.append("priority = ?")
        values.append(priority)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    cursor.execute(query, values)
    tasks = cursor.fetchall()
    connection.close()

    return [dict(task) for task in tasks]

def get_task_by_id(task_id):

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )
    task = cursor.fetchone()
    connection.close()

    return dict(task) if task else None

def update_task(task_id, updated_data):

    connection = get_connection()
    cursor = connection.cursor()
    fields = []
    values = []

    for key, value in updated_data.items():
        fields.append(f"{key} = ?")
        values.append(value)

    query = f"""
        UPDATE tasks
        SET {", ".join(fields)}
        WHERE id = ?
    """
    values.append(task_id)
    cursor.execute(query, values)
    connection.commit()
    updated = cursor.rowcount
    connection.close()

    return updated

def delete_task(task_id):

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )
    connection.commit()
    deleted = cursor.rowcount > 0
    connection.close()
    return deleted