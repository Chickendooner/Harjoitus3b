with open('sanat.txt') as f:
    allText = f.read()
    sanat = list(map(str, allText.split()))
import random
while True:
    a = int(input('Mikä on kokonaisluku? '))
    if(a > 0):
        for i in range(1, a+1):
            sana1 = (random.choice(sanat))
            sana2 = (random.choice(sanat))
            if i % 3 == 0 and i % 5 == 0:
                print(sana1 + sana2)
            elif i % 3 == 0:
                print(sana1)
            elif i % 5 == 0:
                print(sana2)
            else:
                print(i)
                i = i+1
