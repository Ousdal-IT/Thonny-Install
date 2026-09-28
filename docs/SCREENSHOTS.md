# Screenshot workflow

M0.4 innfører sporbarhet for skjermbilder.

Et skjermbilde kan publiseres når:

- det matcher steget det dokumenterer
- OS og relevant versjon er registrert
- Thonny-versjon er registrert når relevant
- kilde og opptaksdato er registrert
- bildet er kontrollert for personopplysninger
- alternativ tekst beskriver hva brukeren skal finne
- status i manifestet er `verified`

## Manifest-felter

Hver oppføring skal minst ha:

- `id`
- `file`
- `step`
- `os`
- `os_version`
- `thonny_version`
- `language`
- `captured_at`
- `source`
- `alt`
- `status`

Tillatte statuser: `candidate`, `verified`, `stale`.

## Prinsipp

Teksten er fasit for handlingen. Bildet skal gjøre steget lettere å kjenne igjen, men aldri være eneste måte å forstå instruksjonen på.
