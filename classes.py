class Timetable:
    nazwaPrzystanku=""
    rozkład =[[]]   #rozklad jest w formacie tablice: [[Bus nazwalinii][godzina1][godzina2] .... itd.
    def __init__(self, przystanek, rozklad):
        self.nazwaPrzystanku =przystanek
        self.rozkład = rozklad
    def rozkladDanejLinii(self,numerLinii):
        for x in self.rozkład:
            if x[0].numerlinii == numerLinii:
                print(x)
                break


class Bus:
    numerLinii=0
    def __init__(self,numerLinii):
        self.numerLinii=numerLinii


class Passenger:
    imieNazwisko="Pasażer Autobusu"
    ulga="brak"
    def __init__(self, imieNazwisko,ulga):
        self.imieNazwisko = imieNazwisko
        self.ulga=ulga


class Ticket:
    #ceny w złotówkach
    cena10min=10
    cena20min=20
    cena40min=30
    #ulgi podawana jako procentowy rabat
    ulgaEmeryt=50
    ulgaStudent=30
    ulgaRencista=ulgaEmeryt

    def __init__(self):
        self. cena10min=10



    def cenaBiletu(self,ileminut,ulga):
        ileminut = int(ileminut)


        print(ileminut)
        if ileminut==10:
            cena=self.cena10min
        if ileminut==20:
            cena=self.cena20min
        if ileminut == 40:
            cena=self.cena40min

        if ulga=="emeryt":
            cena=cena * self.ulgaEmeryt / 100
        if ulga=="student":
            cena=cena * self.ulgaStudent / 100
        if ulga == "rencista":
            cena = cena * self.ulgaRencista / 100

        print("cena biletu: ")
        print(cena)


