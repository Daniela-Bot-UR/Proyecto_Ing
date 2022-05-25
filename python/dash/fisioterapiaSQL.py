def horas_trabajadas():
    return """select p.nombre, sum(date_part('hour', hora_fin_horario-hora_inicio_horario )) as horas
    from profesor as p inner join grupo_profesor as gp on(p.cedula =gp.cedula_profesor)
    inner join horario_grupo as hg on(gp.id_grupo_grupo=hg.id_grupo_grupo and gp.codigo_asignatura_grupo=hg.codigo_asignatura_grupo)
    where p.nombre is not null
    group by p.nombre
    order by(horas) desc
    limit 10;"""

def estudiantes_esperados():
    return """select a.nombre, sum (g.capacidad) as cantidad_esperada
from asignatura as a inner join grupo as g on(a.codigo=g.codigo_asignatura)
group by(a.nombre);"""

def falta_de_profesor():
    return """select a.nombre, count (p.cedula) as vacante
from asignatura as a inner join grupo as g on(a.codigo=g.codigo_asignatura)
                    inner join grupo_profesor as gp on(g.id_grupo=gp.id_grupo_grupo and g.codigo_asignatura=gp.codigo_asignatura_grupo)
                    inner join profesor as p on(gp.cedula_profesor=p.cedula)
        where p.nombre is null
        group by(a.nombre);"""
            
def clases_escalafon():
    return """select ec.tipo_escalafon, count(g.id_grupo) as cantidad
from profesor p inner join escalafon ec on(ec.id=p.id_escalafon)
                inner join grupo_profesor gp on(p.cedula=gp.cedula_profesor)
                inner join grupo g on(gp.id_grupo_grupo=g.id_grupo and gp.codigo_asignatura_grupo=g.codigo_asignatura)
        where ec.tipo_escalafon != '0'
        group by(ec.tipo_escalafon);"""