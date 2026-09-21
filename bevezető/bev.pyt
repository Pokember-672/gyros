

szam1 = float(input ("Adj egy számot"))
szam2 = float(input ("Adj ujra egy szamot"))
szam3 = float(input ("Adj egy harmadik szamot"))





atlag = (szam1 + szam2 +szam3)/3
print ("atlag:",atlag)
if atlag < 2 : 
    print("Megbuktal")
elif atlag == 5 :
    print("gratulalok kituno vagy")
else:
    print("Gratulalok Atmentel!")
