from smart_temperature_system.alert_service import AlertService


class FakeSensor:

    def read_temperature(self):
        return 45


def test_high_temperature():
    service = AlertService(FakeSensor())
    assert service.check_temperature() == "ALERT"
