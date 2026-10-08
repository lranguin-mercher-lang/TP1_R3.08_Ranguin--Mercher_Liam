a=int(input("choisis une valeur pour a :"))
b=int(input("choisis une valeur pour b :"))

print ("La valeur la plus petite est : " , min(a, b))
print ("La somme de a et b est : " , (a + b))
print ("Le produit de a et b est : " , (a * b))

if (a * b)%2 == 0: 
    print ("Le produit est pair")

else : print ("Le produit est impair")
