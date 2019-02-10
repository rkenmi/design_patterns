from threading import Lock, Thread


class SingletonObj(Thread):
    """
    The Singleton Pattern ensures a class has only one instance, and provides a global point of access to it.
    """
    instance = None

    def __init__(self, *args, **kwargs):
        if SingletonObj.instance and not kwargs.get('skip_exception'):
            raise CannotInstantiateMoreThanOneException

        super().__init__()
        self.data = kwargs
        SingletonObj.instance = self

    @staticmethod
    def get_instance():
        lock = Lock()
        with lock:
            return SingletonObj.instance

    def get_data(self):
        return self.data

class CannotInstantiateMoreThanOneException(Exception):
    def __init__(self):
        super().__init__()
