#Import engine database package
import sqlite3

#Create a database connection (database name)
con = sqlite3.connect('school.db')

#creating cursor object
cur = con.cursor()

#create table
cur.execute('''
   CREATE TABLE IF NOT EXISTS Country (
        id_country INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATETIME
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Department (
        id_depart INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        id_country INTEGER,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATETIME,
        FOREIGN KEY (id_country) REFERENCES Country(id_country)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS City (
        id_exp_City INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(100) NOT NULL,
        id_depart INTEGER,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATETIME,
        FOREIGN KEY (id_depart) REFERENCES Department(id_depart)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Identification_types (
        id_ident_type INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(100) NOT NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATETIME
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Persons (
        id_persons INTEGER PRIMARY KEY, 
        first_name VARCHAR(50) NOT NULL, 
        last_name VARCHAR(50),
        id_ident_type INTEGER,
        ident_number VARCHAR(15) NOT NULL,
        id_exp_City INTEGER,
        address VARCHAR(150) NOT NULL,
        mobile VARCHAR(50) NOT NULL,
        id_users INTEGER,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATETIME,
        FOREIGN KEY (id_ident_type) REFERENCES Identification_types(id_ident_type),
        FOREIGN KEY (id_exp_City) REFERENCES City(id_exp_City),
        FOREIGN KEY (id_users) REFERENCES Users(id_users)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id_Student INTEGER PRIMARY KEY NOT NULL,
        code VARCHAR(50) NOT NULL,
        id_persons INTEGER,
        status INTEGER, -- or BIT if your database supports it
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATETIME,
        FOREIGN KEY (id_persons) REFERENCES Persons(id_persons)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id_users INTEGER PRIMARY KEY NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(250) NOT NULL,
        status INTEGER, -- or BIT if your database supports it
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATETIME
    )
''')

#Save changes in database
con.commit()

print("Base de datos creada con éxito.")