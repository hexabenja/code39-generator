import tkinter as tk
from tkinter import scrolledtext
import barcode
from barcode.writer import ImageWriter

class TerminalSimple:
    def __init__(self, root):
        self.root = root
        self.root.title("Terminal Code39")
        self.root.configure(bg='#1e1e1e')
        
        # Área de salida simplificada
        self.output = scrolledtext.ScrolledText(root, bg='#1e1e1e', fg="#d4d4d4", state='disabled', height=15)
        self.output.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Campo de entrada
        self.input_field = tk.Entry(root, bg='#252526', fg="#d4d4d4")
        self.input_field.pack(fill='x', padx=10, pady=10)
        self.input_field.bind('<Return>', self.procesar_entrada)
        
        self.escribir("Escribe el código y presiona Enter. 'salir' para cerrar.\n")
        self.input_field.focus()
    
    def escribir(self, texto):
        self.output.config(state='normal')
        self.output.insert(tk.END, texto)
        self.output.see(tk.END)
        self.output.config(state='disabled', fg="#d4d4d4")
    
    def procesar_entrada(self, event=None):
        codigo = self.input_field.get().strip()
        self.input_field.delete(0, tk.END)
        
        if not codigo: return
        if codigo.lower() in ['salir', 'ya']:
            self.root.quit()
            return
            
        self.escribir(f"> {codigo}\n")
        self.generar_codigo(codigo)
    
    def generar_codigo(self, texto):
            code39 = barcode.get_barcode_class('code39')
            writer = ImageWriter()
            options = {
                "font_path": "arial.ttf", # Windows
                "font_size": 10,
                "text_distance": 5
            }
            # Genera y guarda directamente
            nombre = code39(texto.upper(), writer=ImageWriter(), add_checksum=False).save(texto.upper())
            self.escribir(f"Archivo generado: {nombre}\n")


if __name__ == "__main__":
    root = tk.Tk()
    TerminalSimple(root)
    root.mainloop()
