import math
saldo_anterior=int(input("Cuanto fue su saldo anterior:"))
ingresos=int(input("Cuanto son sus ingresos:"))
egresos=int(input("Cuanto son sus egresos:"))
cheques=int(input("Cantidad de cheques:"))

cheque1=(cheques+13)
costo=(saldo_anterior+ingresos+egresos+cheque1)
porcentaje=((costo*7.5)/100)

costo2=(porcentaje+costo)

print("El saldo final de su cuenta es de:")
print(costo2)

