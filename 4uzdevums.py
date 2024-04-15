#Izveidot Python programmu, kur lietotājs ievada gan faila nosaukumu, gan faila formātu (paplašinājumu), 
#un atkarībā no faila paplašinājuma tiek nolasīts faila saturs.
# Nolasītā informācija ir jāizdrukā terminālī. Ievērot iespejamās kļūdas!

nosaukums = input("Faila nosaukums: ")
paplasinajums = input("Faila formāts: ")


if nosaukums.endswith("." + paplasinajums):
    with open(nosaukums, "r") as bam:
        saturs = bam.read()
        print(saturs)
else:
    print("Kļūda")