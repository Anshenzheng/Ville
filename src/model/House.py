class House(object):
    def __init__(self):
        self._id = None

    @property
    def get_id(self):
        return self._id
