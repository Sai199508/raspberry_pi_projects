class AuthService:

    def __init__(self, valid_pin):
        self.valid_pin = valid_pin

    def authenticate(self, pin):

        if pin == self.valid_pin:
            return True

        return False
    