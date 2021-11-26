import time
import Adafruit_PCA9685

servo_min = 120  # Min pulse length out of 4096
servo_max = 300  # Max pulse length out of 4096
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)


def set_servo_open(channel):
    pwm.set_pwm(channel, 0, servo_max)
    print(channel, "号舵机开启", servo_max)


def set_servo_close(channel):
    time.sleep(1)
    pwm.set_pwm(channel, 0, servo_min)
    print(channel, "号舵机关闭", servo_min)
