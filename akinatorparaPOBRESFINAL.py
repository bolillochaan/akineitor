def adivinar():
    print("¡Adivinaré lo que estás pensando! Pero moderate, tampoco exageres\n")
    print("Responde con 'si', 'no' o 'no lo sé'.\n")

    respuesta = input("1. ¿Es algo vivo? ").strip().lower()
    if respuesta == "si":
        respuesta = input("2. ¿Es un animal? ").strip().lower()
        if respuesta == "si":
            respuesta = input("¿Es un vertebrado? ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Es un mamífero? ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es un ser humano? ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en un ser humano.")
                    else:
                        respuesta = input("¿Es una mascota como un perro, un gato o un conejo? ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("¿Es un perro? ").strip().lower()
                            if respuesta == "si":
                                respuesta = input("¿Es una raza específica como labrador, pastor alemán o chihuahua? ").strip().lower()
                                if respuesta == "si":
                                    print("Estás pensando en una raza de perro.")
                                else:
                                    print("Estás pensando en un perro en general.")
                            elif respuesta == "no":
                                respuesta = input("¿Es un gato? ").strip().lower()
                                if respuesta == "si":
                                    print("Estás pensando en un gato.")
                                else:
                                    respuesta = input("¿Es un conejo u otro tipo de mascota pequeña? ").strip().lower()
                                    if respuesta == "si":
                                        print("Estás pensando en un conejo u otra mascota pequeña.")
                                    else:
                                        print("Estás pensando en una mascota menos común.")
                        else:
                            respuesta = input("¿Es un mamífero salvaje como un león, un oso o un delfín? ").strip().lower()
                            if respuesta == "si":
                                print("Estás pensando en un mamífero salvaje.")
                            else:
                                print("Estás pensando en un mamífero menos común.")
                else:
                    respuesta = input("¿Es un ave? ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("¿Es un ave común como un gallo, una paloma o un canario? ").strip().lower()
                        if respuesta == "si":
                            print("Estás pensando en un ave común.")
                        else:
                            respuesta = input("¿Es un ave exótica como un loro, un tucán o un águila? ").strip().lower()
                            if respuesta == "si":
                                print("Estás pensando en un ave exótica.")
                            else:
                                print("Estás pensando en un ave menos conocida.")
                    else:
                        respuesta = input("¿Es un reptil, un anfibio o un pez? ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("¿Es un reptil como una serpiente, un lagarto o una tortuga? ").strip().lower()
                            if respuesta == "si":
                                print("Estás pensando en un reptil.")
                            elif respuesta == "no":
                                respuesta = input("¿Es un anfibio como una rana o un ajolote? ").strip().lower()
                                if respuesta == "si":
                                    print("Estás pensando en un anfibio.")
                                else:
                                    print("Estás pensando en un pez.")
                        else:
                            print("Estás pensando en otro tipo de vertebrado.")
            else:
                respuesta = input("¿Es un insecto como una mariposa, una abeja o una hormiga? ").strip().lower()
                if respuesta == "si":
                    print("Estás pensando en un insecto.")
                else:
                    print("Estás pensando en un invertebrado menos común.")
        else:
            respuesta = input("¿Es una planta? ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Es una planta que da frutos o vegetales como un manzano o un tomate? ").strip().lower()
                if respuesta == "si":
                    print("Estás pensando en una planta frutal o vegetal.")
                else:
                    respuesta = input("¿Es una flor o planta decorativa como una rosa o un girasol? ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en una planta decorativa.")
                    else:
                        print("Estás pensando en otro tipo de planta.")
            else:
                print("Estás pensando en otro ser vivo, como un hongo o bacteria.")
    elif respuesta == "no":
        respuesta = input("2. ¿Es un objeto físico? ").strip().lower()
        if respuesta == "si":
            respuesta = input("¿Es algo tecnológico como un dispositivo electrónico? ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Es portátil como un celular, una tablet o una laptop? ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es un celular? ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en un celular.")
                    else:
                        print("Estás pensando en otro dispositivo portátil.")
                else:
                    print("Estás pensando en otro tipo de tecnología.")
            else:
                respuesta = input("¿Es algo cotidiano como muebles, ropa o herramientas? ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es un mueble como una silla o una mesa? ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en un mueble.")
                    else:
                        respuesta = input("¿Es una prenda de ropa como una camisa o un pantalón? ").strip().lower()
                        if respuesta == "si":
                            print("Estás pensando en ropa.")
                        else:
                            print("Estás pensando en una herramienta o utensilio.")
                else:
                    print("Estás pensando en un objeto físico menos común.")
        else:
            respuesta = input("¿Es algo natural como un fenómeno o un elemento? ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Es un fenómeno meteorológico como la lluvia o el viento? ").strip().lower()
                if respuesta == "si":
                    print("Estás pensando en un fenómeno meteorológico.")
                else:
                    print("Estás pensando en algo natural, como una roca o un elemento químico.")
            else:
                print("Estás pensando en algo abstracto o intangible.")
    else:
        print("No pude determinar lo que estás pensando. ¡Inténtalo de nuevo!")

adivinar()
