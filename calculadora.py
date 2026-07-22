## CALCULADORA - VERSIÓN 3
# Autor(a): Mia Calderon 
# ===========================================
print("calculadora")


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\n 1.sumar")
print("  2.restar")
print(" 3.multiplicar")

print (" 4 .division")

opcion= input("\n seleccione una opcion ")

if opcion =="1":
  print("\n la suma es:",num1 +num2)

elif opcion == "2":
  print("\n la resta es:",num1 -num2)

elif opcion == "3":
  print("\n la multiplicacion es :",num1 *num2)

elif opcion  =="4":
  if num2 !=0
  print("\n la division es :",num1/num2)
else:      
  print(" no se puede dividir entre cero")
  
else:
  print("\n opcion no valida )
