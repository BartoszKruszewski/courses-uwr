---
marp: true
size: 16:9
paginate: true
html: true
title: React
author: Bartosz Kruszewski
style: |
  @import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500&family=Fragment+Mono&display=swap');

  :root {
    --g1: #f4f4f4;
    --g2: #e0e1e4;
    --g3: #a3a5a9;
    --g4: #6f717a;
    --g5: #4f5157;
    --lime: #c7ff9f;
    --green: #2f8a00;
    --violet: #4434fc;
    --lav: #f0f1f9;
    --lav2: #e3e1ff;
    --red: #ff375b;
    --pink: #ffd3db;
    --cyan: #0bb4e0;
    --cyan-t: #d9f6ff;
    --amber: #f08c00;
    --amber-t: #ffefcc;
    --react: #61dafb;
  }

  section {
    font-family: 'Instrument Sans', system-ui, sans-serif;
    background: #fff;
    color: #000;
    font-size: 22px;
    line-height: 1.35;
    padding: 50px 64px 54px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    letter-spacing: -0.005em;
    --acc: var(--violet);
    --acc-t: var(--lav2);
  }
  section.s-hist { --acc: var(--amber); --acc-t: var(--amber-t); }
  section.s-fund { --acc: var(--violet); --acc-t: var(--lav2); }
  section.s-eco  { --acc: var(--cyan); --acc-t: var(--cyan-t); }
  section.s-mkt  { --acc: var(--red); --acc-t: var(--pink); }
  section.s-big  { --acc: var(--green); --acc-t: var(--lime); }
  section.s-fut  { --acc: var(--violet); --acc-t: var(--lav2); }

  section h1 {
    font-size: 46px; font-weight: 400; color: #000;
    margin: 0; padding: 0; border: none;
    letter-spacing: -0.02em; line-height: 1.1;
  }
  .sub { color: var(--g4); font-size: 19px; margin-top: 10px; display: flex; align-items: center; gap: 10px; }
  .mono, code, pre { font-family: 'Fragment Mono', ui-monospace, monospace; }
  .muted { color: var(--g4); }
  .src { position: absolute; left: 64px; bottom: 22px; font-size: 14px; color: var(--g4); }

  section::after {
    font-family: 'Fragment Mono', monospace;
    font-size: 14px; color: var(--g3);
    right: 64px; bottom: 22px;
  }
  header {
    font-family: 'Fragment Mono', monospace;
    font-size: 14px; color: var(--g4);
    top: 24px; left: auto; right: 64px;
    display: flex; align-items: center; gap: 8px;
  }
  header::before { content: ''; width: 9px; height: 9px; border-radius: 50%; background: var(--acc); }

  /* Ikony (Lucide jako maski) */
  .ic { display: inline-block; width: 22px; height: 22px; background: currentColor; vertical-align: middle; flex-shrink: 0;
        -webkit-mask: var(--i) center / contain no-repeat; mask: var(--i) center / contain no-repeat; }
  .i-atom { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-atom%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Ccircle cx=%2212%22 cy=%2212%22 r=%221%22 /%3E %3Cpath d=%22M20.2 20.2c2.04-2.03.02-7.36-4.5-11.9-4.54-4.52-9.87-6.54-11.9-4.5-2.04 2.03-.02 7.36 4.5 11.9 4.54 4.52 9.87 6.54 11.9 4.5Z%22 /%3E %3Cpath d=%22M15.7 15.7c4.52-4.54 6.54-9.87 4.5-11.9-2.03-2.04-7.36-.02-11.9 4.5-4.52 4.54-6.54 9.87-4.5 11.9 2.03 2.04 7.36.02 11.9-4.5Z%22 /%3E %3C/svg%3E"); }
  .i-blocks { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-blocks%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Crect width=%227%22 height=%227%22 x=%2214%22 y=%223%22 rx=%221%22 /%3E %3Cpath d=%22M10 21V8a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-5a1 1 0 0 0-1-1H3%22 /%3E %3C/svg%3E"); }
  .i-box { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-box%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z%22 /%3E %3Cpath d=%22m3.3 7 8.7 5 8.7-5%22 /%3E %3Cpath d=%22M12 22V12%22 /%3E %3C/svg%3E"); }
  .i-bug { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-bug%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22m8 2 1.88 1.88%22 /%3E %3Cpath d=%22M14.12 3.88 16 2%22 /%3E %3Cpath d=%22M9 7.13v-1a3.003 3.003 0 1 1 6 0v1%22 /%3E %3Cpath d=%22M12 20c-3.3 0-6-2.7-6-6v-3a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v3c0 3.3-2.7 6-6 6%22 /%3E %3Cpath d=%22M12 20v-9%22 /%3E %3Cpath d=%22M6.53 9C4.6 8.8 3 7.1 3 5%22 /%3E %3Cpath d=%22M6 13H2%22 /%3E %3Cpath d=%22M3 21c0-2.1 1.7-3.9 3.8-4%22 /%3E %3Cpath d=%22M20.97 5c0 2.1-1.6 3.8-3.5 4%22 /%3E %3Cpath d=%22M22 13h-4%22 /%3E %3Cpath d=%22M17.2 17c2.1.1 3.8 1.9 3.8 4%22 /%3E %3C/svg%3E"); }
  .i-building-2 { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-building-2%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z%22 /%3E %3Cpath d=%22M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2%22 /%3E %3Cpath d=%22M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2%22 /%3E %3Cpath d=%22M10 6h4%22 /%3E %3Cpath d=%22M10 10h4%22 /%3E %3Cpath d=%22M10 14h4%22 /%3E %3Cpath d=%22M10 18h4%22 /%3E %3C/svg%3E"); }
  .i-calendar { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-calendar%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M8 2v4%22 /%3E %3Cpath d=%22M16 2v4%22 /%3E %3Crect width=%2218%22 height=%2218%22 x=%223%22 y=%224%22 rx=%222%22 /%3E %3Cpath d=%22M3 10h18%22 /%3E %3C/svg%3E"); }
  .i-check { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-check%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M20 6 9 17l-5-5%22 /%3E %3C/svg%3E"); }
  .i-clock { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-clock%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Ccircle cx=%2212%22 cy=%2212%22 r=%2210%22 /%3E %3Cpolyline points=%2212 6 12 12 16 14%22 /%3E %3C/svg%3E"); }
  .i-code-xml { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-code-xml%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22m18 16 4-4-4-4%22 /%3E %3Cpath d=%22m6 8-4 4 4 4%22 /%3E %3Cpath d=%22m14.5 4-5 16%22 /%3E %3C/svg%3E"); }
  .i-cpu { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-cpu%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Crect width=%2216%22 height=%2216%22 x=%224%22 y=%224%22 rx=%222%22 /%3E %3Crect width=%226%22 height=%226%22 x=%229%22 y=%229%22 rx=%221%22 /%3E %3Cpath d=%22M15 2v2%22 /%3E %3Cpath d=%22M15 20v2%22 /%3E %3Cpath d=%22M2 15h2%22 /%3E %3Cpath d=%22M2 9h2%22 /%3E %3Cpath d=%22M20 15h2%22 /%3E %3Cpath d=%22M20 9h2%22 /%3E %3Cpath d=%22M9 2v2%22 /%3E %3Cpath d=%22M9 20v2%22 /%3E %3C/svg%3E"); }
  .i-database { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-database%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cellipse cx=%2212%22 cy=%225%22 rx=%229%22 ry=%223%22 /%3E %3Cpath d=%22M3 5V19A9 3 0 0 0 21 19V5%22 /%3E %3Cpath d=%22M3 12A9 3 0 0 0 21 12%22 /%3E %3C/svg%3E"); }
  .i-download { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-download%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4%22 /%3E %3Cpolyline points=%227 10 12 15 17 10%22 /%3E %3Cline x1=%2212%22 x2=%2212%22 y1=%2215%22 y2=%223%22 /%3E %3C/svg%3E"); }
  .i-file-input { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-file-input%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M4 22h14a2 2 0 0 0 2-2V7l-5-5H6a2 2 0 0 0-2 2v4%22 /%3E %3Cpath d=%22M14 2v4a2 2 0 0 0 2 2h4%22 /%3E %3Cpath d=%22M2 15h10%22 /%3E %3Cpath d=%22m9 18 3-3-3-3%22 /%3E %3C/svg%3E"); }
  .i-flame { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-flame%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z%22 /%3E %3C/svg%3E"); }
  .i-folder-tree { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-folder-tree%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M20 10a1 1 0 0 0 1-1V6a1 1 0 0 0-1-1h-2.5a1 1 0 0 1-.8-.4l-.9-1.2A1 1 0 0 0 15 3h-2a1 1 0 0 0-1 1v5a1 1 0 0 0 1 1Z%22 /%3E %3Cpath d=%22M20 21a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1h-2.9a1 1 0 0 1-.88-.55l-.42-.85a1 1 0 0 0-.92-.6H13a1 1 0 0 0-1 1v5a1 1 0 0 0 1 1Z%22 /%3E %3Cpath d=%22M3 5a2 2 0 0 0 2 2h3%22 /%3E %3Cpath d=%22M3 3v13a2 2 0 0 0 2 2h3%22 /%3E %3C/svg%3E"); }
  .i-gauge { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-gauge%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22m12 14 4-4%22 /%3E %3Cpath d=%22M3.34 19a10 10 0 1 1 17.32 0%22 /%3E %3C/svg%3E"); }
  .i-git-branch { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-git-branch%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cline x1=%226%22 x2=%226%22 y1=%223%22 y2=%2215%22 /%3E %3Ccircle cx=%2218%22 cy=%226%22 r=%223%22 /%3E %3Ccircle cx=%226%22 cy=%2218%22 r=%223%22 /%3E %3Cpath d=%22M18 9a9 9 0 0 1-9 9%22 /%3E %3C/svg%3E"); }
  .i-github { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-github%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4%22 /%3E %3Cpath d=%22M9 18c-4.51 2-5-2-7-2%22 /%3E %3C/svg%3E"); }
  .i-globe { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-globe%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Ccircle cx=%2212%22 cy=%2212%22 r=%2210%22 /%3E %3Cpath d=%22M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20%22 /%3E %3Cpath d=%22M2 12h20%22 /%3E %3C/svg%3E"); }
  .i-heart { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-heart%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z%22 /%3E %3C/svg%3E"); }
  .i-history { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-history%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8%22 /%3E %3Cpath d=%22M3 3v5h5%22 /%3E %3Cpath d=%22M12 7v5l4 2%22 /%3E %3C/svg%3E"); }
  .i-layers { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-layers%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z%22 /%3E %3Cpath d=%22m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65%22 /%3E %3Cpath d=%22m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65%22 /%3E %3C/svg%3E"); }
  .i-layout-dashboard { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-layout-dashboard%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Crect width=%227%22 height=%229%22 x=%223%22 y=%223%22 rx=%221%22 /%3E %3Crect width=%227%22 height=%225%22 x=%2214%22 y=%223%22 rx=%221%22 /%3E %3Crect width=%227%22 height=%229%22 x=%2214%22 y=%2212%22 rx=%221%22 /%3E %3Crect width=%227%22 height=%225%22 x=%223%22 y=%2216%22 rx=%221%22 /%3E %3C/svg%3E"); }
  .i-lightbulb { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-lightbulb%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5%22 /%3E %3Cpath d=%22M9 18h6%22 /%3E %3Cpath d=%22M10 22h4%22 /%3E %3C/svg%3E"); }
  .i-lock { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-lock%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Crect width=%2218%22 height=%2211%22 x=%223%22 y=%2211%22 rx=%222%22 ry=%222%22 /%3E %3Cpath d=%22M7 11V7a5 5 0 0 1 10 0v4%22 /%3E %3C/svg%3E"); }
  .i-monitor { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-monitor%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Crect width=%2220%22 height=%2214%22 x=%222%22 y=%223%22 rx=%222%22 /%3E %3Cline x1=%228%22 x2=%2216%22 y1=%2221%22 y2=%2221%22 /%3E %3Cline x1=%2212%22 x2=%2212%22 y1=%2217%22 y2=%2221%22 /%3E %3C/svg%3E"); }
  .i-network { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-network%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Crect x=%2216%22 y=%2216%22 width=%226%22 height=%226%22 rx=%221%22 /%3E %3Crect x=%222%22 y=%2216%22 width=%226%22 height=%226%22 rx=%221%22 /%3E %3Crect x=%229%22 y=%222%22 width=%226%22 height=%226%22 rx=%221%22 /%3E %3Cpath d=%22M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3%22 /%3E %3Cpath d=%22M12 12V8%22 /%3E %3C/svg%3E"); }
  .i-package { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-package%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73z%22 /%3E %3Cpath d=%22M12 22V12%22 /%3E %3Cpath d=%22m3.3 7 7.703 4.734a2 2 0 0 0 1.994 0L20.7 7%22 /%3E %3Cpath d=%22m7.5 4.27 9 5.15%22 /%3E %3C/svg%3E"); }
  .i-palette { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-palette%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Ccircle cx=%2213.5%22 cy=%226.5%22 r=%22.5%22 fill=%22black%22 /%3E %3Ccircle cx=%2217.5%22 cy=%2210.5%22 r=%22.5%22 fill=%22black%22 /%3E %3Ccircle cx=%228.5%22 cy=%227.5%22 r=%22.5%22 fill=%22black%22 /%3E %3Ccircle cx=%226.5%22 cy=%2212.5%22 r=%22.5%22 fill=%22black%22 /%3E %3Cpath d=%22M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.554C21.965 6.012 17.461 2 12 2z%22 /%3E %3C/svg%3E"); }
  .i-puzzle { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-puzzle%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M15.39 4.39a1 1 0 0 0 1.68-.474 2.5 2.5 0 1 1 3.014 3.015 1 1 0 0 0-.474 1.68l1.683 1.682a2.414 2.414 0 0 1 0 3.414L19.61 15.39a1 1 0 0 1-1.68-.474 2.5 2.5 0 1 0-3.014 3.015 1 1 0 0 1 .474 1.68l-1.683 1.682a2.414 2.414 0 0 1-3.414 0L8.61 19.61a1 1 0 0 0-1.68.474 2.5 2.5 0 1 1-3.014-3.015 1 1 0 0 0 .474-1.68l-1.683-1.682a2.414 2.414 0 0 1 0-3.414L4.39 8.61a1 1 0 0 1 1.68.474 2.5 2.5 0 1 0 3.014-3.015 1 1 0 0 1-.474-1.68l1.683-1.682a2.414 2.414 0 0 1 3.414 0z%22 /%3E %3C/svg%3E"); }
  .i-rocket { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-rocket%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z%22 /%3E %3Cpath d=%22m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z%22 /%3E %3Cpath d=%22M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0%22 /%3E %3Cpath d=%22M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5%22 /%3E %3C/svg%3E"); }
  .i-server { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-server%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Crect width=%2220%22 height=%228%22 x=%222%22 y=%222%22 rx=%222%22 ry=%222%22 /%3E %3Crect width=%2220%22 height=%228%22 x=%222%22 y=%2214%22 rx=%222%22 ry=%222%22 /%3E %3Cline x1=%226%22 x2=%226.01%22 y1=%226%22 y2=%226%22 /%3E %3Cline x1=%226%22 x2=%226.01%22 y1=%2218%22 y2=%2218%22 /%3E %3C/svg%3E"); }
  .i-shield-alert { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-shield-alert%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z%22 /%3E %3Cpath d=%22M12 8v4%22 /%3E %3Cpath d=%22M12 16h.01%22 /%3E %3C/svg%3E"); }
  .i-smartphone { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-smartphone%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Crect width=%2214%22 height=%2220%22 x=%225%22 y=%222%22 rx=%222%22 ry=%222%22 /%3E %3Cpath d=%22M12 18h.01%22 /%3E %3C/svg%3E"); }
  .i-sparkles { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-sparkles%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z%22 /%3E %3Cpath d=%22M20 3v4%22 /%3E %3Cpath d=%22M22 5h-4%22 /%3E %3Cpath d=%22M4 17v2%22 /%3E %3Cpath d=%22M5 18H3%22 /%3E %3C/svg%3E"); }
  .i-star { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-star%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z%22 /%3E %3C/svg%3E"); }
  .i-trending-up { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-trending-up%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpolyline points=%2222 7 13.5 15.5 8.5 10.5 2 17%22 /%3E %3Cpolyline points=%2216 7 22 7 22 13%22 /%3E %3C/svg%3E"); }
  .i-users { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-users%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2%22 /%3E %3Ccircle cx=%229%22 cy=%227%22 r=%224%22 /%3E %3Cpath d=%22M22 21v-2a4 4 0 0 0-3-3.87%22 /%3E %3Cpath d=%22M16 3.13a4 4 0 0 1 0 7.75%22 /%3E %3C/svg%3E"); }
  .i-wand-sparkles { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-wand-sparkles%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22m21.64 3.64-1.28-1.28a1.21 1.21 0 0 0-1.72 0L2.36 18.64a1.21 1.21 0 0 0 0 1.72l1.28 1.28a1.2 1.2 0 0 0 1.72 0L21.64 5.36a1.2 1.2 0 0 0 0-1.72%22 /%3E %3Cpath d=%22m14 7 3 3%22 /%3E %3Cpath d=%22M5 6v4%22 /%3E %3Cpath d=%22M19 14v4%22 /%3E %3Cpath d=%22M10 2v2%22 /%3E %3Cpath d=%22M7 8H3%22 /%3E %3Cpath d=%22M21 16h-4%22 /%3E %3Cpath d=%22M11 3H9%22 /%3E %3C/svg%3E"); }
  .i-workflow { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-workflow%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Crect width=%228%22 height=%228%22 x=%223%22 y=%223%22 rx=%222%22 /%3E %3Cpath d=%22M7 11v4a2 2 0 0 0 2 2h4%22 /%3E %3Crect width=%228%22 height=%228%22 x=%2213%22 y=%2213%22 rx=%222%22 /%3E %3C/svg%3E"); }
  .i-x { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-x%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M18 6 6 18%22 /%3E %3Cpath d=%22m6 6 12 12%22 /%3E %3C/svg%3E"); }
  .i-zap { --i: url("data:image/svg+xml,%3Csvg class=%22lucide lucide-zap%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22black%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 %3E %3Cpath d=%22M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z%22 /%3E %3C/svg%3E"); }
  .tile { width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center;
          background: var(--acc-t); color: var(--acc); flex-shrink: 0; }
  .tile .ic { width: 26px; height: 26px; }
  .tile.sm { width: 40px; height: 40px; border-radius: 10px; }
  .tile.sm .ic { width: 21px; height: 21px; }
  .t-v { background: var(--lav2); color: var(--violet); }
  .t-c { background: var(--cyan-t); color: var(--cyan); }
  .t-r { background: var(--pink); color: var(--red); }
  .t-g { background: var(--lime); color: var(--green); }
  .t-a { background: var(--amber-t); color: var(--amber); }
  .t-k { background: #000; color: #fff; }
  .t-w { background: #fff; color: #000; }

  /* Logotypy */
  .lg { height: 30px; width: auto; vertical-align: middle; flex-shrink: 0; }
  .lg.s { height: 22px; } .lg.m { height: 40px; } .lg.l { height: 56px; }
  .logos { display: flex; gap: 12px; align-items: center; min-height: 40px; }
  .ms { display: inline-grid; grid-template-columns: 1fr 1fr; gap: 2px; width: 26px; height: 26px; vertical-align: middle; flex-shrink: 0; }
  .ms.s { width: 20px; height: 20px; }
  .ms.l { width: 36px; height: 36px; gap: 3px; }
  .ms i:nth-child(1) { background: #f25022; } .ms i:nth-child(2) { background: #7fba00; }
  .ms i:nth-child(3) { background: #00a4ef; } .ms i:nth-child(4) { background: #ffb900; }

  /* Układ */
  section *, section *::before { box-sizing: border-box; }
  .zoom { zoom: 1.3; } .zoom-s { zoom: 1.15; }
  .fill { flex: 1; display: flex; align-items: center; justify-content: center; width: 100%; }
  .col { display: flex; flex-direction: column; gap: 14px; }
  .row { display: flex; gap: 16px; align-items: center; }
  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; width: 100%; }
  .grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; width: 100%; }
  .grid4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; width: 100%; }

  /* Karty */
  .card { background: var(--g1); border-radius: 14px; padding: 24px 26px; }
  .card .t { font-size: 25px; line-height: 1.2; margin-bottom: 8px; }
  .card .d { font-size: 18px; color: var(--g5); line-height: 1.4; }
  .card .n { font-family: 'Fragment Mono', monospace; font-size: 15px; color: var(--g4); margin-bottom: 6px; }
  .card .tile { margin-bottom: 22px; }
  .hcard { display: flex; gap: 18px; align-items: flex-start; }
  .hcard .tile { margin: 0; }
  .lime { background: var(--lime) !important; }
  .lav2 { background: var(--lav2) !important; }
  .pink { background: var(--pink) !important; }
  .cyan { background: var(--cyan-t) !important; }
  .amber { background: var(--amber-t) !important; }
  .dark { background: #000 !important; color: #fff !important; }
  .dark .m { color: var(--g3) !important; }
  .outline { background: #fff; border: 1.5px solid #000; }

  .box { background: var(--g1); border-radius: 10px; padding: 13px 18px; font-size: 20px; text-align: center; }
  .box .m { font-family: 'Fragment Mono', monospace; font-size: 15px; color: var(--g4); display: block; margin-top: 3px; }
  .box.l { text-align: left; display: flex; align-items: center; gap: 12px; }
  .arrow { color: var(--g3); font-size: 26px; display: flex; align-items: center; justify-content: center; }
  .chip { display: inline-flex; align-items: center; gap: 8px; background: var(--g1); border-radius: 8px; padding: 8px 14px; font-size: 18px; }
  .chip .ic { width: 18px; height: 18px; }
  .chips { display: flex; flex-wrap: wrap; gap: 10px; }
  .lbl { font-family: 'Fragment Mono', monospace; font-size: 15px; color: var(--g4); margin-bottom: 12px; display: flex; align-items: center; gap: 10px; }
  .lbl .ic { width: 18px; height: 18px; }

  /* Kod */
  pre {
    background: var(--g1) !important; border-radius: 14px; padding: 22px 26px !important;
    font-size: 18px; line-height: 1.55; color: #000; margin: 0; border: none;
  }
  pre code { background: none; font-size: inherit; padding: 0; }
  code { background: var(--g1); border-radius: 5px; padding: 1px 6px; font-size: 0.85em; color: #000; }
  .hljs-comment { color: var(--g3) !important; font-style: normal; }
  .hljs-keyword, .hljs-built_in, .hljs-literal { color: var(--violet) !important; }
  .hljs-string { color: #b8325a !important; }
  .hljs-attr, .hljs-number { color: #0a8bb0 !important; }
  .hljs-title, .hljs-name, .hljs-tag, .hljs-attribute, .hljs-variable, .hljs-params, .hljs-property { color: #000 !important; }

  /* Wykresy */
  .hbars { display: grid; grid-template-columns: 250px 1fr 84px; gap: 12px 18px; align-items: center; width: 100%; font-size: 20px; }
  .hbars .lab { display: flex; align-items: center; gap: 12px; }
  .hbars .lab .lg { width: 24px; height: 24px; object-fit: contain; }
  .hbars .bar { height: 30px; background: var(--g2); border-radius: 4px; }
  .hbars .bar.k { background: #000; }
  .hbars .bar.v { background: var(--violet); }
  .hbars .bar.c { background: var(--cyan); }
  .hbars .bar.r { background: var(--react); }
  .hbars .val { font-family: 'Fragment Mono', monospace; font-size: 18px; color: var(--g5); }
  .dot { display: inline-block; width: 13px; height: 13px; border-radius: 3px; vertical-align: middle; margin-right: 8px; }
  .legend { display: flex; gap: 28px; font-size: 17px; color: var(--g5); }

  /* Tabela */
  section table { border-collapse: collapse; width: 100%; font-size: 21px; display: table; }
  section table th, section table td { border-left: none !important; border-right: none !important; border-top: none; }
  th { font-weight: 400; color: var(--g4); font-size: 16px; text-align: left; padding: 10px 14px; border-bottom: 1.5px solid var(--g2); background: none; }
  td { padding: 14px 14px; border-bottom: 1px solid var(--g2); background: none !important; }
  tr { background: none !important; }
  .pill { display: inline-block; font-family: 'Fragment Mono', monospace; font-size: 18px; padding: 4px 12px; border-radius: 8px; }

  /* Slajdy czarne */
  section.black {
    background: radial-gradient(circle at 76% 50%, rgba(97,218,251,.16), rgba(68,52,252,.06) 30%, transparent 52%), #000;
    color: #fff; justify-content: space-between; padding: 54px 64px;
  }
  section.black h1, section.black .h1 { color: #fff; font-size: 150px; font-weight: 400; letter-spacing: -0.045em; line-height: .95; margin: 0; }
  .orbit { position: absolute; left: 955px; top: 360px; width: 0; height: 0; }
  .orbit .ring { position: absolute; border-radius: 50%; border: 1.5px solid rgba(255,255,255,.09); transform: translate(-50%, -50%); }
  .orbit .ring.d { border-style: dashed; border-color: rgba(255,255,255,.14); }
  .orbit .core { position: absolute; max-width: none; width: auto; transform: translate(-50%, -50%); filter: drop-shadow(0 0 36px rgba(97,218,251,.55)); }
  .orbit .pl { position: absolute; width: 16px; height: 16px; margin: -8px 0 0 -8px; border-radius: 50%; }
  .tsub { font-size: 27px; line-height: 1.35; color: #c9cbd1; margin-top: 26px; }
  .tags { display: grid; grid-template-columns: repeat(3, auto); justify-content: start; gap: 12px 34px; margin-top: 34px; font-family: 'Fragment Mono', monospace; font-size: 15px; color: #a3a5a9; max-width: 640px; }
  .tags span { display: inline-flex; align-items: center; gap: 8px; }
  .tags i { width: 9px; height: 9px; border-radius: 50%; display: inline-block; }
  .foot { display: flex; align-items: center; gap: 20px; border-top: 1px solid rgba(255,255,255,.14); padding-top: 22px; width: 560px; font-size: 20px; }
  .foot .m { font-family: 'Fragment Mono', monospace; font-size: 15px; color: #a3a5a9; }
  .bstat { font-family: 'Fragment Mono', monospace; font-size: 40px; letter-spacing: -0.03em; }
  .bstat small { display: block; font-family: 'Instrument Sans', sans-serif; font-size: 16px; color: #a3a5a9; letter-spacing: 0; margin-top: 4px; }
  .src-card { background: var(--g1); border-radius: 14px; padding: 18px 22px; display: flex; gap: 18px; align-items: center; }
  .src-card .tile { margin: 0; }
  .src-card .t { font-size: 21px; line-height: 1.2; }
  .src-card .u { font-family: 'Fragment Mono', monospace; font-size: 15px; color: var(--g4); margin-top: 4px; }
  section.black::after { display: none; }
  .label-lime { color: var(--lime); font-size: 18px; }
  .who { font-size: 20px; color: #fff; }
  .who span { color: var(--g3); margin-left: 18px; }

  .stat .big { font-family: 'Fragment Mono', monospace; font-size: 64px; letter-spacing: -0.04em; line-height: 1.1; margin-top: 20px; }
  .stat .lab { font-size: 18px; color: var(--g5); margin-top: 6px; }
---

<!-- _class: black -->
<!-- _paginate: false -->

<div class="orbit">
  <div class="ring" style="width:580px; height:580px"></div>
  <div class="ring d" style="width:450px; height:450px"></div>
  <div class="ring" style="width:310px; height:310px; border-color:rgba(97,218,251,.25)"></div>
  <span class="pl" style="background:var(--lime); transform:rotate(-38deg) translateX(290px)"></span>
  <span class="pl" style="background:var(--violet); transform:rotate(152deg) translateX(290px)"></span>
  <span class="pl" style="background:var(--amber); width:12px; height:12px; transform:rotate(68deg) translateX(225px)"></span>
  <span class="pl" style="background:var(--red); width:12px; height:12px; transform:rotate(-120deg) translateX(225px)"></span>
  <span class="pl" style="background:var(--cyan); width:10px; height:10px; transform:rotate(15deg) translateX(155px)"></span>
  <img class="core" src="assets/logos/react.svg" style="height:230px">
</div>

<div class="label-lime">Seminarium: Implementacja Interfejsów Użytkownika</div>

<div>
  <div class="h1">React</div>
</div>

<div class="foot">Bartosz Kruszewski<span class="m">2026</span></div>

<!--
- Przedstawiam się, temat: React – biblioteka do budowania interfejsów.
- Nie będzie live codingu – zamiast tego przegląd: skąd się wziął, jak działa, z czym się go używa, gdzie jest na rynku i dokąd zmierza.
- Ok. 45 minut, pytania najlepiej na koniec.
-->

---

# Plan

<div class="fill">
<div class="grid3">
  <div class="card"><div class="tile t-a"><span class="ic i-history"></span></div><div class="n">01</div><div class="t">Historia</div><div class="d">skąd się wziął i dlaczego</div></div>
  <div class="card"><div class="tile t-v"><span class="ic i-blocks"></span></div><div class="n">02</div><div class="t">Fundamenty</div><div class="d">komponenty, stan, hooki, React 19</div></div>
  <div class="card"><div class="tile t-c"><span class="ic i-puzzle"></span></div><div class="n">03</div><div class="t">Ekosystem</div><div class="d">biblioteki używane razem z Reactem</div></div>
  <div class="card"><div class="tile t-r"><span class="ic i-trending-up"></span></div><div class="n">04</div><div class="t">Rynek</div><div class="d">kto używa, do czego, zalety i wady</div></div>
  <div class="card"><div class="tile t-g"><span class="ic i-building-2"></span></div><div class="n">05</div><div class="t">Duże aplikacje</div><div class="d">architektura i praktyki w produkcji</div></div>
  <div class="card"><div class="tile t-k"><span class="ic i-sparkles"></span></div><div class="n">06</div><div class="t">Społeczność i przyszłość</div><div class="d">React Foundation, 19.3 i dalej</div></div>
</div>
</div>

<!--
- Sześć części, w tej kolejności.
- Najpierw krótko historia, bo wyjaśnia, DLACZEGO React wygląda tak, a nie inaczej.
- Potem najważniejsze koncepcje, ekosystem, rynek, praktyka w dużych projektach, społeczność i przyszłość.
-->

---

<!-- header: 01 · Historia -->
<!-- class: s-hist -->

# Facebook, 2011

<div class="sub"><img class="lg s" src="assets/logos/facebook.svg"> jedna zmiana danych → wiele ręcznych poprawek w DOM</div>

<div class="fill">
<div class="row" style="gap:36px">
  <div class="card amber" style="width:270px; text-align:center; padding:34px 24px">
    <div class="tile t-w" style="margin:0 auto 18px"><span class="ic i-bug" style="color:var(--amber)"></span></div>
    <div class="t">Nowa wiadomość</div>
    <div class="mono muted" style="font-size:16px">model.unread++</div>
  </div>
  <div class="arrow">→</div>
  <div class="col" style="gap:12px; width:700px">
    <div class="row"><div class="box l" style="flex:1">licznik w pasku nawigacji</div><span class="mono row" style="gap:8px; width:230px; font-size:18px; color:var(--green)"><span class="ic i-check"></span>zaktualizowany</span></div>
    <div class="row"><div class="box l" style="flex:1">lista czatów</div><span class="mono row" style="gap:8px; width:230px; font-size:18px; color:var(--green)"><span class="ic i-check"></span>zaktualizowana</span></div>
    <div class="row"><div class="box l" style="flex:1">tytuł karty przeglądarki</div><span class="mono row" style="gap:8px; width:230px; font-size:18px; color:var(--green)"><span class="ic i-check"></span>zaktualizowany</span></div>
    <div class="row"><div class="box l pink" style="flex:1">okno czatu</div><span class="mono row" style="gap:8px; width:230px; font-size:18px; color:var(--red)"><span class="ic i-x"></span>zapomniany</span></div>
  </div>
</div>
</div>

<!--
- Facebook ok. 2011: coraz bardziej interaktywny – czat, powiadomienia, News Feed, reklamy.
- Kod był imperatywny (jQuery-styl): przy każdej zmianie danych trzeba było ręcznie znaleźć i poprawić każde miejsce w DOM.
- Słynny bug: licznik nieprzeczytanych wiadomości pokazywał 1, a wiadomości nie było – wracał co chwilę.
- Wniosek: przy rosnącej liczbie miejsc zależnych od stanu ręczna synchronizacja się nie skaluje.
-->

---

# Od XHP do Reacta

<div class="sub">Jordan Walke, inżynier Facebooka</div>

<div class="fill">
<div class="row" style="gap:20px; align-items:stretch">
  <div class="card" style="width:330px"><img class="lg l" src="assets/logos/php.svg" style="margin-bottom:24px"><div class="n">2010</div><div class="t">XHP</div><div class="d">rozszerzenie PHP: komponenty i znaczniki HTML wprost w kodzie serwera</div></div>
  <div class="arrow">→</div>
  <div class="card" style="width:330px"><img class="lg l" src="assets/logos/javascript.svg" style="margin-bottom:24px"><div class="n">2011</div><div class="t">FaxJS</div><div class="d">ta sama idea w przeglądarce: przy zmianie stanu „renderuj wszystko od nowa”</div></div>
  <div class="arrow">→</div>
  <div class="card cyan" style="width:330px"><div class="logos" style="margin-bottom:24px"><img class="lg l" src="assets/logos/react.svg"><img class="lg m" src="assets/logos/instagram.svg"></div><div class="n">2011–2012</div><div class="t">React</div><div class="d">News Feed na Facebooku, potem Instagram jako pierwszy duży użytkownik</div></div>
</div>
</div>

<!--
- Inspiracja: XHP – w PHP Facebook już pisał komponenty jako znaczniki, a strona była po prostu renderowana od nowa przy każdym żądaniu.
- Jordan Walke przeniósł ten model do przeglądarki: prototyp FaxJS.
- Kluczowa idea: zamiast łatać DOM, wygeneruj opis całego UI na nowo i niech biblioteka sama znajdzie różnice.
- Pierwsze wdrożenie: News Feed (2011), potem Instagram – to Instagram wymusił wydzielenie Reacta z kodu Facebooka.
-->

---

# Oś czasu

<div class="fill">
<div style="width:100%">
  <div style="display:grid; grid-template-columns:repeat(9,1fr); justify-items:center; margin-bottom:22px">
    <div class="tile t-a"><span class="ic i-lightbulb"></span></div>
    <div class="tile t-k"><span class="ic i-github"></span></div>
    <div class="tile t-c"><span class="ic i-smartphone"></span></div>
    <div class="tile t-a"><span class="ic i-cpu"></span></div>
    <div class="tile t-v"><span class="ic i-atom"></span></div>
    <div class="tile t-c"><span class="ic i-zap"></span></div>
    <div class="tile t-v"><span class="ic i-server"></span></div>
    <div class="tile t-g"><span class="ic i-wand-sparkles"></span></div>
    <div class="tile t-r"><span class="ic i-users"></span></div>
  </div>
  <div style="height:4px; background:linear-gradient(90deg, var(--amber), var(--cyan), var(--violet), var(--green), var(--red)); margin:0 60px; border-radius:2px"></div>
  <div style="display:grid; grid-template-columns:repeat(9,1fr); margin-top:-10px; text-align:center">
    <div><div style="width:16px;height:16px;border-radius:50%;background:var(--amber);margin:0 auto"></div><div class="mono" style="margin-top:18px; font-size:22px">2011</div><div style="margin-top:8px; font-size:18px">FaxJS</div><div class="muted" style="font-size:16px">News Feed</div></div>
    <div><div style="width:16px;height:16px;border-radius:50%;background:#000;margin:0 auto"></div><div class="mono" style="margin-top:18px; font-size:22px">2013</div><div style="margin-top:8px; font-size:18px">open source</div><div class="muted" style="font-size:16px">JSConf US</div></div>
    <div><div style="width:16px;height:16px;border-radius:50%;background:var(--cyan);margin:0 auto"></div><div class="mono" style="margin-top:18px; font-size:22px">2015</div><div style="margin-top:8px; font-size:18px">React Native</div><div class="muted" style="font-size:16px">i Redux</div></div>
    <div><div style="width:16px;height:16px;border-radius:50%;background:var(--amber);margin:0 auto"></div><div class="mono" style="margin-top:18px; font-size:22px">2017</div><div style="margin-top:8px; font-size:18px">Fiber</div><div class="muted" style="font-size:16px">licencja MIT</div></div>
    <div><div style="width:16px;height:16px;border-radius:50%;background:var(--violet);margin:0 auto"></div><div class="mono" style="margin-top:18px; font-size:22px">2019</div><div style="margin-top:8px; font-size:18px">Hooki</div><div class="muted" style="font-size:16px">React 16.8</div></div>
    <div><div style="width:16px;height:16px;border-radius:50%;background:var(--cyan);margin:0 auto"></div><div class="mono" style="margin-top:18px; font-size:22px">2022</div><div style="margin-top:8px; font-size:18px">Concurrent</div><div class="muted" style="font-size:16px">React 18</div></div>
    <div><div style="width:16px;height:16px;border-radius:50%;background:var(--violet);margin:0 auto"></div><div class="mono" style="margin-top:18px; font-size:22px">2024</div><div style="margin-top:8px; font-size:18px">Server Comp.</div><div class="muted" style="font-size:16px">React 19</div></div>
    <div><div style="width:16px;height:16px;border-radius:50%;background:var(--green);margin:0 auto"></div><div class="mono" style="margin-top:18px; font-size:22px">2025</div><div style="margin-top:8px; font-size:18px">Compiler 1.0</div><div class="muted" style="font-size:16px">koniec CRA</div></div>
    <div><div style="width:16px;height:16px;border-radius:50%;background:var(--red);margin:0 auto"></div><div class="mono" style="margin-top:18px; font-size:22px">2026</div><div style="margin-top:8px; font-size:18px">Fundacja</div><div class="muted" style="font-size:16px">React 19.3</div></div>
  </div>
</div>
</div>

<!--
- 15 lat w jednym slajdzie. Fioletowe punkty = dwa największe przełomy w sposobie pisania kodu: hooki i Server Components.
- 2017: oprócz przepisania silnika (Fiber) zmiana licencji z BSD+Patents na MIT – po buncie społeczności (m.in. Apache Foundation i WordPress zapowiedzieli odejście).
- 2025: Create React App oficjalnie wygaszony, React Compiler stabilny.
- 2026: React przechodzi pod Linux Foundation, we wrześniu wychodzi 19.3.
-->

---

# 2013: „Rethinking Best Practices”

<div class="sub">JSConf US – JSX budził sprzeciw: „HTML w JavaScripcie to krok wstecz”</div>

<div class="fill">
<div class="grid2" style="gap:60px">
  <div>
    <div class="lbl">separacja technologii</div>
    <div class="row" style="gap:12px; align-items:stretch">
      <div class="box" style="flex:1; padding:44px 0"><img class="lg l" src="assets/logos/html5.svg" style="display:block; margin:0 auto 14px">HTML</div>
      <div class="box" style="flex:1; padding:44px 0"><img class="lg l" src="assets/logos/css.svg" style="display:block; margin:0 auto 14px">CSS</div>
      <div class="box" style="flex:1; padding:44px 0"><img class="lg l" src="assets/logos/javascript.svg" style="display:block; margin:0 auto 14px">JS</div>
    </div>
  </div>
  <div>
    <div class="lbl">separacja odpowiedzialności – komponenty</div>
    <div class="row" style="gap:12px; align-items:stretch">
      <div class="col" style="flex:1; gap:6px"><div class="box cyan">Navbar</div><div class="box" style="font-size:17px">markup</div><div class="box" style="font-size:17px">logika</div><div class="box" style="font-size:17px">styl</div></div>
      <div class="col" style="flex:1; gap:6px"><div class="box lav2">Feed</div><div class="box" style="font-size:17px">markup</div><div class="box" style="font-size:17px">logika</div><div class="box" style="font-size:17px">styl</div></div>
      <div class="col" style="flex:1; gap:6px"><div class="box lime">Chat</div><div class="box" style="font-size:17px">markup</div><div class="box" style="font-size:17px">logika</div><div class="box" style="font-size:17px">styl</div></div>
    </div>
  </div>
</div>
</div>

<!--
- Maj 2013, JSConf US: React zostaje udostępniony jako open source. Reakcja była chłodna, wręcz negatywna.
- Pete Hunt dał wtedy talk „Rethinking Best Practices”: dzielimy kod nie według technologii, ale według funkcji w UI.
- Komponent = wszystko, czego potrzebuje kawałek interfejsu, w jednym miejscu.
- Dziś ten pogląd jest standardem – podobnie robią Vue, Svelte, Angular.
-->

---

# Wzrost popularności

<div class="sub"><img class="lg s" src="assets/logos/npm.svg"> średnie tygodniowe pobrania pakietu react z npm, w milionach</div>

<div class="fill">
<div>
  <div style="display:flex; align-items:flex-end; gap:34px; height:370px; border-bottom:1.5px solid var(--g2)">
    <div class="col" style="width:104px; height:100%; justify-content:flex-end; align-items:center; gap:8px"><div class="mono" style="font-size:19px">0.5</div><div style="width:100%; height:2px; background:#000"></div></div>
    <div class="col" style="width:104px; height:100%; justify-content:flex-end; align-items:center; gap:8px"><div class="mono" style="font-size:19px">3.0</div><div style="width:100%; height:8px; background:#000; border-radius:3px 3px 0 0"></div></div>
    <div class="col" style="width:104px; height:100%; justify-content:flex-end; align-items:center; gap:8px"><div class="mono" style="font-size:19px">8.2</div><div style="width:100%; height:22px; background:#000; border-radius:3px 3px 0 0"></div></div>
    <div class="col" style="width:104px; height:100%; justify-content:flex-end; align-items:center; gap:8px"><div class="mono" style="font-size:19px">16.9</div><div style="width:100%; height:45px; background:#000; border-radius:3px 3px 0 0"></div></div>
    <div class="col" style="width:104px; height:100%; justify-content:flex-end; align-items:center; gap:8px"><div class="mono" style="font-size:19px">25.0</div><div style="width:100%; height:67px; background:#000; border-radius:3px 3px 0 0"></div></div>
    <div class="col" style="width:104px; height:100%; justify-content:flex-end; align-items:center; gap:8px"><div class="mono" style="font-size:19px">44.9</div><div style="width:100%; height:120px; background:#000; border-radius:3px 3px 0 0"></div></div>
    <div class="col" style="width:104px; height:100%; justify-content:flex-end; align-items:center; gap:8px"><img class="lg l" src="assets/logos/react.svg"><div class="mono" style="font-size:22px">116</div><div style="width:100%; height:268px; background:linear-gradient(180deg, var(--react), var(--violet)); border-radius:4px 4px 0 0"></div></div>
  </div>
  <div class="mono" style="display:flex; gap:34px; font-size:18px; color:var(--g4); padding-top:12px">
    <div style="width:104px; text-align:center">2016</div><div style="width:104px; text-align:center">2018</div><div style="width:104px; text-align:center">2020</div><div style="width:104px; text-align:center">2022</div><div style="width:104px; text-align:center">2024</div><div style="width:104px; text-align:center">2025</div><div style="width:104px; text-align:center">2026</div>
  </div>
</div>
</div>

<div class="src">npm registry API · wrzesień danego roku, 2026: tydzień do 18.10 · pobrania obejmują CI i boty</div>

<!--
- Dane prosto z API npm: dziś ok. 116 mln pobrań tygodniowo. Dla porównania Vue ma ok. 10 mln, Angular ok. 3,4 mln.
- Wzrost jest wykładniczy – ostatnie dwa lata to skok, bo React jest zależnością wielu narzędzi i generatorów kodu (także AI).
- Uczciwie: pobrania to nie liczba developerów – liczą się buildy CI, boty, cache. Ale trend jest jednoznaczny.
-->

---

<!-- header: 02 · Fundamenty -->
<!-- class: s-fund -->

# Główna idea

<div class="fill">
<div style="text-align:center">
  <div class="mono" style="font-size:120px; letter-spacing:-0.04em; line-height:1">UI = <span style="color:var(--violet)">f</span>(<span style="background:var(--lime); padding:0 14px; border-radius:10px">state</span>)</div>
  <div class="muted" style="margin-top:34px; font-size:24px">opisujesz <b style="font-weight:500;color:#000">jak ma wyglądać</b> interfejs, React ustala <b style="font-weight:500;color:#000">co zmienić</b></div>
  <div class="row" style="justify-content:center; margin-top:40px; gap:14px">
    <span class="chip lime"><span class="ic i-database"></span>stan</span>
    <span class="arrow">→</span>
    <span class="chip lav2"><span class="ic i-code-xml"></span>komponent</span>
    <span class="arrow">→</span>
    <span class="chip cyan"><span class="ic i-monitor"></span>DOM</span>
  </div>
</div>
</div>

<!--
- Najważniejszy slajd całej prezentacji.
- Programista pisze funkcję: dla danego stanu zwróć opis interfejsu.
- Gdy stan się zmienia, React wywołuje funkcję ponownie i sam aktualizuje DOM.
- Nie myślimy o przejściach („dodaj klasę, usuń element”), tylko o stanach docelowych.
-->

---

# Imperatywnie vs deklaratywnie

<div class="sub">ten sam przycisk „Lubię to” na dwa sposoby</div>

<div class="fill">
<div class="grid2">
<div>
<div class="lbl"><img class="lg s" src="assets/logos/jquery.svg"> jQuery – jak to zrobić</div>

```js
$('#like').on('click', () => {
  liked = !liked;
  $('#like').toggleClass('active');
  $('#like .label')
    .text(liked ? 'Lubię' : 'Polub');
  $('#count').text(liked ? n + 1 : n);
});
```

</div>
<div>
<div class="lbl"><img class="lg s" src="assets/logos/react.svg"> React – co ma być widać</div>

```jsx
function Like({ n }) {
  const [liked, setLiked] = useState(false);
  return (
    <button onClick={() => setLiked(!liked)}>
      {liked ? 'Lubię' : 'Polub'}
      {liked ? n + 1 : n}
    </button>
  );
}
```

</div>
</div>
</div>

<!--
- Ten sam przycisk „Lubię to” na dwa sposoby.
- Po lewej: każdą zmianę trzeba opisać jako sekwencję operacji na DOM; łatwo o niespójność.
- Po prawej: opisujemy wynik dla każdego stanu. Nie ma kodu, który „przełącza” etykietę – jest tylko warunek.
- Przy dziesiątkach takich elementów różnica w utrzymaniu jest ogromna.
-->

---

# Komponenty

<div class="sub">UI to drzewo małych, wielokrotnie używanych funkcji</div>

<div class="fill">
<div class="card outline" style="width:980px; padding:22px">
  <div class="mono muted" style="font-size:16px; margin-bottom:12px">&lt;App&gt;</div>
  <div class="box cyan" style="margin-bottom:12px">&lt;Navbar /&gt;</div>
  <div class="row" style="gap:12px; align-items:stretch">
    <div class="card" style="flex:3; background:#fff; border:1.5px solid var(--g2); padding:16px">
      <div class="mono muted" style="font-size:16px; margin-bottom:10px">&lt;Feed&gt;</div>
      <div class="col" style="gap:10px">
        <div class="box lav2 row" style="justify-content:space-between">&lt;Post /&gt;<span class="box lime row" style="padding:6px 14px; gap:8px; font-size:17px"><span class="ic i-heart" style="width:16px; height:16px; color:var(--red)"></span>&lt;LikeButton /&gt;</span></div>
        <div class="box lav2 row" style="justify-content:space-between">&lt;Post /&gt;<span class="box lime row" style="padding:6px 14px; gap:8px; font-size:17px"><span class="ic i-heart" style="width:16px; height:16px; color:var(--red)"></span>&lt;LikeButton /&gt;</span></div>
        <div class="box lav2 row" style="justify-content:space-between">&lt;Post /&gt;<span class="box lime row" style="padding:6px 14px; gap:8px; font-size:17px"><span class="ic i-heart" style="width:16px; height:16px; color:var(--red)"></span>&lt;LikeButton /&gt;</span></div>
      </div>
    </div>
    <div class="box amber" style="flex:1; display:flex; align-items:center; justify-content:center">&lt;Sidebar /&gt;</div>
  </div>
</div>
</div>

<!--
- Komponent to funkcja zwracająca fragment UI. Komponenty składamy jak klocki – kompozycja zamiast dziedziczenia.
- LikeButton napisany raz jest używany w każdym poście.
- Cała aplikacja to drzewo komponentów z korzeniem App.
- Dzięki temu zespoły mogą pracować nad osobnymi gałęziami drzewa niezależnie.
-->

---

# JSX

<div class="sub">składnia podobna do HTML, kompilowana do zwykłych wywołań funkcji</div>

<div class="fill">
<div class="row" style="gap:26px">
<div style="width:420px">
<div class="lbl"><span class="ic i-code-xml" style="color:var(--violet)"></span> to piszesz</div>

```jsx
<Post author="Ala" likes={3}>
  <h2>Cześć!</h2>
</Post>
```

</div>
<div class="col" style="align-items:center; gap:8px; margin-top:30px"><img class="lg m" src="assets/logos/babel.svg"><span class="arrow">→</span></div>
<div style="width:560px">
<div class="lbl"><span class="ic i-monitor" style="color:var(--cyan)"></span> to dostaje przeglądarka</div>

```js
jsx(Post, {
  author: "Ala",
  likes: 3,
  children: jsx("h2", {
    children: "Cześć!"
  })
})
```

</div>
</div>
</div>

<!--
- JSX to nie HTML i nie szablon – to cukier składniowy na wywołania funkcji. Kompiluje go Babel, SWC, esbuild.
- Wynik to zwykły obiekt JS opisujący element („React element”).
- Zaleta: w „szablonie” mamy pełny JavaScript – map, warunki, zmienne – zamiast specjalnego języka szablonów jak v-for czy *ngFor.
- Wielkie litery = komponent, małe = tag HTML.
-->

---

# Props i stan

<div class="sub">dane płyną w dół, zdarzenia w górę</div>

<div class="fill">
<div class="row" style="gap:70px">
  <div class="col" style="align-items:center; gap:14px; width:440px">
    <div class="box lime" style="width:100%; padding:20px">&lt;Cart&gt;<span class="m">state: items = [...]</span></div>
    <div class="row" style="gap:60px">
      <span class="mono" style="font-size:18px; color:var(--green)">props ↓</span>
      <span class="mono" style="font-size:18px; color:var(--violet)">↑ onRemove(id)</span>
    </div>
    <div class="box lav2" style="width:100%; padding:20px">&lt;CartItem&gt;<span class="m">props: item, onRemove</span></div>
  </div>
  <div class="col" style="width:500px; gap:18px">
    <div class="card lav2"><div class="t">props</div><div class="d">wejście komponentu od rodzica, tylko do odczytu</div></div>
    <div class="card lime"><div class="t">state</div><div class="d">pamięć komponentu; zmiana przez <span class="mono">setState</span> powoduje ponowny render</div></div>
  </div>
</div>
</div>

<!--
- Props – jak argumenty funkcji: rodzic przekazuje, dziecko ich nie zmienia.
- State – lokalna pamięć komponentu. Jedyny sposób na zmianę UI to zmiana stanu.
- Jednokierunkowy przepływ danych: dziecko nie modyfikuje stanu rodzica bezpośrednio, tylko wywołuje callback.
- Dzięki temu zawsze wiadomo, kto jest właścicielem danych – łatwiej debugować niż przy two-way binding.
-->

---

# Virtual DOM i rekonsyliacja

<div class="sub">React porównuje stare i nowe drzewo, w DOM aplikuje tylko różnicę</div>

<div class="fill">
<div class="row" style="gap:22px; zoom:1.2">
  <div class="col" style="align-items:center; gap:12px">
    <div class="lbl" style="margin:0">przed</div>
    <div class="box mono" style="width:90px">ul</div>
    <div class="row" style="gap:10px"><div class="box">Ala</div><div class="box">Ola</div></div>
  </div>
  <div class="arrow mono" style="font-size:20px">vs</div>
  <div class="col" style="align-items:center; gap:12px">
    <div class="lbl" style="margin:0">po</div>
    <div class="box mono" style="width:90px">ul</div>
    <div class="row" style="gap:10px"><div class="box">Ala</div><div class="box amber">Ula</div><div class="box lime">Ela</div></div>
  </div>
  <div class="arrow">→</div>
  <div class="card" style="width:300px">
    <div class="lbl">operacje na DOM</div>
    <div class="mono" style="font-size:18px"><span class="dot" style="background:var(--amber)"></span>li[1].text = "Ula"</div>
    <div class="mono" style="font-size:18px; margin-top:10px"><span class="dot" style="background:var(--green)"></span>ul.append(li "Ela")</div>
    <div class="d" style="margin-top:18px">2 operacje zamiast przebudowy całej listy</div>
  </div>
</div>
</div>

<!--
- Render tworzy lekkie drzewo obiektów JS (virtual DOM). To tanie.
- Rekonsyliacja: React porównuje nowe drzewo z poprzednim i wylicza minimalny zestaw zmian.
- Heurystyki O(n): inny typ elementu = wymień całe poddrzewo; listy rozpoznawane po atrybucie key – dlatego key jest ważny.
- Uwaga: virtual DOM to nie „magia wydajności” – to sposób, by deklaratywny model był wystarczająco szybki.
-->

---

# Fiber (React 16, 2017)

<div class="sub">renderowanie można przerwać i wznowić</div>

<div class="fill">
<div style="width:100%" class="col">
  <div class="row" style="gap:10px; font-size:20px"><span class="ic i-clock" style="color:var(--red)"></span>stary silnik – jeden nieprzerywalny blok</div>
  <div class="row" style="gap:5px; height:58px; align-items:stretch">
    <div style="flex:10; background:#000; border-radius:8px; color:#fff; font-size:18px; display:flex; align-items:center; padding-left:18px">render dużej listy · 300 ms</div>
    <div style="flex:1.4; background:var(--red); border-radius:8px; color:#fff; font-size:18px; display:flex; align-items:center; justify-content:center">klik</div>
  </div>
  <div class="row" style="gap:10px; font-size:20px; margin-top:40px"><span class="ic i-zap" style="color:var(--green)"></span>Fiber – praca w kawałkach, pilne zdarzenia wchodzą w środek</div>
  <div class="row" style="gap:5px; height:58px; align-items:stretch">
    <div style="flex:2; background:#000; border-radius:8px"></div>
    <div style="flex:2; background:#000; border-radius:8px"></div>
    <div style="flex:1.4; background:var(--lime); border-radius:8px; font-size:18px; display:flex; align-items:center; justify-content:center">klik</div>
    <div style="flex:2; background:#000; border-radius:8px"></div>
    <div style="flex:2; background:#000; border-radius:8px"></div>
    <div style="flex:2; background:#000; border-radius:8px"></div>
  </div>
  <div class="mono muted" style="font-size:16px">czas →</div>
</div>
</div>

<!--
- React 16 to przepisany od zera silnik – „Fiber”. Każdy komponent to jednostka pracy, którą można wstrzymać.
- Wcześniej długi render blokował wątek główny: klik czekał, aż skończy się renderowanie, interfejs „zamarzał”.
- Fiber pozwala nadać priorytety: interakcja użytkownika jest ważniejsza niż przerysowanie listy w tle.
- To fundament pod wszystko, co przyszło później: Suspense, concurrent rendering, transitions.
-->

---

# Hooki (16.8, 2019)

<div class="sub">logika ze stanem w zwykłych funkcjach zamiast klas</div>

<div class="fill">
<div class="grid2">
<div>
<div class="lbl"><span class="ic i-x" style="color:var(--red)"></span> przed: komponent klasowy</div>

```jsx
class Counter extends Component {
  state = { n: 0 };
  componentDidMount() {
    document.title = this.state.n;
  }
  componentDidUpdate() {
    document.title = this.state.n;
  }
  render() { /* ... */ }
}
```

</div>
<div>
<div class="lbl"><span class="ic i-check" style="color:var(--green)"></span> po: hooki</div>

```jsx
function Counter() {
  const [n, setN] = useState(0);

  useEffect(() => {
    document.title = n;
  }, [n]);

  return <button onClick={() =>
    setN(n + 1)}>{n}</button>;
}
```

</div>
</div>
</div>

<!--
- Hooki to największa zmiana w sposobie pisania Reacta. Dziś klasy praktycznie nie występują w nowym kodzie.
- useState – stan, useEffect – synchronizacja z czymś zewnętrznym (DOM, API, subskrypcje), useContext, useRef, useMemo, useReducer.
- Najważniejsza zaleta: własne hooki (useAuth, useDebounce) – logikę ze stanem można wydzielić i współdzielić między komponentami.
- Zasady: wywołuj hooki tylko na górnym poziomie komponentu, nie w warunkach i pętlach.
-->

---

# Concurrent rendering (React 18)

<div class="sub">nie każda aktualizacja jest równie pilna</div>

<div class="fill">
<div class="row" style="gap:30px">
<div style="width:600px">

```jsx
const [pending, startTransition] =
  useTransition();

function onChange(e) {
  setQuery(e.target.value);    // pilne
  startTransition(() => {
    setFilter(e.target.value); // w tle
  });
}
```

</div>
<div class="col" style="width:490px; gap:18px">
  <div class="card lime hcard"><div class="tile t-w"><span class="ic i-zap" style="color:var(--green)"></span></div><div><div class="t">wpisywany tekst</div><div class="d">pilne – pole reaguje natychmiast</div></div></div>
  <div class="card hcard"><div class="tile t-v"><span class="ic i-clock"></span></div><div><div class="t">filtrowanie 10 000 wierszy</div><div class="d">transition – liczone w tle, przerywane przy kolejnym znaku</div></div></div>
</div>
</div>
</div>

<!--
- React 18 (2022) udostępnił możliwości Fibera w API: useTransition, useDeferredValue, Suspense przy ładowaniu danych.
- Przykład: wyszukiwarka nad dużą listą. Bez transition każda litera blokuje UI do czasu przefiltrowania listy.
- Z transition pole tekstowe jest zawsze responsywne, a lista „dogania” w tle.
- Do tego automatyczny batching aktualizacji i streaming SSR.
-->

---

# Server Components (React 19)

<div class="sub">część komponentów działa tylko na serwerze i nie trafia do bundla</div>

<div class="fill">
<div class="row" style="gap:24px">
  <div class="card outline" style="width:450px; padding:22px">
    <div class="row" style="gap:14px; margin-bottom:18px"><div class="tile sm t-v"><span class="ic i-server"></span></div><span style="font-size:20px">serwer</span></div>
    <div class="col" style="gap:10px">
      <div class="box lav2">&lt;ProductPage&gt;<span class="m">await db.product.find(id)</span></div>
      <div class="box lav2">&lt;Description&gt;<span class="m">markdown → HTML, 0 KB JS</span></div>
    </div>
  </div>
  <div class="col" style="align-items:center; gap:6px"><div class="arrow">→</div><span class="mono muted" style="font-size:15px; text-align:center">RSC<br>stream</span></div>
  <div class="card outline" style="width:450px; padding:22px">
    <div class="row" style="gap:14px; margin-bottom:18px"><div class="tile sm t-g"><span class="ic i-monitor"></span></div><span style="font-size:20px">przeglądarka</span></div>
    <div class="col" style="gap:10px">
      <div class="box">gotowy wynik renderu<span class="m">bez kodu komponentu</span></div>
      <div class="box lime">&lt;AddToCart&gt;<span class="m">'use client' · interaktywny</span></div>
    </div>
  </div>
</div>
</div>

<!--
- React 19 (grudzień 2024). Server Components: komponent może być async i pobrać dane bezpośrednio z bazy – bez osobnego API.
- Ich kod nigdy nie trafia do przeglądarki – ciężkie biblioteki (parser markdown, formatowanie dat) nie zwiększają bundla.
- Komponenty interaktywne oznaczamy dyrektywą 'use client' – one działają jak klasyczny React.
- W praktyce RSC używa się przez framework (Next.js App Router, React Router, Waku).
-->

---

# Actions i formularze (React 19)

<div class="sub">asynchroniczne akcje jako wbudowany element API</div>

<div class="fill">
<div class="row" style="gap:30px">
<div style="width:620px">

```jsx
const [state, action, pending] =
  useActionState(async (prev, form) => {
    return await subscribe(form.get('email'));
  }, null);

<form action={action}>
  <input name="email" />
  <button disabled={pending}>Zapisz</button>
</form>
```

</div>
<div class="col" style="width:470px; gap:14px">
  <div class="card hcard" style="padding:20px 22px; align-items:center"><div class="tile t-v"><span class="ic i-file-input"></span></div><div><div class="t mono" style="font-size:21px">useActionState</div><div class="d">wynik, błąd i stan „pending”</div></div></div>
  <div class="card hcard" style="padding:20px 22px; align-items:center"><div class="tile t-g"><span class="ic i-rocket"></span></div><div><div class="t mono" style="font-size:21px">useOptimistic</div><div class="d">UI zmienia się, zanim serwer odpowie</div></div></div>
  <div class="card hcard" style="padding:20px 22px; align-items:center"><div class="tile t-c"><span class="ic i-package"></span></div><div><div class="t mono" style="font-size:21px">use()</div><div class="d">odczyt Promise lub kontekstu w renderze</div></div></div>
</div>
</div>
</div>

<!--
- React 19 (grudzień 2024) uprościł typowy kod: obsługę wysyłania formularza, ładowania, błędów.
- Wcześniej: ręcznie useState dla loading, error, data + try/catch.
- useOptimistic – np. „polubienie” widać od razu, a jeśli serwer odrzuci, React cofa zmianę.
- Akcje działają też z Server Functions – formularz może wywołać funkcję po stronie serwera.
-->

---

# React Compiler 1.0 (2025)

<div class="sub">automatyczna memoizacja w czasie kompilacji</div>

<div class="fill">
<div class="grid2" style="gap:24px">
<div>
<div class="lbl"><span class="ic i-x" style="color:var(--red)"></span> przed: ręczna optymalizacja</div>

```jsx
const sorted = useMemo(
  () => items.toSorted(byPrice),
  [items]
);
const onSelect = useCallback(
  (id) => setSelected(id), []
);
export default memo(ProductList);
```

</div>
<div>
<div class="lbl"><span class="ic i-wand-sparkles" style="color:var(--violet)"></span> z kompilatorem</div>

```jsx
const sorted = items.toSorted(byPrice);
const onSelect = (id) => setSelected(id);
export default ProductList;
```

<div class="card lime hcard" style="margin-top:20px; align-items:center"><div class="tile t-w"><span class="ic i-gauge" style="color:var(--green)"></span></div><div><div class="t">do 12% szybsze ładowanie</div><div class="d">Meta Quest Store; część interakcji ponad 2,5× szybsza</div></div></div>
</div>
</div>
</div>

<!--
- Problem: React domyślnie re-renderuje całe poddrzewo. Developerzy ręcznie wstawiali useMemo/useCallback/memo – łatwo o błąd i bałagan.
- React Compiler (stabilny od października 2025) analizuje kod i sam wstawia memoizację.
- Działa jako plugin do Babel/Vite/Next.js; wymaga przestrzegania „zasad Reacta” – linter to sprawdza.
- Dane z Meta: Quest Store do 12% szybsze ładowanie i nawigacja.
-->

---

<!-- header: 03 · Ekosystem -->
<!-- class: s-eco -->

# React to biblioteka, nie framework

<div class="sub">resztę dobiera się z ekosystemu</div>

<div class="fill">
<div class="grid3">
  <div class="card cyan"><div class="logos" style="margin-bottom:20px"><img class="lg m" src="assets/logos/nextdotjs.svg"><img class="lg m" src="assets/logos/reactrouter.svg"></div><div class="n">framework</div><div class="t">Next.js · React Router</div><div class="d">routing, SSR, RSC, build</div></div>
  <div class="card"><div class="logos" style="margin-bottom:20px"><img class="lg m" src="assets/logos/reactquery.svg"><img class="lg m" src="assets/logos/swr.svg"></div><div class="n">dane z serwera</div><div class="t">TanStack Query · SWR</div><div class="d">cache, ponawianie, odświeżanie</div></div>
  <div class="card"><div class="logos" style="margin-bottom:20px"><img class="lg m" src="assets/logos/redux.svg"><span class="tile sm t-a" style="width:40px; height:40px; margin:0"><span class="ic i-box"></span></span></div><div class="n">stan klienta</div><div class="t">Zustand · Redux Toolkit</div><div class="d">globalny stan aplikacji</div></div>
  <div class="card"><div class="logos" style="margin-bottom:20px"><img class="lg m" src="assets/logos/reacthookform.svg"><img class="lg m" src="assets/logos/zod.svg"></div><div class="n">formularze</div><div class="t">React Hook Form · Zod</div><div class="d">walidacja i typy z jednego schematu</div></div>
  <div class="card"><div class="logos" style="margin-bottom:20px"><img class="lg m" src="assets/logos/tailwindcss.svg"><img class="lg m" src="assets/logos/shadcnui.svg"></div><div class="n">UI i style</div><div class="t">Tailwind · shadcn/ui</div><div class="d">Radix, MUI, CSS Modules</div></div>
  <div class="card"><div class="logos" style="margin-bottom:20px"><img class="lg m" src="assets/logos/vitest.svg"><img class="lg m" src="assets/logos/testinglibrary.svg"></div><div class="n">testy</div><div class="t">Vitest · Testing Library</div><div class="d">Playwright, Storybook</div></div>
</div>
</div>

<!--
- React odpowiada tylko za warstwę widoku. Routing, pobieranie danych, formularze – to wybory zespołu.
- To jednocześnie zaleta (elastyczność) i wada (trzeba podjąć dużo decyzji).
- Formularze: React Hook Form (32 mln pobrań/tydz.) + Zod (207 mln) – jeden schemat daje walidację i typy TypeScript, ten sam schemat działa też na backendzie.
- Dla porównania: Angular ma większość tych rzeczy wbudowanych.
-->

---

# Frameworki i narzędzia startowe

<div class="sub">Create React App wygaszony w lutym 2025 – oficjalnie zalecany jest framework</div>

<div class="fill">
<div class="col" style="width:100%; gap:22px">
<div class="grid4">
  <div class="card cyan"><img class="lg l" src="assets/logos/nextdotjs.svg" style="margin-bottom:22px"><div class="n">Vercel</div><div class="t">Next.js</div><div class="d">App Router, Server Components, SSR/SSG</div></div>
  <div class="card"><img class="lg l" src="assets/logos/reactrouter.svg" style="margin-bottom:22px"><div class="n">Shopify</div><div class="t">React Router 7</div><div class="d">dawniej Remix; od SPA po pełny framework</div></div>
  <div class="card"><div class="tile t-k" style="width:56px; height:56px; margin-bottom:22px"><img class="lg m" src="assets/logos/tanstack.svg"></div><div class="n">TanStack</div><div class="t">TanStack Start</div><div class="d">w pełni typowany routing</div></div>
  <div class="card"><img class="lg l" src="assets/logos/expo.svg" style="margin-bottom:22px"><div class="n">Expo</div><div class="t">Expo</div><div class="d">framework dla React Native</div></div>
</div>
<div class="card amber row" style="gap:20px; padding:18px 26px"><img class="lg m" src="assets/logos/vite.svg"><div style="font-size:21px">Vite <span class="mono muted" style="font-size:17px; margin-left:8px">119 mln pobrań / tydz.</span></div><div class="d" style="margin-left:auto">czysty SPA bez serwera: Vite + React + router</div></div>
</div>
</div>

<!--
- Kiedyś każdy zaczynał od create-react-app. W 2025 zespół Reacta oficjalnie go wygasił.
- Dziś dokumentacja zaleca start od frameworka: Next.js, React Router, Expo dla mobile.
- Next.js – de facto standard dla aplikacji z SSR, rozwijany przez Vercel; pierwszy wdrożył Server Components.
- Jeśli nie potrzebujemy serwera (panel admina, narzędzie wewnętrzne) – Vite + React jest prostszy.
-->

---

# Zarządzanie stanem

<div class="sub"><img class="lg s" src="assets/logos/npm.svg"> tygodniowe pobrania z npm, w milionach</div>

<div class="fill">
<div class="col" style="width:100%; gap:26px">
<div class="hbars">
  <div class="lab"><img class="lg" src="assets/logos/reactquery.svg">TanStack Query</div><div><div class="bar c" style="width:100%"></div></div><div class="val">40.1</div>
  <div class="lab"><span class="ic i-box" style="color:var(--amber); width:24px; height:24px"></span>Zustand</div><div><div class="bar v" style="width:94%"></div></div><div class="val">37.7</div>
  <div class="lab"><img class="lg" src="assets/logos/redux.svg">Redux</div><div><div class="bar" style="width:68%"></div></div><div class="val">27.1</div>
  <div class="lab"><img class="lg" src="assets/logos/redux.svg">Redux Toolkit</div><div><div class="bar v" style="width:50%"></div></div><div class="val">19.9</div>
  <div class="lab"><img class="lg" src="assets/logos/swr.svg">SWR</div><div><div class="bar c" style="width:28%"></div></div><div class="val">11.4</div>
  <div class="lab"><span class="ic i-atom" style="color:var(--g4); width:24px; height:24px"></span>Jotai</div><div><div class="bar v" style="width:9.4%"></div></div><div class="val">3.8</div>
</div>
<div class="legend"><span><span class="dot" style="background:var(--cyan)"></span>dane z serwera</span><span><span class="dot" style="background:var(--violet)"></span>stan klienta</span><span><span class="dot" style="background:var(--g2)"></span>klasyczny Redux</span></div>
</div>
</div>

<div class="src">npm registry API · tydzień 12–18.10.2026</div>

<!--
- Kiedyś „React + Redux” było niemal synonimem. Dziś Redux to głównie istniejące, starsze projekty (stąd wysoki „goły” redux).
- Kluczowa zmiana myślenia: większość „stanu” to kopia danych z serwera – tym zajmuje się TanStack Query lub SWR.
- TanStack Query: jeden hook useQuery zamiast useEffect + fetch + 3× useState; cache po kluczu, deduplikacja zapytań, ponawianie, odświeżanie w tle.
- Na to, co zostaje (motyw, koszyk, otwarte modale), wystarcza lekki Zustand albo zwykły Context.
- Redux Toolkit dalej ma sens w dużych aplikacjach ze złożoną logiką i potrzebą devtools/time-travel.
-->

---

# Stylowanie i komponenty UI

<div class="sub"><img class="lg s" src="assets/logos/tailwindcss.svg"> Tailwind CSS – 85 mln pobrań tygodniowo</div>

<div class="fill">
<div class="grid2" style="gap:28px; align-items:center">
<div>

```jsx
<button className="
  rounded-lg bg-black
  px-4 py-2 text-white
  hover:bg-zinc-800">
  Zapisz
</button>
```

<div class="d muted" style="margin-top:16px; font-size:18px">klasy narzędziowe zamiast osobnych plików CSS</div>
</div>
<div class="col">
  <div class="card cyan hcard" style="align-items:center"><img class="lg l" src="assets/logos/shadcnui.svg"><div><div class="t">shadcn/ui</div><div class="d">kod komponentów kopiowany do repozytorium</div></div></div>
  <div class="card hcard" style="align-items:center"><img class="lg l" src="assets/logos/radixui.svg"><div><div class="t">Radix UI · React Aria</div><div class="d">„headless” – dostępność bez wyglądu</div></div></div>
  <div class="card hcard" style="align-items:center"><img class="lg l" src="assets/logos/mui.svg"><div><div class="t">MUI · Ant Design</div><div class="d">gotowe, kompletne zestawy komponentów</div></div></div>
</div>
</div>
</div>

<!--
- Dominujący trend: Tailwind. Style obok markupu, spójne z filozofią komponentów.
- CSS-in-JS (styled-components) traci popularność, m.in. przez słabą zgodność z Server Components.
- shadcn/ui – ciekawe podejście: nie biblioteka, tylko generator kodu. Komponenty oparte na Radix + Tailwind lądują w naszym repo.
- Headless (Radix, React Aria Adobe) – rozwiązują trudne rzeczy: focus, ARIA, nawigację klawiaturą.
-->

---

# Testowanie

<div class="sub">„Im bardziej testy przypominają sposób użycia aplikacji, tym więcej dają pewności”</div>

<div class="fill">
<div class="col" style="align-items:center; gap:12px">
  <div class="box dark row" style="width:420px; padding:16px; gap:16px; justify-content:center"><img class="lg m" src="assets/logos/playwright.svg"><span style="text-align:left">E2E · Playwright<span class="m">prawdziwa przeglądarka</span></span></div>
  <div class="box cyan row" style="width:700px; padding:16px; gap:16px; justify-content:center"><img class="lg m" src="assets/logos/testinglibrary.svg"><span style="text-align:left">komponenty · React Testing Library<span class="m">render i interakcje jak użytkownik</span></span></div>
  <div class="box row" style="width:980px; padding:16px; gap:16px; justify-content:center"><img class="lg m" src="assets/logos/vitest.svg"><img class="lg m" src="assets/logos/jest.svg"><span style="text-align:left">jednostkowe · Vitest / Jest<span class="m">hooki, logika, funkcje pomocnicze</span></span></div>
  <div class="row" style="margin-top:16px; gap:12px; font-size:19px; color:var(--g5)"><img class="lg" src="assets/logos/storybook.svg">Storybook – katalog komponentów i testy wizualne</div>
</div>
</div>

<!--
- Piramida testów w świecie Reacta.
- React Testing Library (Kent C. Dodds): testujemy to, co widzi użytkownik – teksty, role, kliknięcia – a nie wewnętrzny stan komponentu.
- Vitest wypiera Jesta w nowych projektach (77 mln pobrań/tydz.) – szybszy, zgodny z Vite.
- Playwright (Microsoft) – testy end-to-end w Chromium, Firefoxie i WebKicie.
-->

---

# React Native

<div class="sub">ten sam model komponentów, natywne widoki zamiast DOM</div>

<div class="fill">
<div class="row zoom-s" style="gap:30px">
  <div class="card outline" style="width:310px; padding:26px">
    <img class="lg m" src="assets/logos/react.svg" style="margin-bottom:16px">
    <div class="mono" style="font-size:19px; line-height:1.6">&lt;View&gt;<br>&nbsp;&nbsp;&lt;Text&gt;Cześć&lt;/Text&gt;<br>&nbsp;&nbsp;&lt;Pressable /&gt;<br>&lt;/View&gt;</div>
  </div>
  <div class="arrow">→</div>
  <div class="col" style="gap:10px; width:290px">
    <div class="box l cyan"><img class="lg s" src="assets/logos/apple.svg">iOS</div>
    <div class="box l lime"><img class="lg s" src="assets/logos/android.svg">Android</div>
    <div class="box l"><span class="ms s"><i></i><i></i><i></i><i></i></span>Windows, macOS</div>
    <div class="box l"><img class="lg s" src="assets/logos/meta.svg">Web, TV, Quest</div>
  </div>
  <div class="col" style="width:280px; gap:16px">
    <div class="lbl" style="margin:0">używają m.in.</div>
    <div class="row" style="gap:16px; flex-wrap:wrap"><img class="lg m" src="assets/logos/facebook.svg"><img class="lg m" src="assets/logos/instagram.svg"><span class="ms l"><i></i><i></i><i></i><i></i></span><img class="lg m" src="assets/logos/shopify.svg"><img class="lg m" src="assets/logos/discord.svg"></div>
  </div>
</div>
</div>

<!--
- React Native (2015): React nie jest związany z przeglądarką – „renderer” można podmienić.
- Zamiast div/span mamy View/Text, a na ekranie powstają prawdziwe natywne kontrolki, nie WebView.
- Nowa architektura (Fabric, JSI) jest domyślna – szybsza komunikacja JS z kodem natywnym.
- Używają: Facebook, Instagram, Microsoft (Office, Outlook), Shopify, Discord, Coinbase.
- Polski akcent: Callstack (Wrocław) i Software Mansion (Kraków) to jedni z głównych kontrybutorów RN.
-->

---

<!-- header: 04 · Rynek -->
<!-- class: s-mkt -->

# Najpopularniejsze technologie webowe

<div class="sub"><img class="lg s" src="assets/logos/stackoverflow.svg"> Stack Overflow Developer Survey 2025 · % respondentów</div>

<div class="fill">
<div class="row" style="gap:40px; width:100%">
<div class="hbars" style="grid-template-columns:190px 1fr 80px; flex:1; gap:10px 16px">
  <div class="lab"><img class="lg" src="assets/logos/nodedotjs.svg">Node.js</div><div><div class="bar" style="width:100%"></div></div><div class="val">48.7%</div>
  <div class="lab"><img class="lg" src="assets/logos/react.svg"><b style="font-weight:500">React</b></div><div><div class="bar r" style="width:91.8%"></div></div><div class="val" style="color:#000">44.7%</div>
  <div class="lab"><img class="lg" src="assets/logos/jquery.svg">jQuery</div><div><div class="bar" style="width:48%"></div></div><div class="val">23.4%</div>
  <div class="lab"><img class="lg" src="assets/logos/nextdotjs.svg">Next.js</div><div><div class="bar r" style="width:42.7%"></div></div><div class="val">20.8%</div>
  <div class="lab"><img class="lg" src="assets/logos/angular.svg">Angular</div><div><div class="bar k" style="width:37.4%"></div></div><div class="val">18.2%</div>
  <div class="lab"><img class="lg" src="assets/logos/vuedotjs.svg">Vue.js</div><div><div class="bar k" style="width:36.1%"></div></div><div class="val">17.6%</div>
  <div class="lab"><img class="lg" src="assets/logos/svelte.svg">Svelte</div><div><div class="bar k" style="width:14.8%"></div></div><div class="val">7.2%</div>
</div>
<div class="card pink" style="width:280px">
  <div class="tile t-w"><img class="lg" src="assets/logos/npm.svg"></div>
  <div class="mono" style="font-size:44px; letter-spacing:-0.03em">11×</div>
  <div class="d" style="margin-top:8px">więcej pobrań z npm niż Vue<br><span class="mono" style="font-size:16px">116 mln vs 10 mln / tydz.</span></div>
</div>
</div>
</div>

<!--
- Największa ankieta developerów na świecie.
- React to najpopularniejszy framework frontendowy – ponad 2× więcej użytkowników niż Angular czy Vue.
- Next.js (oparty na Reacie) sam w sobie wyprzedza Angulara i Vue. Wyżej jest tylko Node.js – środowisko uruchomieniowe, nie framework UI.
- Na npm przewaga jest jeszcze większa: ok. 116 mln pobrań tygodniowo vs ok. 10 mln Vue i 3,4 mln Angulara.
- Angular jest nadal mocny w korporacjach, ale na rynku pracy dominuje React.
-->

---

# Kto używa Reacta

<div class="fill">
<div class="grid4">
  <div class="card"><img class="lg l" src="assets/logos/meta.svg" style="margin-bottom:20px"><div class="t">Meta</div><div class="d">Facebook, Instagram, Threads</div></div>
  <div class="card"><div style="height:56px; margin-bottom:20px; display:flex; align-items:center"><span class="ms l" style="width:44px; height:44px"><i></i><i></i><i></i><i></i></span></div><div class="t">Microsoft</div><div class="d">Outlook, Teams, Office</div></div>
  <div class="card"><img class="lg l" src="assets/logos/netflix.svg" style="margin-bottom:20px"><div class="t">Netflix</div><div class="d">web i interfejsy na TV</div></div>
  <div class="card"><img class="lg l" src="assets/logos/airbnb.svg" style="margin-bottom:20px"><div class="t">Airbnb</div><div class="d">web i design system</div></div>
  <div class="card"><img class="lg l" src="assets/logos/discord.svg" style="margin-bottom:20px"><div class="t">Discord</div><div class="d">desktop, web, mobile</div></div>
  <div class="card"><img class="lg l" src="assets/logos/atlassian.svg" style="margin-bottom:20px"><div class="t">Atlassian</div><div class="d">Jira, Confluence</div></div>
  <div class="card"><img class="lg l" src="assets/logos/shopify.svg" style="margin-bottom:20px"><div class="t">Shopify</div><div class="d">aplikacje mobilne</div></div>
  <div class="card"><div class="logos" style="height:56px; margin-bottom:20px"><img class="lg m" src="assets/logos/notion.svg"><img class="lg m" src="assets/logos/vercel.svg"></div><div class="t">Notion · Vercel</div><div class="d">i tysiące innych</div></div>
</div>
</div>

<!--
- Kilka rozpoznawalnych przykładów, wszystkie to aplikacje o ogromnej skali.
- Meta używa Reacta w swoich produktach na co dzień – to gwarancja, że framework działa w produkcji przy miliardach użytkowników.
- Microsoft stawia na React Native nawet na desktopie (części Office, Xbox).
- W Polsce: Allegro, banki (aplikacje webowe), software house'y – React jest najczęstszym wymaganiem w ofertach frontend.
-->

---

# Do czego się nadaje

<div class="fill">
<div class="grid2" style="gap:44px">
<div class="col" style="gap:12px">
  <div class="row" style="gap:10px; font-size:21px; color:var(--green); margin-bottom:4px"><span class="ic i-check"></span>dobry wybór</div>
  <div class="box l lime"><span class="ic i-layout-dashboard"></span>aplikacje SPA i SaaS</div>
  <div class="box l lime"><span class="ic i-gauge"></span>panele i dashboardy</div>
  <div class="box l lime"><span class="ic i-globe"></span>e-commerce z SSR (Next.js)</div>
  <div class="box l lime"><span class="ic i-smartphone"></span>mobile i desktop (RN, Electron)</div>
  <div class="box l lime"><span class="ic i-palette"></span>design systemy wielu zespołów</div>
</div>
<div class="col" style="gap:12px">
  <div class="row" style="gap:10px; font-size:21px; color:var(--red); margin-bottom:4px"><span class="ic i-x"></span>są lepsze opcje</div>
  <div class="box l"><img class="lg s" src="assets/logos/astro.svg">blog, dokumentacja → Astro</div>
  <div class="box l"><img class="lg s" src="assets/logos/htmx.svg">proste strony z serwera → htmx</div>
  <div class="box l"><img class="lg s" src="assets/logos/preact.svg">mały widget → Preact, Svelte</div>
  <div class="box l"><span class="ic i-cpu"></span>gry i grafika → Canvas, WebGL</div>
</div>
</div>
</div>

<!--
- React błyszczy, gdy interfejs ma dużo stanu i interakcji, a projekt będzie rozwijany latami przez wiele osób.
- Do strony z treścią (blog, dokumentacja) to przerost formy – Astro wysyła domyślnie 0 KB JS (a może osadzać komponenty Reacta tam, gdzie trzeba).
- htmx/Alpine – gdy chcemy tylko „ożywić” HTML generowany przez serwer.
- Gry: React nie jest silnikiem graficznym, choć istnieje react-three-fiber do sceny 3D.
-->

---

# Zalety

<div class="fill">
<div class="grid3">
  <div class="card lime"><div class="tile t-w"><span class="ic i-lightbulb" style="color:var(--green)"></span></div><div class="t">Prosty model</div><div class="d">UI = f(state), komponenty to funkcje</div></div>
  <div class="card"><div class="tile t-c"><span class="ic i-puzzle"></span></div><div class="t">Ekosystem</div><div class="d">gotowa biblioteka na niemal każdy problem</div></div>
  <div class="card"><div class="tile t-v"><span class="ic i-users"></span></div><div class="t">Rynek pracy</div><div class="d">najwięcej ofert i developerów</div></div>
  <div class="card"><div class="tile t-a"><span class="ic i-smartphone"></span></div><div class="t">Wiele platform</div><div class="d">web, mobile, desktop, VR</div></div>
  <div class="card"><div class="tile t-g"><span class="ic i-shield-alert"></span></div><div class="t">Stabilność</div><div class="d">łagodne migracje, testowany na produktach Meta</div></div>
  <div class="card"><div class="tile t-r"><span class="ic i-sparkles"></span></div><div class="t">Narzędzia i AI</div><div class="d">DevTools, TypeScript; modele AI znają go najlepiej</div></div>
</div>
</div>

<!--
- Prosty model koncepcyjny – mało „magii”, mało specjalnej składni; „to tylko JavaScript”.
- Ekosystem i społeczność – największe na rynku frontend; problemy są już rozwiązane i opisane.
- Biznes: łatwo zatrudnić, łatwo przejąć projekt.
- Stabilność: zmiany API wprowadzane stopniowo; kod sprzed lat nadal działa (klasy wciąż są wspierane).
- Ciekawostka: narzędzia AI generują najlepszy kod właśnie w React, bo mają go najwięcej w danych treningowych.
-->

---

# Wady

<div class="fill">
<div class="grid2">
  <div class="card hcard"><div class="tile t-r"><span class="ic i-workflow"></span></div><div><div class="t">Zmęczenie decyzjami</div><div class="d">routing, dane, style, stan – każdy projekt wygląda inaczej</div></div></div>
  <div class="card hcard"><div class="tile t-r"><span class="ic i-flame"></span></div><div><div class="t">Pułapki wydajności</div><div class="d">zbędne re-rendery, nadużywany useEffect</div></div></div>
  <div class="card hcard"><div class="tile t-r"><span class="ic i-network"></span></div><div><div class="t">Rosnąca złożoność</div><div class="d">Server Components, 'use client', cache – trudniejsze niż klasyczny SPA</div></div></div>
  <div class="card hcard"><div class="tile t-r"><span class="ic i-package"></span></div><div><div class="t">Rozmiar i szybkość</div><div class="d">virtual DOM cięższy niż sygnały (Solid, Svelte 5)</div></div></div>
</div>
</div>

<!--
- „JavaScript fatigue”: ta sama elastyczność, która jest zaletą, oznacza dziesiątki decyzji i różne standardy w każdej firmie.
- useEffect to najczęstsze źródło bugów – używany do rzeczy, do których nie powinien (synchronizacja stanu, pobieranie danych). Ręczna memoizacja – do czasu Compilera.
- RSC i meta-frameworki: granica serwer/klient jest nowym źródłem błędów; część społeczności krytykuje zbyt bliski związek z Vercel/Next.js.
- Konkurenci (Solid, Svelte, Vue Vapor) używają sygnałów i aktualizują DOM precyzyjnie bez porównywania drzew; Preact jest kilkanaście razy mniejszy.
-->

---

# Cena złożoności: React2Shell

<div class="sub"><span class="ic i-shield-alert" style="color:var(--red)"></span> CVE-2025-55182 · zdalne wykonanie kodu w Server Components</div>

<div class="fill">
<div class="row" style="gap:44px">
  <div class="card pink" style="width:320px; text-align:center; padding:40px 24px">
    <div class="mono" style="font-size:110px; line-height:1; letter-spacing:-0.05em; color:var(--red)">10.0</div>
    <div class="d" style="margin-top:14px">CVSS – maksymalna ocena</div>
  </div>
  <div class="col" style="width:720px; gap:0">
    <div class="row" style="padding:16px 0; border-bottom:1px solid var(--g2); gap:24px"><span class="mono" style="width:150px; font-size:19px; color:var(--red)">3.12.2025</span><span style="font-size:20px">publikacja i poprawki w 19.0.1, 19.1.2, 19.2.1</span></div>
    <div class="row" style="padding:16px 0; border-bottom:1px solid var(--g2); gap:24px"><span class="mono" style="width:150px; font-size:19px; color:var(--red)">5.12.2025</span><span style="font-size:20px">CISA: aktywnie wykorzystywana w atakach</span></div>
    <div class="row" style="padding:16px 0; border-bottom:1px solid var(--g2); gap:24px"><span class="mono" style="width:150px; font-size:19px; color:var(--red)">11.12.2025</span><span style="font-size:20px">dwie kolejne podatności: DoS i wyciek kodu</span></div>
    <div class="d" style="margin-top:20px">przyczyna: niebezpieczna deserializacja w protokole Flight – wystarczyło, że aplikacja wspierała RSC</div>
  </div>
</div>
</div>

<!--
- Konkretny przykład ryzyka związanego z przeniesieniem Reacta na serwer.
- Grudzień 2025: krytyczna podatność – nieuwierzytelnione żądanie HTTP mogło wykonać kod na serwerze z Next.js 15/16.
- Dotyczyło to aplikacji, które nawet nie definiowały Server Functions.
- Wniosek: gdy biblioteka UI staje się częścią backendu, dziedziczy też odpowiedzialność za bezpieczeństwo backendu. Szybkie łatanie zależności jest obowiązkowe.
-->

---

<!-- header: 05 · Duże aplikacje -->
<!-- class: s-big -->

# Struktura według funkcji

<div class="sub"><span class="ic i-folder-tree" style="color:var(--green)"></span> feature-based zamiast podziału według typu pliku</div>

<div class="fill">
<div class="row" style="gap:30px; align-items:stretch">
<div class="col" style="width:380px; gap:0">
<div class="lbl" style="color:var(--red)"><span class="ic i-x"></span> według typu</div>
<pre style="flex:1">src/
  components/
    (200 plików)
  hooks/
  services/
  utils/</pre>
</div>
<div class="col" style="width:660px; gap:0">
<div class="lbl" style="color:var(--green)"><span class="ic i-check"></span> według funkcji</div>
<pre style="background:var(--lime)!important">src/
  features/
    checkout/
      components/ api.ts
      index.ts   ← publiczne API
    orders/
  shared/ui/   ← design system
  app/         ← routing, providery</pre>
</div>
</div>
</div>

<!--
- Mały projekt: foldery components/hooks/utils wystarczą. Przy 200+ komponentach to chaos.
- W dużych aplikacjach grupuje się kod wg funkcji biznesowych – zespół „checkout” ma wszystko w jednym folderze.
- Moduł wystawia publiczne API przez index.ts; importowanie „do środka” innego modułu blokuje się lintem.
- Popularne wzorce: Feature-Sliced Design, bulletproof-react.
-->

---

# Monorepo i design system

<div class="sub">kilka aplikacji, wspólne komponenty i konfiguracja</div>

<div class="fill">
<div class="col" style="align-items:center; gap:14px; width:100%">
  <div class="grid3">
    <div class="box l" style="padding:18px 22px"><img class="lg m" src="assets/logos/nextdotjs.svg"><span>apps/web<span class="m">Next.js</span></span></div>
    <div class="box l" style="padding:18px 22px"><img class="lg m" src="assets/logos/vite.svg"><span>apps/admin<span class="m">Vite SPA</span></span></div>
    <div class="box l" style="padding:18px 22px"><img class="lg m" src="assets/logos/expo.svg"><span>apps/mobile<span class="m">Expo</span></span></div>
  </div>
  <div class="arrow">↑ ↑ ↑</div>
  <div class="grid3">
    <div class="box l lime" style="padding:18px 22px"><img class="lg m" src="assets/logos/storybook.svg"><span>packages/ui<span class="m">design system</span></span></div>
    <div class="box l lav2" style="padding:18px 22px"><img class="lg m" src="assets/logos/typescript.svg"><span>packages/api<span class="m">typowany klient</span></span></div>
    <div class="box l" style="padding:18px 22px"><img class="lg m" src="assets/logos/eslint.svg"><span>packages/config<span class="m">ESLint, TS, Tailwind</span></span></div>
  </div>
  <div class="chips" style="margin-top:22px; justify-content:center">
    <span class="chip"><img class="lg s" src="assets/logos/turborepo.svg">Turborepo</span><span class="chip"><img class="lg s" src="assets/logos/nx.svg">Nx</span><span class="chip"><img class="lg s" src="assets/logos/pnpm.svg">pnpm workspaces</span><span class="chip"><img class="lg s" src="assets/logos/typescript.svg">TypeScript wszędzie</span>
  </div>
</div>
</div>

<!--
- Duże firmy mają kilka aplikacji – web, panel, mobile – dzielących komponenty i logikę.
- Monorepo (Turborepo, Nx) pozwala trzymać je w jednym repozytorium i budować tylko to, co się zmieniło.
- Design system: wspólna biblioteka komponentów, dokumentowana w Storybooku – spójny wygląd w całej firmie (np. Fluent UI w Microsoft, Polaris w Shopify).
- TypeScript to dziś standard – praktycznie każdy profesjonalny projekt React.
- Wydajność w dużych aplikacjach: code splitting (React.lazy + Suspense), wirtualizacja długich list, React Compiler, pomiar Core Web Vitals.
-->

---

# Strategie renderowania

<div class="sub">gdzie i kiedy powstaje HTML</div>

<div class="fill">
<div style="width:100%">

| | gdzie | kiedy | typowe użycie |
|---|---|---|---|
| <span class="pill cyan">CSR</span> | przeglądarka | przy każdym wejściu | panel za logowaniem |
| <span class="pill lav2">SSR</span> | serwer | przy każdym żądaniu | dane użytkownika + SEO |
| <span class="pill amber">SSG</span> | serwer | w czasie builda | dokumentacja, landing |
| <span class="pill pink">ISR</span> | serwer | build + odświeżanie | katalog produktów |
| <span class="pill lime">RSC</span> | serwer, per komponent | przy żądaniu, stream | treść + interakcje |

</div>
</div>

<!--
- W dużych aplikacjach wybór strategii renderowania to decyzja architektoniczna.
- CSR – najprostsze, ale słabe SEO i wolniejszy pierwszy ekran.
- SSR/SSG – HTML gotowy od razu, potem „hydratacja” czyni go interaktywnym. ISR – statyczne strony odświeżane co N sekund.
- Nowoczesne frameworki pozwalają mieszać strategie per strona, a z RSC nawet per komponent.
-->

---

<!-- header: 06 · Społeczność i przyszłość -->
<!-- class: s-fut -->

# Społeczność w liczbach

<div class="fill">
<div class="col" style="width:100%; gap:50px">
<div class="grid4" style="gap:30px">
  <div class="stat"><div class="tile t-k"><span class="ic i-github"></span></div><div class="big">251k</div><div class="lab">gwiazdek na GitHubie</div></div>
  <div class="stat"><div class="tile t-r"><span class="ic i-download"></span></div><div class="big" style="color:var(--red)">116M</div><div class="lab">pobrań z npm tygodniowo</div></div>
  <div class="stat"><div class="tile t-a"><span class="ic i-users"></span></div><div class="big" style="color:var(--amber)">44.7%</div><div class="lab">developerów używa Reacta</div></div>
  <div class="stat"><div class="tile t-v"><span class="ic i-building-2"></span></div><div class="big" style="color:var(--violet)">8</div><div class="lab">firm w React Foundation</div></div>
</div>
<div class="chips">
  <span class="chip"><span class="ic i-calendar"></span>React Conf</span><span class="chip"><span class="ic i-calendar"></span>React Summit</span><span class="chip"><span class="ic i-star"></span>This Week In React</span><span class="chip"><span class="ic i-code-xml"></span>react.dev</span><span class="chip"><span class="ic i-users"></span>meetupy w Polsce</span>
</div>
</div>
</div>

<!--
- Repozytorium Reacta ma ponad 250 tys. gwiazdek – jedno z najpopularniejszych na GitHubie. Niedawno przeniesione z facebook/react do react/react.
- 44,7% – Stack Overflow Survey 2025.
- Społeczność to nie tylko kod: konferencje (React Conf, React Summit w Amsterdamie, w Polsce meetupy m.in. w Krakowie i Wrocławiu), newslettery, kursy.
- react.dev – dokumentacja przepisana w 2023 od zera, uważana za jedną z najlepszych w branży, z interaktywnymi przykładami.
-->

---

# React Foundation

<div class="sub"><img class="lg s" src="assets/logos/linuxfoundation.svg"> od 24.02.2026 React należy do Linux Foundation, nie do Meta</div>

<div class="fill">
<div class="row" style="gap:30px">
  <div class="card" style="width:230px; text-align:center"><img class="lg l" src="assets/logos/meta.svg"><div class="t" style="margin-top:14px">Meta</div><div class="d">przekazuje React, React Native i JSX</div></div>
  <div class="arrow">→</div>
  <div class="card outline" style="width:780px; padding:24px">
    <div class="row" style="margin-bottom:18px; gap:12px; font-size:20px"><img class="lg" src="assets/logos/react.svg">React Foundation</div>
    <div class="grid4" style="gap:10px">
      <div class="box">Amazon</div>
      <div class="box lime">Callstack</div>
      <div class="box l" style="justify-content:center"><img class="lg s" src="assets/logos/expo.svg">Expo</div>
      <div class="box l" style="justify-content:center"><img class="lg s" src="assets/logos/huawei.svg">Huawei</div>
      <div class="box l" style="justify-content:center"><img class="lg s" src="assets/logos/meta.svg">Meta</div>
      <div class="box l" style="justify-content:center"><span class="ms s"><i></i><i></i><i></i><i></i></span>Microsoft</div>
      <div class="box lime" style="font-size:18px">Software Mansion</div>
      <div class="box l" style="justify-content:center"><img class="lg s" src="assets/logos/vercel.svg">Vercel</div>
    </div>
    <div class="row" style="margin-top:18px; gap:10px; font-size:17px; color:var(--g5)"><span class="dot" style="background:var(--lime); margin:0"></span>firmy z Polski</div>
  </div>
</div>
</div>

<!--
- Ogłoszone na React Conf w październiku 2025, oficjalnie uruchomione 24 lutego 2026.
- Meta przekazała React, React Native i JSX – projekt ma neutralnego właściciela, jak Node.js czy Kubernetes.
- Fundacją kieruje zarząd z przedstawicieli członków; dyrektor wykonawczy: Seth Webster. Zajmuje się infrastrukturą, znakiem towarowym, konferencjami i finansowaniem ekosystemu.
- Kierunek techniczny ma ustalać osobna struktura złożona z kontrybutorów – żadna firma nie może dominować.
- Polski akcent: dwóch z ośmiu członków założycieli to polskie firmy – Callstack i Software Mansion.
-->

---

# React 19.3 (wrzesień 2026)

<div class="fill">
<div class="grid3">
  <div class="card lav2"><div class="tile t-w"><span class="ic i-sparkles" style="color:var(--violet)"></span></div><div class="t">View Transitions</div><div class="d">animacje wejścia, wyjścia i przejść</div></div>
  <div class="card"><div class="tile t-c"><span class="ic i-layers"></span></div><div class="t">Fragment Refs</div><div class="d">ref na grupę elementów: fokus, zdarzenia</div></div>
  <div class="card"><div class="tile t-g"><span class="ic i-monitor"></span></div><div class="t">browser()</div><div class="d">komponent renderowany tylko w przeglądarce</div></div>
  <div class="card"><div class="tile t-r"><span class="ic i-lock"></span></div><div class="t">Trusted Types</div><div class="d">lepsza ochrona przed XSS</div></div>
  <div class="card"><div class="tile t-a"><span class="ic i-git-branch"></span></div><div class="t">Niezależne transitions</div><div class="d">wolna aktualizacja nie blokuje innych</div></div>
  <div class="card"><div class="tile t-v"><span class="ic i-server"></span></div><div class="t">Context w RSC</div><div class="d">bez wrapperów z 'use client'</div></div>
</div>
</div>

<!--
- Najnowsza wersja, 9 września 2026.
- Najbardziej widoczne: <ViewTransition> – natywne animacje przejść między widokami, zintegrowane z Suspense (fallback → treść animuje się płynnie). Teraz stabilne.
- Fragment Refs – coś, o co społeczność prosiła latami.
- use(browser()) – wyłącza renderowanie komponentu na serwerze.
- Kierunek: mniej zewnętrznych bibliotek (animacje, obsługa fokusu), więcej wbudowane.
-->

---

# Kierunki rozwoju

<div class="fill">
<div class="col zoom-s" style="gap:16px; width:100%">
  <div class="row" style="gap:20px"><div class="tile t-v"><span class="ic i-wand-sparkles"></span></div><div class="box l" style="width:330px">ręczna optymalizacja</div><div class="arrow">→</div><div class="box l lav2" style="flex:1">kompilator robi to za ciebie</div></div>
  <div class="row" style="gap:20px"><div class="tile t-c"><span class="ic i-server"></span></div><div class="box l" style="width:330px">wszystko w przeglądarce</div><div class="arrow">→</div><div class="box l cyan" style="flex:1">serwer i klient jako jedno drzewo</div></div>
  <div class="row" style="gap:20px"><div class="tile t-a"><span class="ic i-sparkles"></span></div><div class="box l" style="width:330px">biblioteki do animacji</div><div class="arrow">→</div><div class="box l amber" style="flex:1">wbudowane View Transitions, także w RN</div></div>
  <div class="row" style="gap:20px"><div class="tile t-g"><span class="ic i-users"></span></div><div class="box l" style="width:330px">projekt Meta</div><div class="arrow">→</div><div class="box l lime" style="flex:1">fundacja i otwarte zarządzanie</div></div>
</div>
</div>

<!--
- Cztery trendy na najbliższe lata.
- Kompilator: React Compiler będzie domyślnie włączony w nowych projektach; w przyszłości może umożliwić dalsze optymalizacje.
- Serwer: RSC dojrzewają, więcej frameworków je wspiera (React Router, TanStack Start).
- Platformy: zespół pracuje nad ViewTransition dla React Native; Activity pozwala zachować stan ukrytych widoków.
- Governance: zespół w dużej części dalej w Meta, ale decyzje mają zapadać w otwartym procesie.
-->

---

<!-- header: "" -->
<!-- class: "" -->

# Podsumowanie

<div class="fill">
<div class="grid3">
  <div class="card amber"><div class="tile t-w"><span class="ic i-lightbulb" style="color:var(--amber)"></span></div><div class="n">01</div><div class="t">Jedna idea</div><div class="d">UI = f(state) – niezmienna od 2013 roku, zmieniają się narzędzia</div></div>
  <div class="card cyan"><div class="tile t-w"><span class="ic i-trending-up" style="color:var(--cyan)"></span></div><div class="n">02</div><div class="t">Standard rynkowy</div><div class="d">najpopularniejszy framework frontendowy z największym ekosystemem</div></div>
  <div class="card lime"><div class="tile t-w"><span class="ic i-rocket" style="color:var(--green)"></span></div><div class="n">03</div><div class="t">Dojrzewa</div><div class="d">kompilator, serwer, fundacja – mniej ręcznej pracy, więcej złożoności pod spodem</div></div>
</div>
</div>

<!--
- Trzy rzeczy do zapamiętania.
- Podstawowa idea jest ta sama od 13 lat – to dlatego React jest stabilnym wyborem.
- Jest standardem: rynek pracy, ekosystem, wsparcie.
- Zmienia się: zespół przenosi coraz więcej pracy do kompilatora i serwera; warto śledzić, ale nie trzeba gonić każdej nowości.
-->

---

<!-- _class: black -->
<!-- _paginate: false -->

<div class="orbit">
  <div class="ring" style="width:580px; height:580px"></div>
  <div class="ring d" style="width:450px; height:450px"></div>
  <div class="ring" style="width:310px; height:310px; border-color:rgba(97,218,251,.25)"></div>
  <span class="pl" style="background:var(--lime); transform:rotate(-150deg) translateX(290px)"></span>
  <span class="pl" style="background:var(--violet); transform:rotate(30deg) translateX(290px)"></span>
  <span class="pl" style="background:var(--amber); width:12px; height:12px; transform:rotate(-60deg) translateX(225px)"></span>
  <span class="pl" style="background:var(--red); width:12px; height:12px; transform:rotate(110deg) translateX(225px)"></span>
  <span class="pl" style="background:var(--cyan); width:10px; height:10px; transform:rotate(15deg) translateX(155px)"></span>
  <img class="core" src="assets/logos/react.svg" style="height:230px">
</div>

<div></div>

<div>
  <div class="h1">Dziękuję</div>
  <div class="row" style="margin-top:34px; gap:16px">
    <span class="chip" style="background:var(--lime); color:#000; font-size:24px; padding:10px 20px"><span class="ic i-users" style="width:22px; height:22px"></span>Pytania?</span>
  </div>
</div>

<div></div>

<!--
- Podziękowanie, czas na pytania.
- Możliwe pytania: React vs Vue/Angular – co wybrać? Czy warto uczyć się RSC? Czy Redux jest martwy? – odpowiedzi są w slajdach o ekosystemie.
-->

---

# Źródła

<div class="fill">
<div class="grid2" style="gap:14px 18px">
  <div class="src-card"><div class="tile t-c"><img class="lg" src="assets/logos/react.svg"></div><div><div class="t">React Blog</div><div class="u">react.dev/blog · 19.x, Compiler, CRA</div></div></div>
  <div class="src-card"><div class="tile t-w"><img class="lg" src="assets/logos/linuxfoundation.svg"></div><div><div class="t">React Foundation</div><div class="u">linuxfoundation.org/press</div></div></div>
  <div class="src-card"><div class="tile t-r"><span class="ic i-shield-alert"></span></div><div><div class="t">React2Shell, CVE-2025-55182</div><div class="u">react.dev/blog/2025/12/03</div></div></div>
  <div class="src-card"><div class="tile t-a"><img class="lg" src="assets/logos/stackoverflow.svg"></div><div><div class="t">Developer Survey 2025</div><div class="u">survey.stackoverflow.co/2025</div></div></div>
  <div class="src-card"><div class="tile t-w"><img class="lg" src="assets/logos/npm.svg"></div><div><div class="t">Statystyki pobrań npm</div><div class="u">api.npmjs.org</div></div></div>
  <div class="src-card"><div class="tile t-k"><span class="ic i-github"></span></div><div><div class="t">Repozytorium Reacta</div><div class="u">github.com/react/react</div></div></div>
  <div class="src-card"><div class="tile t-v"><span class="ic i-history"></span></div><div><div class="t">„Rethinking Best Practices”</div><div class="u">Pete Hunt · JSConf US 2013</div></div></div>
  <div class="src-card"><div class="tile t-g"><span class="ic i-palette"></span></div><div><div class="t">Logotypy i ikony</div><div class="u">simpleicons.org · lucide.dev</div></div></div>
</div>
</div>

<!--
- Slajd do pokazania na końcu / do udostępnienia razem z prezentacją.
-->
