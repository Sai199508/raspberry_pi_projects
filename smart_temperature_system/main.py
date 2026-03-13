from sensor import TemperatureSensor
from alert_service import AlertService

sensor = TemperatureSensor()
service = AlertService(sensor)

status = service.check_temperature()

print("Temperature Status:", status)
