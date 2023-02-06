#Задание 4: Sorteerimine

list=[-45,74,29,-1,0]

list.sort()

print(list)

list.sort(reverse=True)

print(list)

#isikukood

ikoodid = []
arvud = []

# попытки
count = 0

while count < 4:
  personal_code = input("Введи свой код!: ")
  
  # проверка длины
  if len(personal_code) != 11:
    print("Неправльная длина, должно быть 11.")
    arvud.append(personal_code)
    count += 1
    continue
  
  # Проверить первую цифрку
  if personal_code[0] not in "123456":
    print("Неправильная первая цифра, какой твой пол??")
    arvud.append(personal_code)
    count += 1
    continue
  
  # вычислить до с кода
  day = personal_code[5:7]
  month = personal_code[3:5]
  year = personal_code[1:3]
  
  # проверить день рождения
  try:
    datetime.datetime.strptime(day + "-" + month + "-" + year, '%d-%m-%y')
  except ValueError:
    print("Ты родился? Неправльное ДР.")
    arvud.append(personal_code)
    count += 1
    continue
  
  # 1
  ikoodid.append(personal_code)
  
  # 2
  gender = "male" if personal_code[0] in "135" else "female"
  dob = day + "/" + month + "/19" + year
  place_of_birth = "Idavir Keshaigla (Kohtla-Järve, endine Jõhvi)"
  print(f"This is a {gender}, his/her birthday is {dob} and place of birth is {place_of_birth}.")
  
  count += 1

#3
arvud.sort()
print("List of incorrect codes:", arvud)

# 4
ikoodid_women = [code for code in ikoodid if code[0] in "246"]
ikoodid_men = [code for code in ikoodid if code[0] in "135"]
print("List of correct codes for women:", ikoodid_women)
print("List of correct codes for men:", ikoodid_men)
