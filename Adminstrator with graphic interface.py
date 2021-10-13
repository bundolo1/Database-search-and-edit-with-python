import sqlite3
from sqlite3 import Error
import PySimpleGUI as sg


def create_connection (db_file):
  
    """ create a database conection to a SQLite database """
                
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def status (conn, posicion):
    
    """searches the position of an element in a database and returns a phrase for each value of the element"""
    
    sql = """SELECT Status, * FROM Indices WHERE id = ? """
    
    
    cur = conn.cursor()
    cur.execute(sql, (posicion,))
    conn.commit()
    status1 = cur.fetchone()
    status1 = str(status1)
    if "2 Läufe übrig" in status1:
        kenn = "green"
    elif "1 Lauf übrig" in status1:
        kenn = "orange"
    elif "0 Läufe übrig" in status1:
        kenn = "red"
    else:
        kenn = "black"
    return kenn

def get_indice_nombre_10(conn):

    """selects and returns the first row in a database with a simple condition"""
   
    cur = conn.cursor() 
   
    cur.execute("SELECT * FROM Indices WHERE vol = 10")

    rows = cur.fetchone()
    
    return rows
        
def get_indice_nombre_5 (conn):

    """selects and returns the first row in a simple database with a simple condition"""
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM Indices WHERE vol = 5")
   
    rows = cur.fetchone()
    
    return rows
         
def get_indice_10 (conn):
    
    """selects and returns the first row in a simple database with a simple condition based on the ID"""
   
    cur = conn.cursor()
    cur.execute("SELECT id, * FROM Indices WHERE vol = 10")

    ID = cur.fetchone()
    return ID
    
def get_indice_5 (conn):
    
    """selects and returns the first row in a simple database with a simple condition based on the ID"""  
    
    cur = conn.cursor()
    cur.execute("SELECT id, * FROM Indices WHERE vol = 5")
   
    ID = cur.fetchone()
    return ID  
     
def update_indice_5 (conn, indice):
   
    """updates a position in a database based on the users input"""
    
    sql = """ UPDATE Indices
              SET vol = 5,
                  status = '1 Lauf übrig'
              WHERE id = ?"""
    
    cur = conn.cursor()
    cur.execute(sql, (indice,))
    conn.commit()   
        
def update_indice_0 (conn, indice):
    
    """updates a position in a database based on the users input"""
    
    sql = """ UPDATE Indices
              SET vol = 0,
                  status = '0 Läufe übrig'
              WHERE id = ?"""
    
    cur = conn.cursor()
    cur.execute(sql, (indice,))
    conn.commit()
        
def reset_database (conn):
    
    """resets all values of a database"""
    
    sql = """ UPDATE Indices
              SET vol = 10,
                  status = '2 Läufe übrig'
              WHERE vol =0 """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()        
    
def entsorgt_indice (conn, indice):
    
    """updates custom status on database, based on user input"""
    
    sql = """ UPDATE Indices
              SET vol = 0,
                  status = 'Entsorgt'
              WHERE id = ?"""
    
    cur = conn.cursor()
    cur.execute(sql, (indice,))
    conn.commit()


def main_1():
    
    """search and modify in a database based on previously defined functions"""
    
    database = r"directory_of_your_db"
    conn = create_connection(database)
    
    with conn:                      
        nro_util = range(int(values["-nro_util-"]))
        sg.Print("Indices zu verfügen")
        for i in nro_util:                       
            if get_indice_nombre_10(conn) != None:                
                sg.Print(get_indice_nombre_10(conn))
                k = str(get_indice_10(conn))          
                try:                    
                    if int(k[1:3]) >= 10: 
                        indi = k[1:3]                       
                except:
                    indi = k[1]
                update_indice_5(conn, indi)
                
            elif get_indice_nombre_5(conn) != None:                
                sg.Print(get_indice_nombre_5(conn))                
                k = str(get_indice_5(conn))          
                try:
                    if int(k[1:3]) >= 10: 
                        indi = k[1:3]                       
                except:
                    indi = k[1]               
                update_indice_0(conn, indi)                       
            
            else:
                reset_database(conn)
                sg.Print("Neue Indices müssen gelöst werden. Die Tabelle wurde aktualiziert. Falls die Indizes schon gelöst worden sind, starten Sie bitte das Program neu und geben Sie die Anzahl der indizelose Proben ein")
                break
                window.close()            

def main_2():
    
    """updates a single cell in a database based on user input"""
   
    database = r"directory_of_your_db"
    conn = create_connection(database)
    
    with conn:                              
        ente = int(values["-entsorgen-"])
        entsorgt_indice(conn, ente)
        sg.Print("Indize", ente, "entsorgt")


#Graphic Interface



sg.theme("Dark Teal 7")


database = r"directory_of_your_db"
conn = create_connection(database)


layout_1 = [[sg.Text("Geben Sie bitte der Anzahl der Proben ein")],
           [sg.Input(key = "-nro_util-"), sg.Button("Wählen", key = "-buscar-")],
           [sg.Text("Indizes zu entsorgen")],
           [sg.Input(key = "-entsorgen-"), sg.Button("Entsorgen", key = "-descartar-")],
           [sg.Button("Abbrechen", key = "-cerrar-")]]

            
layout_2 = [[sg.Button("Index 1",  size=(6,1), button_color = ("white", status(conn,1))), 	sg.Button("Index 9",  size=(6,1), button_color = ("white", status(conn,9))), 	sg.Button("Index 17",  size=(6,1), button_color = ("white", status(conn,17))), 	sg.Button("Index 25",  size=(6,1), button_color = ("white", status(conn,25))), 	sg.Button("Index 33",  size=(6,1), button_color = ("white", status(conn,33))), 	sg.Button("Index 41",  size=(6,1), button_color = ("white", status(conn,41))), 	sg.Button("Index 49",  size=(6,1), button_color = ("white", status(conn,49))), 	sg.Button("Index 57",  size=(6,1), button_color = ("white", status(conn,57))), 	sg.Button("Index 65",  size=(6,1), button_color = ("white", status(conn,65))), 	sg.Button("Index 73",  size=(6,1), button_color = ("white", status(conn,73))), 	sg.Button("Index 81",  size=(6,1), button_color = ("white", status(conn,81))), 	sg.Button("Index 89",  size=(6,1), button_color = ("white", status(conn,89)))], 
            [sg.Button("Index 2",  size=(6,1), button_color = ("white", status(conn,2))), 	sg.Button("Index 10",  size=(6,1), button_color = ("white", status(conn,10))), 	sg.Button("Index 18",  size=(6,1), button_color = ("white", status(conn,18))), 	sg.Button("Index 26",  size=(6,1), button_color = ("white", status(conn,26))), 	sg.Button("Index 34",  size=(6,1), button_color = ("white", status(conn,34))), 	sg.Button("Index 42",  size=(6,1), button_color = ("white", status(conn,42))), 	sg.Button("Index 50",  size=(6,1), button_color = ("white", status(conn,50))), 	sg.Button("Index 58",  size=(6,1), button_color = ("white", status(conn,58))), 	sg.Button("Index 66",  size=(6,1), button_color = ("white", status(conn,66))), 	sg.Button("Index 74",  size=(6,1), button_color = ("white", status(conn,74))), 	sg.Button("Index 82",  size=(6,1), button_color = ("white", status(conn,82))), 	sg.Button("Index 90",  size=(6,1), button_color = ("white", status(conn,90)))], 
            [sg.Button("Index 3",  size=(6,1), button_color = ("white", status(conn,3))), 	sg.Button("Index 11",  size=(6,1), button_color = ("white", status(conn,11))), 	sg.Button("Index 19",  size=(6,1), button_color = ("white", status(conn,19))), 	sg.Button("Index 27",  size=(6,1), button_color = ("white", status(conn,27))), 	sg.Button("Index 35",  size=(6,1), button_color = ("white", status(conn,35))), 	sg.Button("Index 43",  size=(6,1), button_color = ("white", status(conn,43))), 	sg.Button("Index 51",  size=(6,1), button_color = ("white", status(conn,51))), 	sg.Button("Index 59",  size=(6,1), button_color = ("white", status(conn,59))), 	sg.Button("Index 67",  size=(6,1), button_color = ("white", status(conn,67))), 	sg.Button("Index 75",  size=(6,1), button_color = ("white", status(conn,75))), 	sg.Button("Index 83",  size=(6,1), button_color = ("white", status(conn,83))), 	sg.Button("Index 91",  size=(6,1), button_color = ("white", status(conn,91)))], 
            [sg.Button("Index 4",  size=(6,1), button_color = ("white", status(conn,4))), 	sg.Button("Index 12",  size=(6,1), button_color = ("white", status(conn,12))), 	sg.Button("Index 20",  size=(6,1), button_color = ("white", status(conn,20))), 	sg.Button("Index 28",  size=(6,1), button_color = ("white", status(conn,28))), 	sg.Button("Index 36",  size=(6,1), button_color = ("white", status(conn,36))), 	sg.Button("Index 44",  size=(6,1), button_color = ("white", status(conn,44))), 	sg.Button("Index 52",  size=(6,1), button_color = ("white", status(conn,52))), 	sg.Button("Index 60",  size=(6,1), button_color = ("white", status(conn,60))), 	sg.Button("Index 68",  size=(6,1), button_color = ("white", status(conn,68))), 	sg.Button("Index 76",  size=(6,1), button_color = ("white", status(conn,76))), 	sg.Button("Index 84",  size=(6,1), button_color = ("white", status(conn,84))), 	sg.Button("Index 92",  size=(6,1), button_color = ("white", status(conn,92)))], 
            [sg.Button("Index 5",  size=(6,1), button_color = ("white", status(conn,5))), 	sg.Button("Index 13",  size=(6,1), button_color = ("white", status(conn,13))), 	sg.Button("Index 21",  size=(6,1), button_color = ("white", status(conn,21))), 	sg.Button("Index 29",  size=(6,1), button_color = ("white", status(conn,29))), 	sg.Button("Index 37",  size=(6,1), button_color = ("white", status(conn,37))), 	sg.Button("Index 45",  size=(6,1), button_color = ("white", status(conn,45))), 	sg.Button("Index 53",  size=(6,1), button_color = ("white", status(conn,53))), 	sg.Button("Index 61",  size=(6,1), button_color = ("white", status(conn,61))), 	sg.Button("Index 69",  size=(6,1), button_color = ("white", status(conn,69))), 	sg.Button("Index 77",  size=(6,1), button_color = ("white", status(conn,77))), 	sg.Button("Index 85",  size=(6,1), button_color = ("white", status(conn,85))), 	sg.Button("Index 93",  size=(6,1), button_color = ("white", status(conn,93)))], 
            [sg.Button("Index 6",  size=(6,1), button_color = ("white", status(conn,6))), 	sg.Button("Index 14",  size=(6,1), button_color = ("white", status(conn,14))), 	sg.Button("Index 22",  size=(6,1), button_color = ("white", status(conn,22))), 	sg.Button("Index 30",  size=(6,1), button_color = ("white", status(conn,30))), 	sg.Button("Index 38",  size=(6,1), button_color = ("white", status(conn,38))), 	sg.Button("Index 46",  size=(6,1), button_color = ("white", status(conn,46))), 	sg.Button("Index 54",  size=(6,1), button_color = ("white", status(conn,54))), 	sg.Button("Index 62",  size=(6,1), button_color = ("white", status(conn,62))), 	sg.Button("Index 70",  size=(6,1), button_color = ("white", status(conn,70))), 	sg.Button("Index 78",  size=(6,1), button_color = ("white", status(conn,78))), 	sg.Button("Index 86",  size=(6,1), button_color = ("white", status(conn,86))), 	sg.Button("Index 94",  size=(6,1), button_color = ("white", status(conn,94)))], 
            [sg.Button("Index 7",  size=(6,1), button_color = ("white", status(conn,7))), 	sg.Button("Index 15",  size=(6,1), button_color = ("white", status(conn,15))), 	sg.Button("Index 23",  size=(6,1), button_color = ("white", status(conn,23))), 	sg.Button("Index 31",  size=(6,1), button_color = ("white", status(conn,31))), 	sg.Button("Index 39",  size=(6,1), button_color = ("white", status(conn,39))), 	sg.Button("Index 47",  size=(6,1), button_color = ("white", status(conn,47))), 	sg.Button("Index 55",  size=(6,1), button_color = ("white", status(conn,55))), 	sg.Button("Index 63",  size=(6,1), button_color = ("white", status(conn,63))), 	sg.Button("Index 71",  size=(6,1), button_color = ("white", status(conn,71))), 	sg.Button("Index 79",  size=(6,1), button_color = ("white", status(conn,79))), 	sg.Button("Index 87",  size=(6,1), button_color = ("white", status(conn,87))), 	sg.Button("Index 95",  size=(6,1), button_color = ("white", status(conn,95)))], 
            [sg.Button("Index 8",  size=(6,1), button_color = ("white", status(conn,8))), 	sg.Button("Index 16",  size=(6,1), button_color = ("white", status(conn,16))), 	sg.Button("Index 24",  size=(6,1), button_color = ("white", status(conn,24))), 	sg.Button("Index 32",  size=(6,1), button_color = ("white", status(conn,32))), 	sg.Button("Index 40",  size=(6,1), button_color = ("white", status(conn,40))), 	sg.Button("Index 48",  size=(6,1), button_color = ("white", status(conn,48))), 	sg.Button("Index 56",  size=(6,1), button_color = ("white", status(conn,56))), 	sg.Button("Index 64",  size=(6,1), button_color = ("white", status(conn,64))), 	sg.Button("Index 72",  size=(6,1), button_color = ("white", status(conn,72))), 	sg.Button("Index 80",  size=(6,1), button_color = ("white", status(conn,80))), 	sg.Button("Index 88",  size=(6,1), button_color = ("white", status(conn,88))), 	sg.Button("Index 96",  size=(6,1), button_color = ("white", status(conn,96)))],
            ]


layout = [[sg.TabGroup ( [[ sg.Tab("Indize Auswähler", layout_1),
                            sg.Tab("Plate", layout_2)]] ) ]]

window = sg.Window("Indize Auswähler", layout)

while True:
    event,values = window.read()  

    if event == "-buscar-":
        main_1()
        window["-nro_util-"]("")
        
    if event == "-descartar-":
        main_2()
        window["-entsorgen-"]("")   
        
    if event == sg.WIN_CLOSED or event == "-cerrar-":
        break        
        
        
window.close()        
        
 
if __name__ == "__main__":
    main_1()
    main_2()










































































"""
@author: Andres.Muriel
"""
