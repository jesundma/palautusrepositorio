Testit olivat hyviä ja laadukkaita, käytössäni oleva CoPilot tarjoaa hyvin innokkaasti testejä kirjoittaessa automaattista täydennystä. Selailin commit- listaa ja uskon tuon automaattitäydennyksen olevan syyllinen siihen, että samaan commit on tullut alun perin 3 kohdassa kaksi testiä kerralla. Testien määrä on 15 erillistä testiä, jotka agentin parannusehdotuksen jälkeen tiivistyivät 12 testiin.

Parannusehdotuksen sisältö oli:

ostoskori.py: Lisäys ja poisto hakevat ostoksen nimellä erikseen. Yhteinen hakumetodi vähentäisi toistoa.

ostoskori.py: Samannimisten mutta erihintaisten tuotteiden käsittely voi jättää korin hinnan virheelliseksi. Hintakäytäntö pitäisi määritellä ja testata.

ostoskori_test.py: Poistotesti voisi tarkistaa myös korin hinnan ja tuotemäärän. Tyhjän korin tarkistukset voisi tarvittaessa koota testien apumetodiin.

Näistä ei toteutettu samannimisten tuotteiden tarkistusta. Lopputuloksena koodi ei lyhentynyt, ostoskori.py kasvoi 5 rivillä ja testit mukaan lukien rivejä tuli yhteensä 33 lisää. Testien luettavuus mielestäni parani. Agentti ei missään vaiheessa yrittänyt huijata millään lailla. Ainoa omituisuus oli, että yhdessä testissä agentti määritteli tuotteen ensin muuttujaksi ja sitten käytti tuota muuttujaa metodissa. Kaikissa aiemmissa tapauksissa ja myös tämän jälkeen oli käytetty tuote- oliota suoraan.

Olen tottunut toimimaan molemmilla tavoilla, kirjoittamaan suoraan koodia tai antamalla agentin tuottaa se kokonaan. Tässä harjoituksessa en törmännyt koodin hajoamiseen, koska testien kautta tehtävä koodaaminen oli selkeää ja kohdistui vain muutamaan tiedostoon. Oman kokemuksen perusteella kovin moneen tiedostoon ulottuva agentin koodaus tuottaa helposti hajoavaa koodia. Hajoavalla koodilla tarkoitan koodia, joka muuttuu ristiriitaiseksi ja epäloogiseksi. Lyhyet ja selkeät määrittelyt (TDD- hengessä) toimivat näköjään hyvin.
