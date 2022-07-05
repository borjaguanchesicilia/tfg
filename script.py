import os

badget = "coverage.svg"

ficheros = []

os.system(
    "python3.6 -m coverage run -m pytest ./pruebas/controlador/t_c_parametros.py ./pruebas/controlador/t_c_etl.py ./pruebas/controlador/t_c_planificar.py ./pruebas/modelo/t_lectura_fichero.py ./pruebas/modelo/t_proceso_etl.py ./pruebas/modelo/t_modelo_matematico.py ./pruebas/modelo/t_modelo_matematico_resolver.py ./pruebas/t_funciones_aux.py ./pruebas/vistas/componentes/t_parametro_dia.py ./pruebas/vistas/componentes/t_scroll.py ./pruebas/vistas/componentes/t_barra_progreso.py"
)


os.system(f"rm {badget}")
os.system("coverage-badge -o coverage.svg")
