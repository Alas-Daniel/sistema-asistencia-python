import json
import os

RUTA_ALUMNOS = "data/alumnos.json"
RUTA_ASISTENCIAS = "data/asistencias.json"
RUTA_USUARIOS = "data/usuarios.json"

os.makedirs("data", exist_ok=True)
os.makedirs("codigos", exist_ok=True)

def cargar_datos(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_datos(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def agregar_alumno(nombre, codigo):
    alumnos = cargar_datos(RUTA_ALUMNOS)
    alumnos.append({"nombre": nombre, "codigo": codigo})
    guardar_datos(RUTA_ALUMNOS, alumnos)

def obtener_alumnos():
    return cargar_datos(RUTA_ALUMNOS)

def registrar_asistencia(codigo, fecha):
    asistencias = cargar_datos(RUTA_ASISTENCIAS)
    asistencias.append({"codigo": codigo, "fecha": fecha})
    guardar_datos(RUTA_ASISTENCIAS, asistencias)

def obtener_asistencias():
    return cargar_datos(RUTA_ASISTENCIAS)

def validar_usuario(usuario, password, rol=None):
    import os, json
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "data", "usuarios.json")

    with open(file_path, "r", encoding="utf-8") as f:
        usuarios = json.load(f)

    for u in usuarios:
        if u["usuario"] == usuario and u["password"] == password:
            if rol and u["rol"] != rol:
                return None
            return u 

    return None
