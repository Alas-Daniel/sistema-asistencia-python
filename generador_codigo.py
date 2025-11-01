import barcode
from barcode.writer import ImageWriter
import os

os.makedirs("codigos", exist_ok=True)

def generar_codigo(nombre_archivo, codigo):
    tipo = barcode.get_barcode_class('code128')
    codigo_barra = tipo(codigo, writer=ImageWriter())
    ruta_completa = f"codigos/{nombre_archivo}.png"
    codigo_barra.save(ruta_completa)
    return ruta_completa
