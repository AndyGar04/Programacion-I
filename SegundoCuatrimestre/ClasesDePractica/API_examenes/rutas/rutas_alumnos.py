from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorios import obtenerRepoAlumnos
from modelos.entidades.alumno import Alumno

repostorio_alumnos = obtenerRepoAlumnos()

bp_alumnos = Blueprint("bp_alumnos", __name__)

@bp_alumnos.route("/alumnos", methods = ["GET"])
def obtener_todos_los_alumnos():
    lista_dicc = []
    for alumno in repostorio_alumnos.obtenerTodos():
        lista_dicc.append(alumno.toDiccionario())
    return jsonify(lista_dicc), 200

@bp_alumnos.route("/alumnos/<int:legajo>", methods =["GET"])
def obtener_alumno_por_legajo(legajo):
    alumno_encontrado = repostorio_alumnos.obtenerAlumnoPorLegajo(legajo)
    if alumno_encontrado is not None:
        return jsonify(alumno_encontrado.toDiccionario()), 200
    else:
        return jsonify({"mensaje":"No se encontro el legajo ingresado"}), 404
    
@bp_alumnos.route("/alumnos", methods =["POST"])
def agregar_alumno():
    if request.is_json:
        datos = request.json
        try:
            alumno = Alumno.fromDiccionario(datos)
        except Exception as e:
            return jsonify({"error":"No se pudo crear el alumno con los datos recibidos.\n" + str(e)}),400
        if not repostorio_alumnos.existeAlumnoConLegajo(alumno.obtenerLegajo()):
            if repostorio_alumnos.agregar(alumno):
                return jsonify({"mesaje":"Se agregó con éxito", "alumno": datos}), 201
            else:
                 return jsonify({"mesaje":"Error al agregar el alumno"}), 400
        else:
            return jsonify({"mesaje":"El legajo ya se encuentra registrado"}),400
    else: 
        return jsonify({"mesaje":"Error, los datos deben estar en formato json"}),400
    
# Alternativa en POST
def agregar_alumno_diccinoario():
    if request.is_json:
        datos = request.json
        if not repostorio_alumnos.existeAlumnoConLegajo(datos["legajo"]):
            if repostorio_alumnos.agregarDesdeDiccionario(datos):
                respuesta={"mesaje":"Se agregó con éxito", "alumno": datos}
                codgoRespuesta=201
            else:
                 respuesta ={"mesaje":"Error al agregar el alumno"}
                 codgoRespuesta=400
        else:
            respuesta={"mesaje":"El legajo ya se encuentra registrado"}
            codgoRespuesta=400
    else: 
        respuesta = {"mesaje":"Error, los datos deben estar en formato json"}
        codgoRespuesta=400
    return jsonify(respuesta), codgoRespuesta