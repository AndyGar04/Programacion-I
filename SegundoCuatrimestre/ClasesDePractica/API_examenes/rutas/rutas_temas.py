from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorios import obtenerRepoTemas
from modelos.entidades.tema import Tema

repo_temas = obtenerRepoTemas()

bp_temas = Blueprint("bp_temas", __name__)

@bp_temas.route("/temas", methods=["GET"])
def obtener_todos():
    return jsonify([tema.toDiccionario() for tema in repo_temas.obtenerTodos()]), 200

@bp_temas.route("/temas", methods =["POST"])
def agregar_tema():
    if request.is_json:
        diccDatos = request.get_json()
        if "numero" in diccDatos and "nombre" in diccDatos and "enunciado" in diccDatos:
            if not repo_temas.existeTemaNumero(diccDatos["numero"]):
                tema=Tema.fromDiccionario(diccDatos)
                repo_temas.agregar(tema)
                respuesta = {"mensaje":"Tema agregado exitosamente", "tema": tema.toDiccionario()}
                codigoRespuesta=201
            else:
                respuesta = {"mensaje":"Ya existe un tema con ese numero"}
                codigoRespuesta=400
        else:
            respuesta = {"error":"Se requieren los datos 'numero', 'nombre' y 'enunciado' en el JSON"}
            codigoRespuesta=400
    else:
        respuesta = {"error":"Se requieren los datos en JSON"}
        codigoRespuesta=400
    return jsonify(respuesta), codigoRespuesta