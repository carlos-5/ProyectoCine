from read_json import read_clientes, read_movies, read_employees, read_movies, read_room
from Pila import Pila
from classes import Client, Movie, Employee, Room, Cash_registrer
import os
import random

class Main:

    def __init__(self):
        self.movies = []
        self.clients_stack = Pila()
        self.fillStack()
        self.fillMovies()
        self.fillEmployees()
        self.fillRooms()
        self.pointer = self.clients_stack.top 
        self.serve_clients = []
        self.boxes = []
        for i in range(0, 5):
            box = Cash_registrer()
            self.boxes.append(box)


    def fillRooms(self):
        data = read_room()
        self.rooms = []
        for room in data:
            new_room = Room()
            new_room.num = room['num']
            new_room.tickets = room['tickets'] 
            new_room.max = room['max']
            p1 = room['d1']
            p2 = room['d2']
            p3 = room['d3']
            list_ = [p1, p2, p3]
            new_room.dimensions = list_
            self.rooms.append(new_room)


    def fillEmployees(self):
        data = read_employees()
        emps = []
        for emp in data:
            new_emp = Employee()
            new_emp.name = emp['name']
            new_emp.salary = emp['salary'] 
            new_emp.job = emp['job']
            new_emp.packages = emp['packages']
            new_emp.extra_hours = emp['extra_hours']
            new_emp.membership = emp['membership']
            emps.append(new_emp)

        self.sales_clerks = [emp for emp in emps if emp.job == "Ventas"]
        self.maint_employees = [emp for emp in emps if emp.job == "Mante"]
        self.admin_employees = [emp for emp in emps if emp.job == "Admin"]




    def fillMovies(self):
        data = read_movies()
        for movie in data:
            new_movie = Movie()
            new_movie.name = movie['name']
            new_movie.raised = movie['raised']
            new_movie.raised = int(new_movie.raised)
            new_movie.tickets = movie['tickets']
            self.movies.append(new_movie)



    def fillStack(self):
        data = read_clientes()
        for client in data:
            new_client = Client()
            new_client.sex = client['Sexo']
            new_client.age = client['Edad']
            new_client.pregnant = client['Embarazada']
            self.clients_stack.apilar(new_client)


    def print_movies(self):
        print("Movies in billboard")
        pos = 0
        for movie in self.movies:
            print(f"[{pos+1}] >> Pelicula: {movie.name}")
            pos += 1

    def print_rooms(self):
        print("---- Salas -----")
        for i in self.rooms:
            print(f"room No.{i.num} ")
        
    def buy_ticket(self):
        to_pay = 0
        box_pos = self.box_service()
        seller = self.sales_clerks[box_pos]
        print(f"Siendo atendido en caja No.{box_pos} por el vendedor: {seller.name}")

        self.print_movies()
        selected_movie = int(input("seleccione una pelicula por su numero: "))
        selected_movie -= 1
        print(self.movies[selected_movie])


        self.print_rooms()
        room_selected = int(input("sala seleccionada: "))
        room_selected -= 1
        print(f"[1]- 2D Q.{self.rooms[room_selected].dimensions[0]}", end="")
        print(f"  [2]- 3D Q.{self.rooms[room_selected].dimensions[1]}", end="")
        print(f"  [3]- 4D Q.{self.rooms[room_selected].dimensions[2]}")
        dim = int(input("Dimension seleccioanda: "))
        while dim>=4:
            print("ERROR NO EXISTE ESA OPCION DE DIMENSION DE PELICULA")
            os.system("Pause")
            dim = int(input("Dimension seleccioanda: "))
        else:
            if dim == 1:
                to_pay += int(self.rooms[room_selected].dimensions[0])
            elif dim == 2:
                to_pay += int(self.rooms[room_selected].dimensions[1])
            else:
                to_pay += int(self.rooms[room_selected].dimensions[2])

            tickets = int(input("Ingrese cantidad de Tickets: "))
        while tickets>10:
            print("ERROR NUMERO DE TICKETS PERMITIDOS SON 10")
            os.system("Pause")
            tickets = int(input("Ingrese cantidad de Tickets: "))
        else:        
            to_pay = to_pay * tickets
            self.boxes[box_pos].tickets += tickets
            self.boxes[box_pos].profits += to_pay
            self.pointer.client.tikets += tickets
            self.serve_clients.append(self.pointer.client)
            self.pointer = self.pointer.next


        
            self.movies[selected_movie].raised += int(to_pay) 
            self.movies[selected_movie].tickets += tickets 
            print("Muchas gracias por su compra")
            os.system("Pause")





    def box_service(self):
        return random.randint(0, 5)


    def printEmployees(self):
        for emp in self.sales_clerks:
            total = (emp.membership * 45) * 0.05
            total += (emp.packages * 25000) * 0.025
            total += int(emp.salary)
            print(f"Emp: {emp.name}   , salary: {total}")

        for emp in self.maint_employees:
            total = 75 * emp.extra_hours 
            total += int(emp.salary)
            print(f"Emp: {emp.name}   , salary: {total}")

        for emp in self.admin_employees:
            print(f"Emp: {emp.name}   , salary: {emp.salary}")


    def print_boxes(self):
        print("=== CAJAS ====")
        for i in self.boxes:
            print(f"#{i.num}, total de tickets: {i.tickets}")


    def print_movies_data(self):
        print("==== Peliculas ====")
        for i in self.movies:
            print(f"Nombre: {i.name} , tickets: {i.tickets}")

    def get_porc(self):
        if len(self.serve_clients) == 0:
            print("No se ha atendido a ningun cliente ")
            return;
        c1 = 0
        c2 = 0
        for i in self.serve_clients:
            if i.sex == "M": c1 += 1;
            else: c2 += 1;

        p_men = int((c1/len(self.serve_clients)*100))
        p_women = int((c2/len(self.serve_clients)*100))
        print(f"Hombres: {p_men}% y Mujeres: {p_women}%")

            







    def options_menu(self):
        print("*****BINVENIDO AL CINE*******")
        print("1- Comprar ticket de Pelicula")
        print("2- Lista de los Empleados")
        print("3- Lista de las Peliculas")
        print("4- Salir")
        print("*****************************")


    def principal_menu(self):
        while True:
            os.system("cls")
            self.options_menu()
            op = int(input("option: "))
            if(op == 1):
                os.system("cls")
                self.buy_ticket()
            elif op == 2:
                os.system("cls")
                self.printEmployees()
                self.print_boxes()
                os.system("pause")
            elif op == 3:
                os.system("cls")
                self.print_movies_data()
                self.get_porc()
                os.system("pause")
            else:
                salir=int(input("¿Desea Salir?\n 1- Si\n 2- No\n"))
                if salir==1:
                   break;








principal = Main()
principal.principal_menu()

