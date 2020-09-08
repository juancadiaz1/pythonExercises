def calcularDescuento(precio, dia):

    precioTotal = 0

    if (dia) == 'l':
        precioTotal = precio - (precio * 0.10)

    if (dia) == 'm':
        precioTotal = precio - (precio * 0.05)

    if (dia) == 'M':
        precioTotal = precio - (precio * 0.03)

    if (dia) == 'j':
        precioTotal = precio - (precio * 0.01)

    if (dia) == 'v':
        precioTotal = precio - (precio * 0.07)

    if (dia) == 's':
        precioTotal = precio

    if (dia) == 'd':
        precioTotal = precio - (precio * 0.01)

    print("El precio final de su compra es de: ", precioTotal)
    return precioTotal

def main():

    precio=int(input("Ingrese el precio del producto: "))
    dia=input("Ingrese el dia de la semana: Lunes(l), Martes(m), Miercoles(M), Jueves(j), Viernes(v), Sabado(s), Domingo(d)  ")

    calcularDescuento(precio, dia)

if __name__ == '__main__':
    main()
