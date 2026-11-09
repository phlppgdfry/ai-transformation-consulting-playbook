# Enterprise AI portfolio — herstel en finalisering

Datum: 9 november 2026. Dit is de auditmomentopname na de drie herstelmerges en vóór publicatie van dit rapport en de PDF-correctie. De exacte laatste auditcommit en CI-status staan bij [Playbook PR #3](https://github.com/phlppgdfry/ai-transformation-consulting-playbook/pull/3). Historische rapporten behouden hun oorspronkelijke datum; onderstaande controles zijn opnieuw uitgevoerd.

## Resultaat

De waardevolle lokale reviewcommits zijn teruggevonden, gecontroleerd en via PR #2 in elk van de drie publieke repositories gemergd. De bestaande implementaties zijn behouden. De websiteproposal is op de nieuwere websitebasis gebracht en heeft een afzonderlijke draft-PR. Productie is ongewijzigd. Career-materiaal blijft nadrukkelijk een owner-reviewdraft.

De **Automation Hub is het sterkste flagship**: een zichtbaar bedrijfsproces met werkende software en menselijke beslissingen. Gebruik het Playbook als zakelijke ingang en Governance als bewijs van begrenzing en kritische evaluatie. Samen tonen ze Business–IT Analysis, AI Automation, Digital Transformation en AI Implementation op portfolio-/prototype-niveau.

## Repositorystatus

Alle onderstaande remotes zijn geverifieerd onder `https://github.com/phlppgdfry/`. Alle kernwerkdirectories waren bij aanvang schoon. Er waren geen tags of GitHub Releases; het bestaande v1.0-label in documentatie is geen formele release. Geen nieuwe release of applicatiehosting is aangemaakt.

| Repository / lokale directory onder `/Users/philippegodfroy/` | Main na herstelmerge | Herstelbranch en geteste commit | PR / merge | Deployment |
|---|---|---|---|---|
| `enterprise-ai-automation-hub` | `fff7e56a1fa31c9314f7c3b82f67ece722c76624` | `showcase/recruiter-evidence` · `3d5fdb1a50a36da0dd4ea478f76ffdb1b2873a75` | [#2](https://github.com/phlppgdfry/enterprise-ai-automation-hub/pull/2), gemergd | Publieke bron/bewijs; geen gehoste Noordwerk-app |
| `enterprise-ai-agent-governance` | `de6dbe6bde79415722fbe134b000d9f67ed65616` | `showcase/recruiter-evidence` · `69f2d407d99187088a869557cbbce01236f87a06` | [#2](https://github.com/phlppgdfry/enterprise-ai-agent-governance/pull/2), gemergd | Publieke bron/bewijs; geen inference-service |
| `ai-transformation-consulting-playbook` | `7e96b6d34fa0af27a915fb5bc818565c2dd2c8be` | `showcase/recruiter-evidence` · `3c5d52c322d6b0ed224ec7227970414b4b95b9bf` | [#2](https://github.com/phlppgdfry/ai-transformation-consulting-playbook/pull/2), gemergd; [#3](https://github.com/phlppgdfry/ai-transformation-consulting-playbook/pull/3) bevat deze afsluitende audit/PDF-correctie | Publieke documentatie/PDF; geen nieuwe dienst |

`main` hierboven is de exacte geobserveerde snapshot vóór de laatste audit-PR. De live PR vermeldt de eventuele latere merge-SHA; dit rapport claimt geen eigen toekomstige commit-hash.

| Project | Opnieuw uitgevoerde verificatie | Security | Post-merge CI |
|---|---|---|---|
| Hub | `make verify`: Release build zonder waarschuwingen/fouten, 16 HTTP/storagetests, API-contract, BPMN en documentlinks; echte Chromium workflow op 1512×1050 en 390×844 | Gitleaks alle refs: schoon; npm audit: 0; .NET kwetsbare directe/transitieve packages: geen gevonden | [Verify geslaagd](https://github.com/phlppgdfry/enterprise-ai-automation-hub/actions/runs/42615680548) |
| Governance | `make verify`: 27 tests, 30/30 deterministische cases, consistentie modelrapporten; echte lokale HTTP-integratie met Hub opnieuw uitgevoerd | Gitleaks alle refs: schoon; standaardpad gebruikt Python-standaardbibliotheek; modelpad blijft experimenteel | [Verify](https://github.com/phlppgdfry/enterprise-ai-agent-governance/actions/runs/42615681126) en [integratie](https://github.com/phlppgdfry/enterprise-ai-agent-governance/actions/runs/42615681139) geslaagd |
| Playbook | `make verify`: 17 financiële/scenariotests, outputreproductie en document/releasechecks; bestaande tien PDF-pagina's gerenderd en bekeken | Gitleaks alle refs: schoon; runtime zonder externe Python-dependencies; ReportLab alleen voor PDF-bouw | [Verify geslaagd](https://github.com/phlppgdfry/ai-transformation-consulting-playbook/actions/runs/42615898667); afsluitende wijziging krijgt eigen PR-check |

## Herstel en behoud

| Historische referentie | Bevinding en afhandeling |
|---|---|
| Hub `3d5fdb1` | Bestond als lokale HEAD, één commit boven remote main `a2c00b9`; recruiterroute en AI-assistentiedisclosure hersteld zonder duplicaatcommit |
| Governance `69f2d40` | Bestond als lokale HEAD, twee commits boven `4496767`; CLI-captures, bronoutputs en eerlijke holdoutgrafiek behouden |
| Playbook `bceaedc` | Bestond als lokale HEAD, twee commits boven `cf27ae7`; verhaal, architectuur, screenshots en acht career-documenten hersteld; aanvullende expliciete draftlabels toegevoegd in `3c5d52c` |
| Website `3a762d9` | Bestond in worktree `noordwerk-website-review`, branch `showcase/noordwerk-portfolio`; oud lockfile niet over nieuw main heen gezet. Main `9d4bc72` is met behoud van historie geïntegreerd in `566b0c3` |

De eerdere stabiele mainreferenties waren bij de eerste fetch nog actueel voor de drie kernrepos. Lokale oude `main`-branches liepen achter; ze zijn niet gereset. `portfolio/noordwerk-showcase`-branches en alle historische commits blijven bestaan. De herstelbranches bevatten inmiddels publieke main-voorouders. Geen force-push, branchverwijdering of stash/reset gebruikt.

De website hoort bij **`phlppgdfry/pgosprive`**, niet bij een kernrepository. Hoofdcheckout: `/Users/philippegodfroy/pgosprive`. De extra worktrees `/private/tmp/enterprise-ai-career-website` en `/private/tmp/career-production-final` zijn schoon en ongemoeid. Andere carrière-/releasebranches zijn al door nieuwere remote historie vertegenwoordigd; alleen de Noordwerkproposal was de relevante ongepubliceerde websitecommit. Er is geen duplicaatrecoverybranch gemaakt.

## Wat bestond al en wat is nieuw afgerond

Al aanwezig en opnieuw geverifieerd: aanvraag/goedkeuringsapp, idempotency, eigenaarschap, version conflicts, atomische JSON-opslag, deterministische beleidsreferentie, bevestigde HTTP-tool, bevroren echte modelevaluaties, financiële modellen, BPMN en executive PDF. De herstelcommits verbeterden vooral presentatie en navigeerbaarheid; ze worden niet als nieuw gebouwde bedrijfsintegratie voorgesteld.

Nieuw in deze uitvoering: herstelpublicatie met PR/CI, expliciete owner-reviewlabels op alle career-documenten, integratie van huidige website-main zonder overschrijven van nieuwere inhoud, geteste Router-securityupdate, volledige lokale websitechecks en afzonderlijke draft-PR, actuele bewijsbundel en dit rapport. De PDF-review vond een oudere vijfstappenslide tegenover de actuele zeven fasen: slide 9 en de builder zijn gericht gecorrigeerd; de bronroadmap en financiële uitkomsten zijn ongewijzigd. De nieuwe slide is opnieuw gerenderd en visueel gecontroleerd. De PDF blijft ongetagd voor volledige toegankelijkheid.

## Website: security, werking en publicatiegrens

| Onderdeel | Gecontroleerde status |
|---|---|
| Exacte repository / branch | `phlppgdfry/pgosprive` · `showcase/noordwerk-portfolio` |
| Reviewcommit / PR | `566b0c3f9007b757eed6fcd9f2c85ffa50a4851d` · [draft-PR #3](https://github.com/phlppgdfry/pgosprive/pull/3); niet gemergd |
| Bestaande main/productie | `9d4bc72f8c8b77ea2b7a333ac78e2ebaa0c2b346`; [publieke website](https://www.philippegodfroy.com); bestaande deployment `pgosprive-10yk0dkz6-kippiegs-projects.vercel.app` |
| Reviewpreview | `pgosprive-80wrkbc90-kippiegs-projects.vercel.app`; GitHub deploymentstatus success. Geen wijziging van toegangsbeveiliging; directe browserreview van beschermde hosted preview niet geclaimd |
| Hosted checks | [Build en projectlinks geslaagd](https://github.com/phlppgdfry/pgosprive/actions/runs/42615984788); bestaande Vercel-integratie bouwde uitsluitend een preview |
| Lokaal | Schone npm-installatie; typecheck, 31 tests en productiebuild geslaagd; lint 0 errors / 8 bestaande Fast Refresh-waarschuwingen |
| Browser | Lokale productiepreview op `127.0.0.1:4188`; Chromium EN/NL, breedtes 375/768/1024/1440; vier afbeeldingen, zeven bewijslinks, mobiele menuanker, catalogus→case→terug, EN→NL→EN met query/ankerbehoud, toetsenbordfocus en geen pagina-overflow geslaagd |
| Console en metadata | Geen runtime-exceptions of frameworkoverlay; enige resourcefout: lokale `/_vercel/insights/script.js` 404, geleverd door hosting. Titels, taal en canonical gecontroleerd. Bestaande publieke EN/NL-homepages HTTP 200 |
| Toegankelijkheid | axe WCAG 2 A/AA en 2.1 AA op de gewijzigde sectie: 0 overtredingen in acht taal/viewportcombinaties; geen volledige site- of screenreader-certificering |
| Resterende publicatiegrens | Technisch reviewbaar en zonder kritieke/hoge dependencybevindingen. Productie vereist expliciete eigenaarstoestemming; PR blijft draft omdat main automatisch deployt |

De oude lockfile reproduceerde exact **26 packagebevindingen: 2 critical, 17 high, 7 moderate**. De nieuwere main had al **0 critical, 0 high, 2 moderate**. De uiteindelijke candidate heeft **0 op alle niveaus**. Zie [gespecificeerde auditresultaten](docs/portfolio/assets/finalization/website-audit-summary.json) voor alle packagenamen, direct/transitief, severity, kwetsbare ranges en beschikbare fixes.

De twee oude critical packages waren directe devdependency `vitest` en transitieve `tinypool`: test/toolingrisico, geen reden om het oude pakket veilig te noemen. Bestaande main-updates naar Vitest 4.1.12, Vite 6.4.5, compatibele patches en scoped overrides zijn behouden; ongebruikt Zod was daar al verwijderd. Er is geen `npm audit fix --force` uitgevoerd.

De resterende Router-bevindingen betroffen directe `react-router-dom` en transitieve `react-router`: open redirects met onbetrouwbare backslashbestemmingen en SSR-errorhydratie. De app gebruikt statische routes en BrowserRouter, geen router-SSR, waardoor bekende bereikbaarheid beperkt was. Toch zijn beide upstream findings opgelost door een **gecontroleerde update naar 7.18.5**. Context7-migratiedocumentatie bevestigt Node ≥20 / React ≥18 en behouden DOM-reexports; lokaal draait Node 24 / React 18. Absolute routes, catalogusnavigatie, taalprefixen en geschiedenis zijn getest. Geen React- of Vite-majorupgrade in deze uitvoering. Breaking changes rond relatieve splatroutes en data-loaders zijn beoordeeld; die patronen gebruikt de site niet.

Gitleaks op alle websitegeschiedenis vindt één eerder gecommitteerde `.env`-JWT in `f48ec652`. Veilig geclassificeerd als Supabase **anon**, geen service-role; de waarde is niet getoond of gekopieerd. Actuele bron volgt alleen `.env.example` en gebruikt geen Supabase-client/key. De nieuwe reviewcommits scannen schoon. Externe RLS/anonrechten zijn niet beoordeeld; dit is dus geen verklaring dat het historische databaseproject veilig is. Geen database benaderd of gewijzigd en geen historie herschreven. Een eigenaar kan de oude project's key/RLS afzonderlijk beoordelen. Er zijn in deze uitvoering geen nieuwe secrets blootgesteld.

Overige grenzen: bestaande bundle-sizewaarschuwing en lintwarnings; geen Safari/Firefox-, screenreader-, load- of penetratietest. Contactformulier niet verzonden. Geen DNS-, infra-, plan- of productieaanpassing nodig of uitgevoerd.

## Bewijs en claimcontrole

Hubbeelden tonen de echte lokale app met synthetische records; de huidige browserjourney reproduceert indiening, Finance-routing, menselijke beslissing, historie en Bob-isolatie. Governancebeelden zijn expliciet gelabelde presentaties van opgeslagen CLI-output, geen agent-GUI of nieuwe modelinference. Beleidsantwoord, authority-handoff en echte HTTP-integratie zijn opnieuw gecontroleerd. Diagrammen zijn auteurstekeningen. De PDF-cover is een render van het echte document.

De bevroren holdout blijft **v1 22/32 totaal, 4/12 ondersteunde vragen; v2 21/32 totaal, 12/12 ondersteunde vragen**. Beide kwaliteitsgates falen; deze uitvoering heeft geen nieuwe modelevaluatie of modelverbetering verzonnen. De 30/30 deterministische cases bewijzen geen modelnauwkeurigheid. Een toegestane bron-ID bewijst geen relevantie. Het model heeft geen actietools; alleen de afzonderlijk bevestigde CLI kan lokaal een aanvraag indienen. Een mens beslist.

De financiële basis blijft **−€7.695 in jaar één, eerste niet-negatieve cumulatieve maand 25**. De oorspronkelijke immediate-benefitvariant blijft afzonderlijk −€4.860 / 20,17 maanden. PDF-sensitiviteiten zonder ramp zijn als steady-state gelabeld. Alle kosten/adoptie zijn fictieve planningsaannames, geen actuele offertes of gemeten klantresultaten. Vrijgekomen uren zijn geen automatische kasbesparing.

Microsoft/Entra/Power Platform/Copilot/Dataverse-onderdelen zijn ontwerpen en offline handoff, geen Noordwerk-tenantintegratie. Publieke fixturetokens en CLI-persona's zijn geen productieauthenticatie. JSON-audit is niet tamperproof; productie-identiteit, opslag, recovery en onafhankelijke modelevaluatie blijven onuitgevoerd. Die beperkingen blokkeren productiegebruik, niet een eerlijk technisch interview.

## Career-materiaal en portfolio-oordeel

Alle acht gevraagde bestanden staan in [`docs/career/`](docs/career/): `FLAGSHIP_PROJECT_STRATEGY.md`, `CAREER_POSITIONING.md`, `PROFESSIONAL_MATERIALS.md`, `AI_PORTFOLIO_INTERVIEW_PLAYBOOK.md`, `CAREER_OPPORTUNITIES.md`, `OUTREACH_STRATEGY.md`, `30_DAY_EXECUTION_PLAN.md` en `CAREER_LAUNCH_EXECUTIVE_SUMMARY.md`.

Ze zijn owner-reviewdrafts. Geen afgeronde bachelor, eerdere IT-analist/developerbaan, toegekende certificering, klantimplementatie of senior enterprise-ervaring is toegevoegd. Persoonlijke opleiding, werkverleden, talen, beschikbaarheid en bijdrage vereisen eigenaarbevestiging. Vacatures behouden hun historische peildatum 6 november en moeten voor gebruik worden hercontroleerd. Geen LinkedIn, CV, openbare bio of sollicitatie/outreach gepubliceerd of verstuurd.

| Portfolio-eis | Onderbouwd bewijs / grens |
|---|---|
| Bedrijfsprobleem, procesanalyse en AI-kansen | Fictieve intakeproblemen, AS-IS/TO-BE BPMN, keuze voor regels vóór AI |
| Functionele requirements en architectuur | Acceptatiecriteria→API/UI, codekaart, trust boundaries en offline tenantontwerp |
| Governance en systeemintegratie | Gepubliceerde/per-persona evidence, validator, human boundary; echte bevestigde CLI→Hub HTTP |
| Testen, evaluatie en risico | 16/27/17 tests, browserchecks, raw holdoutfouten en threat model; geen onafhankelijke productieassurance |
| Financieel redeneren en implementatie | Ramp, scenario's, negatieve basis, zeven beslisfasen en go/no-go |
| Stakeholdercommunicatie | Executive PDF, RACI, adoption/measurement en interviewroutes; workshops zijn synthetisch |

**Recruiter-ready binnen deze grenzen:** Hub en Playbook als onafhankelijke portfolio-case; Governance als technisch inspecteerbaar experiment met mislukte modelgates. Geen van de drie bewijst professionele klantdelivery of zelfstandige beheersing van alle gegenereerde code. De eigenaar moet de demo en eigen bijdrage kunnen uitleggen.

Belangrijke code, tests, architectuur, oorspronkelijke PDF, financiële outputs en modelrapporten staan publiek op main. Nieuwe CLI-assets en narratief zijn na merge via publieke HTTP 200 gecontroleerd. Websitebron is privé; de showcase blijft reviewpreview. De huidige screenshot- en controlesamenvattingen bij dit rapport worden met de afsluitende PR gepubliceerd. Een korte eigenaarvideo en persoonlijke bijdragebevestiging bestaan nog niet en worden niet als voltooid voorgesteld.

## Bewijsbundel en veiligheid

- [Hub browserrapport](docs/portfolio/assets/finalization/hub-browser-report.json): echte geïsoleerde workflow; enige consolefout is bewust geïnjecteerde netwerkuitval.
- [Website browserrapport](docs/portfolio/assets/finalization/website-browser-report.json), [desktop](docs/portfolio/assets/finalization/website-desktop.png), [mobiel](docs/portfolio/assets/finalization/website-mobile.png): lokale candidate, geen live-productieclaim.
- [Publieke linkcontrole](docs/portfolio/assets/finalization/public-links.json): tien Noordwerk-bewijsbestanden en twee bestaande websitepagina's HTTP 200.
- [Dependency-audit](docs/portfolio/assets/finalization/website-audit-summary.json): oude, huidige-main- en eindcandidate-lockfile apart.

Geen HarborVoice-, ElevenLabs-, Flows-, Studio-, creditledger-, Neon- of HarborVoice-deploymentmutaties. Geen lokale reviewbranch of eigenaarwerk vernietigd/overschreven. Geen financiële resultaten, klantadoptie, modelkwaliteit of beroepsverleden gefabriceerd. Geen nieuwe secrets gepubliceerd; historische website-anonkeybevinding hierboven expliciet afgebakend. Geen betaalde dienst ingeschakeld. Geen ongeautoriseerde productiedeployment; uitsluitend de bestaande website-PR-preview ontstond via bestaande Git-integratie.

Open punten zijn precies begrensd: eigenaarreview van persoonlijke carrièreclaims en websiteproductie, onafhankelijke praktijk-/modelvalidatie voor eventueel zakelijk gebruik, en de vermelde toegankelijkheids-/productiegrenzen. Er is geen nieuw project of brede roadmap gestart.
