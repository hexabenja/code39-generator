import sys
import barcode
from barcode.writer import ImageWriter

def generar_code39(texto):
    # Crear clase Code39
    code39 = barcode.get_barcode_class('code39')

    # Generar código de barras
    codigo = code39(texto, writer=ImageWriter(), add_checksum=False)

    # Guardar imagen en el directorio actual
    nombre_archivo = codigo.save(texto)

    print(f"Código de barras generado: {nombre_archivo}.png")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python app.py \"texto\"")
        sys.exit(1)

    texto = sys.argv[1]
    generar_code39(texto)
