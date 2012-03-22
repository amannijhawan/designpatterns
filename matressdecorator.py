#Implementing the decorator pattern for a class of matresses
_basecost = 10



class Mattress(object):
    def __init__(self):
        test = 1
        print test

    def price(self):
        return  _basecost


class SpringMattress(object):
    _mulfactor = 1.5
    def __init__(self, decorated_mattress):
        self._decorated_mattress = decorated_mattress


    def price(self):
        return self._mulfactor * self._decorated_mattress.price()


class LatexFoamMattress(SpringMattress):
    _mulfactor = 2.0


class MemoryFoamMattress(SpringMattress):
    _mulfactor = 4.0

class TwinMattress(SpringMattress):
    _mulfactor = 1.0

class FullMattress(SpringMattress):
    _mulfactor = 1.5

class QueenMattress(SpringMattress):
    _mulfactor = 2.0

class KingMattress(SpringMattress):
    _mulfactor = 4.0

def main():
    print SpringMattress(QueenMattress(Mattress())).price()


if __name__ == '__main__':
    main()


