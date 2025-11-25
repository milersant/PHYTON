import pandas as pd  # Importamos pandas para manejo de datos en tablas (DataFrames)

# --- LECTURA DE ARCHIVOS ---
# Cargamos las respuestas de los estudiantes desde un archivo CSV
df_estudiante = pd.read_csv("./archivos/respuestas_estudiantes.csv")

# Cargamos la clave de respuestas correctas desde un archivo Excel
df_correctas = pd.read_excel("./archivos/respuestas_correctas.xlsx")

# --- OBTENCIÓN DE PREGUNTAS ---
# Guardamos todas las preguntas en una lista (columna 'Pregunta')
preguntas = df_correctas['Pregunta'].values  

# --- CREACIÓN DE CLAVE DE RESPUESTAS ---
# Diccionario: { Pregunta : Respuesta Correcta }
clave_respuestas = {}
for i in range(df_correctas.shape[0]):  # recorremos fila por fila
    pregunta = df_correctas['Pregunta'].iloc[i]
    respuesta = df_correctas['Respuesta'].iloc[i]
    clave_respuestas[pregunta] = respuesta

# --- CALCULO DE PUNTUACIONES ---
# Inicializamos la puntuación de cada estudiante en 0
df_estudiante['Puntuacion'] = 0

# Recorremos todas las preguntas
for p in preguntas:  
    respuesta_correcta = clave_respuestas[p] 
    # Comparación: si coincide la respuesta del estudiante con la correcta → suma 1 punto
    df_estudiante['Puntuacion'] += (df_estudiante[p] == respuesta_correcta).astype(int)  

# --- CREACIÓN DE DATAFRAME DETALLADO ---
df_detalle = df_estudiante.copy()  # Copia del original para marcar aciertos y errores

# Recorremos cada pregunta
for p in preguntas:  
    # Si la respuesta es incorrecta → agregamos una "x" al final de la respuesta
    df_detalle[p] = df_detalle[p].where(
        df_detalle[p] == clave_respuestas[p],
        df_detalle[p] + 'x'
    )  

# Ordenamos los resultados por puntuación (de mayor a menor)
df_detalle = df_detalle.sort_values('Puntuacion', ascending=False)  

# --- SALIDA DE RESULTADOS ---
print("leyenda: Respuestax = incorrecta")
print(df_detalle.to_string(index=False))  # Muestra el detalle por pregunta

print("\n==resultado de los estudiantes==")
# Solo mostramos Nombre y Puntuacion ordenados
print(df_estudiante[['Nombre', 'Puntuacion']].sort_values('Puntuacion', ascending=False).to_string(index=False))

# --- GUARDAR RESULTADOS ---
# Guardamos en un nuevo archivo CSV las puntuaciones
df_estudiante.to_csv("resultados_examen.csv", index=False)
print("\nResultados guardados en resultados_examen.csv")
