import sys
from pathlib import Path
import tkinter as tk
from model.modelo import simular_dado
from view.vista import App
from controller.controlador import Controlador

def main():
    root = tk.Tk()
    vista = App(root)
    controlador = Controlador(vista, simular_dado)
    root.mainloop()

if __name__ == "__main__":
    main()