"""Ostoskorin testit."""

import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    """Testaa ostoskorin toimintoja."""

    def setUp(self):
        """Luo jokaiselle testille tyhjän ostoskorin."""
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        """Tyhjän ostoskorin hinta ja määrä ovat nollia."""
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        """Yhden tuotteen lisääminen kasvattaa määrää ja hintaa."""
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        """Kaksi eri tuotetta lisätään erillisinä kappaleina."""
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        """Saman tuotteen lisääminen kahdesti kasvattaa määrää kahteen."""
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 6)

    def test_ostokset_sisaltaa_yhden_ostoksen(self):
        """Yksi tuote muodostaa yhden ostoksen."""
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.assertEqual(len(self.kori.ostokset()), 1)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)
        self.assertEqual(ostos.hinta(), 3)

    def test_ostokset_sisaltaa_kaksi_eri_ostosta(self):
        """Eri tuotteet muodostavat kaksi erillistä ostosta."""
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Leipä", 2))
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 1)
        self.assertEqual(ostokset[1].tuotteen_nimi(), "Leipä")
        self.assertEqual(ostokset[1].lukumaara(), 1)
        self.assertEqual(self.kori.hinta(), 5)

    def test_saman_tuotteen_lisaaminen_kahdesti_tuottaa_yhden_ostoksen(self):
        """Saman tuotteen kappaleet yhdistyvät yhdeksi ostokseksi."""
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 2)
        self.assertEqual(ostokset[0].hinta(), 6)

    def test_tuotteen_poistaminen_jattaa_yhden_kappaleen(self):
        """Yhden kappaleen poistaminen jättää toisen ostoskoriin."""
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Maito", 3))

        self.kori.poista_tuote(Tuote("Maito", 3))

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 1)

    def test_viimeisen_tuotteen_poistaminen_tyhjentaa_korin(self):
        """Ainoan tuotteen poistamisen jälkeen kori on tyhjä."""
        self.kori.lisaa_tuote(Tuote("Maito", 3))

        self.kori.poista_tuote(Tuote("Maito", 3))

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_tyhjenna_poistaa_kaikki_ostokset(self):
        """Tyhjentäminen poistaa tuotteet ja nollaa määrän ja hinnan."""
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Leipä", 2))

        self.kori.tyhjenna()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)
