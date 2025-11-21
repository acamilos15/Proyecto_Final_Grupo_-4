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

def percentiles(archivo, columna):
    try:
        df = pd.read_csv(archivo)
        
        if columna not in df.columns:
            return "No existe la comuna"
        
        datos = df[columna]

        
        p25 = datos.quantile(0.25)
        p50 = datos.quantile(0.50)
        p75 = datos.quantile(0.75)
        
        return {
            'percentil_25': round(float(p25), 2),
            'percentil_50': round(float(p50), 2),
            'percentil_75': round(float(p75), 2)
        }
        
    except:
        return "Error al procesar la columna"
