print("Mostrar el valor absoluto de cualquier numero")
numero = int(input("ingresa cualqiuier numero positivo o negativo: "))
if numero<0:
    numero = numero*-1
    print ("su valor absoluto es:", numero)
else:
    print ("El valor absoluto es: ",numero)