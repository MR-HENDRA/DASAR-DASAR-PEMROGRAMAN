#LARIK/ARRAY
#REKAMAN/RECORD
#LIST IN PYTHON
#PENDEFINISIAN TIPE DATA LIST

word= ["Belajar", "Python", "di", "Teknik Informatika"]
value= [50, 100, 200, 400]
com= ["Python", 6.99, True]
print(word)
print(value)
print(com)
['Belajar', 'Python', 'di', 'Teknik Informatika']
[50, 100, 200, 400]
['Python', 6.99, True]

#PENGAKSESAN TIPE DATA LIST

com= ["Python",100, 5.99, True, 'TeknikInformatika', 80j]
print(com[0])
print(com[1])
print(com[3])
Python
100
True

#PENGGANTIAN NILAI PADA ELEMEN TIPE DATA LIST

com= ["Python",100, 5.99, True, 'TeknikInformatika', 80j]
print(com)

com[1]=200
com[3]=False
print(com)
['Python', 100, 5.99, True, 'TeknikInformatika', 80j]
['Python', 200, 5.99, False, 'TeknikInformatika', 80j]

#MENAMPILKAN SEBAGIAN NILAI PADA TIPE DATA LIST

com= ["Python",100, 5.99, True, 'TeknikInformatika', 80j]
print(com[2:5])
print(com[:3])
print(com[3:])
print(com[:])
[5.99, True, 'TeknikInformatika']
['Python', 100, 5.99]
[True, 'TeknikInformatika', 80j]
['Python', 100, 5.99, True, 'TeknikInformatika', 80j]

#PENAMBAHAN DATA PADA TIPE DATA LIST

com= ["Python",100, 5.99, True, 'TeknikInformatika', 80j]
com.append(2)

print(com)
['Python', 100, 5.99, True, 'TeknikInformatika', 80j, 2]

#TUPLE IN PYTHON

word=("Belajar", "Python", "di", "TeknikInformatika")
value=(50, 100, 200, 400)
com=("Python", 200,6.99, True)

print(word)
print(value)
print(com)
('Belajar', 'Python', 'di', 'TeknikInformatika')
(50, 100, 200, 400)
('Python', 200, 6.99, True)

com= ("Python", 200, 6.99, True, 'TeknikInformatika', 89j)

print(com[0])
print(com[1])
print(com[3])
print(com[2:5])
print(com[:4])
print(com[:])
Python
200
True
(6.99, True, 'TeknikInformatika')
('Python', 200, 6.99, True)
('Python', 200, 6.99, True, 'TeknikInformatika', 89j)

#TIPE DATA SET
#PENDEFINISIAN TIPE DATA SET PADA PYTHON

word={"Belajar", "Python", "di", "TeknikInformatika"}
value={50, 100, 200, 400}
com={"Python", 200, 6.99, True}

print(word)
print(value)
print(com)
{'Python', 'di', 'Belajar', 'TeknikInformatika'}
{200, 50, 100, 400}
{200, 'Python', 6.99, True}

#SIFAT TIPE DATA SET PADA PYTHON

word={"Belajar", "Python", "di", "TeknikInformatika", "di"}
value={50, 100, 200, 400, 50, 200}

print(word)
print(value)
{'TeknikInformatika', 'Belajar', 'Python', 'di'}
{200, 50, 100, 400}

#OPERASI HIMPUNAN TIPE DATA PADA SET PADA PYTHON

value1={1,2,3,4,5}
value2={3,4,5,6,7}

print(value1|value2)#union
print(value1&value2)#intersection
{1, 2, 3, 4, 5, 6, 7}
{3, 4, 5}

#TIPE DATA DICTIONARY
#PENDEFINISIAN TIPE DATA DICTIONARY PADA PYTHON

word={1:"Learn", 2:"Python", 3:"TekikInformatika"}
que={"why":"Learn", "what":"Python", "where":"TeknikInformatika"}
word2={1:"Learn","what":"Python","where":"TeknikInformatika"}

print(type(word))
print(type(que))
print(type(word2))

print(word)
print(que)
print(word2)

{1: 'Learn', 2: 'Python', 3: 'TekikInformatika'}
{'why': 'Learn', 'what': 'Python', 'where': 'TeknikInformatika'}
{1: 'Learn', 'what': 'Python', 'where': 'TeknikInformatika'}

word=dict(activity="Learn Python", 
          youtube="Fos Algo",
          result="I can do it!")

print(word)
{'activity': 'Learn Python', 'youtube': 'FosAlgo', 'result': 'Ican do it!'}

word={1:"Learn",
      2:["C", "Java", "Python"],
      "youtube":"Fos Algo",
      "target":2021,
      "education_History":{
          "elementary_school":"SD No. 1 Majene",
          "jhs":"SMP 3 Majene",
          "shs":"SMA 2 Majene"}
      }


{1: 'Learn', 2: ['C', 'Java', 'Python'], 'youtube': 'Fos Algo', 'target': 2021, 'education_History': {'elementary_school': 'SD No. 1 Majene', 'jhs': 'SMP 3 Majene', 'shs': 'SMA 2 Majene'}}

#PENGAKSESAN TIPE DATA DICTIONARY PADA PYTHON

word={"activity":"Learn Python",
      "youtube":"Fos Algo",
      "result":"I can do it!"}

print(word)
{'activity': 'Learn Python', 'youtube': 'Fos Algo', 'result': 'I can do it!'}

#PENGUBAHAN ELEMEN PADA TIPE DATA DICTIONARY PADA PYTHON

word={"activity":"Learn Python",
      "youtube":"Fos Algo",
      "result":"I can do it!"}
word["activity"]="Learn Programming"

print(word)
{'activity': 'Learn Programming', 'youtube': 'Fos Algo', 'result': 'I can do it!'}

#PENAMBAHAN ELEMEN PADA TIPE DATA DICTIONARY PADA PYTHON

word={"activity":"Learn Python",
      "youtube":"Fos Algo",
      "result":"I can do it!"}
word["target"]="2021"

print(word)
{'activity': 'Learn Python', 'youtube': 'Fos Algo', 'result': 'I can do it!', 'target': '2021'}

#PENGURANGAN ELEMEN TIPE DATA DICTIONARY PADA PYTHON

word={"activity":"Learn Python",
      "youtube":"Fos Algo",
      "result":"I can do it!"}

del word["result"]
print(word)
{'activity': 'Learn Python', 'youtube': 'Fos Algo'}

p=["Arif","Hendra","Alim"]
q=[1,2,3]
dict(zip(p,q))
{'Alim': 3, 'Arif': 1, 'Hendra': 2}
