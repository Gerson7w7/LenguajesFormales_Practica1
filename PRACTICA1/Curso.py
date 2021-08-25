class Curso(object):
    def __init__(self, nombreCurso, parametros, promedio, min, max, aprobado, reprobado, lleno):
        self.nombreCurso = nombreCurso
        self.parametros = parametros
        self.promedio = promedio
        self.min = min
        self.max = max
        self.aprobado = aprobado
        self.reprobado = reprobado
        self.lleno = lleno