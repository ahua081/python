import pytest
from television import *

class Test:
    def setup_method(self) -> None:
        self.tv1 = Television()

    def teardown_method(self) -> None:
        del self.tv1

    def test_init(self) -> None:
        """
        Test the initialization of Television object.
        """
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self) -> None:
        """
        Test the power on/off functionality
        """
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self) -> None:
        """
        Test the mute/unmute functionality.
        """
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

    def test_channel_up(self) -> None:
        """
        Test the channel increase functionality.
        """
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 1, Volume = 1'

    def test_channel_down(self) -> None:
        """
        Test the channel decrease functionality.
        """
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_volume_up(self) -> None:
        """
        Test the volume increase functionality.
        """
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.mute()
        self.tv1.volume_up()
        assert "Muted" not in self.tv1.__str__()

        for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME):
            self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self) -> None:
        """
        Test the volume decrease functionality.
        """
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.mute()
        self.tv1.volume_down()
        assert "Muted" not in self.tv1.__str__()

        for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME):
            self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
