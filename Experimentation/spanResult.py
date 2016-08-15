import math


class SpanResultItem:

    def __init__(self, distance, referenceSent, citingSent):
        if math.isnan(distance):
            distance = 1.
        self.distance = distance
        self.referenceSent = referenceSent
        self.referenceSentIndex = referenceSent.getIndex()
        self.citingSentence = citingSent
        self.citingSentIndex = citingSent.getIndex()

    def __str__(self):
        return str(self.distance) + '\n' + str(self.referenceSentIndex) + ' : ' \
               + str(self.referenceSent) + '\n'
