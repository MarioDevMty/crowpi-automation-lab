import tkinter as tk


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


def main():
    root = tk.Tk()

    root.title("CrowPi Automation Lab")
    root.attributes("-fullscreen", True)
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
        text="Resolución objetivo: 1280 x 720",
        font=("Arial", 14)
    )
    resolution.pack(pady=30)

    root.mainloop()


if __name__ == "__main__":
    main()