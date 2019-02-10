import unittest

from observer.Publisher import WeatherForecast
from observer.Subscriber import WeatherForecastViewer


class ObserverTest(unittest.TestCase):
    def test_observer(self):
        weatherman_1 = WeatherForecastViewer()
        tv_viewer = WeatherForecastViewer()
        some_dude = WeatherForecastViewer()

        viewers = {weatherman_1, tv_viewer}

        weather_forecast = WeatherForecast(viewers, 0.0, 1.0, 2.0)

        for viewer in viewers:
            self.assertEquals(viewer.get_measurements(), (0.0, 1.0, 2.0))

        weather_forecast.add_observer(some_dude)
        weather_forecast.set_measurements(-15.0, -10, 50)

        self.assertEquals(some_dude.get_measurements(), (-15.0, -10, 50))
        self.assertEquals(weatherman_1.get_measurements(), (-15.0, -10, 50))
        self.assertEquals(tv_viewer.get_measurements(), (-15.0, -10, 50))

        weather_forecast.remove_observer(some_dude)
        weather_forecast.set_measurements(60, 40, 15)

        self.assertEquals(some_dude.get_measurements(), (-15.0, -10, 50))
        self.assertEquals(weatherman_1.get_measurements(), (60, 40, 15))
        self.assertEquals(tv_viewer.get_measurements(), (60, 40, 15))



if __name__ == '__main__':
    unittest.main()
