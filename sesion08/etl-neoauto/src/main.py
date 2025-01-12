from prefect import flow
# from tasks.task_prueba import task_prueba
from tasks.task_extract_neoauto import task_extract_neoauto
from tasks.task_transform_neoauto import task_transform_neauto
from tasks.task_load_neoauto import task_load_neoauto

@flow(name="ETL prueba")
def main_flow():
    # task_prueba()
    
    # Paso 1: Extraer datos
    autos = task_extract_neoauto()

    #Paso 2: Transformar datos
    autos_transform = task_transform_neauto(autos)

    #Paso 3: Cargar datos
    task_load_neoauto(autos_transform)

if __name__ == "__main__":
    main_flow()