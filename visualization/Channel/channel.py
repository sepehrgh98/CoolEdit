from visualization.Channel.channeldata import ChannelData
from visualization.Channel.channelform import ChannelForm


class Channel:
    def __init__(self, _id, _name):
        self._channel = ChannelData(_id, _name)
        self._plot = ChannelForm(_id, _name)
        self._id = _id
        self._name = _name

    @property
    def data(self):
        return self._channel

    @property
    def plot(self):
        return self._plot

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, a):
        if not isinstance(a, int):
            raise ValueError("id must be integer!")
        self._id = a

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a):
        if not isinstance(a, str):
            raise ValueError("name must be integer!")
        self._name = a
