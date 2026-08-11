import tkinter as tk
from datetime import datetime


import tkinter as tk
from datetime import datetime

from config import WINDOW_WIDTH, WINDOW_HEIGHT


class CrowPiLabApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CrowPi Automation Lab")

        # Ventana segura para desarrollo
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+30")
        self.root.resizable(False, False)

        # Salidas
        self.root.bind("<Escape>", lambda event: self.root.destroy())

        # Estado inicial de simulación
        self.button_pressed = False
        self.buzzer_active = False

        self.build_interface()

        self.add_event("Sistema iniciado")
        self.add_event("Modo SIMULACIÓN activo")

    def build_interface(self):

        # =========================
        # ENCABEZADO
        # =========================
        header = tk.Frame(self.root, height=70)
        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="CROWPI AUTOMATION LAB",
            font=("Arial", 24, "bold")
        )
        title.pack(side="left", padx=25, pady=15)

        lab = tk.Label(
            header,
            text="LAB 01 - Botón + Buzzer",
            font=("Arial", 16)
        )
        lab.pack(side="right", padx=25)

        # =========================
        # ZONA PRINCIPAL
        # =========================
        main_area = tk.Frame(self.root, height=300)
        main_area.pack(fill="x", padx=25, pady=10)
        main_area.pack_propagate(False)

        # -------- ENTRADA --------
        input_frame = tk.LabelFrame(
            main_area,
            text="ENTRADA",
            font=("Arial", 16, "bold"),
            width=330,
            height=260
        )
        input_frame.pack(side="left", padx=10)
        input_frame.pack_propagate(False)

        self.input_indicator = tk.Label(
            input_frame,
            text="●",
            font=("Arial", 70),
            fg="gray"
        )
        self.input_indicator.pack(pady=(15, 0))

        tk.Label(
            input_frame,
            text="BOTÓN",
            font=("Arial", 20, "bold")
        ).pack()

        tk.Label(
            input_frame,
            text="GPIO 26",
            font=("Arial", 14)
        ).pack()

        self.input_state = tk.Label(
            input_frame,
            text="LIBERADO",
            font=("Arial", 16, "bold")
        )
        self.input_state.pack(pady=10)

        # -------- FLECHA --------
        tk.Label(
            main_area,
            text="→",
            font=("Arial", 42, "bold")
        ).pack(side="left", padx=5)

        # -------- LÓGICA --------
        logic_frame = tk.LabelFrame(
            main_area,
            text="LÓGICA",
            font=("Arial", 16, "bold"),
            width=330,
            height=260
        )
        logic_frame.pack(side="left", padx=10)
        logic_frame.pack_propagate(False)

        self.logic_state = tk.Label(
            logic_frame,
            text="SI botón = PRESIONADO\n\nENTONCES\n\nbuzzer = ON",
            font=("Arial", 17),
            justify="center"
        )
        self.logic_state.pack(expand=True)

        # -------- FLECHA --------
        tk.Label(
            main_area,
            text="→",
            font=("Arial", 42, "bold")
        ).pack(side="left", padx=5)

        # -------- SALIDA --------
        output_frame = tk.LabelFrame(
            main_area,
            text="SALIDA",
            font=("Arial", 16, "bold"),
            width=330,
            height=260
        )
        output_frame.pack(side="left", padx=10)
        output_frame.pack_propagate(False)

        self.output_indicator = tk.Label(
            output_frame,
            text="●",
            font=("Arial", 70),
            fg="gray"
        )
        self.output_indicator.pack(pady=(15, 0))

        tk.Label(
            output_frame,
            text="BUZZER",
            font=("Arial", 20, "bold")
        ).pack()

        tk.Label(
            output_frame,
            text="GPIO 18",
            font=("Arial", 14)
        ).pack()

        self.output_state = tk.Label(
            output_frame,
            text="APAGADO",
            font=("Arial", 16, "bold")
        )
        self.output_state.pack(pady=10)

        # =========================
        # CONTROLES
        # =========================
        controls = tk.Frame(self.root, height=100)
        controls.pack(fill="x", padx=25)
        controls.pack_propagate(False)

        mode_label = tk.Label(
            controls,
            text="MODO: SIMULACIÓN",
            font=("Arial", 16, "bold")
        )
        mode_label.pack(side="left", padx=20)

        self.sim_button = tk.Button(
            controls,
            text="PRESIONAR BOTÓN",
            font=("Arial", 16, "bold"),
            width=18,
            height=2
        )
        self.sim_button.pack(side="left", padx=30)

        # Eventos para mantener presionado
        self.sim_button.bind("<ButtonPress-1>", self.press_button)
        self.sim_button.bind("<ButtonRelease-1>", self.release_button)

        exit_button = tk.Button(
            controls,
            text="SALIR",
            font=("Arial", 14),
            width=10,
            command=self.root.destroy
        )
        exit_button.pack(side="right", padx=20)

        # =========================
        # BITÁCORA
        # =========================
        log_frame = tk.LabelFrame(
            self.root,
            text="EVENTOS",
            font=("Arial", 14, "bold")
        )
        log_frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(5, 15)
        )

        self.log_text = tk.Text(
            log_frame,
            height=5,
            font=("Courier", 12),
            state="disabled"
        )
        self.log_text.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def press_button(self, event=None):

        if self.button_pressed:
            return

        self.button_pressed = True
        self.buzzer_active = True

        self.input_indicator.config(fg="green")
        self.output_indicator.config(fg="red")

        self.input_state.config(text="PRESIONADO")
        self.output_state.config(text="ACTIVO")

        self.logic_state.config(
            text="botón = PRESIONADO\n\nCONDICIÓN = TRUE\n\nbuzzer = ON"
        )

        self.add_event("Botón presionado")
        self.add_event("Buzzer activado")

    def release_button(self, event=None):

        if not self.button_pressed:
            return

        self.button_pressed = False
        self.buzzer_active = False
        
        self.input_indicator.config(fg="gray")
        self.output_indicator.config(fg="gray")
        
        self.input_state.config(text="LIBERADO")
        self.output_state.config(text="APAGADO")

        self.logic_state.config(
            text="botón = LIBERADO\n\nCONDICIÓN = FALSE\n\nbuzzer = OFF"
        )

        self.add_event("Botón liberado")
        self.add_event("Buzzer apagado")

    def add_event(self, message):

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.log_text.config(state="normal")
        self.log_text.insert(
            "end",
            f"{timestamp}  {message}\n"
        )
        self.log_text.see("end")
        self.log_text.config(state="disabled")


def main():
    root = tk.Tk()
    app = CrowPiLabApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()