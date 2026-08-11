from gpiozero import Button, Buzzer


class RealGPIOController:
    def __init__(self, button_gpio, buzzer_gpio):

        self.button = Button(
            button_gpio,
            pull_up=True,
            bounce_time=0.05
        )

        self.buzzer = Buzzer(
            buzzer_gpio
        )

        self.buzzer.off()

    def is_button_pressed(self):
        return self.button.is_pressed

    def buzzer_on(self):
        self.buzzer.on()

    def buzzer_off(self):
        self.buzzer.off()

    def cleanup(self):
        self.buzzer.off()
        self.button.close()
        self.buzzer.close()
        