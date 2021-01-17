class Pets:
    name = "pets"

    @classmethod
    def about(cls):
        print("This class is about {0}!".format(cls.name))


class Dogs(Pets):
    name = "dogs"


class Cats(Pets):
    name = "cats"


p = Pets()
p.about()

d = Dogs()
d.about()

c = Cats()
c.about()
