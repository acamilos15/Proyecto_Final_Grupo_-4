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
        return df['columna'].std()
    except Exception as e:
        print("Error al procesar la columna:", e)
        return None
    