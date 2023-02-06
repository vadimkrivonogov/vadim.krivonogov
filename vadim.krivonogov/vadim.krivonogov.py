#Задание 4: Sorteerimine

list=[-45,74,29,-1,0]

list.sort()

print(list)

list.sort(reverse=True)

print(list)

#isikukood
arvud = []
while True:
    isikukood = input("Kirjutage teie isikukood: ")
    n = len(isikukood)
    if n != 11 or not isikukood.isdigit():
        print("Isikukood peab olema 11-kohaline ja ainult numbritega.")
        continue

    year = int(isikukood[1:3])
    month = int(isikukood[3:5])
    day = int(isikukood[5:7])
    if not (1 <= month <= 12) or not (1 <= day <= 31):
        print("Sünnipäev ei saa luua.")
        continue
   
    century = 18 if int(isikukood[0]) in [1, 2] else 19 if int(isikukood[0]) in [3, 4] else 20
    birthdate = f"{day}.{month}.{century}{year}"
    print(f"Sünnipäev on {birthdate}")
   
    gender = "Mees" if int(isikukood[0]) in [1, 3, 5] else "Naine"
    print(f"Sugu on {gender}")
   
    hospital_id = int(isikukood[7:10])
    if 1 <= hospital_id <= 10:
        hospital = "Kure Saare Haigla"
    elif 11 <= hospital_id <= 19:
        hospital = "Tartu Ülikooli Naistekliinik"
    elif 20 <= hospital_id <= 220:
        hospital = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif 221 <= hospital_id <= 270:
        hospital = "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271 <= hospital_id <= 310:
        hospital = "Maarjamõisa kliinikum (Tartu)"
    else:
        hospital = "Teadmata"
    print(f"Haigla on {hospital}")

    control_sum = sum([int(c) * (2 if i % 2 == 0 else 1) for i, c in enumerate(isikukood[:9])]) % 11
    if control_sum != int(isikukood[9]):
        print("Isikukood ei ole korrektne.")
        continue
   
    arvud.append(isikukood)
    break 