import serial
import mysql.connector
import time

# Configura el puerto serial para Arduino
puerto_serial = "COM7"  # Cambia esto según el puerto de tu Arduino
baud_rate = 9600
arduino = serial.Serial(puerto_serial, baud_rate, timeout=1)

# Configuración de la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="miler",
    password="12345",
    database="acceso_instituto"
)
cursor = conexion.cursor()

# Consulta SQL
sentenciaPregunta = "SELECT * FROM nfc WHERE card_id = %s"

try:
    while True:
        # Lee datos del puerto serial
        if arduino.in_waiting > 0:
            card_id = arduino.readline().decode('utf-8').strip()  # Limpia espacios y saltos de línea
            print(f"Card ID leído: {card_id}")

            # Verifica el ID en la base de datos
            cursor.execute(sentenciaPregunta, (card_id,))
            resultado = cursor.fetchone()  # Recupera el primer resultado

            if resultado:
                print(f"Acceso permitido para: {resultado}")
                arduino.write(b'1')  # Envía un '1' para activar el relevador
            else:
                print("Acceso denegado. ID no encontrado.")
                arduino.write(b'0')  # Envía un '0' para denegar el acceso

            time.sleep(1)  # Pausa para evitar lecturas continuas

except KeyboardInterrupt:
    print("\nSaliendo del programa...")

except mysql.connector.Error as err:
    print(f"Error en la base de datos: {err}")

finally:
    # Cierra conexiones
    cursor.close()
    conexion.close()
    arduino.close()