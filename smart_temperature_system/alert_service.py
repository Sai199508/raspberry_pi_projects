class AlertService:

    def __init__(self, sensor):
        self.sensor = sensor

    def check_temperature(self):

        temp = self.sensor.read_temperature()

        if temp > 40:
            return "ALERT"

        return "NORMAL"
