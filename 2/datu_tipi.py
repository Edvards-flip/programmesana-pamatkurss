a = "5"
b = 5
c = 5.5
print(type(a))
print(type(b))
print(type(c))
print(a + a)

vards = input("Ievadi varoņa vārdu: ")
punkti = int(input("Ievadi bāzes punktus: "))
reizinatajs = float(input("Ievadi reizinātāju: "))
kopa = punkti * reizinatajs
print(vards, "ieguva", kopa, "punktus")

# kļūda radās desmitajā rindā
# abās reizēs bija ValueError
# Secinājums: Komatam Python valodas sintaksē jau ir cita nozīme. Tas kalpo kā atdalītājs, lai uzskaitītu vairākus elementus sarakstos, funkciju argumentos vai izveidotu datu struktūru, ko sauc par kortežu.