from settings import *
import random

class player(object):

    def __init__(self):
        self.poh = 0
        self.mon = start_money
        self.rep = start_reputation
        self.pow = start_powers
        self.leg = start_legality

        #normal cases

        self.quest = [] #self qestion
        self.agree = [] #answear if player is agree
        self.disagree = [] #answear if player disagree
        self.pictcs = [] #id of picture for this case
        self.pictagr = [] #id of picture for this case AGREE
        self.pictdis = [] #id of picture for this case DISAGREE
        self.pohcs = [] #poh points if agree
        self.monagr = [] #money if agree
        self.repagr = [] #reputation if agree
        self.powagr = [] #power if agree
        self.legagr = [] #legality if agree
        self.mondis = [] #money if disagree
        self.repdis = [] #reputation if disagree
        self.powdis = [] #power if disagree
        self.legdis = [] #legality if disagree

        self.emrquest = []
        self.emragr = []
        self.emrpicts = []
        self.emrpicta = []
        self.emrpohcs = []
        self.emrmon = []
        self.emrrep = []
        self.emrpow = []
        self.emrleg = []

        self.empquest = []
        self.empagr = []
        self.emppicts = []
        self.emppicta = []
        self.emppohcs = []
        self.empmon = []
        self.emprep = []
        self.emppow = []
        self.empleg = []

        with open('empow.txt', 'r', encoding='utf-8') as empow:
            for i in range(kolvoemp):
                self.empquest.append(empow.readline())
                self.empagr.append(empow.readline())
                self.emppicts.append(empow.readline())
                self.emppicta.append(empow.readline())
                self.emppohcs.append(empow.readline())
                self.empmon.append(empow.readline())
                self.emprep.append(empow.readline())
                self.emppow.append(empow.readline())
                self.empleg.append(empow.readline())

        with open('emrep.txt', 'r', encoding='utf-8') as emrep:
            for i in range(kolvoemr):
                self.emrquest.append(emrep.readline())
                self.emragr.append(emrep.readline())
                self.emrpicts.append(emrep.readline())
                self.emrpicta.append(emrep.readline())
                self.emrpohcs.append(emrep.readline())
                self.emrmon.append(emrep.readline())
                self.emrrep.append(emrep.readline())
                self.emrpow.append(emrep.readline())
                self.emrleg.append(emrep.readline())

        with open('cases.txt', 'r', encoding='utf-8') as cases:
            for i in range(kolvocases):
                self.quest.append(cases.readline())
                self.agree.append((cases.readline()))
                self.disagree.append(cases.readline())
                self.pictcs.append(cases.readline())
                self.pictagr.append(cases.readline())
                self.pictdis.append(cases.readline())
                self.pohcs.append(cases.readline())
                self.monagr.append(cases.readline())
                self.repagr.append(cases.readline())
                self.powagr.append(cases.readline())
                self.legagr.append(cases.readline())
                self.mondis.append(cases.readline())
                self.repdis.append(cases.readline())
                self.powdis.append(cases.readline())
                self.legdis.append(cases.readline())

        cases.close()
        empow.close()
        emrep.close()

        print('inited sucsessfull')

    def playcard(self):
        csrn = random.randint(0, kolvocases-1)
        print(self.quest[csrn])
        if asknum() == 1:
            print(self.agree[csrn])
            player.change(self, int(self.monagr[csrn]), int(self.legagr[csrn]), int(self.powagr[csrn]), int(self.repagr[csrn]), int(self.pohcs[csrn]))
        else:
            print(self.disagree[csrn])
            player.change(self, int(self.mondis[csrn]), int(self.legdis[csrn]), int(self.powdis[csrn]), int(self.repdis[csrn]), 0)

    def playemrep(self):
        print('Вы в критической ситуации из-за низкой репутациии вашей авиакомпании. Нужно срочно что-то предпринять! Вот 3 доступных пути.')
        way1 = random.randint(0, kolvoemr-1)
        way2 = random.randint(0, kolvoemr-1)
        while way1 == way2:
            way2 = random.randint(0, kolvoemr-1)
        way3 = random.randint(0, kolvoemr-1)
        while way3 == way2 or way3 == way1:
            way3 = random.randint(0,kolvoemr-1)
        print('1 вариант: '+self.emrquest[way1])
        print('2 вариант: '+self.emrquest[way2])
        print('3 вариант: '+self.emrquest[way3])

        if asknum() == 1:
            print(self.emragr[way1])
            player.change(self, int(self.emrmon[way1]), int(self.emrleg[way1]), int(self.emrpow[way1]), int(self.emrrep[way1]), int(self.emrpohcs[way1]))

        elif asknum() == 2:
            print(self.emragr[way2])
            player.change(self, int(self.emrmon[way2]), int(self.emrleg[way2]), int(self.emrpow[way2]), int(self.emrrep[way2]), int(self.emrpohcs[way2]))

        else:
            print(self.emragr[way3])
            player.change(self, int(self.emrmon[way3]), int(self.emrleg[way3]), int(self.emrpow[way3]), int(self.emrrep[way3]), int(self.emrpohcs[way3]))

    def playempow(self):
        print('Вы в критической ситуации из-за нехватки самолётов. Нужно срочно что-то предпринять! Вот 3 доступных пути.')
        way1 = random.randint(0, kolvoemp-1)
        way2 = random.randint(0, kolvoemp-1)
        while way1 == way2:
            way2 = random.randint(0, kolvoemp-1)
        way3 = random.randint(0, kolvoemp-1)
        while way3 == way2 or way3 == way1:
            way3 = random.randint(0, kolvoemp-1)
        print('1 вариант: '+self.empquest[way1])
        print('2 вариант: '+self.empquest[way2])
        print('3 вариант: '+self.empquest[way3])

        if asknum() == 1:
            print(self.empagr[way1])
            player.change(self, int(self.empmon[way1]), int(self.empleg[way1]), int(self.emppow[way1]), int(self.emprep[way1]), int(self.emppohcs[way1]))

        elif asknum() == 2:
            print(self.empagr[way2])
            player.change(self, int(self.empmon[way2]), int(self.empleg[way2]), int(self.emppow[way2]), int(self.emprep[way2]), int(self.emppohcs[way2]))

        else:
            print(self.empagr[way3])
            player.change(self, int(self.empmon[way3]), int(self.empleg[way3]), int(self.emppow[way3]), int(self.emprep[way3]), int(self.emppohcs[way3]))

    def change(self, mc, lc, pc, rc, poh):
        self.poh += poh
        self.mon += mc
        self.leg += lc
        self.pow += pc
        self.rep += rc

    def check(self):
        if self.mon <= 0:
            return "mon"
        if self.rep <= 0:
            return "rep"
        if self.leg <= 0:
            return "leg"
        if self.pow <= 0:
            return "pow"
        if self.poh >= 10:
            return "poh"
        return "0"

    def aircrash(self):
        print('Случилась авиакатастрофа с участием вашего самолёта.')
        self.poh = 0
        self.mon -= 25
        self.rep -= 25
        self.pow -= 5

    def lmb(self):

        self.pow = max(min(100, self.pow), 0)
        self.rep = max(min(100, self.rep), 0)
        self.mon = max(min(100, self.mon), 0)
        self.leg = max(min(100, self.leg), 0)

def asknum():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Error. Try again.")

player.__init__(self=player)

print('STARTED')
while True:

    if player.check(self=player) == "poh":
        player.aircrash(self=player)

    if player.check(self=player) == "mon":
        print("Нам очень жаль, но вы проиграли. Вы - банкрот! У вас нет денег даже что-бы расплатиться по своим счетам.")
        break

    elif player.check(self=player) == "leg":
        print("Нам очень жаль, но вы проиграли. Вы арестованы! Ваши черные схемы по итогу до добра не довели.")
        break

    elif player.check(self=player) == "rep":
        player.playemrep(self=player)

    elif player.check(self=player) == "pow":
        player.playempow(self=player)

    else:
        player.playcard(self=player)

    player.lmb(self=player)

input('GAME OVER')