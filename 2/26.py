# 02.12.26 Edvards Gedrovics, spēles mērķis ir aprēķināt 
vards = input("Ievadi varoņa vārdu: ")

speks = int(input("Uzbrukuma spēks: "))

veiksme = float(input("Veiksmes koeficients: "))

rezultats = (speks ** 2) * veiksme

print(f"{vards} duelī iegūst {rezultats:.1f} punktus!")

# Uzbrukuma spēks kāpināts kvadrātā, pēc tam reizināts ar veiksmes koeficientu.
