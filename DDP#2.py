print("TIPE DATA")
print("NUMBER")
                
a=11 #integer
print(a, "merupakan tipe", type(a))
b=0o1 #octal number=0O/0o
print(b, "merupakan tipe", type(b))
c=0xa #hexadecimal number=0X/0x
print(c, "merupakan tipe", type(c))

a=4.0 #floats
print(a, "merupakan tipe", type(a))
b=4.
print(b, "merupakan tipe", type(b))
c=3e8
print(c, "merupakan tipe", type(c))

a=1+2j #complex
print(a, "merupakan tipe", type(a))
b=7+5j
print(b, "merupakan tipe", type(b))
c=3+1j
print(c, "merupakan tipe", type(c))

print("KONVERSI JENIS BILANGAN !")
a=int(4.2)
print(a, "merupakan tipe", type(a))
b=float(11)
print(b, "merupakan tipe", type(b))

print("STRING")
s= "Ini adalah string satu baris"
print(s)

s= '''Ini adalah string
yang memiliki lebih
dari satu baris'''
print(s)

print('I like "Python" ')

print("BOOLEAN")
print(1<3)
print(2>5)

print("ARITHEMTIC OPERATOR")
print(-4 + 4) #addition
print(-4 + 8)

print(2 * 3) #multiplication
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print(6 / 3) #division
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

print(6 // 3) #integer division
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(2 ** 3) #exponentiation
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

print(14 % 4) #modulo
#14 //4 gives 3
#3 * 4 gives 12
#14 -12 gives 2 --> this is remainder

print("OPERATOR AND THEIR PRIORITIES")
print(2+3*5)
print((2+3)*5)

print("OPERATOR AND THEIR BINDINGS")
print( 9 % 6 % 2)
#from LEFT to RIGHT
#first 9 % 6 gives 3, and then 3 % 2 gives 1.