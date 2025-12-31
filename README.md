# Raytheon-Style Financial Risk & Valuation Model
A hybrid capital-markets and program finance study evaluating whether RTX (Raytheon Technologies) is fairly valued, undervalued, or overvalued given current sector fundamentals, risk-adjusted cash flow assumptions, and peer pricing.

---

## Project Objective
Determine if RTX’s current market pricing is justified by operating performance, sector dynamics, and risk-adjusted fundamentals — or if a pricing dislocation exists that creates upside/downside opportunity.

This project simulates a workflow commonly used in:
- Capital Markets / Investment Analyst roles
- FP&A with external market alignment
- Program Finance & Defense Sector Cost Modeling
- Corporate Strategy / Competitive Benchmarking

---

## Repository Structure

| Folder | Contents |
|--------|-----------|
| `/models` | Core DCF engine with FX + cost escalation hooks |
| `/scripts` | Data pull, chart generation, and comps builder |
| `/data` | Price history, fundamentals, and benchmarking outputs |
| `/charts` | RTX vs sector charts and peer performance visuals |
| `/memo` | 1–2 page program finance & valuation memo (PDF/MD) |
| `README.md` | Project overview and guidance for recruiters/interviewers |

---

## Methodology Summary

**Valuation**
- 5-Year DCF with terminal growth and WACC sensitivity
- FX and cost escalation adjustments applied to operating margins
- IRR threshold testing (10% hurdle assumption)

**Market Validation**
- RTX, LMT, GD, NOC, ITA downloaded via `yfinance`
- Peer multiples: EV/EBITDA, P/FCF, Revenue CAGR
- Sector benchmarking to confirm pricing alignment

**Decision Framework**
- Positive NPV required for “Go”
- IRR > hurdle + WACC spread for value creation
- FX + escalation risk determine operational confidence

---

## Key Results

| Outcome | Result |
|---------|---------|
| Conclusion | RTX trades near fair value |
| Upside Case | Requires margin expansion or lower discount rate |
| Downside Case | Cost pressures + contracting cycle risk |
| Peer Position | RTX sits middle-of-pack in sector multiples |

**High-Level Interpretation:** RTX is not mispriced.  
It does not screen as a value opportunity like NOC or a premium name like GD.

---

## Visual Outputs

**RTX vs ITA (Sector Benchmark)**  
`/charts/rtx_vs_ita.png`

**RTX vs Defense Peers (LMT, GD, NOC)**  
`/charts/rtx_vs_peers.png`

---

## Where to Look (For Recruiters or Hiring Managers)

If you're reviewing this project, start with:
1. `memo/RTX_Program_Finance_Memo.md / .pdf` — business case & conclusion
2. `models/raytheon_core_dcf.py` — valuation logic
3. `scripts/rtx_data_pull.py` — market validation workflow
4. `charts/` — visual context of results

---
