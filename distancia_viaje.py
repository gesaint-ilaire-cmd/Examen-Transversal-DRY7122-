# Examen Transversal DRY7122
# Cálculo de distancia entre Chile y Perú


# Base de datos de ciudades y distancias aproximadas en KM

ciudades = {

    "santiago": {
        "lima": 3300
    },

    "valparaiso": {
        "lima": 3400
    },

    "concepcion": {
        "lima": 3600
    },

    "arica": {
        "lima": 1050
    }
}


while True:

    print("\n--- CALCULADOR DE VIAJE CHILE - PERÚ ---")

    salir = input("Ingrese 's' para salir o presione Enter para continuar: ")

    if salir.lower() == "s":
        print("Programa finalizado")
        break


    origen = input("Ingrese Ciudad de Origen (Chile): ").lower()

    destino = input("Ingrese Ciudad de Destino (Perú): ").lower()


    if origen in ciudades and destino in ciudades[origen]:


        distancia_km = ciudades[origen][destino]


        # Conversión km a millas

        distancia_millas = distancia_km * 0.621371


        print("\nSeleccione medio de transporte")
        print("1 - Automóvil")
        print("2 - Avión")
        print("3 - Bus")


        transporte = input("Opción: ")


        if transporte == "1":

            medio = "Automóvil"

            tiempo = distancia_km / 90


        elif transporte == "2":

            medio = "Avión"

            tiempo = distancia_km / 800


        elif transporte == "3":

            medio = "Bus"

            tiempo = distancia_km / 70


        else:

            medio = "No definido"

            tiempo = 0



        print("\n----- RESULTADO DEL VIAJE -----")

        print("Origen:", origen.title())

        print("Destino:", destino.title())

        print("Distancia:", distancia_km, "Km")

        print("Distancia:", round(distancia_millas,2), "Millas")

        print("Transporte:", medio)

        print("Duración aproximada:",
              round(tiempo,2),
              "horas")


        print("\nNarrativa del viaje:")

        print(
        f"El viaje comienza en {origen.title()}, Chile "
        f"con destino a {destino.title()}, Perú. "
        f"Se recorrerán aproximadamente "
        f"{distancia_km} kilómetros utilizando "
        f"{medio.lower()}."
        )


    else:

        print("Ciudad no disponible en la base de datos")
