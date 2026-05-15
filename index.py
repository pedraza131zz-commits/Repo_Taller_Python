def parar():
    p=input("Presione <ENTER> para continuar")

# opccion qe permite el ingreso de la temperatra 
def capturar ():
    try:
        T=float(input("por favor digite la temperatura: "))
        return T
    except Exception as ex:
        print(ex)

## funcion para convertir la temperatra de grados celcius a fahrenheit
def CelsiusFahrenheit (C):
    ## f=(ºC * 9/5) + 32
    return (C * 9/5) + 32

# funcion para convertir la temperatra de grados celcius a kelvin
def CelsiusKelvin(C):
    ## K = °C + 273.15
    return C + 273.15

## funcion para convertir la temperatra de grados kelvin a fahrenheit
def KelvinFahrenheit(K):
    ## F = (K - 273.15) * 9/5 + 32
    return (K - 273.15) * 9/5 + 32

## funcion para convertir la temperatra de grados kelvin a celcius
def KelvinCelsius(K):
    ## C = K - 273.15
    return K - 273.15

## funcion para convertir la temperatra de grados fahrenheit a kelvin
def FahrenheitKelvin(F):
    ## K = (°F - 32) * 5/9 + 273.15
    return (F - 32) * 5/9 + 273.15

## funcion para convertir la temperatra de grados fahrenheit a celcius
def FahrenheitCelsius(F):
    ## C = (°F - 32) * 5/9
    return (F - 32) * 5/9

def main():
    try:
        continuar = True
        T = 0

        while continuar == True:

            opcion = input(
                "Seleccione una opción:" + chr(13) +
                "1--> Capturar Temperatura" + chr(13) +
                "2--> Celsius a Fahrenheit" + chr(13) +
                "3--> Celsius a Kelvin" + chr(13) +
                "4--> Kelvin a Fahrenheit" + chr(13) +
                "5--> Kelvin a Celsius" + chr(13) +
                "6--> Fahrenheit a Kelvin" + chr(13) +
                "7--> Fahrenheit a Celsius" + chr(13) +
                "0--> Salir"
            )
## si se escoge la opccion 1 solo  se mostrara la temperatura en centimetros
            if opcion == '1':
                T = capturar()

## si se escoge la opccion 2 se convertira la temperatura de celcius a fahrenheit 
            elif opcion == '2':
                print(f"{T}°C = {CelsiusFahrenheit(T)} °F")
                parar()

## si se escoge la opccion 3 se convertira la temperatura de celcius a kelvin
            elif opcion == '3':
                print(f"{T}°C = {CelsiusKelvin(T)} °K")
                parar()

## si se escoge la opccion 4 se convertira la temperatura de kelvin a fahrenheit
            elif opcion == '4':
                print(f"{T}°K = {KelvinFahrenheit(T)} °F")
                parar()

## si se escoge la opccion 5 se convertira la temperatura de kelvin a celcius
            elif opcion == '5':
                print(f"{T}°K = {KelvinCelsius(T)} °C")
                parar()

## si se escoge la opccion 6 se convertira la temperatura de fahrenheit a kelvin
            elif opcion == '6':
                print(f"{T}°F = {FahrenheitKelvin(T)} °K")
                parar()

## si se escoge la opccion 7 se convertira la temperatura de fahrenheit a celcius                
            elif opcion == '7':
                print(f"{T}°F = {FahrenheitCelsius(T)} °C")
                parar()

## si se escoge la opccion 0 el prgrma se terminara y no dara ningn valor
            elif opcion == '0':
                print("Bye")
                continuar = False

## se mostrara el mensaje de print si se ingresa una opccion que no este en el menu
            else:
                print("Seleccione una opción valida")

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()