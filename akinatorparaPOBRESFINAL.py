def adivinar():
    print("¡Adivinaré lo que estás pensando! Pero modérate, tampoco exageres")
    print("Responde con 'si', 'no'.\n")

    # Primera pregunta base
    respuesta = input("1. ¿Es algo vivo? ").strip().lower()
    if respuesta == "si":
        # Rama de seres vivos
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
        # Rama de no vivos
        respuesta = input("2. ¿Es un objeto físico? ").strip().lower()
        if respuesta == "si":
            respuesta = input("3. ¿Es algo tecnológico como un dispositivo electrónico? ").strip().lower()
            if respuesta == "si":
                respuesta = input("4. ¿Es portátil como un celular, una tablet o una laptop? ").strip().lower()
                if respuesta == "si":
                    respuesta = input("5. ¿Es un celular? ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en un celular.")
                    else:
                        print("Estás pensando en otro dispositivo portátil.")
                else:
                    respuesta = input("4. ¿Es una computadora? ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en una computadora.")
                    else:
                        respuesta = input("5. ¿Es una impresora? ").strip().lower()
                        if respuesta == "si":
                            print("Estás pensando en una impresora.")
                        else:
                            print("Estás pensando en otro tipo de tecnología.")
            else:
                respuesta = input("3. ¿Es algo cotidiano como muebles, ropa o herramientas? ").strip().lower()
                if respuesta == "si":
                    respuesta = input("4. ¿Es un mueble como una silla o una mesa? ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en un mueble.")
                    else:
                        respuesta = input("5. ¿Es una prenda de ropa como una camisa o un pantalón? ").strip().lower()
                        if respuesta == "si":
                            print("Estás pensando en ropa.")
                        else:
                            print("Estás pensando en una herramienta o utensilio.")
                else:
                    print("Estás pensando en un objeto físico menos común.")
       
       
       #Rama de INTANGIBLES
        else:
 
            respuesta = input("3. ¿Es intangible? ").strip().lower()
            if respuesta == "si":
                respuesta = input("4. ¿Es creación humana? ").strip().lower()
                if respuesta == "si":
                    respuesta = input("5. ¿Es un acontecimiento? ").strip().lower()
                    if respuesta == "si":
                        print("¡Es una festividad!")
                    else:
                        #CONTENIDO DE ENTRETENIMIENTO
                        respuesta = input("6. ¿Es entretenimiento audiovisual? ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("7. ¿Es animación? ").strip().lower()
                            if respuesta == "si":
                                print("¡Es un Anime!")
                            else:
                                respuesta = input("8. ¿El contenido se divide en capítulos? ").strip().lower()
                                print("¡Es una Serie!" if respuesta == "si" else "¡Es una Película!")
                        else:
                            respuesta = input("6. ¿Es de producción musical? ").strip().lower()
                            if respuesta == "si":
                                print("¡Es Música!")
                            else:
                                respuesta = input("7. ¿Es arte literario? ").strip().lower()
                                print("¡Es un Libro/Novela!" if respuesta == "si" else "¡Es Poesía u obra dramática!")
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
                                respuesta = input("8. ¿Puedes vacacionar, pasar el rato ahí ? ").strip().lower()
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