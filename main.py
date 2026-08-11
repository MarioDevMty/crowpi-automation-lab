import tkinter as tk


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 660


def main():
    root = tk.Tk()

    root.title("CrowPi Automation Lab")

    # Ventana de desarrollo:
    # usa todo el ancho y deja espacio para la barra superior
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+30")

    root.resizable(False, False)

    # Salidas seguras durante desarrollo
    root.bind("<Escape>", lambda event: root.destroy())

    title = tk.Label(
        root,
        text="CROWPI AUTOMATION LAB",
        font=("Arial", 30, "bold")
    )
    title.pack(pady=25)

    subtitle = tk.Label(
        root,
        text="LAB 01 - Botón + Buzzer",
        font=("Arial", 22)
    )
    subtitle.pack(pady=10)

    status = tk.Label(
        root,
        text="Sistema listo",
        font=("Arial", 20)
    )
    status.pack(pady=30)

    test_button = tk.Button(
        root,
        text="BOTÓN DE PRUEBA",
        font=("Arial", 20, "bold"),
        width=20,
        height=2
    )
    test_button.pack(pady=20)

    resolution = tk.Label(
        root,
        text=(
            f"Pantalla detectada: "
            f"{root.winfo_screenwidth()} x "
            f"{root.winfo_screenheight()}"
        ),
        font=("Arial", 14)
    )
    resolution.pack(pady=20)

    exit_button = tk.Button(
        root,
        text="SALIR",
        font=("Arial", 16),
        command=root.destroy
    )
    exit_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()