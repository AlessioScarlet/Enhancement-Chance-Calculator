import os

def inserisci():

    perc = float(input("% of success: "))
    while perc/100>=1.01 or perc<=0:
        perc = float(input("% can't be higher than 100 or 0: "))
    else:
        calcolo(perc)



def calcolo(perc):
    x=float(perc/100)

    tentativi=0
    prob=0
    while prob<=90:
        tentativi += 1
        prob = (1 - ((1 - x) ** tentativi)) * 100
    print((round(prob,2)),"% after ", tentativi, " runs")


    while prob<=99:
        tentativi += 1
        prob = (1 - ((1 - x) ** tentativi)) * 100
    print((round(prob,2)),"% after ", tentativi, " runs")


    tentativi=5
    prob=0
    while prob<=90:
        prob = (1 - ((1 - x) ** tentativi)) * 100
        print(tentativi," runs,", (round(prob,2)), "%")
        tentativi+=5


    ris=input("Would you like to save the sheet (0%-90%) ? (y/n) : ")
    if ris=='n':
        os.system('pause')
    elif ris=='y':

        with open('sheet.txt', mode='w') as f:
            tentativi = 0
            prob = 0
            testo=''
            while prob <= 90:
                tentativi += 1
                prob = (1 - ((1 - x) ** tentativi)) * 100
                testo+='\n'+str(round(prob,2))+"% after "+ str(tentativi)+ " runs"
            print('File saved as "sheet.txt"')
            f.write(testo)
        os.system('pause')


    else:
        os.system('pause')

inserisci()
