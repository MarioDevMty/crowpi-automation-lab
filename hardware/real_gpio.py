try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None


class RealGPIOController:
    def __init__(self, button_gpio, buzzer_gpio):

        if GPIO is None:
            raise RuntimeError(
                "RPi.GPIO no está disponible. "
                "Este controlador debe ejecutarse en Raspberry Pi."
            )

        self.button_gpio = button_gpio
        self.buzzer_gpio = buzzer_gpio

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(
            self.button_gpio,
            GPIO.IN,
            pull_up_down=GPIO.PUD_UP
        )

        GPIO.setup(
            self.buzzer_gpio,
            GPIO.OUT
        )

        GPIO.output(
            self.buzzer_gpio,
            GPIO.LOW
        )

    def is_button_pressed(self):
        return GPIO.input(self.button_gpio) == GPIO.LOW

    def buzzer_on(self):
        GPIO.output(
            self.buzzer_gpio,
            GPIO.HIGH
        )

    def buzzer_off(self):
        GPIO.output(
            self.buzzer_gpio,
            GPIO.LOW
        )

    def cleanup(self):
        GPIO.output(
            self.buzzer_gpio,
            GPIO.LOW
        )

        GPIO.cleanup()