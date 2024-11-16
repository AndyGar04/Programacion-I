from flask import Blueprint, jsonify
from modelos.repositorios.repositorios import obtenerRepoTemasAlumnos

repo_temasAlumnos = obtenerRepoTemasAlumnos()

bp_temaAlumno = Blueprint("bp_temaAlumno", __name__)

@bp_temaAlumno.route("/examenesDisponibles/<int:idInterno>")
def obtener_examen(idInterno):
    temaAlumno = repo_temasAlumnos.obtenerPorAlumnoID(idInterno)
    if temaAlumno != None:
        return jsonify(temaAlumno.toDiccionario()), 200
    else:
        return jsonify({"mensaje":"Error, no se encontró el tema que debe rendir el alumno con ese ID"}), 404