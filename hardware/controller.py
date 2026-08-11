class HardwareController:
    def __init__(self):
        self.button_pressed = False
        self.buzzer_active = False

    def press_button(self):
        self.button_pressed = True
        self.buzzer_active = True

    def release_button(self):
        self.button_pressed = False
        self.buzzer_active = False

    def is_button_pressed(self):
        return self.button_pressed

    def is_buzzer_active(self):
        return self.buzzer_active