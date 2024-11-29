import psycopg2


class PostgreSQLConnection:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Conexión exitosa")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Desconexión exitosa")

    def execute_query(self, query, parameters=None):
        if not self.connection:
            print("Error: No hay conexión a la base de datos.")
            return

        try:
            with self.connection.cursor() as cursor:
                if parameters:
                    cursor.execute(query, parameters)
                else:
                    cursor.execute(query)

                result = cursor.fetchall()
                return result
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None


    def execute_update(self,query,params=None):
        try:

            self.session.execute(query, params)

            self.session.commit()
        except Exception as e:
            print(e)
