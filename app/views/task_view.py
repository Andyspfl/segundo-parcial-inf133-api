def render_task_list(tasks):
    # Representa una lista de tareas como una lista de diccionarios
    return [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "created_at": task.created_at,
            "assigned_to": task.assigned_to
        }
        for task in tasks
    ]

def render_task_detail(task):
    # Representa los detalles de una tarea como un diccionario
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "created_at": task.created_at,
        "assigned_to": task.assigned_to
    }
    