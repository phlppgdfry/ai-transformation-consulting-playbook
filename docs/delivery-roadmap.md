# Roadmap, verantwoordelijkheden en overdracht

Zes weken is een planningshypothese, geen leverbelofte. Tenanttoegang en beschikbare
reviewers zijn randvoorwaarden. De lokale repos kunnen onafhankelijk worden getest.

| Week | Werk | Verantwoordelijk | Acceptatie / afhankelijkheid |
|---|---|---|---|
| 1 | Discovery, baseline, bronnen en licenties | Consultant + proceseigenaar | Probleem/scope bevestigd, datarechten bekend |
| 2 | Proces en API, tenantontwerp | Technisch consultant + IT | Rollen en retries getest, Dev aangewezen |
| 3 | Power Apps/flows en connector | Maker + IT | Echte identiteiten, geen dubbele acties |
| 4 | Copilot-agent en evaluatie | AI-consultant + bronowners | Verboden acties geblokkeerd, bronnen correct |
| 5 | Pilot en training | Change & Adoption + teamlead | Meetplan actief, support geoefend |
| 6 | Herberekening, go/no-go, overdracht | Sponsor + IT + Finance | Getekende beslissing; stop is geldige uitkomst |

## RACI

| Deliverable | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Use-casekeuze | Consultant | Sponsor | Medewerkers/Finance/IT | Change & Adoption |
| Procesregels | Procesanalist | Operations-owner | Finance/IT | Medewerkers |
| Security/release | Platformbeheerder | IT-owner | Privacy/consultant | Sponsor |
| Kennisbron | Beleidsbeheerder | Finance-/IT-owner | HR/consultant | Gebruikers |
| Training | Change & Adoption | Teamlead | Consultant | Sponsor |
| Pilotbesluit | Consultant | Sponsor | IT/Finance/gebruiker | Alle deelnemers |

## Overdracht aan technische collega

Lever API-contract, state machine, rolmatrix, geprioriteerde requirements,
acceptatietests en foutpaden. FR01–FR05 staan in de Hub. Laat de technische collega
de system-of-record-keuze bevestigen; voorkom een flow die zowel API als Dataverse
onafhankelijk bijwerkt. Geef per issue reproduceerstappen en correlation ID.

## Beheeracceptatie

Owner en vervanger bekend; geen afhankelijkheid van een vertrekkende maker;
monitoring en herstelprocedure getest; licenties bevestigd; solution en configuratie
gescheiden; medewerkers weten waar ze hulp vinden; open risico's expliciet geaccepteerd.
Securityrollen, DLP en bronrechten vragen tenantbewijs. Geen checklist afvinken
omdat een ontwerpdocument bestaat.
