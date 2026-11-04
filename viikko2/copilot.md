Virheet ja niiden korjaaminen koodissa CoPilotilla agentti- moodissa
Tein tarkoituksellisen virheen Pylintiä varten helpoimmalla mahdollisella tavalla lisäämällä rivin pituutta kommentilla yli sallitun 100 merkin. En kuitenkaan ollut ajanut Pylintiä ennen tätä muutosta ja kun varmuuden vuoksi päätin commitoida koodin ennen Pylintiä, niin pre-commit hook pysäytti commitin melkoisen Pylint- virhelistan vuoksi. Koodista löytyi useampia .pylintrc määriteltyjä rikkeitä.

Pyysin useammasta virheestä selityksen CoPilotilta ja kaikkien osalta selitys oli paikkansa pitävä. Pyysin virheet jaoteltuina 6 eri kategoriaan virheen mukaisesti ja muodostamaan niistä ratkaisuehdotuksia (proposal). Pyysin suorittamaan kunkin ratkaisuehdotuksen yksittäisenä toimenpiteenä, sillä aiempien kielimallikokemuksien perusteella mallien toteutus helposti hajoaa pidemmissä, monia toimenpiteitä sisältävissä tehtävissä. Muutoksien paloittelu pienempiin osiin todennäköisesti vaikutti siihen, että koodiin ei tehty mitään pyytämättömiä muutoksia. Testasin jokaisen ratkaisuehdotuksen toteuttamisen jälkeen vaikutusta ajamalla Pylintin läpi ja jokaisella kerralla pistetytys nousi (= ratkaisuehdotuksella oli korjattu toivotut virheet). 

Testit
Testejä varten pyysin CoPilotia (agent) luomaan erikseen StubPlayerReader- luokan ja testit TestPlayerStats- luokkaan. Syötteet olivat englanniksi ja pyysin luomaan unit tests. CoPilot loi molemmat luokat (erillisiin tiedostoihin) oikein, mutta todennäköisesti johtuen kontekstista, vain kaksi yksikkötestiä viimeisintä luotua metodia koskien. Pyysin uudella syötteellä tekemään yksikkötestit kolmelle metodeille, jotka löytyvät luokasta PlayerStats. Testejä luotiin 8 kappaletta ja ne testaavat metodien toimivuuden oikein. Virhetapauksien, kuten tuntematon pelaajanimi, osalta testit eivät ole täysin kattavia, osasta metodeista virhetapaustestit puuttuvat. 

CoPilot- käytön hyödyllisyys
Olen aiemmin jo käyttänyt CoPilotia koodin tarkistamiseen ja luomiseen. Ohjelmistotuotanto- kurssi on ensimmäinen kerta, kun olen käyttänyt sitä kurinalaisesti koodin testaamisessa ja testien luomiseen. Testatut metodit olivat suurimmaksi osaksi CoPilotin luomia. Mielenkiintoinen kokeilu olisi ollut test-driven-development- hengessä pyytää ensin luomaan sopivat testit ja sitten metodit, jotka selvittävät testit. Tässä harjoituksessa luokan PlayerStats- metodit olivat sen verran yksinkertaisia, että en usko tällä tavalla toteutettujen metodien poikkeavan suoraan CoPilotin luomista metodeista.

Symlink (symbolic link) ja CoPilot
Palautukseni sisältää kaikki viikkojen 1-6- harjoitukset ja huomasin, että Pylint käytti asetuksien haussa alakansion viikko2/nhl-reader juuresta löytyvää .pylintrc- tiedostoa. CoPilotin mukaan, jos kyseistä tiedostoa ei löydy, tiedostoa etsitään tiedostopuusta. Tämä ei varsinaisesti ole ongelma, mutta halusin, että kaikki harjoitukset käyttäisivät samaa .pylintrc- tiedostoa ja kaikki muutokset yhteen tiedostoon heijastuisivat kaikkiin .pylintrc- tiedostoihin koko tiedostopuussa. Pitkällisen keskustelun jälkeen CoPilot tarjosi ratkaisuksi symbolisten linkkien luomista, joka oli minulle uusi asia. Keskustelun pituuteen saattoi vaikuttaa se, että syötteet olivat mallille monitulkintaisia ja siksi tarvittiin useampi iteraatio tavoitteen saavuttamiseksi.

Halusin myös varmistaa, että miten linkit käyttäytyvät, jos reposta otetaan klooni sekä miten, linkit käyttäyvät linux- tai windows- käyttöjärjestelmässä paikallisella koneella.

Pyysin CoPilotin jälkikäteen selittämään, miten symbolinen linkki on luotu:
- komento on annettu silmukassa, joka käy läpi kaikki harjoituskansiot: ln -s ../../.pylintrc "$dir/.pylintrc"

- ln creates a link.
- s says to create a symbolic link.
- ../../.pylintrc is the link’s target. It means “go up two directories, then use .pylintrc.”
- "$dir/.pylintrc" is where the link is created: .pylintrc. The quotes keep the expanded path together as one argument.

The target is interpreted relative to the link’s location, not the shell’s current directory. From int-joukko, ../../.pylintrc leads to the repository-root .pylintrc. So Pylint opening the nested path reads the root config through the link.
If that destination already exists, ln reports an error instead of replacing it. You can inspect a link with ls -l viikko5/int-joukko/.pylintrc or see just its target with readlink viikko5/int-joukko/.pylintrc.