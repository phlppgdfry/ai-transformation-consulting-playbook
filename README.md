# AI Transformation Consulting Playbook

**Een toepasbaar consultingpakket: discovery, procesanalyse, use-casekeuze, berekende waardecase, governance en adoptie.**

Fictieve klant Noordwerk. Dit is een uitgewerkte oefencase en herbruikbare methode,
geen verslag van echte workshops. Bedragen zijn aannames, geen Microsoft-offerte
of gemeten klantbesparing. De formule en brondata zijn volledig controleerbaar.

## Start

Python 3.11+ en Make, zonder externe packages.

```bash
make verify
python3 playbook.py
python3 playbook.py --output output/business-case.json
```

De berekening toont in het basisscenario 42 uur vrijgemaakte capaciteit per maand,
595 EUR netto gerealiseerde maandwaarde na operationele kosten en een negatief
eerste jaar van -4.860 EUR. De berekende terugverdientijd is 20,17 maanden bij
constant volume en baten vanaf maand één. Tijdens een pilot zijn die baten niet gegarandeerd.

## Leesroute

| Moment | Materiaal | Uitkomst |
|---|---|---|
| Discovery | [Draaiboek](docs/discovery-workshop.md), [voorbeeldbevindingen](docs/case-brief.md) | Eigenaar, knelpunt en baseline |
| Prioriteren | [Scoremodel en businesscase](docs/business-case.md), [CSV](data/use-cases.csv) | Eerst rules-based routering, daarna bronagent |
| Ontwerpen | [Roadmap en RACI](docs/delivery-roadmap.md), [beslislog](docs/decision-log.md) | Scope, afhankelijkheden, stopcriteria |
| Realiseren | [Hub](https://github.com/phlppgdfry/enterprise-ai-automation-hub), [Agent](https://github.com/phlppgdfry/enterprise-ai-agent-governance) | Werkende lokale referentie en Microsoft-bouwgids |
| Adopteren | [Trainings- en meetplan](docs/adoption-and-measurement.md) | Werkafspraken, support en effectmeting |
| Presenteren | [Klantpresentatie: 10 slides](deliverables/client-presentation.md), [Engelse pitch](deliverables/interview-pitch-en.md) | Advies dat risico en financiële uitkomst benoemt |

De presentatie is een bewerkbare Markdown-bron van tien slides, geen PPTX/PDF.
De [invultemplates](templates/discovery-notes.md) en [pilotbeslissing](templates/pilot-review.md)
zijn bedoeld voor toekomstig echt gebruik; ingevulde voorbeelden blijven fictief.

## Afbakening

Geen echte klant, certificering, workshop, Microsoft-deployment of gerealiseerde ROI.
De berekening is operationele scenarioanalyse en geen financieel advies. Het model
veronderstelt constante volumes, geen discontering en geen implementatievertraging.
Licenties, credits, hosting, support en change-kosten moeten met tenantoffertes en
werkelijke metingen worden bevestigd. Zie [Bewijs](EVIDENCE.md) en [MIT](LICENSE).
