import requests

# URL base de la API
BASE_URL = "http://localhost:5000/api"

# Definir los encabezados de la solicitud
headers = {"Content-Type": "application/json"}

# Crear una nueva tarea
url = f"{BASE_URL}/tasks"
nueva_tarea = {"description": "Completar informe", "status": "Pendiente", "assignee": "Juan"}
response = requests.post(url, json=nueva_tarea, headers=headers)
print("Creando una nueva tarea:")
print(response.json())

# Crear la segunda tarea
tarea_2 = {"description": "Revisar presentación", "status": "En proceso", "assignee": "María"}
response = requests.post(url, json=tarea_2, headers=headers)
print("\nCreando la segunda tarea:")
print(response.json())

# Obtener la lista de todas las tareas
url = f"{BASE_URL}/tasks"
response = requests.get(url, headers=headers)
print("\nLista de tareas:")
print(response.json())

# Obtener una tarea específica por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/tasks/1"
response = requests.get(url, headers=headers)
print("\nDetalles de la tarea con ID 1:")
print(response.json())

# Actualizar una tarea existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/tasks/1"
datos_actualizacion = {"description": "Completar informe mensual", "status": "En proceso", "assignee": "Juan"}
response = requests.put(url, json=datos_actualizacion, headers=headers)
print("\nActualizando la tarea con ID 1:")
print(response.json())

# Eliminar una tarea existente por su ID (por ejemplo, ID=2)
url = f"{BASE_URL}/tasks/2"
response = requests.delete(url, headers=headers)
print("\nEliminando la tarea con ID 2:")
if response.status_code == 204:
    print(f"Tarea con ID 2 eliminada con éxito.")
else:
    print(f"Error: {response.status_code} - {response.text}")
