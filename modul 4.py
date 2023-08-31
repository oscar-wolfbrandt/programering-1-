#1#
L = float(input("hur lång e du: "))

if L > 120:
    print(" då får komma in")

elif L < 120:
    print("du får inte komma in ")


#2#
a = input("hur gamal är du: ")
try:
    print(int(a))
except:
    print("skriv ett namn tack")

b = input("skriv ditt namn: ")


#3#
Vikt = input("hur mycket väger du:")
Längd = input("hur lång e du i M:")

try:
    print("ditt BMI är:", float(Vikt) / ((float(Längd) * float(Längd))))
except:
    print("skriv nummer")


#4#
radie = input("vad är radien av din cikel i cm: ")
print("arean av din cikel är", (float(radie) **2) * 3.14, "cm")


räknesät = input("vilket räknesät vill du anvenda + - / elletr *:")
tal_1 = input("skriv första talet: ")
tal_2 = input("skriv andra talet : ")
svar = "något gick fel försök igen"

try:
    if räknesät == "+":
        try:
            svar = float(tal_1) + float(tal_2)
        except:
            print("skriv ett tal")
except:
    print(svar)

try:
    if räknesät == "-":
        try:
            svar = float(tal_1) - float(tal_2)
        except:
            print("skriv ett tal")
except:
    print(svar)

try:
    if räknesät == "*":
        try:
            svar = float(tal_1) * float(tal_2)
        except:
            print("skriv ett tal")
except:
    print(svar)

try:
    if räknesät == "/":
        try:
            svar = float(tal_1) / float(tal_2)
        except:
            print("skriv ett tal")
except:
    print(svar)

print(svar)


#6#
import random
print(random.randint(1,6))

#7#
import random

dice = input("hur många gånger vill du kasta ")

for o in range(1, int(dice)):
    print(random.randint(1, 6))