print("Hello","World",sep=", ",end= ".\n")
print("Hello Yassir")


age = 19
nom = "Yassir"


print("Hello", nom, "tu as", age)
print(f"Hello {nom}, tu as {age}")


var = f"name = {print(nom)}"


print(var)



var = None
type(var)


print(id(var))
var = 3
print(id(var))


entree = int(input("Entree une valeur "))

entree



age=int(input("qu'elle est votre age?"))

print(age,type(age))




temp=int(input("entrez lla temp en celsius:"))
print(temp)

conv=(temp*9/5)+temp
print(conv)




mots_de_passe=input("entrer votre mots de passe:")

if mots_de_passe=="200709" :
    print("\nbien venu(e)\n")
    
else :
    print("pouvez-vous repeter le mots de passe il vous reste 5 chance")




mots_de_passe=input("entrer votre passe:")

print(len(mots_de_passe))



moyenne=float(input("entrer votre moyenne:"))

if 12<=moyenne<14:
    print("assez-bien")

elif 14<=moyenne<16:
    print("bien")

elif 16<=moyenne<18:
    print("tres bien")

elif 18<=moyenne<20:
    print("filicitation")

else:
       print("pas de mention")




ma_liste=[42,'abc',1.1,30]
print(ma_liste[0:3])




ma_liste=[42,'abc',1.1,30]

ma_liste.append(500) 

print(ma_liste[4])






print('b' in ['a','b','c'])



for lettre in ['a','b','c']:
    print(lettre)


for i in range(5):
    print(i)


projet to try :

   
nb_vie=7

mot_myster='aziz'

mot_public="_" * len(mot_myster)

while nb_vie >0 and mot_myster!=mot_public:

    lettre=input("entrer une lettre :")

if lettre in mot_myster:
    for i in range(len(mot_myster)):
        if mot_myster[i]==lettre:
            mot_public=mot_public[:i]+lettre+mot_public[i+1:]
else:
    nb_vie-=1

if mot_public==mot_myster:
    print("exellent le mots est ",mot_myster)
elif nb_vie==0:
    print("malhereusement tu as pas reussis")
else:
    print("nombre de vie qu'il vous reste est ",nb_vie)
    print("le mots est ",mot_public)



def my_fonction():
    ma_variable=1
    print("ma variable est :",ma_variable)

my_fonction()




def my_fonction(ma_variable):
    print("ma variable est :",ma_variable)

my_fonction(67)



def my_fonction(*args):
    print("ma variable est :",*args)
    print(type(args))
my_fonction(1,2,3,4)




def my_fonction(**kwargs):
    print("ma variable est :",*kwargs)
    print(type(kwargs))
    
my_fonction(un=1,deux=2,trois=3,quatre=4)




def somme(a,b):
    return a+b
s=somme(10,10)
print(s)




def simple_font(n):
    l=[]
    i=0
    while i<n:
     l.append(i)   
     i+=1

    return l

print(simple_font(5))




nombre.add:ajout de nombre dans an tableau 





set_1={0,1,2}
set_2={2,3,4}

print(set_1.union(set_2))



set_1={0,1,2}
set_2={2,3,4}

print(set_1.intersection(set_2))




set_1={0,1,2}
set_2={2,3,4}

print(set_1.difference(set_2))



nombre={"un":1,"deux":2,"trois":3}

print(nombre.get("cinq","pas trouve"))


set_1={0,1,2}
set_2={2,3,4}

print(dir(set_1))
