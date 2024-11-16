from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorios import obtenerRepoExamenesConfirmados
from modelos.entidades.temaAlumno import TemaAlumno

repo_examenesConfirmados = obtenerRepoExamenesConfirmados()

bp_examenes = Blueprint("bp_examenes", __name__)

@bp_examenes.route("/examenesConfirmados", methods=["POST"])
def agregar_confirmacion():
    if request.is_json:
        datos = request.get_json()
        #VALIDACIONES!!
        repo_examenesConfirmados.agregar(TemaAlumno.fromDiccionario(datos))
        return jsonify({"mensaje":"Confirmado con exito"}), 201
    else:
        return jsonify({"error":"error al confirmar"}), 400