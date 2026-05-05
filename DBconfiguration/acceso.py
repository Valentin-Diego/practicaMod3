import os
import psycopg2
import getpass

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "credenciales"
DB_USER = "Admin"
DB_PASSWORD = "p4ssw0rdDB"

def conectar_db():
    try:
        return psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
    except Exception as e:
        print("Error de conexión:", e)
        return None

def obtener_datos_usuario(username, password):
    conn = conectar_db()
    if not conn:
        return

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT u.id_usuario, u.nombre, u.correo, u.telefono, u.fecha_nacimiento
                FROM credenciales c
                JOIN usuarios u ON c.id_usuario = u.id_usuario
                WHERE c.username = %s AND c.password_hash = %s
            """, (username, password))

            usuario = cursor.fetchone()

            if usuario:
                print("\nDatos del usuario encontrado:")
                print("ID:", usuario[0])
                print("Nombre:", usuario[1])
                print("Correo:", usuario[2])
                print("Teléfono:", usuario[3])
                print("Fecha:", usuario[4])
            else:
                print("\nUsuario o contraseña incorrectos")

    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    user = input("Usuario: ")
    pwd = getpass.getpass("Password: ")
    obtener_datos_usuario(user, pwd)
