from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_mail import Mail, Message

import os

app = Flask(__name__, template_folder='templates', static_url_path='/static')

# Cargar las variables de entorno desde el archivo .env
load_dotenv()


# Obtener los valores de las variables de entorno
mongo_username = os.environ.get('MONGO_USERNAME')
mongo_password = os.environ.get('MONGO_PASSWORD')
mongo_cluster = os.environ.get('MONGO_CLUSTER')

mongo_uri = os.environ.get('MONGO_URI')
db_name = os.environ.get('DB_NAME')
collection_name = os.environ.get('COLLECTION_NAME')

client = MongoClient(mongo_uri)
db = client[db_name]
collection = db[collection_name]

#variable de entorno para correo
mail_server = os.environ.get('MAIL_SERVER')
mail_port = os.environ.get('MAIL_PORT')
mail_use_tls = os.environ.get('MAIL_USE_TLS')
mail_username = os.environ.get('MAIL_USERNAME')
mail_password = os.environ.get('MAIL_PASSWORD')
recipients = os.environ.get('RECIPIENTS_MAIL')

app.config['MAIL_SERVER'] = mail_server
app.config['MAIL_PORT'] = mail_port
app.config['MAIL_USE_TLS'] = mail_use_tls
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password 



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/es')
def index2():
    return render_template('es/index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    email = request.form['correo']
    mensaje = request.form['mensaje']

    # Guardar los datos en la base de datos
    data = {'nombre': nombre, 'email': email, 'mensaje': mensaje}
    collection.insert_one(data)
    enviar_correo(nombre, email, mensaje)

    return redirect(url_for('index', enviado='true'))

@app.route('/guardar-es', methods=['POST'])
def guardar2():
    nombre = request.form['nombre']
    email = request.form['correo']
    mensaje = request.form['mensaje'] 

    # Guardar los datos en la base de datos
    data = {'nombre': nombre, 'email': email, 'mensaje': mensaje}
    collection.insert_one(data)
    enviar_correo(nombre, email, mensaje)

    return redirect(url_for('index2', enviado='true'))

#envio de correo
mail = Mail(app)
def enviar_correo(nombre, correo, mensaje):
    msg = Message('Respuesta de formulario',  # Asunto del correo
                  sender=mail_username,  # Tu dirección de correo electrónico
                  recipients=[recipients ])  # Tu dirección de correo electrónico de destino
    msg.body = f"Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}"
    mail.send(msg)


#ejecucion local
#if __name__ == '__main__':
#    app.run()
