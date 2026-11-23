"""Ostoskorin toiminnallisuus."""

from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    """Hallinnoi ostoskorin tuotteita, määriä ja hintaa."""

    def __init__(self):
        """Luo tyhjän ostoskorin."""
        self._maara = 0
        self._hinta = 0
        self._ostokset = []

    def tavaroita_korissa(self):
        """Palauttaa ostoskorissa olevien tuotteiden kappalemäärän."""
        return self._maara

    def hinta(self):
        """Palauttaa ostoskorin kokonaishinnan."""
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        """Lisää tuotteen ostoskoriin."""
        self._maara += 1
        self._hinta += lisattava.hinta()
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        """Poistaa yhden kappaleen annettua tuotetta ostoskorista."""
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi() != poistettava.nimi():
                continue
            ostos.muuta_lukumaaraa(-1)
            self._maara -= 1
            self._hinta -= ostos.tuote.hinta()
            if ostos.lukumaara() == 0:
                self._ostokset.remove(ostos)
            return

    def tyhjenna(self):
        """Tyhjennystoimintoa ei ole vielä toteutettu."""

    def ostokset(self):
        """Palauttaa ostoskorin ostokset."""
        return self._ostokset
