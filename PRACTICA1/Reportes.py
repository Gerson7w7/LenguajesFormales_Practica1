def reportes(curso, alumnosL, alumnosL2, alumnosL3): #generación de reportes
    html = open("reporte.html", 'w')
    html.write("<!DOCTYPE html>"
               + "<html lang=\"en\">"
               + "<head>"
               + "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">"
               + "<meta name=\"name\" content=\"Reporte\"><!--nombre de la pagina-->"
               + "<meta name=\"description\" content=\"name\"><!--autor de la pagina-->"
               + "<meta name=\"keywods\" content=\"uno,dos,tres\"><!--Palabras claavez para, separadas por comas-->"
               + "<meta name=\"robots\" content=\"Index, Follow\"><!--Mejora la busqueda-->"
               + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><!--visibilidaad en diferentes pantallas -->"
               + "<link rel=\"stylesheet\" type=\"text/css\" href=\"css/styles.css\"/><!--css /estilo/tipo/ruta relativa -->"
               + "<title>Reporte</title><!--Titulo visible de la pagina-->"
               + "</head>"
               + "<body>"
               + "<center><!--centra todos lo que este dentro-->"
               + f"<h6 class=\"titulos\"><b> {curso.nombreCurso} </b></h6>")


    html.write( "<h2>Lista Desordenada</h2>"
                + "<!----tabla 2-->"
                + "<table class=\"steelBlueCols\">"
                + "<thead>"
                + "<tr> <th>Nombre</th> <th>Nota</th> </tr>"
                + "</thead>"
                + "<tbody>")
    for alumno in alumnosL3:
        if(alumno.nota >=61):
            html.write(f"<tr> <td>{alumno.nombre}</td> <td style=\"color: blue\">{str(alumno.nota)}</td> </tr>")
        else:
            html.write(f"<tr> <td>{alumno.nombre}</td> <td style=\"color: red\">{str(alumno.nota)}</td> </tr>")
    html.write("</tbody>"
                + "</table>")
    html.write("<br>  <br>  <br>")


    if("ASC" in curso.parametros):
        html.write( "<h2>Lista Ascendente</h2>"
                + "<!----tabla 2-->"
                + "<table class=\"steelBlueCols\">"
                + "<thead>"
                + "<tr> <th>Nombre</th> <th>Nota</th> </tr>"
                + "</thead>"
                + "<tbody>")
        for alumno in alumnosL2:
            if(alumno.nota >=61):
                html.write(f"<tr> <td>{alumno.nombre}</td> <td style=\"color: blue\">{str(alumno.nota)}</td> </tr>")
            else:
                html.write(f"<tr> <td>{alumno.nombre}</td> <td style=\"color: red\">{str(alumno.nota)}</td> </tr>")
        html.write("</tbody>"
                + "</table>")
    html.write("<br>  <br>  <br>")


    if ("DESC" in curso.parametros):
        html.write("<h2>Lista Descendente</h2>"
                + "<!----tabla 2-->"
                + "<table class=\"steelBlueCols\">"
                + "<thead>"
                + "<tr> <th>Nombre</th> <th>Nota</th> </tr>"
                + "</thead>"
                + "<tbody>")
        for alumno in alumnosL:
            if(alumno.nota >=61):
                html.write(f"<tr> <td>{alumno.nombre}</td> <td style=\"color: blue\">{str(alumno.nota)}</td> </tr>")
            else:
                html.write(f"<tr> <td>{alumno.nombre}</td> <td style=\"color: red\">{str(alumno.nota)}</td> </tr>")
        html.write("</tbody>"
                + "</table>")
    html.write("<br>  <br>  <br>" 
               + "<!----Espacio 1-->"
               + "<div>"
               + "<br>" 
               + "<h6> Parametros: </h6>"
               + "<br>")
    if("AVG" in curso.parametros):
        html.write(f"<h3>Promedio: {curso.promedio}</h3>")
    if("MIN" in curso.parametros):
        html.write(f"<h3>Nota minima: Nombre: {curso.min.nombre} Nota: {curso.min.nota}</h3>")
    if("MAX" in curso.parametros):
        html.write(f"<h3>Nota maxima: Nombre: {curso.max.nombre} Nota: {curso.max.nota}</h3>")   
    if("APR" in curso.parametros):
        html.write(f"<h3>Alumnos aprobados: {curso.aprobado}</h3>")  
    if("APR" in curso.parametros):
        html.write(f"<h3>Alumnos reprobado: {curso.reprobado}</h3>")                   
    html.write("<br>  <br>  <br>"
               + "</div>"
               + "<!--Termina espacio 1-->"
               + "</body>"
               + "</html>")