def main():
    #escribe tu código abajo de esta línea
    pass
num_pal=int(input("Numero de paginas:"))

if num_pal>=475:
    pag= num_pal / 475
    semi_t= pag * 60
    
    dis= (semi_t * 0.1)
    total= semi_t - dis
    print("Costo total es:", total)
else: print ("No hay suficientes palabras")


if __name__ == '__main__':
    main()
