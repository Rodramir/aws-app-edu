import pymysql

db_host  = 'db-app-edu.cbkmo4kuk7al.us-east-2.rds.amazonaws.com'
db_user  = 'Rodri'
db_passw = 'Claveaws*'
db_name  = 'db_npat'

def connectionSQL():
    try:
        connection = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_passw,
            database = db_name
            )
        print("Succesffull conection to DB")
        return connection
    except Exception as err:
        print("Error connecting to DB", err)
        return None

def insert_records(patnr, titel, vname, nname, gbdat):
    print("insert records db")
    query = "INSERT INTO npat (patnr, titel, nname, vname, gbdat)  VALUES ("+patnr+", '"+titel+"', '"+nname+"', '"+vname+"', '"+gbdat+"')"

    try:
        connection = connectionSQL()
        if connection != None:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print("Patient Added")
        else:
            print("Error in DB Connection")

            
    except Exception as err:
            print("Error creating the Patient", err)

def consult_records(patnr):
    print("consult_records")
    query = "SELECT * FROM npat WHERE patnr = " + patnr
    try:
        connection = connectionSQL()
        cursor = connection.cursor()
        if connection != None:
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
            return result
        else:
            print("Error in the connection")
            return None
    except Exception as err:
        print("Error consulting the user", err)
        return None