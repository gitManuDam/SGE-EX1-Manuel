from datetime import datetime

import gestionlog
from Administrador import Administrador
from Empleados import Empleados
import constantes as cons
import db
from sqlalchemy import text
import pandas as pd

from Recepcionista import Recepcionista
from constantes import UPDATE_ESTADO_VUELO, UPDATE_FECHA_DEF


def conexion ():
    db_config = {
        'dbname': cons.dbname,
        'user': cons.user,
        'password': cons.password,
        'host': cons.host,
        'port': cons.port,
    }
    return db_config


def crearConexion():
    db_config = conexion()
    db_connection = db.PostgreSQLConnection(**db_config)
    db_connection.connect()
    return db_connection

def vuelos_cliente(id_cliente):
    try:
        query = text(cons.QUERY_VUELOS_CLIENTE)
        result = db_connection.execute_query(query,{'id':id_cliente})
        if not result:
            print("No se ha encontrado ningun cliente\n")
        else:
            df = pd.DataFrame(result)
            print("VUELOS DEL CLIENTE "+id_cliente)
            print(df)
            print(df["idciudadorigen","idciudaddestino"] )
            gestionlog.escribir_log(cons.INFO,"Consulta vuelos de un cliente realizada")

    except Exception as e:
        print("Error, no hay conexion o el id es inválido\n")
        gestionlog.escribir_log(cons.ERROR,"Fallo al consultar")

def cliente_direccion(id_cliente):
    try:
        query = text(cons.QUERY_CLIENTE_DIRECCION)
        result = db_connection.execute_query(query,{'id':id_cliente})
        if not result:
            print("No se ha encontrado ningun cliente\n")
        else:
            print(result)
            gestionlog.escribir_log(cons.INFO, "Consulta direcciones de un cliente realizada")
    except Exception as e:
        print("Error, no hay conexion o el id es inválido\n")
        gestionlog.escribir_log(cons.ERROR, "Fallo al consultar")

def datos_vuelo(id_vuelo):
    try:
        query = text(cons.QUERY_VUELO_DATOS)
        result = db_connection.execute_query(query,{'id':id_vuelo})
        if not result:
            print("No se ha encontrado ningun cliente\n")
        else:
            df=pd.DataFrame(result)
            print(df)

            gestionlog.escribir_log(cons.INFO, "Consulta datos de un vuelo realizada")
    except Exception as e:
        print("Error, no hay conexion o el id es inválido\n")
        gestionlog.escribir_log(cons.ERROR, "Fallo al consultar")

def consultas_sobre_vuelo(df):
    while True:
        print("\n--- MENÚ ---")
        print("1. Usuario que mas ha pagado por el billete")
        print("2. Media de los billetes ")
        print("3. Salir")


        opcion = input("Elige una opcion")

        if opcion == "1":
            max = df["preciobillete"].max()
            print(df[df["preciobillete"]==max])

        elif opcion == "2":
            df['media']=df["preciobillete"].mean()
            print(df["media"])

        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break  # Salimos del bucle
        else:
            print("Opción no válida, intenta nuevamente.")

def actualizar_vuelo():
    try:
        db_connection.execute_update((text(UPDATE_FECHA_DEF),{'fechadef':datetime.now().strftime("%d/%m/%Y")}))
        db_connection.execute_update(text(UPDATE_ESTADO_VUELO))
        gestionlog.escribir_log(cons.INFO,"Datos de vuelos actualizados")
    except Exception as e:
        print("Fallo al actulizar")
        gestionlog.escribir_log(cons.ERROR,"Fallo al actulizar los vuelos")

def menu():

    empleados = Empleados()
    empleados.empleados.append(Administrador("Admin","admin@admin.com"))
    empleados.empleados.append(Recepcionista("Recepcionista","recep@gmail.com"))
    #añadir aqui a los empleados el admin y el recepcionista
    #cada vez que se realice una actualización o una consulta se deberá sumar 1.

    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar los vuelos de un cliente")
        print("2. Mostrar la dirección de un usuario")
        print("3. Vuelo de los pasajeros")
        print("4. Actualización de muertos")
        print("5. Salir")

        opcion= input("Elige una opcion")

        if opcion == "1":
            opcion2= int(input("Quien va a realizar la consulta Admin->0 o Recepcionista -> 1"))
            if opcion2 == 0:
                print("No tiene permiso")
                gestionlog.escribir_log(cons.ERROR,"Admin intenta realizar consulta")
            else:
                id_cliente=int(input("Dime el id del cliente"))
                vuelos_cliente(id_cliente)
                empleados.empleados[opcion2].num_consultas+=1

        elif opcion == "2":
            opcion2 = int(input("Quien va a realizar la consulta Admin->0 o Recepcionista -> 1"))
            if opcion2 == 0:
                print("No tiene permiso")
                gestionlog.escribir_log(cons.ERROR, "Admin intenta realizar consulta")
            else:
                id_cliente = int(input("Dime el id del cliente"))
                cliente_direccion(id_cliente)
                empleados.empleados[opcion2].num_consultas += 1
        elif opcion == "3":
            opcion2 = int(input("Quien va a realizar la consulta Admin->0 o Recepcionista -> 1"))
            if opcion2 == 0:
                print("No tiene permiso")
                gestionlog.escribir_log(cons.ERROR, "Admin intenta realizar consulta")
            else:
                id_vuelo = int(input("Dime el id del vuelo "))
                datos_vuelo(id_vuelo)
                empleados.empleados[opcion2].num_consultas += 1
        elif opcion == "4":
            opcion2 = int(input("Quien va a realizar la consulta Admin->0 o Recepcionista -> 1"))
            if opcion2 == 1:
                print("No tiene permiso")
                gestionlog.escribir_log(cons.ERROR, "Recepcionista intenta realizar actualizacion")
            else:
                actualizar_vuelo()
                empleados.empleados[0].num_actulizaciones+=1
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break  # Salimos del bucle
        else:
            print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    db_connection = crearConexion()


    menu()
