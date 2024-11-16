from flask import Flask
from rutas.rutas_alumnos import bp_alumnos
from rutas.rutas_temasAlumnos import bp_temaAlumno
from rutas.rutas_temas import bp_temas
from rutas.rutas_examenesConfirmados import bp_examenes

app = Flask(__name__)

app.register_blueprint(bp_alumnos)
app.register_blueprint(bp_temaAlumno)
app.register_blueprint(bp_temas)
app.register_blueprint(bp_examenes)

if __name__=="__main__":
    app.run(debug=True)