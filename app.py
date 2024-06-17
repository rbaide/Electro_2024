import csv
import streamlit as st

# Definir la base de datos de cursos con requisitos y horarios específicos
cursos = {
    "MAT101": {"nombre": "Introducción al Álgebra", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "ESP103": {"nombre": "Comunicación Oral y Escrita", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "SEL102": {"nombre": "Introducción a la Ingeniería en Electrónica", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "HIS101": {"nombre": "Historia de Honduras", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "MAT102": {"nombre": "Álgebra", "requisitos": ["MAT101"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "SOC101": {"nombre": "Sociología", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "LCC104": {"nombre": "Ofimática Avanzada", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "EIE1": {"nombre": "Electiva de Idioma Extranjero I", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "EIE2": {"nombre": "Electiva de Idioma Extranjero II", "requisitos": ["EIE1"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "EIE3": {"nombre": "Electiva de Idioma Extranjero III", "requisitos": ["EIE2"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "EIE4": {"nombre": "Electiva de Idioma Extranjero IV", "requisitos": ["EIE3"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "MAT103": {"nombre": "Geometría y Trigonometría", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "QUI101": {"nombre": "Química General", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "TLL314": {"nombre": "Metodología de la Investigación", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "MAT109": {"nombre": "Cálculo I", "requisitos": ["MAT101"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "MAT105": {"nombre": "Álgebra Lineal", "requisitos": ["MAT102"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "CCC207": {"nombre": "Programación para Ingeniería", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "MAT210": {"nombre": "Cálculo II", "requisitos": ["MAT109"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "FIS201": {"nombre": "Física I", "requisitos": ["MAT109"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "CCC212": {"nombre": "Programación de Sistemas", "requisitos": ["CCC207"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "MAT203": {"nombre": "Ecuaciones Diferenciales", "requisitos": ["MAT210"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "FIS202": {"nombre": "Física II", "requisitos": ["FIS201"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "MAT301": {"nombre": "Estadística Matemática I", "requisitos": ["MAT210"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "MAT209": {"nombre": "Variable Compleja", "requisitos": ["MAT210"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "FIS203": {"nombre": "Física III", "requisitos": ["FIS202"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "CIV103": {"nombre": "Dibujo para Ingeniería", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "BIO": {"nombre": "Electiva de Ciencias Naturales", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "SEL301": {"nombre": "Circuitos Eléctricos I", "requisitos": ["FIS202"], "horarios": ["Lunes, Miércoles y Viernes 6:00-7:30pm", "Lunes, Miércoles y Viernes 7:30-9:00pm", "Martes, Jueves y Sábado 6:00-7:30pm", "Martes, Jueves y Sábado 7:30-9:00pm"]},
    "TEL201": {"nombre": "Redes", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "FIL101": {"nombre": "Filosofía", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "ART/DEP": {"nombre": "Electiva de Arte o Deporte", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "SEL306": {"nombre": "Circuitos Eléctricos II", "requisitos": ["SEL301"], "horarios": ["Lunes, Miércoles y Viernes 6:00-7:30pm", "Lunes, Miércoles y Viernes 7:30-9:00pm", "Martes, Jueves y Sábado 6:00-7:30pm", "Martes, Jueves y Sábado 7:30-9:00pm"]},
    "SEL303": {"nombre": "Instalaciones Eléctricas", "requisitos": ["SEL301"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "SEL308": {"nombre": "Ingeniería de Control", "requisitos": ["SEL306"], "horarios": ["Lunes, Miércoles y Viernes 6:00-7:30pm", "Lunes, Miércoles y Viernes 7:30-9:00pm", "Martes, Jueves y Sábado 6:00-7:30pm", "Martes, Jueves y Sábado 7:30-9:00pm"]},
    "SEL309": {"nombre": "Electrónica II", "requisitos": ["SEL306"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "MEC306": {"nombre": "Sensores y Actuadores", "requisitos": ["SEL301"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "SEL401": {"nombre": "Control Digital", "requisitos": ["SEL308"], "horarios": ["Lunes, Miércoles y Viernes 6:00-7:30pm", "Lunes, Miércoles y Viernes 7:30-9:00pm", "Martes, Jueves y Sábado 6:00-7:30pm", "Martes, Jueves y Sábado 7:30-9:00pm"]},
    "SEL307": {"nombre": "Electrónica I", "requisitos": ["SEL306"], "horarios": ["Lunes, Miércoles y Viernes 6:00-7:30pm", "Lunes, Miércoles y Viernes 7:30-9:00pm", "Martes, Jueves y Sábado 6:00-7:30pm", "Martes, Jueves y Sábado 7:30-9:00pm"]},
    "SEL406": {"nombre": "Diseño de Sistemas Lógicos", "requisitos": ["SEL306"], "horarios": ["Lunes, Miércoles y Viernes 6:00-7:30pm", "Lunes, Miércoles y Viernes 7:30-9:00pm", "Martes, Jueves y Sábado 6:00-7:30pm", "Martes, Jueves y Sábado 7:30-9:00pm"]},
    "AMD102": {"nombre": "Administración I", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "EFESEL1": {"nombre": "Electiva de Formación Específica I", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "ENE402": {"nombre": "Máquinas Eléctricas", "requisitos": ["SEL306"], "horarios": ["Lunes, Miércoles y Viernes 6:00-7:30pm", "Lunes, Miércoles y Viernes 7:30-9:00pm", "Martes, Jueves y Sábado 6:00-7:30pm", "Martes, Jueves y Sábado 7:30-9:00pm"]},
    "SEL402": {"nombre": "Microprocesadores I", "requisitos": ["SEL306"], "horarios": ["Lunes, Miércoles y Viernes 6:00-7:30pm", "Lunes, Miércoles y Viernes 7:30-9:00pm", "Martes, Jueves y Sábado 6:00-7:30pm", "Martes, Jueves y Sábado 7:30-9:00pm"]},
    "CON319": {"nombre": "Contabilidad Gerencial", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "EFESEL2": {"nombre": "Electiva de Formación Específica II", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "SEL403": {"nombre": "Microprocesadores II", "requisitos": ["SEL402"], "horarios": ["Lunes, Miércoles y Viernes 6:00-7:30pm", "Lunes, Miércoles y Viernes 7:30-9:00pm", "Martes, Jueves y Sábado 6:00-7:30pm", "Martes, Jueves y Sábado 7:30-9:00pm"]},
    "SEL413": {"nombre": "Microelectrónica", "requisitos": ["SEL402"], "horarios": ["Lunes, Miércoles y Viernes 6:00-7:30pm", "Lunes, Miércoles y Viernes 7:30-9:00pm", "Martes, Jueves y Sábado 6:00-7:30pm", "Martes, Jueves y Sábado 7:30-9:00pm"]},
    "IND404": {"nombre": "Administración de Proyectos", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "SEL414": {"nombre": "Arquitectura de Computadoras", "requisitos": ["SEL402"], "horarios": ["Lunes, Miércoles y Viernes 6:00-7:30pm", "Lunes, Miércoles y Viernes 7:30-9:00pm", "Martes, Jueves y Sábado 6:00-7:30pm", "Martes, Jueves y Sábado 7:30-9:00pm"]},
    "SEL415": {"nombre": "Diseño de Sistemas Electrónicos", "requisitos": ["SEL402"], "horarios": ["Lunes, Miércoles y Viernes 6:00-7:30pm", "Lunes, Miércoles y Viernes 7:30-9:00pm", "Martes, Jueves y Sábado 6:00-7:30pm", "Martes, Jueves y Sábado 7:30-9:00pm"]},
    "SEL416": {"nombre": "Instrumentación y Control", "requisitos": ["SEL308"], "horarios": ["Lunes, Miércoles y Viernes 6:00-7:30pm", "Lunes, Miércoles y Viernes 7:30-9:00pm", "Martes, Jueves y Sábado 6:00-7:30pm", "Martes, Jueves y Sábado 7:30-9:00pm"]},
    "EMP401": {"nombre": "Generación de Empresas I", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "SEL491": {"nombre": "Proyecto Fase I", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "EMP402": {"nombre": "Generación de Empresas II", "requisitos": ["EMP401"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "SEL493": {"nombre": "Práctica Profesional", "requisitos": [], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]},
    "SEL492": {"nombre": "Proyecto Fase II", "requisitos": ["SEL491"], "horarios": ["Lunes y Miércoles 7:00-8:30", "Martes y Jueves 8:30-10:00", "Viernes 10:00-13:00", "Sábado 15:00-18:00", "Domingo 16:30-19:30"]}
}

def guardar_datos_estudiante(nombre, numero_cuenta, cursos_aprobados, cursos_seleccionados, horarios_seleccionados):
    with open('prematricula_estudiantes.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, numero_cuenta, ",".join(cursos_aprobados), ",".join(cursos_seleccionados), ",".join([f"{curso}:{horarios_seleccionados[curso]}" for curso in horarios_seleccionados])])

def validar_requisitos(cursos_seleccionados, cursos_aprobados):
    cursos_validados = []
    for curso in cursos_seleccionados:
        requisitos = cursos[curso]["requisitos"]
        if all(req in cursos_aprobados for req in requisitos):
            cursos_validados.append(curso)
        else:
            st.warning(f"No cumple con los requisitos para {cursos[curso]['nombre']}")
    return cursos_validados

st.title("Prematrícula Estudiantil")

nombre = st.text_input("Nombre Completo")
numero_cuenta = st.text_input("Número de Cuenta")

cursos_aprobados = []
cursos_seleccionados = []
horarios_seleccionados = {}

st.subheader("Seleccione los cursos que ya ha aprobado:")
for codigo, detalles in cursos.items():
    if st.checkbox(f"{detalles['nombre']} ({codigo})", key=f"aprobado_{codigo}"):
        cursos_aprobados.append(codigo)

st.subheader("Seleccione los cursos que desea matricular y sus horarios:")
for codigo, detalles in cursos.items():
    if st.checkbox(f"{detalles['nombre']} ({codigo})", key=f"matricular_{codigo}"):
        cursos_seleccionados.append(codigo)
        horario = st.selectbox(f"Seleccione un horario para {detalles['nombre']}", detalles['horarios'], key=f"horario_{codigo}")
        horarios_seleccionados[codigo] = horario

if st.button("Enviar"):
    if not nombre or not numero_cuenta:
        st.warning("Por favor, ingrese su nombre y número de cuenta.")
    elif not cursos_seleccionados:
        st.warning("Por favor, seleccione al menos un curso y su horario.")
    else:
        cursos_validados = validar_requisitos(cursos_seleccionados, cursos_aprobados)
        if cursos_validados:
            guardar_datos_estudiante(nombre, numero_cuenta, cursos_aprobados, cursos_validados, horarios_seleccionados)
            st.success("Datos enviados correctamente.")
