import sys
import platform

def main():
    # Determinar la arquitectura del sistema
    arquitectura = platform.architecture()[0]
    
    print(f"Este programa está corriendo en un sistema de {arquitectura}")
    
    # Aquí puedes agregar la lógica principal de tu programa
    # que funcionará tanto en 32 como en 64 bits
    
    print("Hola, mundo!")

    input("Presiona Enter para continuar...")
if __name__ == "__main__":
    main()

