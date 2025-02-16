def adivinar():
    print("Adivinaré lo que estás pensando")
    
    respuesta = input("1. ¿Es algo vivo? (si/no/no lo se): ").strip().lower()
    if respuesta == "si":
        respuesta = input("2. ¿Es un animal? (si/no/no lo se): ").strip().lower()
        if respuesta == "si":
            respuesta = input("¿Es un vertebrado? (si/no/no lo se): ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Es un mamífero? (si/no/no lo se): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es un ser humano? (si/no/no lo se): ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en un ser humano.")
                    else:
                        print("Estás pensando en otro mamífero.")
                else:
                    print("Estás pensando en un vertebrado que no es mamífero.")
            else:
                print("Estás pensando en un invertebrado.")
        else:
            print("Estás pensando en un ser vivo que no es un animal.")
    elif respuesta == "no":
        respuesta = input("2. ¿Es un objeto? (si/no/no lo se): ").strip().lower()
        if respuesta == "si":
            respuesta = input("3. ¿Se encuentra en un entorno conocido? (si/no/no lo se): ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Está en un aula? (si/no/no lo se): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Estás pensando en un escritorio? (si/no/no lo se): ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en un escritorio.")
                        return
                    respuesta = input("¿Estás pensando en una pizarra? (si/no/no lo se): ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en una pizarra.")
                        return
                respuesta = input("¿Está en una casa? (si/no/no lo se): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Estás pensando en una puerta? (si/no/no lo se): ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en una puerta.")
                        return
                    respuesta = input("¿Estás pensando en un sofá? (si/no/no lo se): ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en un sofá.")
                        return
                respuesta = input("¿Está en una oficina? (si/no/no lo se): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Estás pensando en una computadora? (si/no/no lo se): ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en una computadora.")
                        return
                    respuesta = input("¿Estás pensando en una impresora? (si/no/no lo se): ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en una impresora.")
                        return
                respuesta = input("¿Está en un exterior? (si/no/no lo se): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Estás pensando en una farola? (si/no/no lo se): ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en una farola.")
                        return
                    respuesta = input("¿Estás pensando en un banco? (si/no/no lo se): ").strip().lower()
                    if respuesta == "si":
                        print("Estás pensando en un banco.")
                        return
            print("No se pudo determinar el objeto.")
        else:
            print("Estás pensando en algo intangible.")
    else:
        print("No se pudo determinar lo que estás pensando.")

adivinar()
