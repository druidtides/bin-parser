from bin_parser import BinReadFunctions, BinWriteFunctions


class PrinceReadFunctions(BinReadFunctions):
    def min(self, data):
        return super(PrinceReadFunctions, self).int(data) - 1

    def sec(self, data):
        return super(PrinceReadFunctions, self).int(data) // 12


class PrinceWriteFunctions(BinWriteFunctions):
    def min(self, minutes):
        return super(PrinceWriteFunctions, self).int(minutes + 1)

    def sec(self, seconds):
        return super(PrinceWriteFunctions, self).int(seconds * 12)
