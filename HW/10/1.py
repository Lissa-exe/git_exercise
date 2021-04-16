class NotMainHero:

    def __init__(self, name, act):
        self.name = name
        self.act = act

Babka = NotMainHero("Babka", 'gotovit')
Ded = NotMainHero("Ded", 'ask')
Lisa = NotMainHero("Lisa", 'eat')

class MainHero:
    def __init__(self, name, ispechen, sbejal, poet, sjeden):
        self.name = name
        self.ispechen = ispechen
        self.sbejal = sbejal
        self.poet = poet
        self.sjeden = sjeden

Kolobok = MainHero("Kolobok", 'ispechen', 'sbejal', 'poet', 'sjeden')

class Ded(NotMainHero):
    def ask(Ded):
        print('"Babka, please, bake me Kolobok".')

def act(self):
    print(f'{self.name} govorit:')


class Babka(NotMainHero):
    def gotovit(self, Kolobok):
        print('"Ok then", \n and Babka poskrebla po susekam i ispekla Kolobok')
        Kolobok.ispechen()

class Kolobok(MainHero):
    def pobeg(self):
        print('And then, Kolobok has had run away')


babka = Babka("Babka", 'gotovit')
ded = Ded("Ded", 'ask')
kolobok = Kolobok("Kolobok", 'ispechen', 'sbejal', 'poet', 'sjeden')

def tale():
    babka.gotovit(kolobok)
    kolobok.pobeg()

tale()