class Person:

    def __init__(self, vorname, nachname, geburtsdatum):
        self._vorname = vorname
        self._nachname = nachname
        self._geburtsdatum = geburtsdatum

    def __str__(self):
        ret = self._vorname + " " + self._nachname
        ret += ", " + self._geburtsdatum
        return ret


class Angestellter(Person):

    def __init__(self, vorname, nachname, geburtsdatum, personalnummer):
        # alternativ:
        super().__init__(vorname, nachname, geburtsdatum)
        # Person.__init__(self, vorname, nachname, geburtsdatum)
        self.__personalnummer = personalnummer

    def __str__(self):
        return super().__str__() + " " + self.__personalnummer
        # return Person.__str__(self) + " " + self.__personalnummer


x = Angestellter("Homer", "Simpson", "09.08.1969", "007")
print(x)
