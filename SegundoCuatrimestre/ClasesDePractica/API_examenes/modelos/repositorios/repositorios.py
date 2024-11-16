from modelos.repositorios.repositorio_alumnos import RepositorioAlumno
from modelos.repositorios.repositorio_temas import RepositorioTema
from modelos.repositorios.repositorio_temaAlumno import RepositorioTemasAlumnos
from modelos.repositorios.repositorio_examenesConfirmados import RepositorioExamenesConfirmados
repo_alumnos = None
repo_temas =None
repo_temaAlumnos = None
repo_examenesConfirmados =None

def obtenerRepoAlumnos()-> RepositorioAlumno:
    global repo_alumnos
    if not isinstance(repo_alumnos, RepositorioAlumno):
        repo_alumnos = RepositorioAlumno()
    return repo_alumnos

def obtenerRepoTemas()-> RepositorioTema:
    global repo_temas
    if not isinstance(repo_temas, RepositorioTema):
        repo_temas = RepositorioTema()
    return repo_temas

def obtenerRepoTemasAlumnos()-> RepositorioTemasAlumnos:
    global repo_temaAlumnos
    if not isinstance(repo_temaAlumnos, RepositorioTemasAlumnos):
        repo_temaAlumnos = RepositorioTemasAlumnos()
    return repo_temaAlumnos

def obtenerRepoExamenesConfirmados()-> RepositorioExamenesConfirmados:
    global repo_examenesConfirmados
    if not isinstance(repo_examenesConfirmados, RepositorioExamenesConfirmados):
        repo_examenesConfirmados = RepositorioExamenesConfirmados()
    return repo_examenesConfirmados