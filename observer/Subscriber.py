"""
The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.
"""


class Subscriber:
    # Alternatively known as the 'Observer'
    def update(self, *args):
        raise NotImplementedError


class WeatherForecastViewer(Subscriber):
    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure

    def get_temp(self):
        return self.temp

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    def get_measurements(self):
        return self.temp, self.humidity, self.pressure

    def announce_to_people(self):
        print('Hey yall, did ya know that the temperature is going to be roughly ' + \
              self.temp + ' today with a humidity of ' + self.humidity + ' and pressure of ' + self.pressure + ' ?')