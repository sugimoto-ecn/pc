from gpiozero import Button
from gpiozero import LED
from gpiozero import PWMLED
 
p_button = Button(27, bounce_time=0.05)
n_button = Button(22, bounce_time=0.05)

led_pwm = PWMLED(17)
led_pwm.value = 0.1
 
def increment_pwm():
    global pwm_value

    pwm_value += 0.1
    print('increment')

def decrement_pwm():
    global pwm_value

    pwm_value -= 0.1
    print("decrement")
 
def main_loop():
    global pwm_value , p_button, n_button
    while True:
        p_button.when_pressed = increment_pwm
        n_button.when_pressed = decrement_pwm
 
if __name__ == '__main__':
    main_loop()