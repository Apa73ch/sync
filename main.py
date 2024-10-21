import sys
import platform
import os
import msvcrt
from colorama import init, Fore, Back, Style
import ctypes

init(autoreset=True)

def set_console_size(columns, rows):
    os.system(f'mode con: cols={columns} lines={rows}')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write(Back.BLUE + ' ' * (ANCHO * ALTO))
    sys.stdout.flush()
    sys.stdout.write('\033[H')
    sys.stdout.flush()

def imprimir_logo(x, y):
    logo = [
        f"{Fore.GREEN}     ╔═╗ {Fore.CYAN} ╔═╗ {Fore.YELLOW} ╔═╗  ",
        f"{Fore.GREEN}    ╔╝ ║{Fore.CYAN} ╔╝ ║{Fore.YELLOW} ╔╝ ║  ",
        f"{Fore.GREEN}   ╔╝  ║{Fore.CYAN}╔╝  ║{Fore.YELLOW}╔╝  ║  ",
        f"{Fore.GREEN}   ║ ▄ ║{Fore.CYAN}║ ▄ ║{Fore.YELLOW}║ ▄ ║  ",
        f"{Fore.GREEN}   ║ █ ║{Fore.CYAN}║ █ ║{Fore.YELLOW}║ █ ║  ",
        f"{Fore.GREEN}   ╚═══╝{Fore.CYAN}╚═══╝{Fore.YELLOW}╚═══╝  ",
        f"{Fore.WHITE}  INDUSTRIAS JUFECA "
    ]
    for i, line in enumerate(logo):
        sys.stdout.write(f"\033[{y+i};{x}H" + Style.BRIGHT + line)

def imprimir_menu(opciones, seleccionada):
    clear_screen()
    ancho_menu = max(len(opcion) for opcion in opciones) + 4  # +4 para el margen
    margen_izquierdo = 5
    margen_superior = 3

    # Fondo azul para toda la pantalla
    for _ in range(ALTO):
        sys.stdout.write(Back.BLUE + ' ' * ANCHO + '\n')
    sys.stdout.write('\033[H')  # Volver al inicio de la pantalla

    # Margen superior
    for _ in range(margen_superior):
        sys.stdout.write(Back.BLUE + ' ' * ANCHO + '\n')

    # Borde superior del menú
    sys.stdout.write(Back.BLUE + ' ' * margen_izquierdo + Fore.WHITE + '┌' + '─' * (ancho_menu + 2) + '┐\n')

    # Título del menú
    sys.stdout.write(Back.BLUE + ' ' * margen_izquierdo + Fore.WHITE + '│ ' + Style.BRIGHT + "Menú Principal".center(ancho_menu) + ' │\n')

    # Línea separadora
    sys.stdout.write(Back.BLUE + ' ' * margen_izquierdo + Fore.WHITE + '├' + '─' * (ancho_menu + 2) + '┤\n')

    # Opciones del menú
    for i, opcion in enumerate(opciones):
        linea = Back.BLUE + ' ' * margen_izquierdo + Fore.WHITE + '│ '
        if i == seleccionada:
            linea += Fore.BLACK + Back.WHITE + Style.BRIGHT + f"{opcion.ljust(ancho_menu)}" + Fore.WHITE + Back.BLUE
        else:
            linea += Fore.WHITE + Back.BLUE + Style.BRIGHT + f"{opcion.ljust(ancho_menu)}"
        linea += ' │'
        sys.stdout.write(linea + '\n')

    # Borde inferior del menú
    sys.stdout.write(Back.BLUE + ' ' * margen_izquierdo + Fore.WHITE + '└' + '─' * (ancho_menu + 2) + '┘\n')

    # Opciones adicionales
    sys.stdout.write(Back.BLUE + '\n' + ' ' * margen_izquierdo + Fore.YELLOW + Style.BRIGHT + "╔═══════════════════════════════════════╗")
    sys.stdout.write(Back.BLUE + '\n' + ' ' * margen_izquierdo + Fore.YELLOW + Style.BRIGHT + "║ F7 - Ver listado de pagos             ║")
    sys.stdout.write(Back.BLUE + '\n' + ' ' * margen_izquierdo + Fore.YELLOW + Style.BRIGHT + "║ F8 - Ver listado de bancos            ║")
    sys.stdout.write(Back.BLUE + '\n' + ' ' * margen_izquierdo + Fore.YELLOW + Style.BRIGHT + "╚═══════════════════════════════════════╝")

    # Imprimir logo
    imprimir_logo(ANCHO - 25, margen_superior + 1)

    sys.stdout.flush()

def mostrar_mensaje(mensaje):
    clear_screen()
    sys.stdout.write(Fore.WHITE + Back.BLUE + Style.BRIGHT + f"\n{mensaje}\n")
    sys.stdout.write(Fore.WHITE + Back.BLUE + Style.BRIGHT + "\nPresiona Enter para continuar...")
    sys.stdout.flush()
    msvcrt.getch()

def main():
    arquitectura = platform.architecture()[0]
    clear_screen()

    opciones = [
        "Opción 1: Hacer algo",
        "Opción 2: Hacer otra cosa",
        "Opción 3: Calcular algo",
        "Opción 4: Mostrar información",
        "Opción 5: Procesar datos",
        "Opción 6: Configurar algo",
        "Opción 7: Salir"
    ]
    seleccionada = 0

    while True:
        imprimir_menu(opciones, seleccionada)
        
        key = msvcrt.getch()
        print(key)
        key = msvcrt.getch()
        if key == b'H':  # Flecha arriba
            seleccionada = (seleccionada - 1) % len(opciones)
        elif key == b'P':  # Flecha abajo
            seleccionada = (seleccionada + 1) % len(opciones)
        elif key == b'A':  # F7
            mostrar_mensaje("Has seleccionado: Ver listado de pagos")
        elif key == b'B':  # F8
            mostrar_mensaje("Has seleccionado: Ver listado de bancos")
        elif key == b'\r':  # Enter
            if seleccionada == len(opciones) - 1:  # Última opción (Salir)
                break
            else:
                mostrar_mensaje(f"Has seleccionado: {opciones[seleccionada]}")

    clear_screen()
    sys.stdout.write(Fore.WHITE + Back.BLUE + Style.BRIGHT + "¡Gracias por usar el programa!\n")
    sys.stdout.flush()

if __name__ == "__main__":
    ANCHO, ALTO = 80, 25  # Tamaño fijo de la ventana
    set_console_size(ANCHO, ALTO)
    
    # Cambiar el título de la ventana
    ctypes.windll.kernel32.SetConsoleTitleW("Industrias JUFECA - Menú Principal")
    
    main()
