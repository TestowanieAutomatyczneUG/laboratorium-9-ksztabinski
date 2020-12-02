class Env:
    def getTime(self):
        pass

    def playWavFile(self, file):
        pass

    def wavWasPlayed(self):
        pass

    def resetWav(self):
        pass


class Checker:
    def __init__(self):
        self.mp3 = Env()

    def remainder(self, file):
        time = self.mp3.getTime()

        if int(time) > 17:
            self.mp3.playWavFile(file)
            self.mp3.wavWasPlayed()
        else:
            self.mp3.resetWav()



