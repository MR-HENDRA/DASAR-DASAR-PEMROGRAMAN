def ss (list):
    iterasi=0
    for i in range (len(list)-1):
        min=i
        for j in range(i+1,len(list)):
            if list[j]<list[min]:
                min=j
        iterasi=+1
        list[i],list [min]=list[min], list[i]
        print(iterasi, list)

list=[2,54,38,76,23,56,84,90]
print('Data yang akan di sort: ',list)
print('selection sort:')
ss (list)

cari=int(input('Angka yang dicari: '))
indeks=0
iterasi=0
akhir=len(list)-1
found=False
while indeks<=akhir and not found:
    iterasi+=1
    if list[indeks]==cari:
        found=True
    else:
        indeks=indeks+1
if found:
    print("Angka yang dicari terletak pada indeks: ", indeks)
    print("Iterasi sebanyak= ", iterasi, "kali")
else:
    print("Angka yang dicari tidak ditemukan!")
    print("Iterasi dilakukan sebanyak=", iterasi, "kali")