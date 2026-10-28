# Adoptie, training en effectmeting

## Pilotopzet

Vijf medewerkers en één Operations-goedkeurder; Finance en IT als support. Meet
twee weken baseline en twee weken pilot met dezelfde aanvraagdefinitie. Vergelijk
per categorie en complexiteit, niet alleen het gemiddelde. Kleine aantallen geven
geen bewijs van causaal effect: toon aantallen, spreiding en context.

## Training van 45 minuten

5 min doel en grenzen; 10 min voordoen (beleidsvraag, bron openen, aanvraag
bevestigen); 15 min oefenen met drie veilige voorbeeldtaken; 10 min fouten en
privacy (onbekend antwoord, dossier weigeren, dubbele klik); 5 min supportkanaal
en feedback. Een deelnemer moet zelfstandig één aanvraag indienen, de status
vinden en uitleggen dat alleen een mens goedkeurt.

## KPI-definities

| KPI | Definitie | Databron | Owner | Voorgestelde pilotgate |
|---|---|---|---|---|
| Actieve behandeltijd | Minuten menselijk werk per afgeronde aanvraag | Tijdsteekproef | Operations | Mediaan minstens 20% lager, uitzonderingen apart |
| Doorlooptijd | SubmittedAt tot beslissing, incl. wachten | Eventlog | Operations | Geen verslechtering p90 |
| Correct bronantwoord | Correct antwoord én juiste bron / beoordeelde kennisvragen | Geblindeerde review | Finance/IT | Minstens 90% op echte evalset |
| Ongeautoriseerde actie | Actie/antwoord buiten persona-rechten | Securitytest + incidenten | IT | Nul; één bevestigd incident stopt de pilot |
| Adoptie | Afgeronde via nieuw proces / alle in-scope aanvragen | Proceslog, geen paginaweergaven | Change & Adoption | Doelwaarde 60%, redenen niet-gebruik bespreken |
| Herstelwerk | Aanvragen met correctie / alle afgeronde aanvragen | Steekproef | Teamlead | Niet hoger dan baseline |
| Kosten | Werkelijke licenties/credits/hosting/support | Facturen en tijdlog | Finance | Binnen vooraf bevestigd plafond |

Gates zijn voorstellen, geen behaalde resultaten. Maak denominator, tijdzone,
weekenden, incompleet werk en uitschieters vooraf expliciet. Sla geen volledige
gesprekken op om gebruik te meten; gebruik pseudonieme event-ID's waar passend.

## Feedback en change

Sponsor communiceert doel en eigenaars. Teamlead plant oefentijd. Een champion
verzamelt onduidelijke antwoorden. Bespreek feedback wekelijks en publiceer alleen
gecontroleerde beleidswijzigingen. Als medewerkers het systeem overslaan, onderzoek
formulierlast, vertrouwen en rolproblemen voordat je extra training voorschrijft.

## Besluit na pilot

Herbereken volume, behandeltijd, adoptie, realisatiefactor en maandkosten.
Gebruik `templates/pilot-review.md`. Opschalen vereist goedgekeurde securitygate,
voldoende kwaliteit en een geaccepteerde waardecase. Bij onvoldoende waarde:
versimpel de scope, houd alleen routering of stop. Leg eigenaar en datum vast.
