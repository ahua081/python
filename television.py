class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initialize a Television object with default values.

        Instance Variables:
        __status (bool): Power status (True if on, False if off).
        __muted (bool): Whether the TV is muted.
        __volume (int): Current volume level.
        __channel (int): Current channel.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to turn the TV on or off
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to mute or unmute the TV when it's on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method to increase the TV channel when the TV is on.
        If the TV is on the maximum channel and this method is called,
        it should set the TV channel to the minimum channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the TV channel when the TV is on.
        If the TV is on the minimum channel and this method is called,
        it should set the TV channel to the maximum channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the TV volume when the TV is on.
        If the TV is on the maximum volume and this method is called,
        the volume should just remain at the maximum.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MIN_VOLUME

    def volume_down(self) -> None:
        """
        Method to decrease the TV volume when the TV is on.
        If the TV is on the minimum volume and this method is called,
        the volume should just remain at the minimum.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MAX_VOLUME

    def __str__(self) -> str:
        """
        Method to show the TV status.
        Return the TV status as a string.
        :return: TV status.
        """
        if self.__muted:
            return f'Power = {(self.__status)}, Channel = {(self.__channel)}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {(self.__status)}, Channel = {(self.__channel)}, Volume = {(self.__volume)}'
