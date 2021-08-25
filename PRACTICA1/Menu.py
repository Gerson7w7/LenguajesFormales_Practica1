from tkinter.filedialog import askopenfilename
from Alumno import Alumno
from Curso import Curso
from Reportes import reportes


def cargarArchivo():  # carga el archivo que ingrese el usuario
    print("==================Cargar Archivo==================")
    file = askopenfilename()
    archivo = open(file, 'r')
    contenido = ""
    if(archivo.name[-4:] == ".lfp"):
        contenido = archivo.read()
        print("Archivos cargados! :D")
    else:
        print("Solo se admiten archivos con extensión .lfp")
    archivo.close()
    return contenido


def analizarArchivo(contenido):  # analiza y separa los datos del archivo
    tituloCuerpo = contenido.split("=")  # [0] titulo, [1] cuerpo
    nombreCurso = tituloCuerpo[0].strip()  # nombre del curso
    curso.nombreCurso = nombreCurso
    alumnosParam = tituloCuerpo[1].split("}")  # [0] alumnos, [1] parámetros
    alumnosStr = alumnosParam[0].replace("{", "")  # alumnos como string
    alumnos = alumnosStr.split(",")  # lista de alumnos
    for alumno in alumnos:  # separando cada alumno
        alumno = alumno.replace("<", "")
        alumno = alumno.replace(">", "")
        alumno = alumno.strip()
        datos = alumno.split(";")  # [0] nombre, [1] nota
        nombre = datos[0].replace('"', '')
        nota = int(datos[1].strip())
        # agregando a una lista de objetos cada
        alumnosL.append(Alumno(nombre, nota))
        alumnosL2.append(Alumno(nombre, nota))
        alumnosL3.append(Alumno(nombre, nota))
    alumnosParam[1] = alumnosParam[1].replace(" ", "")
    parametros = alumnosParam[1].split(",")  # lista de parámetros
    curso.parametros = parametros
    ejecutarContenido(parametros, alumnosL, alumnosL2)


# ejecuta los parametros del archivo
def ejecutarContenido(parametros, alumnosL, alumnosL2): 
    if("ASC" in parametros):
        bubbleSortASC(alumnosL2)
    if("DESC" in parametros):
        bubbleSortDESC(alumnosL)
    if("AVG" in parametros):
        promedioF(alumnosL)
    if("MIN" in parametros):
        if("ASC" in parametros):
            min = alumnosL2[0]
            curso.min = min
        else:
            min = alumnosL[-1]
            curso.min = min
    if("MAX" in parametros):
        if("ASC" in parametros):
            max = alumnosL2[-1]
            curso.max = max
        else:
            max = alumnosL[0]
            curso.max = max
    if("APR" in parametros or "REP" in parametros):
        aprobadosReprobados(alumnosL)


def bubbleSortASC(alumnosL):  # algoritmo de ordenamiento ascendente
    n = len(alumnosL)
    # itera cada elemento de la lista
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            # recorre la lista de 0 a n-i-1.
            # intercambia el elemento actual si
            # es mayor que el siguiente elemento.
            if alumnosL[j].nota > alumnosL[j+1].nota:
                alumnosL[j], alumnosL[j+1] = alumnosL[j+1], alumnosL[j]
                swapped = True
        # Si los elementos no se intercambian por el loop
        # entonces se para con un break
        if swapped == False:
            break


def bubbleSortDESC(alumnosL):  # algoritmo de ordenamiento descendiente
    n = len(alumnosL)
    # itera cada elemento de la lista
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            # recorre la lista de 0 a n-i-1.
            # intercambia el elemento actual si
            # es mayor que el siguiente elemento.
            if alumnosL[j].nota < alumnosL[j+1].nota:
                alumnosL[j], alumnosL[j+1] = alumnosL[j+1], alumnosL[j]
                swapped = True
        # Si los elementos no se intercambian por el loop
        # entonces se para con un break
        if swapped == False:
            break


def promedioF(alumnosL):  # promedio de las notas del curso
    suma = 0
    for alumno in alumnosL:
        suma += alumno.nota
    promedio = suma/len(alumnosL)
    curso.promedio = promedio


def aprobadosReprobados(alumnosL):  # número de alumnos aprobados y reprobados
    aprobados = 0
    reprobados = 0
    for alumno in alumnosL:
        if(alumno.nota >= 61):
            aprobados += 1
        else:
            reprobados += 1
    curso.aprobado = aprobados
    curso.reprobado = reprobados


def mostrarReporte(): # función para mostrar el reporte en consola
    nombreCurso = curso.nombreCurso
    print("==================== REPORTE ====================")
    print("Nombre del curso: " + nombreCurso)
    print("Alumnos: " + str(len(alumnosL)))
    print("")
    parametros = curso.parametros

    print("=========== Lista desordenada: ===========")
    for alumno in alumnosL3:
        print("Nombre: " + alumno.nombre + "\nNota: " + str(alumno.nota))
    print("")

    if("ASC" in parametros):
        print("=========== Lista ascendente: ===========")
        for alumno in alumnosL2:
            print("Nombre: " + alumno.nombre + "\nNota: " + str(alumno.nota))
    print("")

    if("DESC" in parametros):
        print("=========== Lista descendente: ===========")
        for alumno in alumnosL:
                print("Nombre: " + alumno.nombre + "\nNota: " + str(alumno.nota))
    
    print("")
    
    if("AVG" in parametros):
        print("Promedio: " + str(curso.promedio))
        print("")
    if("MIN" in parametros):
        print("Nota mínima: " + "\nNombre: " + curso.min.nombre + "Nota: " + str(curso.min.nota))
        print("")
    if("MAX" in parametros):
        print("Nota máxima: " + "\nNombre: " + curso.max.nombre + "Nota: " + str(curso.max.nota))
        print("")
    if("APR" in parametros):
        print("Alumnos aprobados: " + str(curso.aprobado))
        print("")
    if("REP" in parametros):
        print("Alumnos reprobados:" + str(curso.reprobado))
        print("")
        

# menú principal
# variables globales
alumnosL = list()
alumnosL2 = list() 
alumnosL3 = list() # desordenada 
curso = Curso("", [], 0, 0, 0, 0, 0, False)

while(True): 
    print("=====================Bienvenido!====================")
    print("¿Qué acción desea realizar?")
    print("1. Cargar archivo")
    print("2. Mostrar reporte")
    print("3. Exportar reporte")
    print("4. Salir")
    try:  # opciones del menú
        menu = int(input('Ingrese un número:\n'))
        print("\n")
        if(menu == 1):
            contenido = cargarArchivo()
            curso.lleno = True    
            if(contenido != ""):
                analizarArchivo(contenido)      
        elif(menu == 2):
            if(curso.lleno):
                mostrarReporte()
            else:
                print("No se ha cargado ningún arhcivo")
        elif(menu == 3):
            if(curso.lleno):
                reportes(curso, alumnosL, alumnosL2, alumnosL3)
                print("Reporte creado! :D")
            else:
                print("No se ha cargado ningún arhcivo")
        elif(menu == 4):
            exit()
        else:
            print("Opción fuera de rango\n\n")
    except ValueError:  # si no se ingresa un número, salta la excepción
        print("Ingrese un número.\n\n")