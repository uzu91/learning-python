from school_db import con, cur, sqlite3
import os 

status_menu = True
global status_op

def create_country(op):
    os.system('clear')

    name = input("Ingrese el nombre del país: ")
    abrev = input("Ingrese la abreviatura del país: ")
    descrip = input("Ingrese la descripción del país: ")
    cur.execute("INSERT INTO Country (name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", (name, abrev, descrip))
    con.commit()
    print("Registro de país creado con éxito.")

    os.system('pause')
    menu()

def create_department(op):
    os.system('clear')

    name = input("Ingrese el nombre del departamento: ")
    abrev = input("Ingrese la abreviatura del departamento: ")
    descrip = input("Ingrese la descripción del departamento: ")
    cur.execute("SELECT * from Country")
    print(cur.fetchall)
    id_country = input("Ingrese el ID del país al que pertenece el departamento: ")
    cur.execute("INSERT INTO Department (name, abrev, descrip, id_country, created_at, updated_at) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", 
                (name, abrev, descrip, id_country))
    con.commit()
    print("Registro de departamento creado con éxito.")

    os.system('pause')
    menu()

def create_city(op):
    os.system('clear')

    name = input("Ingrese el nombre de la ciudad: ")
    abrev = input("Ingrese la abreviatura de la ciudad: ")
    descrip = input("Ingrese la descripción de la ciudad: ")
    cur.execute("SELECT * from Department")
    print(cur.fetchall)
    id_depart = input("Ingrese el ID del departamento al que pertenece la ciudad: ")
    cur.execute("INSERT INTO City (name, abrev, descrip, id_depart, created_at, updated_at) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", 
                (name, abrev, descrip, id_depart))
    con.commit()
    print("Registro de ciudad creado con éxito.")

    os.system('pause')
    menu()

def create_identification_type(op):
    os.system('clear')

    name = input("Ingrese el nombre del tipo de identificación: ")
    abrev = input("Ingrese la abreviatura del tipo de identificación: ")
    descrip = input("Ingrese la descripción del tipo de identificación: ")
    cur.execute("INSERT INTO Identification_types (name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (name, abrev, descrip))
    con.commit()
    print("Registro de tipo de identificación creado con éxito.")

    os.system('pause')
    menu()

def create_person(op):
    os.system('clear')

    first_name = input("Ingrese el primer nombre de la persona: ")
    last_name = input("Ingrese el apellido de la persona: ")
    id_ident_type = input("Ingrese el ID del tipo de identificación de la persona: ")
    ident_number = input("Ingrese el número de identificación de la persona: ")
    id_exp_city = input("Ingrese el ID de la ciudad de expedición de la identificación: ")
    address = input("Ingrese la dirección de la persona: ")
    mobile = input("Ingrese el número de teléfono móvil de la persona: ")
    id_users = input("Ingrese el ID del usuario asociado a la persona: ")
    cur.execute("INSERT INTO Persons (first_name, last_name, id_ident_type, ident_number, id_exp_City, address, mobile, id_users, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (first_name, last_name, id_ident_type, ident_number, id_exp_city, address, mobile, id_users))
    con.commit()
    print("Registro de persona creado con éxito.")

    os.system('pause')
    menu()

def create_student(op):
    os.system('clear')

    code = input("Ingrese el código del estudiante: ")
    id_persons = input("Ingrese el ID del estudiante: ")
    cur.execute("INSERT INTO Students (code, id_persons, status, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (code, id_persons, 0))  # Estado predeterminado
    con.commit()
    print("Registro de estudiante creado con éxito.")

    os.system('pause')
    menu()

def create_user(op):
    os.system('clear')

    email = input("Ingrese el correo electrónico del usuario: ")
    password = input("Ingrese la contraseña del usuario: ")
    cur.execute("INSERT INTO Users (email, password, status, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", 
                (email, password, 0))  # Estado predeterminado
    con.commit()
    print("Registro de usuario creado con éxito.")

    os.system('pause')
    menu()

def menu():
    status_opt = True
    while status_menu:
        os.system("clear")
        print("===== Main Menu =====")
        print("[1] Create country")
        print("[2] Create department")
        print("[3] Create city")
        print("[4] Create identification type")
        print("[5] Create person")
        print("[6] Create student")
        print("[7] Create user")
        print("[8] Exit")

        while status_opt:
            opt = input("Press an option: ")
            if opt < '1' or opt > '8':
                print(".:::::: Invalid option, try again.")
            else :
                status_opt = False

        if opt == '1':
            create_country(opt)
        elif opt == '2':
            create_department(opt)
        elif opt == '3':
            create_city(opt)
        elif opt == '4':
            create_identification_type(opt)
        elif opt == '5':
            create_person(opt)
        elif opt == '6':
            create_student(opt)
        elif opt == '7':
            create_user(opt)
        else:
            print("::: See 'u soon :::")
            exit()
            
menu()

#close connection
con.close()
