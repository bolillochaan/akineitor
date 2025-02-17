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
        respuesta = input("2. ¿Es un objeto? (si/no): ").strip().lower()
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
          respuesta = input("5. ¿Es intangible? (si/no): ").strip().lower()
    if respuesta == "si":
        respuesta = input("6. ¿Es creación humana? (si/no): ").strip().lower()
        if respuesta == "si":
            respuesta = input("7. ¿Es entretenimiento audiovisual? (si/no): ").strip().lower()
            if respuesta == "si":
                respuesta = input("8. ¿Es animación? (si/no): ").strip().lower()
                if respuesta == "si":
                    print("¡Es un Anime!")
                else:
                    respuesta = input("9. ¿Es contenido que se divide en capitulos? (si/no): ").strip().lower()
                    print("¡Es una Serie!" if respuesta == "si" else "¡Es una Película!")
            else:
                respuesta = input("7. ¿Es producción musical? (si/no): ").strip().lower()
                if respuesta == "si":
                    print("¡Es Música!")
                else:
                    respuesta = input("8. ¿Es arte literario? (si/no): ").strip().lower()
                    print("¡Es un Libro/Novela!" if respuesta == "si" else "¡Es Poesía u obra dramática!")
        else:
            print("¡Es un fenómeno natural intangible como una aurora boreal o sonido ambiental!")
    
    else:
        # Sección de Tangibles
        respuesta = input("6. ¿Es un material? (si/no): ").strip().lower()
        if respuesta == "si":
            respuesta = input("7. ¿Es una Elemento? (si/no): ").strip().lower()
            
            if respuesta == "si":
                respuesta = input("8. ¿Es de origen natural? (si/no): ").strip().lower()
                if respuesta == "si":
                    print("Elemento Natural (Ej: Oro Au, Oxígeno O)")
                else:
                    print("Elemento Sintético (Ej: Plutonio Pu)")
            
            else:
                respuesta = input("7. ¿Es compuesto? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("8. ¿Es orgánico? (si/no): ").strip().lower()
                    print("Compuesto Orgánico" if respuesta == "si" else "Compuesto Inorgánico")
                else:
                    respuesta = input("8. ¿Es mezcla homogénea? (si/no): ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("9. ¿Es aleación? (si/no): ").strip().lower()
                        print("Aleación metálica" if respuesta == "si" else "Mezcla homogénea")
                    else:
                        print("Mezcla heterogénea o coloide")
        
        else:
            # Sección de fenómenos
            respuesta = input("6. ¿Se obtiene de la tierra? (si/no): ").strip().lower()
            if respuesta == "si":
                respuesta = input("7. ¿Se produce de manera artificial? (si/no): ").strip().lower()
                if respuesta == "si":
                    print("Estás pensando en un Combustible.")
                else:
                    print("Estás pensando en un Recurso Geológico (como minerales o rocas).")
            else:
                respuesta = input("8. ¿El fenómeno ocurre en la Tierra? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("9. ¿Causa catástrofes? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en un Fenómeno Climático (huracanes, terremotos).")
                    else: 
                        respuesta = input("10. ¿Es un campo de estudio científico? (si/no): ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("11. ¿Es una fuerza fundamental? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Estás pensando en una Fuerza Natural (gravedad, magnetismo).")
                            else:
                                respuesta = input("12. ¿Se manifiesta como vibración o pulsación? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Estás pensando en Ondas (sonoras, electromagnéticas, sísmicas).")
                                else:
                                    print("Estás pensando en una Forma de Energía (cinética, térmica).")
                else:
                    print("Estás pensando en un Fenómeno Extraterrestre (auroras boreales, lluvias de meteoros).")


adivinar()