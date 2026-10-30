"""Build a ten-page executive decision deck from committed synthetic evidence.

Optional build dependency: reportlab (BSD). Runtime models remain dependency-free.
Run from any directory: python3 scripts/build_executive_pdf.py
"""
from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader

ROOT=Path(__file__).resolve().parents[1]
R=json.loads((ROOT/'output/investment-case.json').read_text())
W,H=960,540
NAV='#20384a'; TEAL='#096b62'; MUTED='#5c6e7a'; LINE='#dce5e9'; BG='#f3f6f8'; AMBER='#85510d'
OUT=ROOT/'deliverables/noordwerk-executive-brief.pdf'
c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
c.setTitle('Noordwerk | A bounded automation pilot')
c.setAuthor('Philippe Godfroy | Fictional portfolio case')


def text(x,y,value,size=16,color=NAV,bold=False):
    c.setFillColor(HexColor(color));c.setFont('Helvetica-Bold' if bold else 'Helvetica',size)
    c.drawString(x,y,str(value))


def para(x,y,value,width,size=15,color=NAV,leading=None):
    style=ParagraphStyle('body',fontName='Helvetica',fontSize=size,leading=leading or size*1.45,textColor=HexColor(color))
    p=Paragraph(value,style);_,height=p.wrap(width,1000);p.drawOn(c,x,y-height)
    return y-height


def line(x1,y1,x2,y2,color=LINE,width=1):
    c.setStrokeColor(HexColor(color));c.setLineWidth(width);c.line(x1,y1,x2,y2)


def rect(x,y,w,h,color):
    c.setFillColor(HexColor(color));c.rect(x,y,w,h,fill=1,stroke=0)


def page(n,title,subtitle=None,dark=False):
    rect(0,0,W,H,NAV if dark else '#ffffff')
    text(48,505,'noordwerk',15,'#ffffff' if dark else NAV,True)
    text(690,505,'Enterprise transformation / Decision brief',9,'#c1d2dc' if dark else MUTED)
    if title:text(48,449,title,30,'#ffffff' if dark else NAV,True)
    if subtitle:para(48,425,subtitle,850,12,'#c1d2dc' if dark else MUTED)
    line(48,36,912,36,'#496372' if dark else LINE)
    text(48,20,'Fictional company. Synthetic assumptions. No production or customer outcome claims.',8,'#c1d2dc' if dark else MUTED)
    text(884,20,f'{n:02d} / 10',8,'#c1d2dc' if dark else MUTED)


def end():c.showPage()


def node(x,y,w,title,body,filled=False):
    rect(x,y,w,72,TEAL if filled else BG)
    text(x+14,y+48,title,14,'#ffffff' if filled else NAV,True)
    para(x+14,y+35,body,w-28,10,'#e4f2ed' if filled else MUTED)


def arrow(x1,y,x2):
    line(x1,y,x2,y,'#7893a4',1.5)
    line(x2-5,y+3,x2,y,'#7893a4',1.5);line(x2-5,y-3,x2,y,'#7893a4',1.5)

page(1,None,dark=True)
text(48,414,'A bounded',47,'#ffffff',True)
text(48,358,'automation pilot',47,'#ffffff',True)
para(50,310,'Reliable request routing. Accountable human decisions.<br/>A separate, measurable policy-assistant experiment.',700,21,'#d4e4ec',30)
line(50,188,910,188,'#496372')
for x,title,body in [(50,'Decide','Is the investment justified?'),(340,'Deliver','Does the process work?'),(630,'Govern','Are the boundaries proven?')]:
    text(x,144,title,21,'#8fd3c2',True);text(x,118,body,13,'#d4e4ec')
text(50,65,'Sponsor recommendation: fund discovery; gate further spend on measured evidence.',12,'#ffffff')
end()

page(2,'The employee-to-reviewer journey','A real local application on the existing .NET API. Microsoft tenant integration remains a target design.')
screenshot=ROOT/'docs/assets/hub-overview.png'
if screenshot.exists():
    image=ImageReader(str(screenshot));iw,ih=image.getSize();scale=min(625/iw,345/ih)
    c.drawImage(image,48,57,width=iw*scale,height=ih*scale,mask='auto')
    x=700
else:
    x=48
text(x,362,'Working locally',18,TEAL,True)
y=330
for title,body in [('Submit','Category, amount, explicit confirmation.'),('Review','A separate identity records a reason.'),('Follow up','Status and durable decision history.'),('Recover','Safe retries and version conflicts.')]:
    text(x,y,title,14,NAV,True);y=para(x,y-12,body,210,12,MUTED)-24
end()

page(3,'Where the process loses time','Scenario assumptions: 140 employees, 600 requests a month. Baseline observations still need to be collected.')
text(48,359,'Current process',18,NAV,True)
for x,t,b in [(48,'Email intake','Missing category or amount'),(342,'Find an owner','Unclear queue and follow-up'),(636,'Reconcile decisions','Approval buried in messages')]:
    node(x,253,255,t,b); 
arrow(310,289,332);arrow(604,289,626)
text(48,210,'Proposed process',18,TEAL,True)
for x,t,b in [(48,'Validated request','Employee confirms the details'),(342,'Deterministic routing','IT / Finance / Operations'),(636,'Human decision','Reason, version and audit event')]:
    node(x,106,255,t,b,True)
arrow(310,142,332);arrow(604,142,626)
text(48,68,'Measure active work and approval waiting separately; workflow software cannot remove reviewer workload.',11,MUTED)
end()

page(4,'Choose the smallest useful intervention','Use-case scoring guides the discussion; ownership, data permission and risk are hard gates.')
rows=[('Rules-only routing','High readiness / low model risk','Pilot first'),('Policy evidence assistant','Source ownership + model quality required','Experiment'),('Document extraction','Input quality and secure storage unresolved','Defer'),('Autonomous HR decisions','No owner / no data permission / high risk','Block')]
for y,(a,b,d) in zip([342,267,192,117],rows):
    line(48,y-25,912,y-25)
    text(48,y,a,17,NAV,True);text(365,y,b,12,MUTED);text(800,y,d,12,TEAL if d=='Pilot first' else AMBER,True)
para(48,74,'Alternative: standardise email intake and name queue owners first. Choose Power Platform only after entitlement and support review.',850,12,MUTED)
end()

page(5,'Architecture and trust boundaries','Solid components run locally. Microsoft products below the boundary are the deployment target, not a fabricated live integration.')
node(48,292,240,'Employee / approver','Public synthetic identities')
node(360,292,240,'.NET API','Ownership, validation, state machine',True)
node(672,292,240,'Local JSON store','One process; not tamper resistant')
arrow(295,328,350);arrow(606,328,662)
node(48,183,240,'Policy model experiment','Local Ollama; no action tools')
node(360,183,240,'Evidence validator','Published + persona filter; exact quote',True)
node(672,183,240,'Approved policy excerpts','Small curated corpus; public fixtures')
arrow(295,219,350);arrow(606,219,662)
line(48,151,912,151,'#7893a4')
text(48,127,'Tenant gate',12,TEAL,True)
para(180,138,'Entra identity + queue permissions / Power Apps + Power Automate / Dataverse + protected audit / Copilot Studio + source access / approved HTTPS ingress',720,13)
text(48,65,'Model gate FAILED: v2 answers supported questions but misses safe abstention. No action tools.',11,TEAL,True)
end()

page(6,'The economics do not justify immediate rollout','Capacity is an assumption. Only 50% of released capacity is treated as economically realised value.')
text(48,350,'EUR -7,695',49,AMBER,True)
text(50,320,'Year-one net, including adoption ramp',16,MUTED)
text(565,353,'25 months',36,NAV,True)
text(566,320,'First non-negative cumulative month',13,MUTED)
for x,title,body in [(48,'EUR 12,000','Implementation allowance'),(345,'EUR 350 / month','Licensing, AI, hosting and support'),(650,'42 hours / month','Capacity at 60% steady adoption')]:
    line(x,265,x+250,265);text(x,235,title,21,NAV,True);para(x,218,body,245,12,MUTED)
para(48,153,'Ramp assumption: no benefits in months 1-2; adoption 20% in month 3, 40% in month 4, then 60%. Recurring cost begins in month 1.',850,15)
para(48,87,'Source: output/investment-case.json. Original immediate-benefit model: EUR -4,860 in year one and 20.17-month payback. No vendor quotes or measured customer savings.',850,10,MUTED)
end()

page(7,'Cash flow and sensitivity','A useful business case must make it easy to reject an unfavourable investment.')
# Reproducible financial chart; no decorative assets or invented measurements.
x0,y0,cw,ch=60,140,440,245
vals=[-12000]+[r['cumulative'] for r in R['cash_flow']]
lo=min(vals)-1000;hi=max(vals)+1000
def px(i):return x0+i/36*cw
def py(v):return y0+(v-lo)/(hi-lo)*ch
for value in [-12000,-6000,0,6000]:
    line(x0,py(value),x0+cw,py(value),LINE)
    text(x0,py(value)+5,f'EUR {value:,}',9,MUTED)
for i in range(1,len(vals)):
    line(px(i-1),py(vals[i-1]),px(i),py(vals[i]),TEAL,2)
for i in [0,12,24,36]:text(px(i)-5,y0-20,str(i),10,MUTED)
text(175,y0-42,'Months after implementation spend',11,MUTED)
text(555,365,'Year-one net by adoption and cost',14,NAV,True)
text(555,333,'Adoption',11,MUTED)
for j,cost in enumerate([200,350,600]):text(665+j*82,333,f'EUR {cost}',11,MUTED)
for i,a in enumerate([.3,.6,.9]):
    y=283-i*54;text(555,y,f'{int(a*100)}%',14,NAV,True)
    for j,cost in enumerate([200,350,600]):
        row=next(r for r in R['sensitivity'] if r['adoption']==a and r['monthly_operating_cost']==cost)
        text(665+j*82,y,f"{row['first_year_net']:,.0f}",12,TEAL if row['first_year_net']>=0 else AMBER)
para(555,98,'Right: steady-state scenarios without ramp. Base first-year break-even adoption is 85.71%. All amounts are synthetic EUR.',350,10,MUTED)
end()

page(8,'Governance determines whether the pilot can proceed','Controls implemented in a public local demo are not a substitute for tenant identity and operational acceptance.')
items=[('Access','IT','Real employee and reviewer logins; negative access tests.'),('Policy quality','Finance / IT','Publish and revoke sources; independently review model relevance.'),('Consequential actions','Process owner','No model approval authority; human reason and current version.'),('Release and recovery','Platform owner','Managed Test import, connection ownership and recovery drill.'),('Value and adoption','Sponsor / Change','Measure time, rework, usage and cost; stop if value is absent.')]
for y,(a,b,d) in zip([351,290,229,168,107],items):
    text(48,y,a,16,NAV,True);text(270,y,b,12,TEAL,True);para(445,y+11,d,465,13);line(48,y-23,912,y-23)
end()

page(9,'A staged delivery decision','Six weeks is a planning hypothesis. Tenant access, reviewers and confirmed entitlements are dependencies.')
steps=[('Discover','Baseline + process validation','Sponsor signs scope'),('Prototype','Controlled local reference','Safety tests pass'),('Pilot','Identity, training, support','IT accepts Test evidence'),('Evaluate','Independent tasks + quality','Refresh costs and risks'),('Decide','Go/no-go, conditional rollout','Scale, simplify or stop')]
for i,(a,b,d) in enumerate(steps):
    x=48+i*175
    text(x,353,str(i+1),28,TEAL,True);text(x,307,a,18,NAV,True)
    para(x,279,b,145,13,MUTED)
    line(x,206,x+145,206)
    para(x,184,d,145,12,NAV)
para(48,111,'Operational handover: named owner and deputy, source review cadence, support channel, incident response, reconciled pending requests and a tested restore procedure.',850,15)
end()

page(10,'Approve the learning, then earn the rollout','A bounded pilot is valuable only if it can lead to a well-supported stop decision.',dark=True)
for y,a,b in [(345,'Confirm the problem','Measure active handling time, approval delay and incomplete submissions.'),(260,'Set the spending limit','Separate discovery, platform, support and model consumption allowances.'),(175,'Require evidence at each gate','No rollout without accepted security, model quality and a refreshed business case.')]:
    text(48,y,a,22,'#8fd3c2',True);para(48,y-18,b,830,16,'#d4e4ec')
text(48,79,'Companion evidence: Hub source + tests / Agent model reports / Playbook inputs + monthly cash flow',10,'#d4e4ec')
text(48,59,'Prepared by Philippe Godfroy. Fictional consulting exercise; not a real engagement or procurement recommendation.',9,'#d4e4ec')
end()
c.save()
print(OUT)
