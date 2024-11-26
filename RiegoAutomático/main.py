import gpiod
import time

# Definir el nombre del chip GPIO
CHIP_NAME = "/dev/gpiochip4"

# Número de línea GPIO que queremos controlar (17)
LINE_NUMBER = 27

def main():
    # Crear un objeto de chip GPIO
    chip = gpiod.Chip(CHIP_NAME)
    
    # Solicitar la línea GPIO
    line = chip.get_line(LINE_NUMBER)
    
    # Configurar como salida
    line.request(consumer="riegoAutomatico", type=gpiod.LINE_REQ_DIR_OUT)

    try:
        # Activar la línea GPIO (valor 1)
        line.set_value(1)
        print(f"GPIO {LINE_NUMBER} activado durante 3 segundos.")
        
        # Esperar 3 segundos
        time.sleep(3)
        
        # Desactivar la línea GPIO (valor 0)
        line.set_value(0)
        print(f"GPIO {LINE_NUMBER} desactivado.")
        
    finally:
        # Liberar la línea GPIO
        line.release()

if __name__ == "__main__":
    main()