from datetime import datetime
from playsound import playsound

def parbaudiet_laiku(modinatajs_laiks): 
    if len(modinatajs_laiks) != 8: 
        return "Nepareizs formāts, mēģiniet vēlreiz"
    else:
        if int(modinatajs_laiks[0:2]) > 23: 
            return "Nepareizs stundu formāts, mēģiniet vēlreiz"
        elif int(modinatajs_laiks[3:5]) > 59: 
            return "Nepareizs minūšu formāts, mēģiniet vēlreiz"
        elif int(modinatajs_laiks[6:8]) > 59: 
            return "Nepareizs sekundžu formāts, mēģiniet vēlreiz"
        else:
            return "ok"

while True:
    modinatajs_laiks = input("Ievadiet modinatāja laiku šajā formātā 'HH:MM:SS' \n Modinātāja laiks: ") 

    parbaudiet = parbaudiet_laiku(modinatajs_laiks) 
    if parbaudiet != "ok":
        print(parbaudiet)
    else:
        print(f"Modinātājs iestatīts uz laiku: {modinatajs_laiks}")
        break

modinatajs_stunda = int(modinatajs_laiks[0:2])
modinatajs_minute = int(modinatajs_laiks[3:5])
modinatajs_sekunde = int(modinatajs_laiks[6:8])

while True:
    now = datetime.now()

    tagad_stunda = now.hour
    tagad_minute = now.minute
    tagad_sekunde = now.second

    if modinatajs_stunda == tagad_stunda:
        if modinatajs_minute == tagad_minute:
            if modinatajs_sekunde == tagad_sekunde:
                print("Celšanās!")
                playsound(r"sound.mp3")
                break