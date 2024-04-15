#Izveidot Python programmu, kas ļauj lietotājam ievadīt savu vārdu terminālī.
#Ievadīto vārdu pēc tam ierakstīt teksta failā (piemēram, "lietotajs.txt").
#Programmai jābūt spējīgai apstrādāt kļūdas, piemēram, faila nepieejamību vai rakstīšanas problēmas.
#Pēc ierakstīšanas izvadīt paziņojumu par veiksmīgu darbību vai kļūdu gadījumā attiecīgu kļūdas ziņojumu.

bam = input("Vārds: ")

try:
    with open("lietotajs.txt", "w") as bra:
        bra.write(bam)
except (FileNotFoundError, ValueError):
    print("Nepareizs faila formāts")
with open("lietotajs.txt", "r") as bum:
    name = bum.read()

print(bam)