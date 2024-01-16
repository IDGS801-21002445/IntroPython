print("Condicionantes : ")

num1 = int(input("Dame n1: "))
num2 = int(input("Dame n2: "))

if num1 > num2 :
    print("El {} es mayor que el {}".format(num1, num2))
else :
    print("El {} es mayor que el {}".format(num2, num1))
    
print("---------------------------------------------------\n")

print("Pedir una edad: ")

edad = int(input("Ingrese su edad : "))

if edad > 18 :
    print("Eres mayor de edad")
elif edad == 18 :
    print("Estas chiquillo pero ya eres un adulto")
else : 
    print("No eres mayor de edad, no te creas grande")