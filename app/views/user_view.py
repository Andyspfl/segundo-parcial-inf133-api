def render_user_list(users):
    # Representa una lista de dulces como una lista de diccionarios
    return [
        {
            "id": user.id,
            "name": user.name,
            "e-mail": user.email,
            "password": user.password,
            "roles": user.roles,
        }
        for user in users
    ]

def render_user_detail(user):
    # Representa los detalles de un dulce como un diccionario
    return {
            "id": user.id,
            "name": user.name,
            "e-mail": user.email,
            "password": user.password,
            "roles": user.roles,
        }
    

    