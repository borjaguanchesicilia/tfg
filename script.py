import os

badget = "coverage.svg"

ficheros = []

os.system(
    "python3.6 -m coverage run -m pytest ./pruebas/controlador/t_c_parametros.py ./pruebas/controlador/t_c_etl.py ./pruebas/modelo/t_lectura_fichero.py ./pruebas/t_funciones_aux.py"
)


os.system(f"rm {badget}")
os.system("coverage-badge -o coverage.svg")
