import classes

cenybiletow = classes.Ticket() #obiekt potrzebny do obliczenia ceny biletów
#utwórzmy kilka linii autobusowych umieszczając je w tablicy
listaLinii=[]
listaLinii=[classes.Bus(10)]
listaLinii.append(classes.Bus(11))
listaLinii.append(classes.Bus(22))
listaLinii.append(classes.Bus(25))
listaLinii.append(classes.Bus(33))
listaLinii.append(classes.Bus(47))
listaLinii.append(classes.Bus(52))

#utwórzmy listę przystanku z nazwą przystanku i tablicą rozkladu
#rozklad sklada sie z linijki zawierającej obiekt klasy Bus oraz następującej po nim tablicy godzin odjazdów z danego przystanku

rozklad1=[[listaLinii[0],["06:00","07:00","15:00","18:00"]]]
rozklad1.append([listaLinii[1],["06:05","07:05","15:05","18:05"]])
rozklad1.append([listaLinii[2],["06:15","07:15","15:15","18:15"]])
linia1 = classes.Timetable("Woronicza/Składowa",rozklad1)
listarozkladow=[linia1]

rozklad2=[[listaLinii[3],["07:00","08:00","16:00","19:00"]]]
rozklad2.append([listaLinii[4],["07:05","08:05","16:05","19:05"]])
rozklad2.append([listaLinii[5],["07:15","08:15","16:15","19:15"]])
linia2 = classes.Timetable("Palmowa/Liściowa",rozklad2)
listarozkladow.append(linia2)

rozklad3=[[listaLinii[6],["08:00","09:00","17:00","20:00"]]]
rozklad3.append([listaLinii[0],["08:05","09:05","17:05","20:05"]])
rozklad3.append([listaLinii[1],["08:15","09:15","17:15","20:15"]])
linia3 = classes.Timetable("Sobieskiego/Jagiełły",rozklad3)
listarozkladow.append(linia3)
##--------------------------------------------------------------------------------
#teraz użytkownik poda jak się nazywa jaką ma ulgę i ilu minutowy bilet chce kupić

print('Podaj swoje imię i nazwisko:')
nazwisko = input()
print('Podaj jaka ulga ci przysługuje (np:emeryt, student czy rencista:')
ulga = input()
pasażer = classes.Passenger(nazwisko,ulga)
print('Podaj iluminutowy bilet Cię interesuje(do wyboru 10,20 i 40 min:')
jakibilet= input()
cenybiletow.cenaBiletu(jakibilet,pasażer.ulga) # użytkownik otrzyma cenę za swój bilet

print("dostępne przystanki na liście:") #zlistuj przystanki
for x in listarozkladow:
    print(x.nazwaPrzystanku)
print('Na jakim jesteś przystanku ?:') #uzytkownik wybiera przystanek na jakim się znajduje
przystanek = input()

print("dostępne linie:") #zlistuj wszystkie linie dla danego przystanku
for x in listarozkladow:
    if przystanek==x.nazwaPrzystanku:
        for y in x.rozkład:
            print(y[0].numerLinii)
print('Jaka linia Cię interesuje?:') #użytkownik wybiera linie
liniaAuto = input()

for x in listarozkladow:
    if przystanek==x.nazwaPrzystanku:
        for y in x.rozkład:
            if y[0].numerLinii==int(liniaAuto):
                print("Odjazdy:") #wyświetlamy godziny odjazdów dla tej linii
                print(y[1])





#print(cenybiletow.cena10min)