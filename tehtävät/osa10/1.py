class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin_kerros or kerros > self.ylin_kerros:
            print("Virheellinen kerros!")
            return
        while self.nykyinen_kerros != kerros:
            if self.nykyinen_kerros < kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print("Hissi on nyt kerroksessa:", self.nykyinen_kerros)

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print("Hissi on nyt kerroksessa:", self.nykyinen_kerros)


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumäärä):
        self.hissit = [Hissi(alin_kerros, ylin_kerros)
                       for _ in range(hissien_lukumäärä)]

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        if hissi_numero < 1 or hissi_numero > len(self.hissit):
            print("Virheellinen hissin numero!")
            return
        self.hissit[hissi_numero - 1].siirry_kerrokseen(kohde_kerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin_kerros)


h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)

t = Talo(1, 10, 5)
