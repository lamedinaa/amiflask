from flask import Flask,json, Response
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config["SECRET_KEY"] = "my secret key"

class RecursoInfo(Resource):

    def get(self):
        print("hola mundo")
        message = json.dumps({"message":"prueba de server flaks port: 5000","message2":"hola mundo"})
        return Response(message,status=201,mimetype='application/json')



api.add_resource(RecursoInfo,"/api/info")



if __name__ == '__main__':
    app.run(debug=True)





