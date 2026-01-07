# Raytheon Financial Risk & Resilience Analysis  
**Rate Sensitivity, Cost Escalation, and Valuation Stability Case Study**

**View-Only Model (Google Sheets):**  
https://docs.google.com/spreadsheets/d/1xDqe5Ms85I5aapY7dcH9hZSisjrabVbkXWgWOXCfNg4/edit?usp=sharing

---

## Business Question
How resilient is RTX’s valuation and financial profile if interest rates remain elevated and defense-sector cost pressures persist?

This project evaluates whether RTX’s current market pricing is supported by realistic assumptions around discount rates, margin durability, and operating risk — or whether downside risk emerges under a higher-for-longer rate environment.

---

## Why This Matters
In long-cycle, capital-intensive industries such as defense, valuation risk is often driven less by revenue growth and more by **discount rates, cost escalation, and cash-flow durability**.

As interest rates rise and input costs remain volatile, FP&A, treasury, and strategy teams must understand:
- How sensitive enterprise value is to changes in WACC  
- Whether margins can absorb cost pressure without eroding returns  
- How valuation confidence changes under downside macro scenarios  

This analysis mirrors the type of stress testing used in:
- Corporate FP&A and long-range planning  
- Treasury and capital allocation decisions  
- Defense program finance and contract evaluation  

---

## Analytical Framework
The model is structured as a **financial risk and valuation-stability assessment**, rather than a pure equity-selection exercise:

- Discounted cash flow framework with explicit WACC sensitivity  
- Margin and cost-escalation stress testing  
- Scenario analysis across base, upside, and downside cases  
- Peer benchmarking to contextualize valuation outcomes  
- Decision thresholds based on NPV and IRR relative to WACC  

All outputs are directly linked to rate, cost, and operating assumptions to ensure traceability and transparency.

---

## Analytical Tooling & Validation
The analysis combines spreadsheet-based financial modeling with Python-based market validation to ensure conclusions are both internally consistent and externally grounded.

Google Sheets was used as the primary modeling environment for:
- Discounted cash flow construction
- Rate and cost sensitivity analysis
- Scenario modeling and valuation interpretation

Python was used to support and validate the analysis by:
- Pulling historical price and peer data (RTX, LMT, GD, NOC, ITA)
- Normalizing valuation multiples for cross-company comparison
- Generating benchmark and sensitivity visuals
- Cross-checking model conclusions against observed market pricing

This hybrid workflow mirrors how finance teams use programmatic tools to validate spreadsheet-driven conclusions rather than replacing judgment with automation.

---

## Key Assumptions
- Interest rates remain structurally higher relative to the prior decade  
- Cost escalation pressure persists across labor and materials  
- Defense demand remains stable, but margin expansion is constrained  
- Valuation decisions must clear both IRR hurdles and WACC-based thresholds  

Assumptions are intentionally conservative to test **valuation durability**, not to optimize upside scenarios.

---

## Key Findings
- RTX trades near fair value under base-case assumptions  
- Upside scenarios require either margin expansion or a lower discount rate  
- Downside risk emerges if cost pressures persist alongside elevated rates  
- Relative to peers, RTX sits middle-of-the-pack on valuation multiples rather than screening as a clear value opportunity  

Overall, valuation outcomes are more sensitive to **rates and cost structure** than to top-line growth assumptions.

---

## Decision Implications
- Capital allocation decisions should prioritize margin resilience over growth optimism  
- Valuation confidence depends heavily on discount-rate assumptions in a higher-rate regime  
- Management guidance should be evaluated through a rate- and cost-adjusted lens  
- RTX appears better suited for stability-oriented portfolios than for aggressive re-rating strategies  

This project demonstrates how finance teams translate macro conditions into **risk-aware valuation judgment**, not just point estimates.

---

## Supporting Context
*A short executive memo summarizing the program-finance logic and valuation conclusions is included in the repository for additional context.*

---

## Appendix: Model Screenshots (Executive Review Views)

*Screenshots reflect executive-level outputs and decision-support views.  
The full underlying model is maintained in Google Sheets.*

### RTX Public Data & Baseline Inputs
![RTX Public Data]([assets/1.png)

### Valuation Sensitivity (Rates & Cost Pressure)
![RTX Sensitivity](assets/RTX_Sensitivity.png)

### Scenario Outcomes (Base / Upside / Downside)
![RTX Scenarios](assets/RTX_Scenarios.png)



