import os

badget = "coverage.svg"

ficheros = ['./pruebas/controlador/t_c_parametros.py',
' ./pruebas/controlador/t_c_etl.py',
' ./pruebas/controlador/t_c_planificar.py',
' ./pruebas/modelo/t_lectura_fichero.py',
' ./pruebas/modelo/t_proceso_etl.py',
' ./pruebas/modelo/t_modelo_matematico.py',
' ./pruebas/t_funciones_aux.py',
' ./pruebas/vistas/componentes/t_parametro_dia.py',
' ./pruebas/vistas/componentes/t_scroll.py',
' ./pruebas/vistas/componentes/t_barra_progreso.py']

pruebas = ''.join(str(fichero) for fichero in ficheros)

os.system(
    f'python3.6 -m coverage run -m pytest {pruebas}'
)

os.system(f"rm {badget}")
os.system("coverage-badge -o coverage.svg")