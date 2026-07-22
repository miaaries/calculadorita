## CALCULADORA - VERSIÓN 2
# Autor(a): Mia Calderon 
# ===========================================
print("calculadora")


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\n 1.sumar")
print(" n 2.restar")

opcion= input("\n seleccione una opcion ")

if opcion =="1":
  print("\n la suma es:",num1 +num2)

elif opcion == "2":
  print("\n la resta es:",num1 -num2)

else:
  print("\n opcion no valida )
