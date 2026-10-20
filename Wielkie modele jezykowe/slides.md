---
marp: true
theme: default
paginate: true
size: 16:9
title: Textbooks Are All You Need
style: |
  @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');
  :root {
    --ink: #14111c; --mute: #7d7788; --line: #e3dee5; --soft: #fffdf9;
    --lime: #ffd84d; --indigo: #5b2fd6; --violet: #9c86e4; --lav: #eee8fb;
    --pink: #c8326b; --pinksoft: #f8e3eb; --green: #3d7a3a;
    --ext: #e09a00; --extsoft: #fdf1d2;
    --night: #120e19; --bar: #dcd7e4; --paper: #f7f5f0;
    --edge: rgba(20, 17, 28, .08);
    --lift: 0 1px 2px rgba(20, 17, 28, .04), 0 6px 18px -10px rgba(20, 17, 28, .14);
  }
  section {
    background: var(--paper); color: var(--ink);
    font-family: 'Manrope', system-ui, sans-serif; font-weight: 400;
    font-size: 26px; letter-spacing: -0.01em; line-height: 1.35;
    padding: 64px 80px 60px;
    display: flex; flex-direction: column; justify-content: flex-start;
  }
  section::after {
    font-family: 'IBM Plex Mono', monospace; font-size: 16px; color: #b3acbd;
    right: 40px; bottom: 28px;
  }
  h1 {
    font-size: 54px; font-weight: 400; letter-spacing: -0.025em; line-height: 1.1;
    color: var(--ink); margin: 0 0 8px; padding: 0; border: none;
  }
  h1 strong { font-weight: 500; }
  p { margin: 0; }
  .sub { color: var(--mute); font-size: 24px; margin-top: 2px; }
  .src { position: absolute; left: 80px; bottom: 30px; font-size: 17px; color: var(--mute); }
  .mono { font-family: 'IBM Plex Mono', monospace; }
  .muted { color: var(--mute); }
  .small { font-size: 20px; color: var(--mute); }
  .center { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; }
  .row { display: flex; gap: 22px; align-items: center; justify-content: center; }
  .col { display: flex; flex-direction: column; gap: 14px; }
  .box { background: var(--soft); border: 1px solid var(--edge); box-shadow: var(--lift); border-radius: 18px; padding: 16px 24px; font-size: 22px; white-space: nowrap; }
  .box.lime { background: var(--lime); }
  .box.lav { background: var(--lav); }
  .box.dark { background: var(--night); color: #fff; border-color: rgba(255, 255, 255, .08); }
  .box.pink { background: var(--pinksoft); color: #9c1f50; }
  .box.ext { background: var(--extsoft); color: #8a5a00; }
  .box .s { display: block; font-size: 17px; color: var(--mute); font-family: 'IBM Plex Mono', monospace; margin-top: 4px; }
  .box.dark .s { color: #a49dbb; }
  .arrow { color: #b3a9c9; font-size: 28px; }
  .hl { background: var(--lime); padding: 0 8px; border-radius: 6px; }
  .tag { display: inline-block; border: 1px solid var(--edge); font-size: 16px; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; padding: 6px 12px; border-radius: 999px; background: var(--soft); color: var(--mute); }

  /* title & dividers */
  section.title, section.divider, section.statement.dark { background: var(--night); color: #fff; justify-content: center; }
  section.title h1 { font-size: 104px; color: #fff; letter-spacing: -0.035em; margin: 40px 0 16px; }
  section.divider h1 { font-size: 84px; color: #fff; letter-spacing: -0.03em; }
  .kicker { color: var(--lime); font-size: 22px; }
  section.title .who { position: absolute; left: 80px; bottom: 70px; font-size: 22px; }
  section.title .who span { color: #8a7fae; margin-left: 24px; }
  section.divider .num { font-family: 'IBM Plex Mono', monospace; color: #7d6fae; font-size: 22px; margin-bottom: 18px; }
  section.divider .sub { color: #9b93ad; font-size: 26px; margin-top: 10px; }
  section.title::after, section.divider::after { color: #5a4f72; }
  section.statement { justify-content: center; }
  section.statement h1 { font-size: 72px; letter-spacing: -0.035em; }
  section.statement.dark h1 { color: #fff; }

  /* external-knowledge slides */
  section.ext { box-shadow: inset 12px 0 0 var(--ext); }
  section.ext::before {
    content: "Beyond the paper · web sources";
    position: absolute; top: 26px; right: 40px;
    background: var(--ext); color: var(--night); font: 600 15px/1 'Manrope', sans-serif;
    letter-spacing: .12em; text-transform: uppercase; padding: 9px 14px; border-radius: 999px;
  }
  section.ext.divider .kicker { color: var(--ext); }

  /* stat tiles */
  .stats { display: grid; grid-template-columns: repeat(var(--n, 3), 1fr); gap: 36px; width: 100%; }
  .stat .v { font-family: 'IBM Plex Mono', monospace; font-size: 88px; letter-spacing: -0.05em; line-height: 1; }
  .stat .l { font-size: 23px; color: var(--mute); margin-top: 14px; }
  .stat.hi .v { color: var(--indigo); }
  .stat.exthi .v { color: var(--ext); }

  /* horizontal bars */
  .hbars { width: 100%; display: flex; flex-direction: column; gap: 11px; }
  .hbar { display: grid; grid-template-columns: 300px 1fr; align-items: center; gap: 16px; font-size: 20px; }
  .hbar .lab small { color: var(--mute); font-family: 'IBM Plex Mono', monospace; font-size: 16px; margin-left: 8px; }
  .hbar .track { position: relative; height: 28px; }
  .hbar .fill { height: 100%; width: var(--w); background: var(--bar); border-radius: 6px; }
  .fill.hi, .vbar.hi { background: var(--night) !important; }
  .fill.lime, .vbar.lime { background: var(--lime) !important; }
  .fill.ind, .vbar.ind { background: var(--indigo) !important; }
  .fill.vio, .vbar.vio { background: var(--violet) !important; }
  .fill.ext, .vbar.ext { background: var(--ext) !important; }
  .fill.pink, .vbar.pink { background: var(--pink) !important; }
  .hbar .val { position: absolute; left: calc(var(--w) + 12px); top: 50%; transform: translateY(-50%); font-family: 'IBM Plex Mono', monospace; font-size: 19px; white-space: nowrap; }

  /* vertical bars */
  .vchart { display: flex; align-items: flex-end; justify-content: center; gap: 56px; }
  .vcol { display: flex; flex-direction: column; align-items: center; }
  .vbars { display: flex; align-items: flex-end; gap: 10px; height: var(--hh, 320px); border-bottom: 1px solid var(--line); padding: 0 8px; }
  .vbar { width: var(--bw, 60px); height: var(--h); background: var(--bar); border-radius: 7px 7px 0 0; position: relative; }
  .vbar span { position: absolute; top: -28px; left: -20px; right: -20px; text-align: center; font-family: 'IBM Plex Mono', monospace; font-size: 19px; }
  .vcap { font-size: 20px; margin-top: 12px; text-align: center; }
  .vcap small { display: block; color: var(--mute); font-family: 'IBM Plex Mono', monospace; font-size: 16px; }
  .legend { display: flex; gap: 30px; font-size: 20px; color: #4a4458; justify-content: center; margin-top: 26px; }
  .legend i { display: inline-block; width: 16px; height: 16px; border-radius: 4px; margin-right: 8px; vertical-align: -2px; background: var(--bar); }

  /* cards */
  .cards { display: grid; grid-template-columns: repeat(var(--n, 4), 1fr); gap: 20px; width: 100%; }
  .card { background: var(--soft); border: 1px solid var(--edge); box-shadow: var(--lift); border-radius: 20px; padding: 26px 26px 28px; }
  .card .k { font-family: 'IBM Plex Mono', monospace; color: var(--mute); font-size: 17px; }
  .card .t { font-size: 27px; margin-top: 14px; line-height: 1.2; }
  .card .d { font-size: 20px; color: var(--mute); margin-top: 10px; line-height: 1.35; }
  .card.lime { background: var(--lime); } .card.lime .k, .card.lime .d { color: #6b4e00; }
  .card.dark { background: var(--night); color: #fff; border-color: rgba(255, 255, 255, .08); }
  .card.lav { background: var(--lav); }
  .card.pink { background: var(--pinksoft); } .card.pink .t { color: #9c1f50; }
  .card.ext { background: var(--extsoft); } .card.ext .k { color: #a86f00; }

  /* timeline */
  .tl { position: relative; display: grid; grid-template-columns: repeat(var(--n, 4), 1fr); width: 100%; gap: 12px; }
  .tl::before { content: ""; position: absolute; left: 0; right: 0; top: 51px; height: 2px; background: var(--line); }
  .tl .date { font-family: 'IBM Plex Mono', monospace; font-size: 17px; color: var(--mute); height: 36px; }
  .tl .dot { width: 16px; height: 16px; border-radius: 50%; background: var(--indigo); margin: 8px 0 20px; position: relative; }
  .tl .dot.ext { background: var(--ext); }
  .tl .name { font-size: 25px; line-height: 1.15; }
  .tl.dense .name { font-size: 21px; white-space: nowrap; }
  .tl.dense7 .name { font-size: 19px; }
  .stats.four .v { font-size: 70px; }
  .tl .meta { font-size: 19px; color: var(--mute); margin-top: 8px; line-height: 1.35; }

  /* code */
  pre { background: var(--soft) !important; border-radius: 18px; padding: 18px 24px !important; font-size: 18px; line-height: 1.45; margin: 0; border: 1px solid var(--edge); box-shadow: var(--lift); }
  code { font-family: 'IBM Plex Mono', monospace; }
  p code, li code, .box code, .card code { background: rgba(20, 17, 28, .05); padding: 2px 7px; border-radius: 6px; font-size: .85em; }
  pre code { background: none !important; padding: 0 !important; font-size: inherit; }
  .codecap { font-size: 17px; font-family: 'IBM Plex Mono', monospace; color: var(--mute); margin: 0 0 8px; }
  .codecap.good { color: var(--green); } .codecap.bad { color: var(--pink); }

  /* verdict chips */
  .ok { color: var(--green); } .no { color: var(--pink); } .meh { color: #b5730b; }
  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; width: 100%; align-items: start; }
  section table { display: table; border-collapse: collapse; width: auto; font-size: 24px; margin: 0 auto; border: 0; }
  section table tr { background: transparent !important; border: 0 !important; }
  section table th, section table td { border: 0 !important; border-bottom: 1px solid var(--line) !important; background: transparent !important; padding: 14px 28px; text-align: left; }
  section table th { font-weight: 400; color: var(--mute); }
  section table td.mono { font-size: 22px; }
---

<!-- _class: title -->
<!-- _paginate: skip -->

<p class="kicker">Seminar: Large Language Models</p>

# Textbooks Are<br>All You Need

<p class="sub" style="color:#9b93ad">Gunasekar et al. · Microsoft Research · 2023</p>

<div class="who">Bartosz Kruszewski</div>

<!--
- Microsoft Research, June 2023 
- phi-1 — first model of the Phi family
- reference to "Attention Is All You Need" Transformer paper
-->

---

<!-- _class: statement -->

# What if <span class="hl">better data</span><br>beats bigger models?

<!--
- One-sentence thesis of the paper
- Instead of more params / more compute → better data
- How much of an LLM's quality is data vs size?
- Better for ecology
-->

---

# Scaling laws

<p class="sub">more parameters, more compute → lower loss</p>

<div class="center">
<svg width="900" height="380" viewBox="0 0 900 380">
  <line x1="60" y1="40" x2="880" y2="40" stroke="#e7e3ee"/>
  <line x1="60" y1="140" x2="880" y2="140" stroke="#e7e3ee"/>
  <line x1="60" y1="240" x2="880" y2="240" stroke="#e7e3ee"/>
  <line x1="60" y1="340" x2="880" y2="340" stroke="#e7e3ee"/>
  <polyline points="80,60 280,130 480,195 680,250 860,295" fill="none" stroke="#5b2fd6" stroke-width="2.5"/>
  <circle cx="80" cy="60" r="7"/><circle cx="280" cy="130" r="7"/><circle cx="480" cy="195" r="7"/><circle cx="680" cy="250" r="7"/><circle cx="860" cy="295" r="7"/>
  <text x="60" y="372" font-size="18" fill="#857f90">small</text>
  <text x="880" y="372" font-size="18" fill="#857f90" text-anchor="end">large  (log scale)</text>
  <text x="56" y="28" font-size="18" fill="#857f90">loss</text>
</svg>
</div>

<p class="src">Kaplan et al., 2020 · Hoffmann et al., 2022 (cited in the paper) · TinyStories: Eldan &amp; Li, 2023</p>

<!--
- Scaling laws: loss falls predictably as a power laws
- Two classic knobs: parameters, compute
- ignored data QUALITY
- Inspiration: TinyStories (same authors) — synthetic simple stories, tiny models speak fluent English
- This paper: does it work for a code task
-->

---

# The domain: code

<p class="sub">write a Python function from its docstring</p>

<div class="center">
<div class="grid2" style="grid-template-columns:1.25fr 1fr; align-items:center">

```python
def incr_list(l: list):
    """Return list with elements
    incremented by 1."""
    return [x + 1 for x in l]
```

<div class="col">
  <div class="box"><b>HumanEval</b><span class="s">164 problems · unit tests</span></div>
  <div class="box"><b>MBPP</b><span class="s">mostly basic Python problems</span></div>
  <div class="box lav"><b>pass@1</b><span class="s">one try, must pass all tests</span></div>
</div>
</div>
</div>

<!--
- Build simple Python functions from docstrings
- HumanEval: code benchmark - unit tests
- MBPP - basic programs benchmark
- pass@1 - single generation, correct or not — strict
-->

---

# phi-1 at a glance

<div class="center">
<div class="stats four" style="--n:4">
  <div class="stat"><div class="v">1.3B</div><div class="l">parameters</div></div>
  <div class="stat"><div class="v">7B</div><div class="l">tokens of data</div></div>
  <div class="stat"><div class="v">4 days</div><div class="l">on 8 × A100</div></div>
  <div class="stat hi"><div class="v">50.6%</div><div class="l">HumanEval pass@1</div></div>
</div>
</div>

<!--
- 1.3B params — tiny vs 15B–540B code models of 2023
- 7B unique tokens, ~8 passes → ~50B tokens seen
- Training 4 days on 8 A100 + 7 h finetuning — academic budget
- 50.6% HumanEval, 55.5% MBPP — among best single-generation results (mid-2023)
- phi-1-small (350M) still 45% HumanEval
-->

---

# HumanEval vs open & closed models

<p class="sub">pass@1, self-reported · June 2023</p>

<div class="center">
<div class="hbars">
  <div class="hbar"><div class="lab">GPT-4<small>?</small></div><div class="track"><div class="fill" style="--w:83.75%"></div><div class="val" style="--w:83.75%">67%</div></div></div>
  <div class="hbar"><div class="lab">WizardCoder<small>16B</small></div><div class="track"><div class="fill" style="--w:71.6%"></div><div class="val" style="--w:71.6%">57.3%</div></div></div>
  <div class="hbar"><div class="lab"><b>phi-1</b><small>1.3B</small></div><div class="track"><div class="fill lime" style="--w:63.25%"></div><div class="val" style="--w:63.25%">50.6%</div></div></div>
  <div class="hbar"><div class="lab">GPT-3.5<small>175B</small></div><div class="track"><div class="fill" style="--w:58.75%"></div><div class="val" style="--w:58.75%">47%</div></div></div>
  <div class="hbar"><div class="lab">StarCoder-Prompted<small>15.5B</small></div><div class="track"><div class="fill" style="--w:51%"></div><div class="val" style="--w:51%">40.8%</div></div></div>
  <div class="hbar"><div class="lab">PaLM-Coder<small>540B</small></div><div class="track"><div class="fill" style="--w:44.9%"></div><div class="val" style="--w:44.9%">35.9%</div></div></div>
  <div class="hbar"><div class="lab">CodeGen-Mono<small>16.1B</small></div><div class="track"><div class="fill" style="--w:36.6%"></div><div class="val" style="--w:36.6%">29.3%</div></div></div>
  <div class="hbar"><div class="lab">Codex<small>12B</small></div><div class="track"><div class="fill" style="--w:36%"></div><div class="val" style="--w:36%">28.8%</div></div></div>
  <div class="hbar"><div class="lab">SantaCoder<small>1.1B</small></div><div class="track"><div class="fill" style="--w:17.5%"></div><div class="val" style="--w:17.5%">14.0%</div></div></div>
</div>
</div>

<p class="src">Table 1 of the paper</p>

<!--
- Only GPT-4 beats it clearly
- WizardCoder: better HumanEval, but worse MBPP (51.8 vs 55.5)
- Beats GPT-3.5 (175B) and PaLM-Coder (540B)
- Data size: competitors 100B–1T tokens, phi-1 7B → ~100× less
- WARNING! self-reported scores by paper authors
-->

---

# Size vs score

<p class="sub">HumanEval pass@1 vs parameters</p>

<div class="center">
<svg width="960" height="430" viewBox="0 0 960 430">
  <g stroke="#e7e3ee"><line x1="60" y1="40" x2="920" y2="40"/><line x1="60" y1="160" x2="920" y2="160"/><line x1="60" y1="280" x2="920" y2="280"/><line x1="60" y1="400" x2="920" y2="400"/></g>
  <g font-size="16" fill="#857f90" font-family="IBM Plex Mono, monospace">
    <text x="48" y="45" text-anchor="end">60</text><text x="48" y="165" text-anchor="end">40</text><text x="48" y="285" text-anchor="end">20</text><text x="48" y="405" text-anchor="end">0</text>
    <text x="208" y="424" text-anchor="middle">1B</text><text x="455" y="424" text-anchor="middle">10B</text><text x="702" y="424" text-anchor="middle">100B</text>
  </g>
  <g fill="#cbc4d6">
    <circle cx="79" cy="321" r="8"/><circle cx="475" cy="227" r="8"/><circle cx="96" cy="323" r="8"/><circle cx="506" cy="224" r="8"/>
    <circle cx="883" cy="185" r="8"/><circle cx="484" cy="263" r="8"/><circle cx="218" cy="316" r="8"/><circle cx="315" cy="269" r="8"/>
    <circle cx="315" cy="217" r="8"/><circle cx="208" cy="338" r="8"/><circle cx="417" cy="285" r="8"/><circle cx="502" cy="198" r="8"/>
    <circle cx="283" cy="255" r="8"/><circle cx="506" cy="215" r="8"/><circle cx="762" cy="118" r="8"/><circle cx="506" cy="56" r="8"/>
  </g>
  <g font-size="16" fill="#857f90">
    <text x="522" y="61">WizardCoder</text><text x="778" y="123">GPT-3.5</text><text x="868" y="170" text-anchor="end">PaLM-Coder 540B</text>
    <text x="518" y="194">StarCoder</text><text x="489" y="243">Codex-12B</text><text x="230" y="320">SantaCoder</text>
  </g>
  <circle cx="236" cy="96" r="12" fill="#5b2fd6"/>
  <text x="256" y="102" font-size="22" fill="#5b2fd6">phi-1 · 1.3B</text>
</svg>
</div>

<p class="src">Table 1 · x axis log scale</p>

<!--
- Each dot = one model from Table 1
- Gray cloud: score roughly grows with size
- phi-1 (blue): far above the trend for its size
- Visual version of "breaking scaling laws"
-->

---

# What's wrong with web code?

<p class="sub">The Stack · StackOverflow — huge, diverse, but not instructive</p>

<div class="center">
<div class="cards" style="--n:4">
  <div class="card"><div class="k">01</div><div class="t">Not self-contained</div><div class="d">depends on other files</div></div>
  <div class="card"><div class="k">02</div><div class="t">Boilerplate</div><div class="d">constants, configs, GUI setup</div></div>
  <div class="card"><div class="k">03</div><div class="t">Buried logic</div><div class="d">inside long, undocumented functions</div></div>
  <div class="card"><div class="k">04</div><div class="t">Skewed topics</div><div class="d">unbalanced coverage of skills</div></div>
</div>
</div>

<!--
- Standard datasets: The Stack (permissive GitHub code), StackOverflow, CodeContests
- Authors manually inspected random samples
- 1: imports from other modules, missing context
- 2: no real logic
- 3: algorithms hidden, poorly documented
- 4: some topics overrepresented
- Human analogy: frustrating to learn coding from noise → same for LMs
-->

---

# High vs low educational value

<div class="grid2" style="margin-top:30px">
<div>
<p class="codecap good">✓ high educational value</p>

```python
def cosine_dist(x, y):
    """Computes Cosine Distance."""
    x = F.normalize(x, dim=1)
    y = F.normalize(y, dim=1)
    dist = 2 - 2 * torch.mm(x, y.t())
    return dist
```

</div>
<div>
<p class="codecap bad">✗ low educational value</p>

```python
class Default(object):
    def __init__(self, vim):
        self._vim = vim
        self._bufnr = -1
        self._winid = -1
        self._winrestcmd = ''
        self._initialized = False
```

</div>
</div>

<!--
- Real examples from the paper
- Left: docstring, real computation, self-contained
- Right: only state initialisation, no logic
-->

---

<!-- _class: statement -->

# A good textbook is<br><span class="hl">clear</span>, <span class="hl">self-contained</span>,<br><span class="hl">instructive</span>, <span class="hl">balanced</span>

<!--
- The four qualities the authors want
- Directly opposite of the four problems
- Title of the paper comes from this idea
- Next: how they build such data (core of the paper)
-->

---

# The data recipe

<div class="center">
<div class="row" style="align-items:stretch">
  <div class="col">
    <div class="box">Filtered web code<span class="s">≈ 6B tokens</span></div>
    <div class="box">Synthetic textbooks<span class="s">&lt; 1B tokens · GPT-3.5</span></div>
  </div>
  <div class="arrow" style="align-self:center">→</div>
  <div class="box lav" style="align-self:center">CodeTextbook<span class="s">pretraining</span></div>
  <div class="arrow" style="align-self:center">→</div>
  <div class="box" style="align-self:center">phi-1-base</div>
</div>
<div class="row" style="margin-top:30px">
  <div class="box">CodeExercises<span class="s">≈ 180M tokens · GPT-3.5</span></div>
  <div class="arrow">→</div>
  <div class="box lav">finetuning</div>
  <div class="arrow">→</div>
  <div class="box lime"><b>phi-1</b></div>
</div>
</div>

<!--
- Three datasets, total < 7B tokens
- Pretraining = CodeTextbook = filtered web + synthetic textbooks → phi-1-base (29% HumanEval)
- Finetune on small CodeExercises → phi-1
- Architecture is boring on purpose — data is the contribution
-->

---

# Step 1 · Filter the web

<div class="center">
<div class="row">
  <div class="box">The Stack + SO<span class="s">35M files · 35B tokens</span></div>
  <div class="arrow">→</div>
  <div class="box lav">GPT-4 labels<span class="s">~100k samples</span></div>
  <div class="arrow">→</div>
  <div class="box lav">random forest<span class="s">on CodeGen embeddings</span></div>
  <div class="arrow">→</div>
  <div class="box lime">≈ 6B tokens</div>
</div>
<p class="small" style="margin-top:40px">prompt: <em>“determine its educational value for a student whose goal is to learn basic coding concepts”</em></p>
</div>

<!--
- Python subset of deduplicated Stack + StackOverflow
- GPT-4 annotates only a small subset — replaces human labelers (its expensive)
- Classifier: random forest on embeddings from pretrained CodeGen
- Cheap to apply classifier to all 35M files → keep ~6B of 35B tokens
-->

---

# Filtering alone helps

<p class="sub">350M model · HumanEval pass@1</p>

<div class="center">
<div class="hbars">
  <div class="hbar"><div class="lab">Unfiltered<small>~200B tok seen</small></div><div class="track"><div class="fill" style="--w:48.8%"></div><div class="val" style="--w:48.8%">12.19%  saturates</div></div></div>
  <div class="hbar"><div class="lab">Filtered<small>36k steps</small></div><div class="track"><div class="fill vio" style="--w:70.7%"></div><div class="val" style="--w:70.7%">17.68%</div></div></div>
  <div class="hbar"><div class="lab">Filtered + textbooks</div><div class="track"><div class="fill hi" style="--w:80.5%"></div><div class="val" style="--w:80.5%">20.12%</div></div></div>
</div>
</div>

<p class="src">Section 2.1</p>

<!--
- Unfiltered plateaus at 12.19% even after 96k steps (~200B tokens)
- Filtered subset: 17.68% after only 36k steps
- Adding synthetic textbooks: 20.12%
- Less data, better model
-->

---

# Step 2 · Synthetic textbooks: diversity

<p class="sub">GPT-3.5 · LLMs follow the most probable path</p>

<div class="center">
<div class="grid2" style="width:900px">
<div class="col" style="align-items:center">
  <div class="row" style="gap:10px"><div class="box">sort</div><div class="box">sort</div><div class="box">sort</div></div>
  <div class="row" style="gap:10px"><div class="box">sort</div><div class="box">sort</div><div class="box">sort</div></div>
  <p class="small" style="margin-top:14px">naive prompting</p>
</div>
<div class="col" style="align-items:center">
  <div class="row" style="gap:10px"><div class="box lav">graphs</div><div class="box lime">matrices</div><div class="box">strings</div></div>
  <div class="row" style="gap:10px"><div class="box">games</div><div class="box lav">recursion</div><div class="box lime">dates</div></div>
  <p class="small" style="margin-top:14px">random topic + random audience</p>
</div>
</div>
</div>

<!--
- Problem: "write a coding textbook" many times → same content repeated
- Trick: inject randomness — constraints on topic and target audience in each prompt
- TinyStories did the same with random words that must appear
-->

---

# A synthetic textbook page

<div class="center">
<div style="width:900px">
<p class="small" style="margin-bottom:12px">“A matrix is said to be singular if its determinant is zero… Now, let's explore these concepts through examples.”</p>

```python
import numpy as np

def is_singular(A):
    det = np.linalg.det(A)
    return det == 0

A = np.array([[1, 2], [2, 4]])
print(is_singular(A))  # True
```

</div>
</div>

<!--
- Real sample from the paper (shortened)
- Note: float == 0 is fragile — GPT-3.5 data has many errors (authors admit it) authors expect GPT-4 data to be even better
-->

---

# Step 3 · CodeExercises

<p class="sub">≈ 180M tokens · docstring → solution · diversity via function names</p>

<div class="center">
<div style="width:960px">

```python
def valid_guessing_letters(word: str, guesses: List[str]) -> List[str]:
    """Returns a list of valid guessing letters, which are letters
    that have not been guessed yet and are present in the word."""
    valid_letters = []
    for letter in word:
        if letter not in guesses and letter not in valid_letters:
            valid_letters.append(letter)
    return valid_letters
```

</div>
</div>

<!--
- Same format as HumanEval: docstring + function body
- Goal: align model to function completion from instructions
- ~880K exercises, basic libraries only (math, random, typing…)
- Because it looks like HumanEval → contamination checks later
-->

---

# Model &amp; training

<p class="sub">decoder-only transformer, deliberately plain</p>

<div class="center">
<table style="width:760px">
<tr><th></th><th>phi-1</th><th>phi-1-small</th></tr>
<tr><td>Parameters</td><td class="mono">1.3B</td><td class="mono">350M</td></tr>
<tr><td>Layers</td><td class="mono">24</td><td class="mono">20</td></tr>
<tr><td>Hidden / MLP dim</td><td class="mono">2048 / 8192</td><td class="mono">1024 / 4096</td></tr>
<tr><td>Heads × dim</td><td class="mono">32 × 64</td><td class="mono">16 × 64</td></tr>
</table>
<div class="row" style="margin-top:34px">
  <div class="box lime">FlashAttention</div><div class="box lime">parallel MHA + MLP</div><div class="box lime">RoPE</div>
  <div class="box pink">✗ FIM</div><div class="box pink">✗ MQA</div>
</div>
</div>

<!--
- Decoder-only, FlashAttention, parallel attention + MLP (like CodeGen, PaLM), rotary embeddings
- No Fill-In-the-Middle, no Multi-Query Attention — gains come from data, not tricks
-->

---

# The key experiment

<p class="sub">HumanEval pass@1 (%) · Figure 2.1</p>

<div class="center">
<div class="vchart">
  <div class="vcol"><div class="vbars" style="--hh:300px">
    <div class="vbar" style="--h:60px"><span>11</span></div><div class="vbar vio" style="--h:87px"><span>16</span></div><div class="vbar hi" style="--h:224px"><span>41</span></div>
  </div><div class="vcap">350M · 26B tokens<small>135 GPU h</small></div></div>
  <div class="vcol"><div class="vbars" style="--hh:300px">
    <div class="vbar" style="--h:65px"><span>12</span></div><div class="vbar vio" style="--h:109px"><span>20</span></div><div class="vbar hi" style="--h:245px"><span>45</span></div>
  </div><div class="vcap">350M · 76B tokens<small>410 GPU h</small></div></div>
  <div class="vcol"><div class="vbars" style="--hh:300px">
    <div class="vbar" style="--h:93px"><span>17</span></div><div class="vbar vio" style="--h:158px"><span>29</span></div><div class="vbar lime" style="--h:278px"><span>51</span></div>
  </div><div class="vcap">1.3B · 51–76B tokens<small>770–1090 GPU h</small></div></div>
</div>
<div class="legend"><span><i></i>The Stack+</span><span><i style="background:var(--violet)"></i>CodeTextbook</span><span><i style="background:var(--night)"></i>→ CodeExercises</span></div>
</div>

<!--
- Black/lime: + finetuning — huge jump
-->

---

<!-- _class: statement -->

# 180M tokens of exercises:<br><span class="hl">29% → 51%</span>

<!--
- Smallest dataset, biggest jump — < 200M tokens, 7 hours
- Two questions: does finetuning unlock *new* skills? is it just memorization?
-->

---

# Emergent skills · understanding

<p class="sub">finetuning on simple exercises unlocks skills not in the exercises</p>

<div class="center">
<div class="cards" style="--n:3">
  <div class="card lime"><div class="k">phi-1</div><div class="t ok">✓ correct</div><div class="d">follows every rule</div></div>
  <div class="card"><div class="k">phi-1-base</div><div class="t no">✗ rambles</div><div class="d">endless <code>self.x = …</code></div></div>
  <div class="card"><div class="k">phi-1-small</div><div class="t meh">~ partial</div><div class="d">gets the idea, wrong logic</div></div>
</div>
<p class="small" style="margin-top:36px">prompt: Alice, Bob and Charles pick numbers… simulate 30 rounds</p>
</div>

<!--
- Hypothesis: finetuning "reorganizes" knowledge learned in pretraining
- Prompt with nested ranges and divisibility rule
- phi-1: correct loop and condition
- base: defines attributes, never solves
- small (350M): understands somewhat, but wrong ranges
-->

---

# Emergent skills · libraries

<p class="sub">PyGame &amp; Tkinter — absent from the exercises</p>

<div class="center">
<table style="width:860px">
<tr><th></th><th>knows the API</th><th>follows the logic</th></tr>
<tr><td><b>phi-1</b></td><td class="ok">✓</td><td class="ok">✓</td></tr>
<tr><td>phi-1-base</td><td class="ok">✓</td><td class="no">✗</td></tr>
<tr><td>phi-1-small</td><td class="no">✗</td><td class="ok">✓</td></tr>
</table>
</div>

<!--
- Exercises use only basic libraries — no pygame, no tkinter
- PyGame (bouncing ball): base knows calls but ignores task; small gets logic but lacks API
- Tkinter (pew button app): phi-1 correct except typo; others invent APIs (tk.popup())
- Also wins on PyTorch
-->

---

# Memorization? · 50 new problems

<p class="sub">separate team · designed to be unusual · graded 0–10 by GPT-4</p>

<div class="center">
<div style="width:980px">

```python
def sort_concat_square_deduplicate(list1, list2, my_threshold):
    """Sorts each list, concatenates them, squares the entries
    at even indices, filters out entries smaller than
    my_threshold and then removes duplicates."""
```

</div>
</div>

<!--
- Worry: CodeExercises has the same format as HumanEval → possible leakage
- Three answers: new benchmark, n-gram check, aggressive pruning
- Team had no access to CodeExercises or the model
- Weird combinations of steps → can't be memorized
- GPT-4 as grader: verbal evaluation then 0–10 grade; finer than pass/fail, no tests needed
-->

---

# Same ranking on new problems

<div class="center">
<div class="hbars">
  <div class="hbar"><div class="lab"><b>phi-1</b><small>1.3B</small></div><div class="track"><div class="fill lime" style="--w:86.7%"></div><div class="val" style="--w:86.7%">52%</div></div></div>
  <div class="hbar"><div class="lab">StarCoder<small>15.5B</small></div><div class="track"><div class="fill" style="--w:85%"></div><div class="val" style="--w:85%">51%</div></div></div>
  <div class="hbar"><div class="lab">phi-1-small<small>350M</small></div><div class="track"><div class="fill vio" style="--w:75%"></div><div class="val" style="--w:75%">45%</div></div></div>
  <div class="hbar"><div class="lab">CodeGen-Mono<small>16.1B</small></div><div class="track"><div class="fill" style="--w:63.3%"></div><div class="val" style="--w:63.3%">38%</div></div></div>
  <div class="hbar"><div class="lab">phi-1-base<small>1.3B</small></div><div class="track"><div class="fill vio" style="--w:61.7%"></div><div class="val" style="--w:61.7%">37%</div></div></div>
  <div class="hbar"><div class="lab">Replit<small>2.7B</small></div><div class="track"><div class="fill" style="--w:61.7%"></div><div class="val" style="--w:61.7%">37%</div></div></div>
  <div class="hbar"><div class="lab">CodeGen-Mono<small>350M</small></div><div class="track"><div class="fill" style="--w:31.7%"></div><div class="val" style="--w:31.7%">19%</div></div></div>
</div>
</div>

<p class="src">Table 2 · LLM-graded understanding score on 50 unconventional problems</p>

<!--
- Ranking matches HumanEval
- phi-1 52% vs StarCoder 51% — closer here (HumanEval: 51 vs 34)
- phi-1-small (350M) 45% — beats 16B CodeGen
-->

---

# n-gram overlap

<div class="center">
<div class="stats" style="--n:3">
  <div class="stat"><div class="v">13</div><div class="l">-gram window</div></div>
  <div class="stat"><div class="v">4</div><div class="l">HumanEval hits</div></div>
  <div class="stat hi"><div class="v">0</div><div class="l">real matches</div></div>
</div>
<p class="small" style="margin-top:44px">all 4 were false positives — shared phrase “frequency of an integer…”</p>
</div>

<!--
- Standard contamination check
- Only 4 hits, all false positives (same generic sentence)
- But n-grams miss paraphrases → need a stronger test
-->

---

# Prune anything similar

<div class="center">
<div class="row">
  <div class="box lav">embedding distance<span class="s">CodeGen-350M</span></div>
  <div class="arrow">+</div>
  <div class="box lav">AST edit distance<span class="s">match rate τ</span></div>
  <div class="arrow">→</div>
  <div class="box pink">remove similar</div>
  <div class="arrow">→</div>
  <div class="box lime">retrain phi-1</div>
</div>
<div class="hbars" style="margin-top:56px; width:900px">
  <div class="hbar" style="grid-template-columns:140px 1fr"><div class="lab">τ = 0.95</div><div class="track"><div class="fill pink" style="--w:4.8%"></div><div class="val" style="--w:4.8%">42.5K removed (5%)</div></div></div>
  <div class="hbar" style="grid-template-columns:140px 1fr"><div class="lab">τ = 0.80</div><div class="track"><div class="fill pink" style="--w:40.2%"></div><div class="val" style="--w:40.2%">354K removed (40%)</div></div></div>
</div>
</div>

<!--
- Embeddings: semantic similarity (docstring, names, structure)
- AST distance: structure, ignores names/comments
- "Strong form" of decontamination, retrain from scratch
- Lower τ = looser similarity = more removed; up to 40% of 879.5K exercises
-->

---

# Still beats StarCoder

<p class="sub">HumanEval pass@1 after retraining on pruned data</p>

<div class="center">
<div style="position:relative">
<div class="vchart" style="gap:46px">
  <div class="vcol"><div class="vbars" style="border:none"><div class="vbar hi" style="--h:270px"><span>50.6</span></div></div><div class="vcap">full data</div></div>
  <div class="vcol"><div class="vbars" style="border:none"><div class="vbar lime" style="--h:270px"><span>50.6</span></div></div><div class="vcap">τ 0.95</div></div>
  <div class="vcol"><div class="vbars" style="border:none"><div class="vbar lime" style="--h:241px"><span>45.1</span></div></div><div class="vcap">τ 0.90</div></div>
  <div class="vcol"><div class="vbars" style="border:none"><div class="vbar lime" style="--h:247px"><span>46.3</span></div></div><div class="vcap">τ 0.85</div></div>
  <div class="vcol"><div class="vbars" style="border:none"><div class="vbar lime" style="--h:241px"><span>45.1</span></div></div><div class="vcap">τ 0.80</div></div>
</div>
<div style="position:absolute; left:0; right:0; bottom:calc(43px + 221px); border-top:2px dashed var(--pink)"></div>
<div style="position:absolute; right:-150px; bottom:calc(43px + 210px); color:var(--pink); font-size:17px" class="mono">StarCoder 41.5</div>
</div>
</div>

<p class="src">Table 3</p>

<!--
- Some drop (50.6 → ~45) — similar data did help a bit
- All models score higher on the "similar" subset → those problems may simply be easier
-->

---

# Limitations

<div class="center">
<div class="cards" style="--n:4">
  <div class="card"><div class="k">scope</div><div class="t">Python only</div><div class="d">narrow APIs, no complex apps</div></div>
  <div class="card pink"><div class="k">prompts</div><div class="t">long prompts fail</div><div class="d">3 layers ✓ · 4 layers ✗ · + <code>import torch</code> ✓</div></div>
  <div class="card pink"><div class="k">language</div><div class="t">typos &amp; wording</div><div class="d">“x stays unchanged” → <code>x = 0</code></div></div>
  <div class="card pink"><div class="k">reasoning</div><div class="t">counting &amp; layout</div><div class="d">extra text field, wrong buttons</div></div>
</div>
</div>

<!--
- Specialist: Python only, lacks domain knowledge of big models (e.g. Flask apps)
- Exercises are short
- Grammar mistakes
- Trade-off: textbook-clean data vs messy real-world users
-->

---

# Open problems they name

<div class="center">
<div class="cards" style="--n:4">
  <div class="card"><div class="k">01</div><div class="t">Coverage</div><div class="d">all concepts, balanced</div></div>
  <div class="card"><div class="k">02</div><div class="t">Diversity</div><div class="d">no repetition</div></div>
  <div class="card"><div class="k">03</div><div class="t">Measurement</div><div class="d">how to quantify diversity?</div></div>
  <div class="card"><div class="k">04</div><div class="t">Ethics</div><div class="d">LLMs curating data for LLMs</div></div>
</div>
<p class="small" style="margin-top:40px">paper in one line: 10× smaller model · 100× less data · near-SOTA on code</p>
</div>

<!--
- Dataset creation methodology = central research direction
- No good metric for diversity / redundancy
- Accountability, transparency, bias when models train models; "recursive training" debate
- GPT-3.5 data noisy — better teacher should help
-->

---

<!-- _class: divider ext -->

<p class="kicker">Beyond the paper</p>

# What happened next

<p class="sub">the Phi family and its impact · 2023 → 2026</p>

<!--
- From here: knowledge from web sources, not from the paper
- Orange tag on every such slide
- ~10 min: Phi family, impact on the field, state today
-->

---

<!-- _class: ext -->

# The Phi family

<div class="center">
<div class="tl dense dense7" style="--n:7">
  <div><div class="date">Jun 2023</div><div class="dot"></div><div class="name">phi-1</div><div class="meta">1.3B · code<br>this paper</div></div>
  <div><div class="date">Sep 2023</div><div class="dot ext"></div><div class="name">phi-1.5</div><div class="meta">1.3B · common<br>sense</div></div>
  <div><div class="date">Dec 2023</div><div class="dot ext"></div><div class="name">phi-2</div><div class="meta">2.7B · general</div></div>
  <div><div class="date">Apr 2024</div><div class="dot ext"></div><div class="name">Phi-3</div><div class="meta">3.8B–14B<br>on a phone</div></div>
  <div><div class="date">Dec 2024</div><div class="dot ext"></div><div class="name">Phi-4</div><div class="meta">14B · mostly<br>synthetic</div></div>
  <div><div class="date">Apr 2025</div><div class="dot ext"></div><div class="name">Phi-4-reasoning</div><div class="meta">14B · thinks</div></div>
  <div><div class="date">Mar 2026</div><div class="dot ext"></div><div class="name">Phi-4-r-vision</div><div class="meta">15B · knows<br>when to think</div></div>
</div>
</div>

<p class="src">Microsoft tech reports, Azure blog, VentureBeat</p>

<!--
- phi-1.5 ("Textbooks Are All You Need II"): same recipe beyond code → common sense
- phi-2: 2.7B, 1.4T tokens; claimed to match models up to 25× larger
- Phi-3-mini 3.8B: 69% MMLU ≈ GPT-3.5, runs on a phone;
- Size grew 1.3B → 15B — still small vs frontier
-->

---

<!-- _class: ext -->

# Small model ≠ small data anymore

<p class="sub">unique training tokens · log scale</p>

<div class="center">
<div class="vchart" style="gap:48px">
  <div class="vcol"><div class="vbars"><div class="vbar hi" style="--h:59px"><span>7B</span></div></div><div class="vcap">phi-1</div></div>
  <div class="vcol"><div class="vbars"><div class="vbar ext" style="--h:104px"><span>~30B</span></div></div><div class="vcap">phi-1.5</div></div>
  <div class="vcol"><div class="vbars"><div class="vbar ext" style="--h:220px"><span>1.4T</span></div></div><div class="vcap">phi-2</div></div>
  <div class="vcol"><div class="vbars"><div class="vbar ext" style="--h:246px"><span>3.3T</span></div></div><div class="vcap">Phi-3-mini</div></div>
  <div class="vcol"><div class="vbars"><div class="vbar ext" style="--h:280px"><span>~10T</span></div></div><div class="vcap">Phi-4</div></div>
</div>
</div>

<!--
- phi-1 was famous for tiny data (7B)
- Later Phi models: trillions of tokens
- "Less data" part did NOT survive; "better data" part did
-->

---

<!-- _class: ext -->

# Phi-4 · student beats teacher

<p class="sub">14B · ~400B synthetic tokens · vs its data generator GPT-4o</p>

<div class="center">
<div class="vchart" style="gap:90px">
  <div class="vcol"><div class="vbars"><div class="vbar ext" style="--h:168px"><span>56.1</span></div><div class="vbar" style="--h:152px"><span>50.6</span></div></div><div class="vcap">GPQA</div></div>
  <div class="vcol"><div class="vbars"><div class="vbar ext" style="--h:241px"><span>80.4</span></div><div class="vbar" style="--h:224px"><span>74.6</span></div></div><div class="vcap">MATH</div></div>
</div>
<div class="legend"><span><i style="background:var(--ext)"></i>Phi-4</span><span><i></i>GPT-4o</span></div>
</div>

<p class="src">Phi-4 Technical Report, Dec 2024</p>

<!--
- Techniques: multi-agent prompting, self-revision, instruction reversal — far beyond phi-1's random-topic trick
- phi-1 paper hinted: on narrow tasks student can beat teacher → here it happens
-->

---

<!-- _class: ext -->

# Phi today · October 2026

<div class="center">
<div class="cards" style="--n:4">
  <div class="card"><div class="k">models</div><div class="t">No Phi-5 yet</div><div class="d">Phi-4 line keeps specializing</div></div>
  <div class="card ext"><div class="k">where</div><div class="t">Windows, Azure, HF</div><div class="d">Phi Silica on-device · MIT weights</div></div>
  <div class="card"><div class="k">people</div><div class="t">Bubeck → OpenAI</div><div class="d">Oct 2024 · most co-authors stayed</div></div>
  <div class="card"><div class="k">Microsoft</div><div class="t">Also MAI models</div><div class="d">in-house large models next to Phi</div></div>
</div>
</div>

<!--
- No announced Phi-5; "Phi-5 guides" online are speculation
- Phi Silica built into Windows Copilot+ PCs (NPU); Azure Foundry; Hugging Face, Ollama
- Sébastien Bubeck (Phi lead, co-author) moved to OpenAI Oct 2024
- Microsoft builds its own MAI frontier models; Phi = small-model track
-->

---

<!-- _class: ext -->

# Impact · “educational value” filters

<p class="sub">FineWeb-Edu (Hugging Face, 2024) · Llama-3-70B labels → classifier → keep score ≥ 3/5</p>

<div class="center">
<div class="vchart" style="gap:90px">
  <div class="vcol"><div class="vbars"><div class="vbar" style="--h:178px"><span>33</span></div><div class="vbar ext" style="--h:200px"><span>37</span></div></div><div class="vcap">MMLU</div></div>
  <div class="vcol"><div class="vbars"><div class="vbar" style="--h:248px"><span>46</span></div><div class="vbar ext" style="--h:300px"><span>57</span></div></div><div class="vcap">ARC</div></div>
</div>
<div class="legend"><span><i></i>FineWeb</span><span><i style="background:var(--ext)"></i>FineWeb-Edu</span></div>
</div>

<p class="src">Penedo et al., 2024 · arXiv 2406.17557</p>

<!--
- Exactly the phi-1 filter idea: LLM labels samples, small classifier scales it up
- Open version — Microsoft never released its classifier/data
- 1.3T tokens kept
- Same technique used in Llama 3 and Phi-3 pretraining (per FineWeb paper)
-->

---

<!-- _class: ext -->

# Impact · synthetic data goes mainstream

<div class="center">
<div class="cards" style="--n:3">
  <div class="card ext"><div class="k">open textbooks</div><div class="t">Cosmopedia → SmolLM</div><div class="d">~25B tokens by Mixtral · data + code released</div></div>
  <div class="card ext"><div class="k">rewrite the web</div><div class="t">rephrase as QA, tutorials</div><div class="d">WRAP · Nemotron-CC · BeyondWeb</div></div>
  <div class="card ext"><div class="k">distillation</div><div class="t">teacher writes the textbook</div><div class="d">GPT-4o → Phi-4 · R1 → small reasoners</div></div>
</div>
</div>

<p class="src">Hugging Face blog 2024 · NVIDIA Nemotron-CC · DatologyAI</p>

<!--
- Cosmopedia: Hugging Face's open reproduction of phi-1.5 data; v2 is the synthetic core of SmolLM
- Rephrasing: middle ground between filtering and generating from scratch; now standard pretraining practice
- 2026 studies: structured formats (tables, FAQs, tutorials) beat curated web → textbook style wins
- Distillation through data: DeepSeek-R1 distilled into Qwen/Llama (Jan 2025), Phi-4-reasoning from o3-mini
- Small models everywhere: Phi-4, Gemma 3, Qwen3, Llama 3.2, SmolLM3 — the data recipe is the moat
-->

---

<!-- _class: ext -->

# Critiques

<div class="center">
<div class="cards" style="--n:3">
  <div class="card"><div class="k">Sep 2023 · parody</div><div class="t">“Pretraining on the Test Set Is All You Need”</div><div class="d">1M-param phi-CTNL “beats everything”</div></div>
  <div class="card"><div class="k">community</div><div class="t">benchmarks ≫ vibes?</div><div class="d">strong scores, weaker in messy real use</div></div>
  <div class="card pink"><div class="k">Nature 2024</div><div class="t">model collapse</div><div class="d">recursive training on own outputs degrades models</div></div>
</div>
</div>

<p class="src">Schaeffer, arXiv 2309.08632 · Shumailov et al., Nature 2024</p>

<!--
- Satire inspired by phi-1.5 — joke about contamination; synthetic data close to benchmark format → suspicion
- Users often report Phi weaker in open-ended chat than benchmarks suggest — matches paper's robustness limits
- Microsoft later: fresh contests (Phi-4), publishing eval logs (2026)
-->

---

<!-- _class: ext -->

# Did the paper's claims hold up?

<div class="center">
<table style="width:1040px">
<tr><th>claim in the paper</th><th>today</th></tr>
<tr><td>data quality bends scaling laws</td><td class="ok">✓ widely accepted</td></tr>
<tr><td>LLM-generated training data works</td><td class="ok">✓ standard practice</td></tr>
<tr><td>LLM-labelled quality filters</td><td class="ok">✓ FineWeb-Edu, Llama 3</td></tr>
<tr><td>tiny data is enough</td><td class="no">✗ Phi now uses trillions</td></tr>
<tr><td>benchmarks reflect real skill</td><td class="meh">~ still debated</td></tr>
</table>
</div>

<!--
- Core message survived and became mainstream
- "Less data" part didn't — quality AND quantity
- Robustness / benchmark trust remains open
- Size still matters (paper's own emergence finding)
-->

---

<!-- _class: statement -->

# Takeaways

<div class="cards" style="--n:3; margin-top:40px">
  <div class="card lime"><div class="k">01</div><div class="t">Data quality is a scaling axis</div></div>
  <div class="card"><div class="k">02</div><div class="t">A small finetune can unlock skills</div></div>
  <div class="card"><div class="k">03</div><div class="t">Check contamination seriously</div></div>
</div>

<!--
- 1: textbook data → 10× smaller, 100× less data
- 2: 180M tokens, 29 → 51%, emergent API use
- 3: new problems, n-grams, pruning — a model for evaluation
- Bonus: the idea is now everywhere (FineWeb-Edu, Phi-4, distillation)
-->

---

<!-- _class: title -->
<!-- _paginate: skip -->

# Thank you

<p class="sub" style="color:#9b93ad">Questions?</p>

---

# Sources

<div class="grid2" style="font-size:20px; margin-top:24px; gap:16px 50px">
  <div><b>Gunasekar et al., 2023</b><br><span class="muted">Textbooks Are All You Need · arXiv:2306.11644</span></div>
  <div><b>Eldan &amp; Li, 2023</b><br><span class="muted">TinyStories · arXiv:2305.07759</span></div>
  <div><b>Kaplan et al., 2020</b><br><span class="muted">Scaling Laws for Neural LMs · arXiv:2001.08361</span></div>
  <div><b>Chen et al., 2021</b><br><span class="muted">Evaluating LLMs Trained on Code · arXiv:2107.03374</span></div>
  <div><span class="tag" style="background:var(--extsoft);color:#a86f00;font-size:13px">web</span> <b>Abdin et al., 2024</b><br><span class="muted">Phi-3 Technical Report · arXiv:2404.14219</span></div>
  <div><span class="tag" style="background:var(--extsoft);color:#a86f00;font-size:13px">web</span> <b>Abdin et al., 2024</b><br><span class="muted">Phi-4 Technical Report · arXiv:2412.08905</span></div>
  <div><span class="tag" style="background:var(--extsoft);color:#a86f00;font-size:13px">web</span> <b>Abdin et al., 2025</b><br><span class="muted">Phi-4-reasoning · arXiv:2504.21318</span></div>
  <div><span class="tag" style="background:var(--extsoft);color:#a86f00;font-size:13px">web</span> <b>Penedo et al., 2024</b><br><span class="muted">The FineWeb Datasets · arXiv:2406.17557</span></div>
  <div><span class="tag" style="background:var(--extsoft);color:#a86f00;font-size:13px">web</span> <b>Hugging Face, 2024</b><br><span class="muted">Cosmopedia blog · huggingface.co/blog/cosmopedia</span></div>
  <div><span class="tag" style="background:var(--extsoft);color:#a86f00;font-size:13px">web</span> <b>Schaeffer, 2023</b><br><span class="muted">Pretraining on the Test Set Is All You Need · arXiv:2309.08632</span></div>
  <div><span class="tag" style="background:var(--extsoft);color:#a86f00;font-size:13px">web</span> <b>Shumailov et al., 2024</b><br><span class="muted">AI models collapse… · Nature 631</span></div>
  <div><span class="tag" style="background:var(--extsoft);color:#a86f00;font-size:13px">web</span> <b>VentureBeat, Mar 2026</b><br><span class="muted">Phi-4-reasoning-vision-15B</span></div>
</div>
