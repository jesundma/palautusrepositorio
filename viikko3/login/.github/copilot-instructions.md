# Projektiohjeet

## Arkkitehtuuri

- Tämä on `uv`-projekti. Suorita projektin komennot sen hakemistosta käyttäen `uv run` -komentoa. Riippuvuudet ja työkalujen versiot määritellään tiedostoissa `pyproject.toml` ja `uv.lock`.
- Reitit ja pyyntöjen käsittely ovat tiedostossa `src/app.py`. Pidä liiketoimintasäännöt hakemistossa `src/services/`, käyttäjätietojen käsittely hakemistossa `src/repositories/` ja käyttäjän toimialueen tiedot hakemistossa `src/entities/`.
- HTML-sivut renderöidään Jinja-malleista hakemistossa `src/templates/`.
- Hyväksymistestit ovat Robot Framework -testikokonaisuuksia hakemistossa `src/tests/`. `src/AppLibrary.py` sisältää testikokonaisuuksien käyttämän Python-kirjaston. Käytä sen nykyistä integraatiota sen sijaan, että toteuttaisit selaimen tai sovelluksen alustuksen uudelleen.
- Käyttäjätiedot tallennetaan muistiin perustuvaan tietovarastoon. Säilytä tämä toimintatapa, kun muutat sovelluksen tai testien työnkulkuja.

## Sovelluksen käynnistys

Käynnistä Flask-sovellus projektin hakemistosta:

```bash
uv run python src/index.py
```

Sovellus kuuntelee porttia `5001` (osoitteessa `http://localhost:5001`). Pidä sovellus käynnissä erillisessä terminaalissa testien suorittamisen ajan.

## Testit

Synkronoi ensin riippuvuudet tarvittaessa komennolla `uv sync`. Käynnissä olevan sovelluksen kanssa suorita kaikki Robot Framework -testit projektin hakemistosta:

```bash
uv run robot src/tests
```

Yksittäisen Robot-testin suorittamista varten etsi ensin testin ratkaistu pitkä nimi ja valitse testi tällä nimellä. Älä anna komennolle yksittäisen `.robot`-tiedoston polkua, sillä tällöin ylemmän tason testikokonaisuuden alustus voi jäädä suorittamatta:

```bash
uv run robotcode discover tests
uv run robotcode robot -bl "<long-name-from-discovery>"
```

## Käyttäjätietojen validointi

- Rekisteröinnin validointi tapahtuu `UserService.validate`-metodissa tiedostossa `src/services/user_service.py`. Se tarkistaa pakolliset kentät, käyttäjänimen vähimmäispituuden ja yksilöllisyyden, salasanan vähimmäispituuden sekä salasanojen täsmäämisen.
- Kirjautumistietojen tarkistus tapahtuu saman luokan `UserService.check_credentials`-metodissa. Se tarkistaa, että käyttäjänimi ja salasana on annettu ja että ne vastaavat tietovarastossa olevaa käyttäjää.
- `src/app.py`-tiedoston reitit kutsuvat näitä palvelumetodeja. Pidä validointi palvelukerroksessa reittien sijaan.

## Linttaus

Repositorion esivalmistelukoukku suorittaa Pylintin käyttäen juurihakemiston `.pylintrc`-asetustiedostoa. Linttaa tämän projektin Python-lähdekoodi suoraan komennolla:

```bash
uv run --with pylint pylint --rcfile=../../.pylintrc src/
```

## Käytännöt

- Pidä reittien käsittelijät suppeina ja delegoi tilien validointi sekä kirjautumistietojen tarkistaminen `UserService`-luokalle.
- Käytä käyttäjien hakuun ja muokkaamiseen tietovarastoabstraktiota. Älä käsittele sen sisäistä listaa suoraan reiteistä tai malleista.
- Robot-testit jakavat resursseja tiedoston `src/tests/resource.robot` kautta. Noudata sitä ja nykyistä testikokonaisuuksien alustusta, kun lisäät tai muokkaat testitapauksia.
