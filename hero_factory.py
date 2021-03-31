from python_factory.police import Police
from python_factory.timo import Timo

class HeroFactory:

    def create_hero(self,name):

        if name == "timo":
            return Timo()
        elif name == "police":
            return Police()
        else:
            raise Exception("")


if __name__ == '__main__':
    factory = HeroFactory()
    hero_timo = factory.create_hero('timo')
    hero_timo.speak_line()
    hero_timo.fight(3000,90)

