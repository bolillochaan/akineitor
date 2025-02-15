def adivinar():
    print("Adivinaré lo que estás pensando")
    
    respuesta = input("1. ¿Es algo vivo? (si/no): ").strip().lower()
    if respuesta == "si":
        respuesta = input("2. ¿Es un animal? (si/no): ").strip().lower()
        if respuesta == "si":
            respuesta = input("¿Es un vertebrado? (si/no): ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Es un mamífero? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿A qué orden pertenece? (humanos/caninos/marsupiales/primates/otros): ").strip().lower()
                    if respuesta == "humanos":
                        print("Estás pensando en un ser humano (Orden: Primates).")
                    elif respuesta == "caninos":
                        print("Estás pensando en un perro, lobo u otro cánido (Orden: Carnivora).")
                    elif respuesta == "marsupiales":
                        print("Estás pensando en un canguro, zarigüeya u otro marsupial (Orden: Diprotodontia).")
                    elif respuesta == "primates":
                        print("Estás pensando en un mono o simio (Orden: Primates).")
                    else:
                        print("Estás pensando en otro mamífero como un oso o caballo.")
                else:
                    print("Estás pensando en un vertebrado que no es mamífero, como un pez, reptil o anfibio.")
            else:
                print("Estás pensando en un invertebrado como un insecto o pulpo.")
        else:
            respuesta = input("3. ¿Es una planta? (si/no): ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Para qué se usa? (alimenticia/medicinal/ornamental): ").strip().lower()
                if respuesta == "alimenticia":
                    print("Estás pensando en una planta usada para alimentación, como trigo o arroz.")
                elif respuesta == "medicinal":
                    print("Estás pensando en una planta medicinal, como aloe vera o manzanilla.")
                elif respuesta == "ornamental":
                    print("Estás pensando en una planta ornamental, como tulipanes o geranios.")
                else:
                    print("Estás pensando en otro tipo de planta.")
            else:
                print("Estás pensando en otro ser vivo, como una bacteria u hongo.")
    else:
        respuesta = input("4. ¿Es un objeto? (si/no): ").strip().lower()
        if respuesta == "si":
            respuesta = input("¿Cómo lo quieres clasificar? (funcion/material/tamaño/uso/caracteristicas/valor/categoria): ").strip().lower()
            if respuesta == "funcion":
                print("Ejemplos: Herramientas, electrodomésticos, muebles.")
            elif respuesta == "material":
                print("Ejemplos: Metálicos, plásticos, madera.")
            elif respuesta == "tamaño":
                print("Ejemplos: Pequeños, medianos, grandes.")
            elif respuesta == "uso":
                print("Ejemplos: Doméstico, industrial, personal.")
            elif respuesta == "caracteristicas":
                print("Ejemplos: Color, forma, peso.")
            elif respuesta == "valor":
                print("Ejemplos: Valiosos, económicos.")
            elif respuesta == "categoria":
                print("Ejemplos: Tecnología, alimentos, vehículos.")
            else:
                print("No se pudo clasificar el objeto.")
        else:
            respuesta = input("5. ¿Es un material? (si/no): ").strip().lower()
            if respuesta == "si":
                respuesta = input("6. ¿Es una Elemento? (si/no): ").strip().lower()
                
                if respuesta == "si":
                    respuesta = input("7. ¿Es de origen natural? (si/no): ").strip().lower()

                    if respuesta == "si":
                        print("Estás pensando en un Elemento Natural (Ej: Oro Au, Oxígeno O, Carbono C).")
                    else:
                        print("Estás pensando en un Elemento Sintético (Ej: Plutonio Pu, Americio Am).")
                
                elif respuesta == "no":
                    respuesta = input("¿6. Es compuesto? (si/no): ").strip().lower()
                    if respuesta == "no":
                     respuesta = input("¿7. Es orgánico o inorgánico? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en un Compuesto Orgánico (Ej: Glucosa C₆H₁₂O₆, Etanol C₂H₅OH).")
                    else:
                        print("Estás pensando en un Compuesto Inorgánico (Ej: Agua H₂O, Sal NaCl).")
                
                elif respuesta == "si":
                    respuesta = input("¿7. Es homogénea o heterogénea? (si/no): ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("8. ¿Es una solución metálica? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Estás pensando en una Aleación (Ej: Acero [Fe+C], Bronce [Cu+Sn]).")
                        else:
                            print("Estás pensando en una Mezcla Homogénea (Ej: Aire, Agua de mar).")
                    else:
                        respuesta = input("¿9. Sus componentes son visibles? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Estás pensando en una Mezcla Heterogénea (Ej: Granito, Ensalada).")
                        else:
                            print("Estás pensando en un Coloide (Ej: Gelatina, Mayonesa).")
                
                else:
                    print("Estás pensando en un material complejo o de clasificación especial.")
            else:
                # Clasificación por origen
                respuesta = input("¿Se obtiene de la tierra? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Se produce de manera artificial? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en un Combustible.")
                    else:
                        print("Estás pensando en un Recurso Geológico (como minerales o rocas).")
                else:
                    respuesta = input("¿El fenómeno ocurre en la Tierra? (si/no): ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("¿Causa catástrofes? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Estás pensando en un Fenómeno Climático (huracanes, terremotos).")
                        else:
                            respuesta = input("¿Es un campo de estudio científico? (si/no): ").strip().lower()
                            if respuesta == "si":
                                respuesta = input("¿Es una fuerza fundamental? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Estás pensando en una Fuerza Natural (gravedad, magnetismo).")
                                else:
                                    respuesta = input("¿Se manifiesta como vibración o pulsación? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Estás pensando en Ondas (sonoras, electromagnéticas, sísmicas).")
                                    else:
                                        print("Estás pensando en una Forma de Energía (cinética, térmica).")
                    else:
                        print("Estás pensando en un Fenómeno Extraterrestre (auroras boreales, lluvias de meteoros).")

    print("No estoy seguro de qué estás pensando, pero seguro es algo interesante.")

adivinar()