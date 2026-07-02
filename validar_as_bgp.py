# Examen Transversal DRY7122
# Validación AS BGP


as_bgp = int(input("Ingrese número de AS BGP: "))


if 64512 <= as_bgp <= 65534:
    print("El AS BGP es PRIVADO")


elif 4200000000 <= as_bgp <= 4294967294:
    print("El AS BGP es PRIVADO")


else:
    print("El AS BGP es PÚBLICO")