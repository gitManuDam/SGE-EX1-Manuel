from datetime import   datetime
nombre_fichero= datetime.now().strftime("%d-%m-%Y")
def escribir_log(tipo, mensaje):

    with open(f"log/{nombre_fichero}_log.txt","a") as file:
        file.write(f"{datetime.now()} {tipo} : {mensaje}\n")