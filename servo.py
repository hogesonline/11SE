class Servo:
    '''
    Made by Amanda Hogan 11/06/2024

    Designed for the SG90 hobbyist servo 
    
    Usage:
    instantiate your servo
    use the method set_angle(angle) where the angle is a number between -90 and +90 and zero is the middle
    
    '''
    def __init__(self, pin, freq=50, angle=180):
        self.freq = freq
        self.max_angle = angle
        self.pin = pin
        self.analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(self.analog_period)


    def set_angle(self, angle):
        pulse_length_ms = 1.5 + 0.9 * angle / (self.max_angle//2)
        duty_cycle = pulse_length_ms / self.analog_period
        max_analog = 2**10 - 1
        self.pin.write_analog(round(max_analog * duty_cycle))
