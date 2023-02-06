#Задание 4: Sorteerimine

list=[-45,74,29,-1,0]

list.sort()

print(list)

list.sort(reverse=True)

print(list)

#isikukood
isikukood = []
arvud = []
isikuoodid = []
while True:
    isikukood = input("Kirjutage teie isikukood: ")
    n = len(isikukood)
    if n == 11 and isikukood.isdigit():
        arvud.append(isikukood)
        isikukod_list = list(isikukood)
        s1 = int(isikukod_list[0])
        print("Esimene number on", isikukod_list[0])
        if s1 in [1, 2, 3, 4, 5, 6]:
            print("isikukood sobib")
            arvud.append(isikukood)
            break
        else:
            print("isikukoodis on viga")
    else:
        print("isikukoodis lubamatud väärtused või liiga vähe sümboleid")
        break

    y = (isikukod_list[1] + isikukod_list[2])  # year
    m = (isikukod_list[3] + isikukod_list[4])  # month
    d = int(isikukod_list[5] + isikukod_list[6])  # day
    if (int(m) < 1 or int(m) > 13) and (int(d) < 1 or int(d) > 31):
        print("Sünnipäev ei saa luua")
        arvud.append(isikukood)
        break
    else:
        if s1 == 1 or s1 == 2:
            yy = "18"
        elif s1 == 3 or s1 == 4:
            yy = "19"
        else:
            yy = "20"
        espäev = str(d) + "." + str(m) + "." + yy + y  # pole 18..,19..,20..
        print(f"Sünnipäev on {espäev}")
        print("Kontroll pole")
        if s1 in [1, 3, 5]:
            sugu = ("Mees")
        if s1 in [2, 4, 6]:
            sugu = ("Naine")
        a1 = int(isikukood[0]) * 1
        b1 = int(isikukood[1]) * 2
        b2 = int(isikukood[2]) * 3
        b3 = int(isikukood[3]) * 4
        b4 = int(isikukood[4]) * 5
        b5 = int(isikukood[5]) * 6
        b6 = int(isikukood[6]) * 7
        b7 = int(isikukood[7]) * 8
        b8 = int(isikukood[8]) * 9
        b9 = int(isikukood[9]) * 1

        s11 = b1 + a1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 +
