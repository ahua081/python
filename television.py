class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Method to turn the TV on or off
        """
        self.__status = not self.__status

    def mute(self):
        """
        Method to mute or unmute the TV when it's on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Method to increase the TV channel when the TV is on.
        If the TV is on the maximum channel and this method is called,
        it should set the TV channel to the minimum channel.
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
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

    def volume_up(self):
        """
        Method to increase the TV volume when the TV is on.
        If the TV is on the maximum volume and this method is called,
        the volume should just remain at the maximum.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Method to decrease the TV volume when the TV is on.
        If the TV is on the minimum volume and this method is called,
        the volume should just remain at the minimum.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MAX_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Method to show the TV status.
        :return: TV status.
        """
        if self.__status:
            if self.__muted:
                return f'Power = {str(self.status)}, Channel = {str(self.__channel)}, Volume = {Television.MIN_VOLUME} (Muted)'
            else:
                return f'Power = {str(self.__status)}, Channel = {str(str.__channel)}, Volume = {str(self.__volume)}'
        else:
            return f'Power = {str(self.__status)}, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'
