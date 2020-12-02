class Env:
    def getTime(self):
        pass

    def playWavFile(self, file):
        pass

    def wavWasPlayed(self,file):
        pass

    def resetWav(self,file):
        pass


class Checker:
    def __init__(self):
        self.mp3 = Env()

    def remainder(self, file):
        time = self.mp3.getTime()

        if int(time) > 17:
            self.mp3.playWavFile(file)
            return self.mp3.wavWasPlayed()
        else:
            return self.mp3.resetWav()



