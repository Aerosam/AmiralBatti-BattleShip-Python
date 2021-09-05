import sys
import random as rn
import os


ships = {'0':'Mayin Gemisi' , '1':'Denizalti', '2':'Firkateyn', '3':'Muhrip Gemisi', '4':'Amiral'}
ship_list = []
columns = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F':'6', 'G':'7', 'H':'8', 'I':'9', 'J':'10' }
game_map = [["0"] * 10 for a in range(10)]
fleet = []
field = [[0] * 10 for a in range(10)]


class ship:
    def __init__(self, dimen, direc, place, name, situa):
        self.dimen = dimen

        if direc == 'Horiz' or direc == 'Verti':
            self.direc = direc
        else:
            print(direc)
            raise ValueError("Value")

        if direc == 'Horiz':
            if place['line'] in range(10):
                self.coordinate = []
                for index in range(dimen):
                    if place['column'] + index in range(10):
                        self.coordinate.append({'line': place['line'], 'column': place['column'] + index})
                    else:
                        raise IndexError("Column is out of range.")
            else:
                raise IndexError("Row is out of range.")

        elif direc == 'Verti':
            if place['column'] in range(10):
                self.coordinate = []
                for index in range(dimen):
                    if place['line'] + index in range(10):
                        self.coordinate.append({'line': place['line'] + index, 'column': place['column']})
                    else:
                        raise IndexError("line is out of range.")
            else:
                raise IndexError("Column is out of range.")

        self.name = name
        self.situa = situa

    def fill(self):
        for coordi in self.coordinate:
            if field [coordi['line']][coordi['column']] == 1:
                return True
        return False

    def placed(self):
        for coordi in self.coordinate:
            field[coordi['line']][coordi['column']] = 1

    def checkplace(self, place):
        for coordi in self.coordinate:
            if coordi == place:
                return True
        return False

    def destroy(self):
        for coordi in self.coordinate:
            if game_map[coordi['line']][coordi['column']] == '0':
                return False
            elif game_map[coordi['line']][coordi['column']] == 'X':
                raise RuntimeError("Board display is not accurate.")
        return True



def random(ship_no):
    dimen = ship_no + 1
    name = ships[str(ship_no)]
    situa = 'saglam'
    direc = 'Horiz' if rn.randint(0, 1) == 0 else 'Verti'
    
    places = search(dimen, direc)
    if places == 'none':
        return 'none'
    else:
        return{'konum': places[rn.randint(0, len(places) - 1)], 'boyutu': dimen, 'yonu': direc, 'isim': name, 'durumu': situa}

    



def search(dimen, direc):
    places = []


    if direc != 'Horiz' and direc != 'Verti':
        raise ValueError("this Error")

    if direc == 'Horiz':
        if dimen <= 10:
            for sr in range(10):
                for st in range(10 - dimen + 1):
                    if 1 not in field[sr][st:st + dimen]:
                        places.append({'line': sr, 'column': st})
    elif direc == 'Verti':
        if dimen <= 10:
            for st in range(10):
                for sr in range(10 - dimen +1):
                    if 1 not in [field[a][st] for a in range(sr, sr + dimen)]:
                        places.append({'line': sr, 'column':st})
    if not places:
        return 'none'
    else:
        return places




def report(tries):
    print(tries + 1, "Atis denemsi yaptiniz.",)
    print("1 mayin gemisi 1 kareyi kaplar.", ship_list[0].situa)
    print("1 Denizalti 2 kareyi kaplar.", ship_list[1].situa)
    print("1 Firkateyn 3 kareyi kaplar.", ship_list[2].situa)
    print("1 Muhrip gemisi 4 kareyi kaplar.", ship_list[3].situa)
    print("1 Amiral gemisi 5 kareyi kaplar.", ship_list[4].situa)


def show(game_map):
    print("   " + " ".join(str(a) for a in columns))
    for b in range(9):
        print(str(b + 1) + "  " + " ".join(str(c) for c in game_map[b]))
    print(str(10) + " " + " ".join(str(c) for c in game_map[9]))


temp = 0
while temp < 5:
    ship_info = random(temp)
    
    if ship_info == 'none':
        continue
    else:
        ship_list.append(ship(ship_info['boyutu'], ship_info['yonu'], ship_info['konum'], ship_info['isim'], ship_info['durumu']))
        
        fleet.append(ship(ship_info['boyutu'], ship_info['yonu'], ship_info['konum'], ship_info['isim'], ship_info['durumu']))
        temp += 1
del temp

os.system('clear')
print("Amiral batti oynayalim!")
show(game_map)
for tries in range(100):
    guess_coordi = {}
    while True:
        guess = input(f"{tries + 1}. tahmininizi girin? ")
        if guess == "r":
            report(tries)
            continue
        elif guess == "q":
            print("Oyun sonlandirildi!")
            sys.exit()
        elif len(guess) < 2 or len(guess) > 3:
            print("Hata! sadece 2 karakter giriniz. 1 ile 10 arasinda bir sayi ve A ile J arasinda bir buyuk harf girilmelidir. Tekrar giriniz.")
            continue
        elif len(guess) == 3:
            try:
                if int(guess[0]) == 1 and int(guess[1]) == 0:
                    row = 10
                    stn = guess[2]
                else:
                    print("Hata! sadece 2 karaktergiriniz. 1 ile 10 arasinda bir sayi ve A ile J arasinda bir buyuk harf girilmelidir. Tekrar giriniz.")
                    continue
            except:
                print("Hata!sadece 2 karakter giriniz! 1 ile 10 arasinda bir sayi ve A ile J arasinda buyuk harf girilmelidir. Tekrar deneyiniz.")
                continue
        elif len(guess) == 2:
                try:
                    row = int(guess[0])
                    stn = guess[1]
                except:
                    print("Hata! 1 ile 10 arasinda bir sayi ve A ile J arainda bir buyuk harf girilmelidir. Tekrar giriniz.")
                    continue
        
        if stn not in columns:
                print("Hata! sayilar 1 ve 10 arasinda olmalidir ve harfler Ave J arasinda buyuk harf olmalidir. Tekrar giriniz.")
                continue

        sutun = int(columns[stn])
        enter = '['+str(guess)+']'
        guess_coordi['line'] = row - 1
        guess_coordi['column'] = sutun - 1
        if game_map[guess_coordi['line']][guess_coordi['column']] == '*' or game_map[guess_coordi['line']][guess_coordi['column']] == 'X':
            print(enter, "Bu koordinat daha once vuruldu, Tekrar atis yapin.")
        else:
            break

    os.system('clear')

    target = False
    for ship in fleet:
        if ship.checkplace(guess_coordi):
            ship_list[ship.dimen - 1].situa = "Yarali"
            target = True
            game_map[guess_coordi['line']][guess_coordi['column']] = '*'
            if ship.destroy():
                print(enter, ship.name, "Batti")
                ship_list[ship.dimen - 1].situa = "Batti"
                fleet.remove(ship)
            else:
                print(enter, ship.name, "Yara Aldi")
            break
    if not target:
        game_map[guess_coordi['line']][guess_coordi['column']] = 'X'
        print(enter, "Iska")


    show(game_map)


    if not fleet:
        break


if not fleet:
    print("Tum gemiler batti. Kazandiniz!")
    sys.exit()
                      
                        
            
        
    
        
        
    
                
            
