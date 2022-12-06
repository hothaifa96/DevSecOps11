import json

from flask import Flask, request

app = Flask(__name__)

cars=[{'id':1,'make':'audi','model':'A7','year':2022},
      {'id':2,'make':'bmw','model':'x6','year':2021},
      {'id':3,'make':'volvo','model':'s90','year':2012},
      {'id':4,'make':'mazda','model':'3','year':2015},
      {'id':5,'make':'skoda','model':'octavia vrs','year':2023}]

@app.route('/',methods=['GET'])
def home():
      return ' <button style="color:red;"> i love DevOps </button> '

@app.route('/cars',methods=['GET'])
def getCars():
      return json.dumps(cars)

@app.route('/cars/<int:id>', methods=['GET'])
def getCar(id):
      return json.dumps(cars[id-1])

@app.route('/cars/<int:id>', methods=['DELETE'])
def deleteCar(id):
      for car in cars:
            if car['id']==id:
                  cars.remove(car)

      return json.dumps(cars)


@app.route('/cars',methods=['POST'])
def addCar():
      car = request.json
      cars.append(car);
      return "sir yes sir"

@app.route('/cars/<int:id>',methods=['PUT'])
def updateCar(id):
      newCar = request.json
      for car in cars:
            if car['id']==id:
                  cars.remove(car)
      cars.append(newCar)
      return 'updated',299

app.run()



# open another python file called foods
# build a new api using flask and python
# this apu must have 5 functions
# the functions are:
# getFood
# deleteFood   recives id
# updateFood   recives id
# addFood
# getFoodByID  recives id

# build a dockerfile for each one of the API's
#
# build anew k8s cluster (minikube) thats have 2 deployments each
# with 1 replicas of the pod
# build a service for each deployment
# use 2 diff ports to get to the pods
# one port used to get to the cars api
# the other one used to get to the food api
