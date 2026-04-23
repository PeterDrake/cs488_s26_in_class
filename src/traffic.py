import time

class Light:
    def __init__(self):
        self._color = 'red'

    def advance(self):
        if self._color == 'red':
            self._color = 'green'
        elif self._color == 'green':
            self._color = 'yellow'
        else:
            self._color = 'red'

    def __repr__(self):
        if self._color == 'red':
            return 'red'
        elif self._color == 'green':
            return 'green'
        else:
            return 'yellow'

light = Light()
while True:
    print(light)
    time.sleep(1)
    light.advance()
