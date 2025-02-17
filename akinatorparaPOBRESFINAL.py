def adivinar():
    print("¡Adivinaré lo que estás pensando! Pero modérate, tampoco exageres")
    print("Responde con 'si', 'no'.\n")

    respuesta = input("1. ¿Es algo vivo? ").strip().lower()
    
    if respuesta == "si":
        # Rama de seres vivos (sin cambios)
        respuesta = input("2. ¿Es un animal? ").strip().lower()
        if respuesta == "si":
            respuesta = input("3. ¿Es un vertebrado? ").strip().lower()
            if respuesta == "si":
                respuesta = input("4. ¿Es un mamífero? ").strip().lower()
                if respuesta == "si":
                    respuesta = input("5. ¿Es un ser humano? ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en un ser humano.")
                    else:
                        print("Estás pensando en otro mamífero.")
                        respuesta = input("6. ¿Es una mascota como un perro, un gato o un conejo? ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("7. ¿Es un perro? ").strip().lower()
                            if respuesta == "si":
                                respuesta = input("8. ¿Es una raza específica como labrador, pastor alemán o chihuahua? ").strip().lower()
                                if respuesta == "si":
                                    print("Estás pensando en una raza de perro.")
                                else:
                                    print("Estás pensando en un perro en general.")
                            elif respuesta == "no":
                                respuesta = input("7. ¿Es un gato? ").strip().lower()
                                if respuesta == "si":
                                    print("Estás pensando en un gato.")
                                else:
                                    respuesta = input("8. ¿Es un conejo u otro tipo de mascota pequeña? ").strip().lower()
                                    if respuesta == "si":
                                        print("Estás pensando en un conejo u otra mascota pequeña.")
                                    else:
                                        print("Estás pensando en una mascota menos común.")
                        else:
                            respuesta = input("6. ¿Es un mamífero salvaje como un león, un oso o un delfín? ").strip().lower()
                            if respuesta == "si":
                                print("Estás pensando en un mamífero salvaje.")
                            else:
                                print("Estás pensando en un mamífero menos común.")
                else:
                    print("Estás pensando en un vertebrado que no es mamífero.")
                    respuesta = input("5. ¿Es un ave? ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("6. ¿Es un ave común como un gallo, una paloma o un canario? ").strip().lower()
                        if respuesta == "si":
                            print("Estás pensando en un ave común.")
                        else:
                            respuesta = input("7. ¿Es un ave exótica como un loro, un tucán o un águila? ").strip().lower()
                            if respuesta == "si":
                                print("Estás pensando en un ave exótica.")
                            else:
                                print("Estás pensando en un ave menos conocida.")
                    else:
                        respuesta = input("5. ¿Es un reptil, un anfibio o un pez? ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("6. ¿Es un reptil como una serpiente, un lagarto o una tortuga? ").strip().lower()
                            if respuesta == "si":
                                print("Estás pensando en un reptil.")
                            elif respuesta == "no":
                                respuesta = input("7. ¿Es un anfibio como una rana o un ajolote? ").strip().lower()
                                if respuesta == "si":
                                    print("Estás pensando en un anfibio.")
                                else:
                                    print("Estás pensando en un pez.")
                        else:
                            print("Estás pensando en otro tipo de vertebrado.")
            else:
                print("Estás pensando en un invertebrado.")
                respuesta = input("4. ¿Es un insecto como una mariposa, una abeja o una hormiga? ").strip().lower()
                if respuesta == "si":
                    print("Estás pensando en un insecto.")
                else:
                    print("Estás pensando en un invertebrado menos común.")
        else:
            print("Estás pensando en un ser vivo que no es un animal.")
            respuesta = input("3. ¿Es una planta? ").strip().lower()
            if respuesta == "si":
                respuesta = input("4. ¿Es una planta que da frutos o vegetales como un manzano o un tomate? ").strip().lower()
                if respuesta == "si":
                    print("Estás pensando en una planta frutal o vegetal.")
                else:
                    respuesta = input("5. ¿Es una flor o planta decorativa como una rosa o un girasol? ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en una planta decorativa.")
                    else:
                        print("Estás pensando en otro tipo de planta.")
            else:
                print("Estás pensando en otro ser vivo, como un hongo o bacteria.")

    elif respuesta == "no":
        # Rama de objetos no vivos
        respuesta = input("2. ¿Es un objeto físico? ").strip().lower()
        
        if respuesta == "si":
            # Categorización de objetos físicos
            respuesta = input("3. ¿Es un dispositivo tecnológico? ").strip().lower()
            
            if respuesta == "si":
                # Subcategorías tecnológicas
                respuesta = input("4. ¿Es portátil? (celular, tablet, laptop) ").strip().lower()
                if respuesta == "si":
                    respuesta = input("5. ¿Es un smartphone? ").strip().lower()
                    print("Es un celular." if respuesta == "si" else "Es otro dispositivo portátil")
                else:
                    respuesta = input("4. ¿Es de uso doméstico? (TV, consola, electrodoméstico) ").strip().lower()
                    if respuesta == "si":
                        print("Es un dispositivo doméstico.")
                    else:
                        respuesta = input("5. ¿Está relacionado con tecnología espacial? (satélites, trajes espaciales) ").strip().lower()
                        if respuesta == "si":
                            print("¡Es tecnología espacial!")
                        else:
                            respuesta = input("6. ¿Es arte digital o realidad virtual? (hologramas, dispositivos VR) ").strip().lower()
                            print("¡Es arte digital o tecnología de realidad virtual!" if respuesta == "si" else "Es otro tipo de tecnología especializada")
            else:
                respuesta = input("4. ¿Es una herramienta? ").strip().lower()
                if respuesta == "si":
                    respuesta = input("5. ¿Lo utilizas en la oficina? ").strip().lower()
                    if respuesta == "si":
                        print("Es una herramienta de oficina.")
                    else:
                        respuesta = input("6. ¿Lo utilizas para limpiar? ").strip().lower()
                        if respuesta == "si":
                            print("Es un objeto de Limpieza.")
                        else:
                            respuesta = input("7. ¿Se utiliza en el ámbito médico? ").strip().lower()
                            if respuesta == "si":
                                print("Es una Herramienta médica.")
                            else:
                                respuesta = input("8. ¿Te puedes transportar en él? ").strip().lower()
                                if respuesta == "si":
                                    print("Es un Medio de Transporte.")
                                else:
                                    respuesta = input("8. ¿Lo ocupas en la cocina? ").strip().lower()
                            if respuesta == "si":
                                    print("Es una herramienta de cocina (cuchillo, batidoras, etc).")
                            else:
                                respuesta = input("9. ¿Es un arma o instrumento de defensa? (espadas, misiles, equipamiento bélico) ").strip().lower()
                    if respuesta == "si":
                        print("Es un arma o equipo bélico!" if respuesta == "si" else "Es un herramienta de construcción")
    
                else:
                    if respuesta == "si":
                        respuesta = input("5. ¿Es un utencilio? ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("6. ¿Lo ocupas en la oficina? ").strip().lower()
                            if respuesta == "si":
                                print("Es utencilio de oficina (boligrafo, pápel, lapiz, etc)")
                            else:
                                respuesta = input("7. ¿Lo ocupas en la cocina? ").strip().lower()
                                if respuesta == "si":
                                    print("Es utencilio de cocina (cuchara, plato, etc)")
                                else:
                                    respuesta = input("8. ¿Lo ocupas para limpar algo o limpiarte? ").strip().lower()
                                    print("Es utencilio de limpieza" if respuesta == "si" else "Es un utincilio de jardinería")
                    else:
                        respuesta = input("9. ¿Es para el hogar o vestimenta? ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("10. ¿Es un mueble? ").strip().lower()
                            if respuesta == "si":
                                print("Tu objeto es un Mueble (silla, mesa, cama)")
                            else:
                                respuesta = input("11. ¿Lo puede poner sobre algún objeto o persona? ").strip().lower()
                                if respuesta == "si":
                                    print("Tu objeto es una ropa, accesorio o ropa de cama")
                                else: 
                                    respuesta = input("12. ¿Lo ocupas para decorar? ").strip().lower()
                                    if respuesta == "si":
                                        print("Tu objeto es alguna decoración del hogar (cuadro, jarrón, lámpara)")
                                    else:
                                        print("Es un objeto de almacenamiento")
                        else:
                            respuesta = input("10. ¿Está relacionado con el entrenimiento o actividad física? ").strip().lower()
                            if respuesta == "si":
                                respuesta = input("11. ¿Lo ocupas en algún deporte? ").strip().lower()
                                if respuesta == "si":
                                    print("Tu objeto es Deportivo (balón, raqueta, pesas)")
                                else:
                                    respuesta = input("12. ¿El objeto produce notas músicales? ").strip().lower()
                                    if respuesta == "si":
                                        print("Tu objeto es un Instrumento Músical")
                                    else:
                                        print("Es un Juguete")
                            else:
                                respuesta = input("11. ¿Se podría considerar un Insumo? ").strip().lower()
                                if respuesta == "si":
                                    respuesta = input("12. ¿Se ocupa en construcciones? ").strip().lower()
                                    print("Tu objeto es un material de construcción)")
                                else:
                                    if respuesta == "si":
                                        respuesta = input("13. ¿Se ocupa para curar/tratar enfermedades/lesiones? ").strip().lower()
                                        print("Tu objeto es un medicamento o un vendaje)")
                                    else:
                                        if respuesta == "si":
                                            respuesta = input("13. ¿Se ocupa para limpiar superficies? ").strip().lower()
                                            print("Tu objeto es un insumo de limpieza(Detergente, Limpiadores, etc.)" if respuesta == "si" else "Es un insumo de oficina")
        else:
            # Rama de INTANGIBLES
            respuesta = input("3. ¿Es intangible? ").strip().lower()
            if respuesta == "si":
                respuesta = input("4. ¿Es creación humana? ").strip().lower()
                if respuesta == "si":
                    respuesta = input("5. ¿Es un acontecimiento? ").strip().lower()
                    if respuesta == "si":
                        print("¡Es una festividad!")
                    else:
                        # CONTENIDO DE ENTRETENIMIENTO
                        respuesta = input("6. ¿Es entretenimiento audiovisual? ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("7. ¿Es de animación japonesa? ").strip().lower()
                            if respuesta == "si":
                                print("¡Es un Anime!")
                            else:
                                respuesta = input("8. ¿El contenido se divide en capítulos? ").strip().lower()
                                print("¡Es una Serie!" if respuesta == "si" else "¡Es una Película!")
                        else:
                            respuesta = input("6. ¿Es de producción musical? ").strip().lower()
                            if respuesta == "si":
                                print("¡Es Música!")
                            # NUEVA CATEGORÍA AÑADIDA AQUÍ
                                respuesta = input("8. ¿Está relacionado con tecnología digital? ").strip().lower()
                                if respuesta == "si":
                                    respuesta = input("9. ¿Es un lenguaje de programación o herramienta de desarrollo? (Ej: Python, Git) ").strip().lower()
                                    if respuesta == "si":
                                        print("¡Es un lenguaje de programación o herramienta de desarrollo!")
                                    else:
                                        respuesta = input("10. ¿Es un sistema de inteligencia artificial? (redes neuronales, machine learning) ").strip().lower()
                                        print("¡Es inteligencia artificial!" if respuesta == "si" else "¡Es otra tecnología digital avanzada!")
                            else:
                                respuesta = input("8. ¿Es texto que narra alguna historia? ").strip().lower()
                                print("¡Es un Libro, Novela u obra dramática!" if respuesta == "si" else "¡Es una Poesía!")
                else:
                    print("¡Estás pensando en alguna religión!")
            else:
                # Rama de materiales y fenómenos
                respuesta = input("4. ¿Es un material? ").strip().lower()
                if respuesta == "si":
                    respuesta = input("5. ¿Es un Elemento? ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("6. ¿Es de origen natural? ").strip().lower()
                        if respuesta == "si":
                            print("Elemento Natural (Ej: Oro Au, Oxígeno O)")
                        else:
                            print("Elemento Sintético (Ej: Plutonio Pu)")
                    else:
                        respuesta = input("5. ¿Es compuesto? ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("6. ¿Es orgánico? ").strip().lower()
                            print("Compuesto Orgánico" if respuesta == "si" else "Compuesto Inorgánico")
                        else:
                            respuesta = input("6. ¿Es mezcla homogénea? ").strip().lower()
                            if respuesta == "si":
                                respuesta = input("7. ¿Es aleación? ").strip().lower()
                                print("Aleación metálica" if respuesta == "si" else "Mezcla homogénea")
                            else:
                                print("Mezcla heterogénea o coloide")
                else:
                    respuesta = input("4. ¿Se obtiene de la tierra? ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("5. ¿Se produce de manera artificial? ").strip().lower()
                        print("Estás pensando en un Combustible." if respuesta == "si" else "Estás pensando en un Recurso Geológico (como minerales o rocas).")
                    else:
                        respuesta = input("6. ¿Ocurre en la Tierra? ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("7. ¿Causa catástrofes naturales? ").strip().lower()
                            if respuesta == "si":
                                print("Estás pensando en un Fenómeno Climático (huracanes, terremotos).")
                            else:
                                respuesta = input("8. ¿Puedes vacacionar, pasar el rato ahí? ").strip().lower()
                                if respuesta == "si":
                                    print("Estás pensando en un Lugar o País.")
                                else: 
                                    respuesta = input("8. ¿Es una fuerza fundamental? ").strip().lower()
                                    if respuesta == "si":
                                        print("Estás pensando en una Fuerza Natural (gravedad, magnetismo).")
                                    else:
                                        respuesta = input("9. ¿Se manifiesta como vibración o pulsación? ").strip().lower()
                                        print("Estás pensando en Ondas (sonoras, electromagnéticas, sísmicas)." if respuesta == "si" else "Estás pensando en una Forma de Energía (cinética, térmica).")
                        else:
                            print("Estás pensando en un Fenómeno Extraterrestre (auroras boreales, lluvias de meteoros).")

adivinar()