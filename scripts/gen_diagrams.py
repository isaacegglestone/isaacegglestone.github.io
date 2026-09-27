import math, os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public", "images")
FONT="font-family='system-ui,-apple-system,Segoe UI,Roboto,sans-serif'"
BG="#0d1117"; FG="#e6edf3"; MUTED="#8b949e"; DEV="#58a6ff"; OPS="#3fb950"; AI="#d2a8ff"

def ai_badge(cx,cy,r=38,label="AI"):
    return (f"<circle cx='{cx}' cy='{cy}' r='{r+10}' fill='{AI}' opacity='0.18'/>"
            f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{BG}' stroke='{AI}' stroke-width='4'/>"
            f"<text x='{cx}' y='{cy+9}' text-anchor='middle' font-size='26' font-weight='700' fill='{AI}' {FONT}>{label}</text>")

# 1. DevOps infinity loop with AI at the centre
def infinity():
    W,H=900,440; cx,cy=450,220
    path=f"M{cx},{cy} C{cx-80},{cy-140} {cx-330},{cy-140} {cx-330},{cy} C{cx-330},{cy+140} {cx-80},{cy+140} {cx},{cy} C{cx+80},{cy-140} {cx+330},{cy-140} {cx+330},{cy} C{cx+330},{cy+140} {cx+80},{cy+140} {cx},{cy} Z"
    labels=[("Plan",cx-235,cy-118,DEV),("Code",cx-330-18,cy-50,DEV),("Build",cx-330-18,cy+62,DEV),("Test",cx-235,cy+140,DEV),
            ("Release",cx+235,cy-118,OPS),("Deploy",cx+330+18,cy-50,OPS),("Operate",cx+330+18,cy+62,OPS),("Monitor",cx+235,cy+140,OPS)]
    s=[f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' role='img' aria-labelledby='t1'>",
       "<title id='t1'>DevOps infinity loop with AI assisting every stage</title>",
       f"<defs><linearGradient id='g' x1='0' x2='1'><stop offset='0' stop-color='{DEV}'/><stop offset='1' stop-color='{OPS}'/></linearGradient></defs>",
       f"<rect width='{W}' height='{H}' rx='16' fill='{BG}'/>",
       f"<path d='{path}' fill='none' stroke='url(#g)' stroke-width='34' stroke-linejoin='round' opacity='0.9'/>",
       f"<text x='{cx-235}' y='{cy+8}' text-anchor='middle' font-size='30' font-weight='700' fill='{DEV}' {FONT}>DEV</text>",
       f"<text x='{cx+235}' y='{cy+8}' text-anchor='middle' font-size='30' font-weight='700' fill='{OPS}' {FONT}>OPS</text>"]
    for t,x,y,c in labels:
        anchor="end" if x<cx-300 else "start" if x>cx+300 else "middle"
        dy=-26 if y<cy-100 else 36 if y>cy+100 else 6
        s.append(f"<text x='{x}' y='{y+dy}' text-anchor='{anchor}' font-size='18' font-weight='600' fill='{FG}' {FONT}>{t}</text>")
    # small AI sparks on each stage
    for t,x,y,c in labels:
        px = x + (18 if x<cx-300 else -18 if x>cx+300 else 0); py = y + (22 if y<cy-100 else -22 if y>cy+100 else 0)
        s.append(f"<circle cx='{px}' cy='{py}' r='6' fill='{AI}'/>")
    s.append(ai_badge(cx,cy))
    s.append(f"<text x='{cx}' y='{H-18}' text-anchor='middle' font-size='15' fill='{MUTED}' {FONT}>AI assists every stage, and humans stay in the loop</text>")
    s.append("</svg>")
    return "\n".join(s)

# 2. AI-augmented feedback loop (cycle)
def cycle():
    W,H=900,600; cx,cy,R=450,315,215
    steps=[("Observe","metrics, logs, traces",OPS),("Analyse","AI anomaly detection",AI),("Suggest","AI-drafted fixes and PRs",AI),
           ("Review","human approval",FG),("Act","IaC and pipelines apply",DEV),("Learn","better runbooks and prompts",AI)]
    n=len(steps); pts=[(cx+R*math.cos(-math.pi/2+2*math.pi*i/n), cy+R*math.sin(-math.pi/2+2*math.pi*i/n)) for i in range(n)]
    s=[f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' role='img' aria-labelledby='t2'>",
       "<title id='t2'>AI-augmented operations feedback loop</title>",
       f"<defs><marker id='a' viewBox='0 0 10 10' refX='8' refY='5' markerUnits='userSpaceOnUse' markerWidth='14' markerHeight='14' orient='auto-start-reverse'><path d='M0,0 L10,5 L0,10 z' fill='{MUTED}'/></marker></defs>",
       f"<rect width='{W}' height='{H}' rx='16' fill='{BG}'/>",
       f"<text x='{cx}' y='42' text-anchor='middle' font-size='22' font-weight='700' fill='{FG}' {FONT}>The AI-augmented feedback loop</text>"]
    for i in range(n):
        a1=-math.pi/2+2*math.pi*i/n+0.36; a2=-math.pi/2+2*math.pi*(i+1)/n-0.36
        x1,y1=cx+R*math.cos(a1),cy+R*math.sin(a1); x2,y2=cx+R*math.cos(a2),cy+R*math.sin(a2)
        s.append(f"<path d='M{x1:.1f},{y1:.1f} A{R},{R} 0 0 1 {x2:.1f},{y2:.1f}' fill='none' stroke='{MUTED}' stroke-width='3' marker-end='url(#a)'/>")
    for (t,sub,c),(x,y) in zip(steps,pts):
        s.append(f"<rect x='{x-105:.1f}' y='{y-34:.1f}' width='210' height='68' rx='12' fill='{BG}' stroke='{c}' stroke-width='3'/>")
        s.append(f"<text x='{x:.1f}' y='{y-5:.1f}' text-anchor='middle' font-size='19' font-weight='700' fill='{c}' {FONT}>{t}</text>")
        s.append(f"<text x='{x:.1f}' y='{y+19:.1f}' text-anchor='middle' font-size='13' fill='{MUTED}' {FONT}>{sub}</text>")
    s.append(ai_badge(cx,cy-12,44,"AI"))
    s.append(f"<text x='{cx}' y='{cy+62}' text-anchor='middle' font-size='14' fill='{MUTED}' {FONT}>faster loops, fewer surprises</text>")
    s.append("</svg>")
    return "\n".join(s)

# 3. Shift-left pipeline with AI checkpoints
def pipeline():
    W,H=900,320
    stages=[("Commit",DEV,"AI pair-programming"),("Review",AI,"AI code review"),("Build",DEV,"cached, reproducible"),
            ("Secure",AI,"AI scan triage"),("Deploy",OPS,"IaC: Terraform/Helm"),("Observe",OPS,"AI incident insights")]
    n=len(stages); bw=118; gap=(W-60-n*bw)/(n-1); y=110
    s=[f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' role='img' aria-labelledby='t3'>",
       "<title id='t3'>Delivery pipeline with AI checkpoints and a feedback path</title>",
       f"<defs><marker id='b' viewBox='0 0 10 10' refX='8' refY='5' markerUnits='userSpaceOnUse' markerWidth='14' markerHeight='14' orient='auto'><path d='M0,0 L10,5 L0,10 z' fill='{MUTED}'/></marker></defs>",
       f"<rect width='{W}' height='{H}' rx='16' fill='{BG}'/>",
       f"<text x='{W/2}' y='44' text-anchor='middle' font-size='22' font-weight='700' fill='{FG}' {FONT}>Shift left with AI checkpoints</text>"]
    xs=[30+i*(bw+gap) for i in range(n)]
    for i,(t,c,sub) in enumerate(stages):
        x=xs[i]
        s.append(f"<rect x='{x:.1f}' y='{y}' width='{bw}' height='56' rx='10' fill='{BG}' stroke='{c}' stroke-width='3'/>")
        s.append(f"<text x='{x+bw/2:.1f}' y='{y+35}' text-anchor='middle' font-size='18' font-weight='700' fill='{c}' {FONT}>{t}</text>")
        s.append(f"<text x='{x+bw/2:.1f}' y='{y+80}' text-anchor='middle' font-size='12.5' fill='{MUTED}' {FONT}>{sub}</text>")
        if c==AI: s.append(f"<circle cx='{x+bw-6:.1f}' cy='{y+6}' r='9' fill='{AI}'/><text x='{x+bw-6:.1f}' y='{y+10}' text-anchor='middle' font-size='9' font-weight='700' fill='{BG}' {FONT}>AI</text>")
        if i<n-1: s.append(f"<line x1='{x+bw+4:.1f}' y1='{y+28}' x2='{xs[i+1]-6:.1f}' y2='{y+28}' stroke='{MUTED}' stroke-width='3' marker-end='url(#b)'/>")
    x0=xs[0]+bw/2; x1=xs[-1]+bw/2; yb=y+128
    s.append(f"<path d='M{x1:.1f},{y+98} L{x1:.1f},{yb} L{x0:.1f},{yb} L{x0:.1f},{y+98}' fill='none' stroke='{AI}' stroke-width='3' stroke-dasharray='8 6' marker-end='url(#b)'/>")
    s.append(f"<text x='{W/2}' y='{yb+24}' text-anchor='middle' font-size='14' fill='{AI}' {FONT}>production feedback informs the next change</text>")
    s.append("</svg>")
    return "\n".join(s)

for name,fn in (("devops-ai-infinity",infinity),("ai-feedback-loop",cycle),("ai-pipeline",pipeline)):
    open(f"{OUT}/{name}.svg","w").write(fn())
print("ok")
