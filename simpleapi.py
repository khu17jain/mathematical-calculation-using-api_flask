from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)

api=Api(app)

indiancuisine=[]

class Cuisine(Resource):

    def get(self,name):
        for dishes in indiancuisine:
            if dishes['name'] == name:
                return dishes

        return {'name':None}

    def post(self,name):

        dishes={'name':name}
        indiancuisine.append(dishes)
        return dishes

    def delete(self,name):

        for ind,dishes in enumerate(indiancuisine):
            if dishes['name'] == name:
                 deleted_dishes = indiancuisine.pop(ind)
                 print(deleted_dishes)
                 return {'note':'delete successfully'}

class ALLNames(Resource):
    def get(self):
        return{'indiancuisine':indiancuisine}

api.add_resource(Cuisine,'/dish/<string:name>')
api.add_resource(ALLNames,'/indiancuisine')

if __name__ == "__main__":
 app.run(debug=True)
