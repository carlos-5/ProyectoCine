import json


def read_clientes():
        with open("C:\\ProyectoCine\\clients.json") as json_file:
            data = json.load(json_file)
            return data['clients']



def read_movies():
        with open("C:\\ProyectoCine\\movies.json") as json_file:
            data = json.load(json_file)
            return data['movies']




def read_room():
        with open("C:\\ProyectoCine\\rooms.json") as json_file:
            data = json.load(json_file)
            return data['rooms']

def read_employees():
        with open("C:\\ProyectoCine\\employees.json") as json_file:
            data = json.load(json_file)
            return data['employees']







