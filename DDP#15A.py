print("-----------------------------")

prima=[2,3,5,7,11,13,17,19,23,29]
for i in prima:
    print(i)
total=sum(prima)
print(total)


print("-----------------------------")

bilangan=[]
for i in range (10,100,10):
    bilangan.append(i)
print(bilangan)

print("-----------------------------")

bilangan.pop(2)
print("Menghapus bilangan ke 3=",bilangan)

print("-----------------------------")

print("Tampilkan bilangan ke 5=",bilangan[4])

print("-----------------------------")

bilangan.insert(2,25)
print("Menampilkan bilangan 25 ke elemen 3=",bilangan)



sulawesi=['Mateng','mamuju','makassar','majene','polewali','pasangkayu','mamasa','manado','palu','gorontalo']
print(sulawesi)

print("-----------------------------")

print("tampilkan elemen ke 4-6",sulawesi[3:6])

print("-----------------------------")

print("tampilkan elemen kedua terakhir=",sulawesi[-2])

print("-----------------------------")

matrix=[[2,4,6,8],
        [1,3,5,7],
        [10,12,14,16],
        [9,11,13,15]]
for i in matrix:
    print(i)

print("-----------------------------")

print("matrix=", matrix[1][2])

print("-----------------------------")

list=[]
for row in matrix:
    list.append(row[3])
print("KOLOM 4:", list)

print("-----------------------------")

matriks1=[[2,4,6,8],
        [1,3,5,7],
        [10,12,14,16],
        [9,11,13,15]]

matriks2=[[1,3,5,7],
          [9,11,13,15],
          [2,4,6,8],
          [10,12,14,16]]
result=[]
for i in range (len(matriks1)):
    row=[]
    for j in range (len(matriks1[i])):
        row.append(matriks1[i][j]+matriks2[i][j])
    result.append(row)

print("The result of addiing 2 matrices:")
for row in result:
    print(row)

print("-----------------------------")

matriks1=[[2,4,6,8],
        [1,3,5,7],
        [10,12,14,16],
        [9,11,13,15]]

matriks2=[[1,3,5,7],
          [9,11,13,15],
          [2,4,6,8],
          [10,12,14,16]]
result=[]
for i in range (len(matriks1)):
    row=[]
    for k in range (len(matriks2[0])):
        val=0
        for j in range(len(matriks1[i])):
            val+=matriks1[i][j]*matriks2[j][k]
        row.append(val)
    result.append(row)

print("The result of multiplying 2 matrices:")
for row in result:
    print(row)

print("-----------------------------")

list=[11,45,8,11,23,45,23,45,23,45,89]
nilai1=min(list)
print("Nilai minimun dari list:", nilai1)

print("-----------------------------")

list=[11,45,8,11,23,45,23,45,23,45,89]
nilai2=max(list)
print("Nilai minimun dari list:", nilai2)

print("-----------------------------")



list=[11,45,8,11,23,45,23,45,23,45,89]
for i in range(len(list)-1,0,-1):
    for j in range(i):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print(list)

print("-----------------------------")

list.sort()
print(list)

print("-----------------------------")

b=[11,45,8,11,23,45,23,45,23,45,89]
hasil=0
for i in range(len(b)):
    y=b[i]
    if y>=hasil:
        hasil=y
print("nilai min: ",y)  

print("-----------------------------")

a=[11,45,8,11,23,45,23,45,23,45,89]
hasil=0
for i in range(len(a)):
    y=a[i]
    if y>= hasil:
        hasil=y
print("nilai max: ",y)  

print("-----------------------------")

matriks1=[[2,4,6,8],
        [1,3,5,7],
        [10,12,14,16],
        [9,11,13,15]]

matriks2=[[1,3,5,7],
          [9,11,13,15],
          [2,4,6,8],
          [10,12,14,16]]
result=[]
for i in range (len(matriks1)):
    row=[]
    for j in range (len(matriks1[i])):
        row.append(matriks1[i][j]+matriks2[i][j])
    result.append(row)

print("The result of adding 2 matrices:")
for row in result:
    print(row)

print("-----------------------------")

matriks1=[[2,4,6,8],
        [1,3,5,7],
        [10,12,14,16],
        [9,11,13,15]]

matriks2=[[1,3,5,7],
          [9,11,13,15],
          [2,4,6,8],
          [10,12,14,16]]
result=[]
for i in range (len(matriks1)):
    row=[]
    for k in range (len(matriks2[0])):
        val=0
        for j in range(len(matriks1[i])):
            val+=matriks1[i][j]*matriks2[j][k]
        row.append(val)
    result.append(row)

print("The result of multiplying 2 matrices:")
for row in result:
    print(row)


print("-----------------------------")

print("-----------------------------")

matriks1=[[6,0,4],
        [1,6,2]]

matriks2=[[2,6,5,1],
          [3,3,4,2],
          [7,1,3,3]]
result=[]
for i in range (len(matriks1)):
    row=[]
    for k in range (len(matriks2[0])):
        val=0
        for j in range(len(matriks1[i])):
            val+=matriks1[i][j]*matriks2[j][k]
        row.append(val)
    result.append(row)

print("The result of multiplying 2 matrices:")
for row in result:
    print(row)


print("-----------------------------")

