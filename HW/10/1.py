class NotMainHero:

    def __init__(self, name):
        self.name = name

Babka = NotMainHero("Старуха")
Ded = NotMainHero("Старик")
Lisa = NotMainHero("Лиса")

class MainHero:
    def __init__(self, name, f_act, s_act, t_act):
        self.name = name
        self.f_act = f_act
        self.s_act = s_act
        self.t_act = t_act

Kolobok = MainHero("Колобок", 'poyavilsia', 'sbejal', 'sjeden')


def sbejal():
    return 'Kolobok sbejal'

def poyavilsia():
    return 'Poyavilsia Kolobok'


Skazochnik = MainHero("Skazochnik", 'start', 'vstrecha_lisa', 'epilog')

def start():
    return 'start of a tale'

class Skazochnik(MainHero):
    def start(self):
        print('Жил-был старик со старухою.')

def act(self):
    print(f'{self.name} говорит:')

class Ded(NotMainHero):
    def ask(Ded):
        print('— Испеки, старуха, колобок! По коробу поскреби, по сусеку помети; авось муки и наберется.')


class Babka(NotMainHero):
    def gotovit(self, Kolobok):
        print('"Будь по твоему". \n Взяла старуха крылышко, по коробу поскребла, по сусеку помела, и набралось муки')
        print('пригоршни с две. Замесила на сметане, изжарила в масле и положила на окошечко постудить.')


class Kolobok(MainHero):
    def sbejal(self):
        print('Колобок полежал — полежал, да вдруг и покатился — с окна на лавку, с лавки на пол, по полу да к дверям,')
        print('перепрыгнул через порог в сени, из сеней на крыльцо, с крыльца — на двор, со двора за ворота, дальше и дальше.')
        kolobok.sbejal


class Skazochnik(MainHero):
    def vstrecha_lisa(self):
        print('Катится, катится колобок, а навстречу ему лиса:')

babka = Babka("Старуха")
ded = Ded("Старик")
kolobok = Kolobok("Колобок", 'poyavilsia', 'sbejal', 'sjeden')
skazochnik = Skazochnik("Skazochnik", 'start', 'vstrecha_lisa', 'epilog')

def tale():
    skazochnik.start()
    act(ded)
    ded.ask()
    babka.gotovit(kolobok)
    kolobok.sbejal()

tale()
