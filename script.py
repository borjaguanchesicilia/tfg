import os

badget = "coverage.svg"

os.system(
    "python3.6 -m coverage run -m pytest ./pruebas/controlador/t_c_parametros.py"
)

os.system(
    "python3.6 -m coverage run -m pytest ./pruebas/controlador/t_c_etl.py"
)

os.system(f"rm {badget}")
os.system("coverage-badge -o coverage.svg")
