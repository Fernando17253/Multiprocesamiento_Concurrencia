import multiprocessing
import numpy as np
import time

def calcular_estadisticas(datos):
    print(f"Media: {np.mean(datos)}, Desviación Estándar: {np.std(datos)}")

def limpiar_datos(datos):
    datos_limpio = list(set(datos))
    print(f"Datos limpiados: {len(datos_limpio)} registros únicos.")

def ejecutar_operacion(func, datos, num_procesos):
    pool = multiprocessing.Pool(processes=num_procesos)
    inicio = time.time()
    pool.apply(func, args=(datos,))
    pool.close()
    pool.join()
    print(f"Tiempo de ejecución para {num_procesos} procesos: {time.time() - inicio} segundos")

datos = np.random.randint(1, 100, size=10000).tolist()

if __name__ == '__main__':
    for num_procesos in [2, 4, 6]:
        ejecutar_operacion(calcular_estadisticas, datos, num_procesos)
        ejecutar_operacion(limpiar_datos, datos, num_procesos)
