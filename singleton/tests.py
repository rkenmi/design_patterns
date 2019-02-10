import unittest

from singleton.Singleton import SingletonObj, CannotInstantiateMoreThanOneException


class SingletonTest(unittest.TestCase):
    def test_singleton_instantiation(self):
        obj1 = SingletonObj(registry={'OS': 'Windows 2020'})

        with self.assertRaises(CannotInstantiateMoreThanOneException):
            obj2 = SingletonObj(registry={'OS': 'Mac OSXtreme'})

        self.assertEqual(SingletonObj.get_instance(), obj1)

    def test_singleton_multithreading(self):
        thread1 = SingletonObj(system={'phone': 'iPhone'}, skip_exception=True)
        thread2 = SingletonObj(system={'phone': 'Android'}, skip_exception=True)

        thread1.start()
        thread2.start()

        # Verify that thread 1 and thread 2 holds a pointer to the same SingletonObj
        self.assertEqual(thread1.get_instance(), thread2.get_instance())



if __name__ == '__main__':
    unittest.main()
