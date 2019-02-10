"""
The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state,
all of its dependents are notified and updated automatically.
"""


class Publisher:
    # Alternatively known as the 'Subject'

    def __init__(self, subscribers=set()):
        self.subscribers = subscribers

    def add_observer(self, subscriber):
        self.subscribers.add(subscriber)

    def remove_observer(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_all(self):
        raise NotImplementedError


class WeatherForecast(Publisher):
    def __init__(self, subscribers=set(), temperature=0.0, humidity=0.0, pressure=0.0):
        super().__init__(subscribers)
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        # Initial value
        self.changed = True
        self.notify_all()

    def notify_all(self):
        if self.changed:
            for observer in self.subscribers:
                observer.update(self.temperature, self.humidity, self.pressure)

        self.changed = False

    def set_measurements(self, temperature, humidity, pressure):
        if temperature != self.temperature or humidity != self.humidity or pressure != self.pressure:
            self.changed = True

        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.notify_all()


