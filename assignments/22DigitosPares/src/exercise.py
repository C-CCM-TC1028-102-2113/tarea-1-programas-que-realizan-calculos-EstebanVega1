def main():
    #escribe tu código abajo de esta línea
    pass
entrada = int(input("Ponga un numero de 4 digitos:"))

par = 0
impar = 0

while(entrada > 0):
  if entrada % 2 == 0:
    par += 1
  else:
    impar += 1
  entrada = entrada // 10

print(f"Numero de numeros pares: {par} | Numero de numeros impares: {impar}")

if __name__ == '__main__':
    main()
