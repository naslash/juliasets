class JuliaSet(object):

    def set_plane(self, _d):
        self._d=_d
        self._complexplane=[]
        x=-2
        y=-2
        while x<=2:
            while y<=2:
                self._complexplane.append(complex(x,y))
                y+=_d
            x+=_d
            y=-2
        return self._complexplane

    def __init__(self, c, n=100):
        self.c = c
        self.n = n
        self._d=0.001
        self._complexplane=[]#self.set_plane(self._d)

    def juliamap(self, z):
        return ((z**2)+self.c)

    def iterate(self, z):
        m = 0
        while True:
            m+=1
            z=self.juliamap(z)
            if abs(z)>2:
                return m
            elif m>=self.n:
                return 0

    def set_spacing(self, d):
        self._d = d
        self._complexplane=self.set_plane(self._d)

    def generate(self):
        self.set = [self.iterate(z) for z in self._complexplane]
        return self.set
