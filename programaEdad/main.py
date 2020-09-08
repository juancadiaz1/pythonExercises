def saberEdad(año, edad):

    edadFut=2070-año+edad 
    print("Su edad en el año 2070 sera: ",edadFut,"años")
    return edadFut
	

def main():

    edad=int(input("Ingrese su edad actual: "))
    año=int(input("Ingrese el año actual: "))

    saberEdad(año,edad)

if __name__ == '__main__':
    main()
