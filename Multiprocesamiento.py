# Importaciones necesarias
import multiprocessing
import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor
import pandas as pd

# Carga de datos desde un archivo CSV
datos_df = pd.read_csv('path_to_your_dataset.csv')
datos = datos_df['column_name'].tolist()  # Asegúrate de ajustar 'column_name' al nombre de tu columna de datos

# Definición de funciones para operaciones
def calcular_estadisticas(datos):
    print(f"Media: {np.mean(datos)}, Desviación Estándar: {np.std(datos)}")

def limpiar_datos(datos):
    datos_limpio = list(set(datos))
    print(f"Datos limpiados: {len(datos_limpio)} registros únicos.")

# Definición de funciones para ejecución de operaciones usando multiprocessing
def ejecutar_con_multiprocessing(func, datos, num_procesos):
    pool = multiprocessing.Pool(processes=num_procesos)
    inicio = time.time()
    pool.apply(func, args=(datos,))
    pool.close()
    pool.join()
    print(f"Multiprocessing - Tiempo de ejecución para {num_procesos} procesos: {time.time() - inicio} segundos")

# Definición de funciones para ejecución de operaciones usando threading
def ejecutar_con_threading(func, datos, num_threads):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        inicio = time.time()
        future = executor.submit(func, datos)
        resultado = future.result()
    print(f"Threading - Tiempo de ejecución para {num_threads} hilos: {time.time() - inicio} segundos")

# Ejecución principal
if __name__ == '__main__':
    print("Ejecución usando Multiprocessing:")
    for num_procesos in [2, 4, 6]:
        ejecutar_con_multiprocessing(calcular_estadisticas, datos, num_procesos)
        ejecutar_con_multiprocessing(limpiar_datos, datos, num_procesos)

    print("Ejecución usando Threading:")
    for num_threads in [2, 4, 6]:
        ejecutar_con_threading(calcular_estadisticas, datos, num_threads)
        ejecutar_con_threading(limpiar_datos, datos, num_threads)
