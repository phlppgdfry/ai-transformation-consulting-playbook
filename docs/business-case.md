# Prioritering en waardecase

## Gebruik eerst harde gates

Een ontbrekende menselijke eigenaar, ontbrekende datatoestemming of risicoscore
5 blokkeert de kandidaat. Een hoge businesswaarde kan die gate niet compenseren.
Overige scores lopen van 1 (laag) tot 5 (hoog). Score = 40% waarde + 30%
haalbaarheid + 20% datareadiness + 10% omgekeerd risico (6 − risico).
De gewichten zijn expliciete oefenkeuzes, geen wetenschappelijk gevalideerde schaal.

UC01, vaste routering zonder AI, gaat voor UC02, beleidsvragen met bronnen.
Medische analyse en autonome personeelsbeslissingen zijn in deze case geblokkeerd.
Bij gelijke score kiest de code stabiel op ID; een sponsor mag gemotiveerd anders
prioriteren, maar gates vragen eerst herstel van de blokkade.

## Formule

Bron: `data/business-case.json`. Maandvolume × tijdwinst / 60 × adoptie = uren.
Uren × integraal uurtarief = capaciteitswaarde. Vermenigvuldig die met een
realisatiefactor voor inzetbare economische waarde; trek terugkerende kosten af.
Jaar-1-netto = 12 × netto-maandwaarde − implementatie. ROI jaar 1 = jaar-1-netto /
(implementatie + 12 × maandkosten). Payback = implementatie / netto-maandwaarde
als de netto-maandwaarde positief is; anders is er geen eindige terugverdientijd.

| Aanname | Basisscenario | Te bevestigen met |
|---|---:|---|
| Maandvolume | 600 | Aanvraaglog, seizoenseffect |
| Minuten voor/na | 12 / 5 | Tijdmeting, inclusief uitzonderingen |
| Uurtarief | 45 EUR | Finance, integraal kostentarief |
| Adoptie | 60% | In-scope gebruikers en echte transacties |
| Realisatiefactor | 50% | Herinzet uren en vermeden externe kosten |
| Implementatie | 12.000 EUR | Werkpakket, security, training, reserve |
| Maandkosten | 350 EUR | Tenantofferte: licenties, credits, hosting en beheer |

Deze bedragen zijn scenario-input, geen actuele vendorprijzen. Neem bestaand
licentiebezit, dubbelgetelde baten, beheerwerk en een implementatieramp apart mee.
Vrijgemaakte capaciteit is geen automatische loonkostenbesparing.

## Advies aan de fictieve sponsor

Het basisscenario levert 42 uur per maand capaciteit, 945 EUR gerealiseerde
maandwaarde, 595 EUR na maandkosten en -4.860 EUR netto in jaar één. De payback
van 20,17 maanden veronderstelt baten vanaf maand één. Een ramp-up verlengt die.
Start daarom met een afgebakende pilot met vooraf afgesproken kostenplafond.
Schaal pas op bij gemeten kwaliteit, voldoende gebruik en een geactualiseerde
businesscase. Een negatief scenario is een reden om scope of kosten te veranderen.

`output/business-case.json` bevat tevens gevoeligheid bij 30%, 60% en 90% adoptie.
Het model gebruikt geen discontering, indexatie of statistische onzekerheid.
Maak geen investeringsbesluit uitsluitend op basis van deze oefenberekening.
