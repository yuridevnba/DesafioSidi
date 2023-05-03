from flask import Flask, make_response,jsonify, request
#from bd import Carros
import mysql.connector

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False



cnx = mysql.connector.connect(user='yuri', password= 'euteamo345',
host='localhost',
database='sidi'
)


cursor = cnx.cursor()

@app.route("/verificar/<job_id>", methods=["GET"])
def check_job_id(job_id):
    sql = "SELECT id FROM vagas WHERE id = %s"
    job = (job_id,)
    cursor.execute(sql , job)
    resultado = cursor.fetchall()
    if(len(resultado) < 1):
        return 'Código da vaga não  existe, Por favor, verifique'
    else:
        return 'Código da vaga existe, pode prosseguir'




@app.route("/checartudo/user_id", methods=["GET"])
def get_job_messages(user_id):
    sql = "SELECT id_usuario,nome,email,formacao,tecnologias,experiencias_area,ingles, sidi FROM pergunas_obrigatorias"











if __name__ == '__main__':
    port = 8080 # Definindo a porta 8080
    app.run(port=port)



















































''''

@app.route('/carros', methods=['GET'])
def get_carros():
  return make_response(    
  jsonify(
     messagem='Lista de carros',
     dados=Carros
  )
      
   )

@app.route('/carros', methods=['POST'])
def create_carro():
  carro = request.json
  Carros.append(carro)
  return make_response(
    jsonify(
    
    mensagem='Carro cadastrado com sucesso.',
    carro = carro

    )
  )
   

app.run()

## esse arquivo vai ser colocado pra dentro do contêiner tb, onde tem comandos sql que cria a tabela e faz o insert no bd.
'''