from gpiozero import Button, Buzzer
from time import sleep

BUTTON_GPIO = 26
BUZZER_GPIO = 18

button = Button(
    BUTTON_GPIO,
    pull_up=True,
    bounce_time=0.05
)

buzzer = Buzzer(BUZZER_GPIO)

print("Prueba CrowPi")
print("Presiona el botón físico.")
print("Ctrl+C para terminar.")

try:
    while True:

        if button.is_pressed:
            print("BOTÓN PRESIONADO")
            buzzer.on()

        else:
            buzzer.off()

        sleep(0.05)

except KeyboardInterrupt:
    print("\nFinalizando prueba...")

finally:
    buzzer.off()
    button.close()
    buzzer.close()