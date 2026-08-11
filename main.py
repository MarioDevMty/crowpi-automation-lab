import tkinter as tk


def main():
    root = tk.Tk()

    root.title("CrowPi Automation Lab")

    # Obtener resolución real de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Forzar tamaño exacto de pantalla
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    # Quitar bordes y barra de título
    root.overrideredirect(True)

    # Llevar al frente
    root.lift()

    # ESC para salir
    root.bind("<Escape>", lambda event: root.destroy())

    title = tk.Label(
        root,
        text="CROWPI AUTOMATION LAB",
        font=("Arial", 30, "bold")
    )
    title.pack(pady=40)

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
    status.pack(pady=40)

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
        text=f"Resolución detectada: {screen_width} x {screen_height}",
        font=("Arial", 14)
    )
    resolution.pack(pady=30)

    root.mainloop()


if __name__ == "__main__":
    main()