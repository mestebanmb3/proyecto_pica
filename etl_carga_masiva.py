import cx_Oracle
import psycopg2

# Conexión a Oracle
oracle_conn = cx_Oracle.connect("usuario_oracle", "contraseña_oracle", "nombre_host_oracle:puerto/servicio_oracle")

# Conexión a PostgreSQL
postgres_conn = psycopg2.connect(host="nombre_host_postgres", port="puerto_postgres", database="nombre_base_datos_postgres", user="usuario_postgres", password="contraseña_postgres")


oracle_cursor = oracle_conn.cursor()

# Ejemplo de consulta SQL para leer datos de una tabla en Oracle
oracle_cursor.execute("SELECT * FROM tabla_oracle")

# Obtener los resultados
oracle_data = oracle_cursor.fetchall()
 
postgres_cursor = postgres_conn.cursor()

# Ejemplo de carga masiva en una tabla en PostgreSQL
postgres_cursor.executemany("INSERT INTO tabla_postgres VALUES (%s, %s, %s)", postgres_data)

# Realiza la confirmación para guardar los cambios
postgres_conn.commit()

oracle_conn.close()
postgres_conn.close()