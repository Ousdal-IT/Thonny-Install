# Thonny Install

En enkel, utskriftsvennlig **teskje-guide** fra **Ousdal IT** for å installere Thonny og komme i gang med Python.

## M0.20 — Release Candidate

M0.20 er release candidate for den første publiserbare flyer-versjonen.

### Innhold

- Norsk hovedguide
- Engelsk guide under `/en/`
- Windows 10/11, macOS og Linux
- Trinn-for-trinn-instruksjoner uten krav om tidligere programmeringserfaring
- Egen «Jeg sitter fast» / «I'm stuck»-seksjon
- Første Python-program med `print()`
- A4/print-CSS
- NO- og EN-PDF bygget fra samme HTML-kilde
- GitHub Pages-deploy
- Automatisk HTML-, PDF- og språkparitetskontroll
- Screenshot-manifest med `candidate`, `verified` og `stale`
- Automatisk kobling mellom verifiserte screenshots og riktig steg
- Personvernkrav for screenshots

### Screenshot-status

De ti planlagte screenshots er registrert som `candidate`. **Ingen screenshots er ennå merket `verified`**, og derfor publiseres ingen bilder i guiden.

Dette er med hensikt: guiden skal aldri inneholde konstruerte eller utdaterte OS-/Thonny-bilder.

### Kvalifisering

GitHub Actions må passere hele kjeden:

1. Kildevalidering av norsk og engelsk HTML
2. NO/EN-strukturparitet
3. Screenshot-manifest og anchor-kontroll
4. Generering av GitHub Pages
5. Norsk PDF
6. Engelsk PDF
7. PDF-validering
8. Pages-deploy

### Formater

- Web: GitHub Pages
- PDF: `Thonny-Install-NO.pdf`
- PDF: `Thonny-Install-EN.pdf`

HTML er hovedkilden. PDF bygges fra samme side slik at web og PDF ikke får forskjellig innhold.

## Neste etter M0.20

Første innholdsutvidelse etter RC er å ta de ti screenshots fra rene testmiljøer, registrere eksakt OS-/Thonny-versjon og gjøre personvernkontroll før noen settes til `verified`.

## Eier

**Ousdal IT**

## Lisens

Innhold og kode: se `LICENSE`.
