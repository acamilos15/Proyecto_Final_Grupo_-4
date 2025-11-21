import pandas as pd

def promedios(archivo, columna):
    try:
        df = pd.read_csv(archivo)
        return df[columna].mean()
    except Exception as e:
        print("Error al procesar la columna:", e)
        return None
    


def desviacion(archivo, columna):
    try:
        df = pd.read_csv(archivo) 
        return df[columna].std()
    except Exception as e:
        print("Error al procesar la columna:", e)
        return None

import pandas as pd

def percentiles(archivo, columna):
    try:
        # Intentamos leer el archivo
        df = pd.read_csv(archivo)
        
        # Verificamos si la columna existe
        if columna not in df.columns:
            return 'Error al procesar la columna'
        
        datos = df[columna]
        
        # Calculamos los percentiles requeridos (25, 50, 75)
        p25 = datos.quantile(0.25)
        p50 = datos.quantile(0.50)
        p75 = datos.quantile(0.75)
        
        return {
            'percentil_25': round(float(p25), 2),
            'percentil_50': round(float(p50), 2),
            'percentil_75': round(float(p75), 2)
        }
        
    except Exception:
        # Captura errores de lectura de archivo o cualquier otro fallo
        return 'Error al procesar la columna'