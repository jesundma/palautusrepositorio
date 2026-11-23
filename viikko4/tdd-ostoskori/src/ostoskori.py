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

    def _etsi_ostos(self, tuote: Tuote):
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi() == tuote.nimi():
                return ostos
        return None

    def lisaa_tuote(self, lisattava: Tuote):
        """Lisää tuotteen ostoskoriin."""
        self._maara += 1
        self._hinta += lisattava.hinta()
        ostos = self._etsi_ostos(lisattava)
        if ostos is None:
            self._ostokset.append(Ostos(lisattava))
        else:
            ostos.muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        """Poistaa yhden kappaleen annettua tuotetta ostoskorista."""
        ostos = self._etsi_ostos(poistettava)
        if ostos is None:
            return
        ostos.muuta_lukumaaraa(-1)
        self._maara -= 1
        self._hinta -= ostos.tuote.hinta()
        if ostos.lukumaara() == 0:
            self._ostokset.remove(ostos)

    def tyhjenna(self):
        """Poistaa kaikki ostokset ja nollaa määrän ja hinnan."""
        self._ostokset.clear()
        self._maara = 0
        self._hinta = 0

    def ostokset(self):
        """Palauttaa ostoskorin ostokset."""
        return self._ostokset
