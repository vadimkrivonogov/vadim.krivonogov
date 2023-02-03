#Задание 4: Sorteerimine

list=[-45,74,29,-1,0]

list.sort()

print(list)

list.sort(reverse=True)

print(list)

#isikukood
while True:
    ik=input("Anna isikukood:") #str
    if len(ik)!=11:
        print("Liiga palju või liiga vähe sümboleid. Sisesta veel kord: ")
    else:
            print("Isikukoodi kontroll")
            ik_list=list(ik)
            sl=int(ik_list[0]) #"1"->1
            if sl not in [1,2,3,4,5,6]:
                print("Esimene sümbol ei ole õige")
            else: 
                print("Esimine sümbol on õige")
            
