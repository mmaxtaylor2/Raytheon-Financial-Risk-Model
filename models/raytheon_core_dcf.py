"""
Raytheon-Style Program Finance Model
Core DCF Engine with CSV Inputs + Risk Hooks
"""

import numpy as np
import pandas as pd
import os
import numpy_financial as nf   # <-- CORRECT MODULE NAME

# ------------------------------------------------------
# FILE PATH SETUP
# ------------------------------------------------------
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ------------------------------------------------------
# LOAD INPUTS FROM CSV FILES
# ------------------------------------------------------
def load_inputs():
    revenue_df = pd.read_csv(f"{BASE_PATH}/assumptions/cost_escalation_inputs.csv")
    fx_df = pd.read_csv(f"{BASE_PATH}/assumptions/fx_sensitivity_inputs.csv")
    wacc_df = pd.read_csv(f"{BASE_PATH}/assumptions/wacc_inputs.csv")

    return {
        "revenue_forecast": revenue_df["revenue"].tolist(),
        "operating_margin": revenue_df["operating_margin"].iloc[0],
        "tax_rate": revenue_df["tax_rate"].iloc[0],
        "terminal_growth": revenue_df["terminal_growth"].iloc[0],
        "discount_rate": wacc_df["wacc"].iloc[0],
        "fx_risk_adjustment": fx_df["fx_adjustment"].iloc[0],
        "cost_escalation_adjustment": revenue_df["escalation"].iloc[0]
    }

# ------------------------------------------------------
# CORE DCF CALCULATION
# ------------------------------------------------------
def calculate_dcf(revenue, margin, tax, wacc, g, fx_adj=0, cost_adj=0):

    adjusted_margin = margin * (1 + fx_adj + cost_adj)
    operating_income = [r * adjusted_margin for r in revenue]
    after_tax_cash = [oi * (1 - tax) for oi in operating_income]

    terminal_value = after_tax_cash[-1] * (1 + g) / (wacc - g)
    cash_flows = after_tax_cash[:-1] + [after_tax_cash[-1] + terminal_value]

    discounted = [cf / ((1 + wacc) ** (i + 1)) for i, cf in enumerate(cash_flows)]

    npv = sum(discounted)

    # CORRECT IRR FUNCTION
    irr = nf.irr([-sum(after_tax_cash)*0.1] + after_tax_cash)

    return {
        "NPV": npv,
        "IRR": irr,
        "Adjusted Margin": adjusted_margin,
        "Cash Flows": cash_flows
    }

# ------------------------------------------------------
# MAIN EXECUTION BLOCK
# (Ensures the script runs when executed directly)
# ------------------------------------------------------
if __name__ == "__main__":
    inputs = load_inputs()

    results = calculate_dcf(
        inputs["revenue_forecast"],
        inputs["operating_margin"],
        inputs["tax_rate"],
        inputs["discount_rate"],
        inputs["terminal_growth"],
        fx_adj=inputs["fx_risk_adjustment"],
        cost_adj=inputs["cost_escalation_adjustment"]
    )

    go_no_go_threshold = 0
    required_irr = 0.10

    decision = "GO" if (results["NPV"] > go_no_go_threshold 
                        and results["IRR"] > required_irr) else "NO-GO"

    print("\n================ RAYTHEON-STYLE PROGRAM FINANCE MODEL ================\n")
    print(f"Adjusted Operating Margin:  {results['Adjusted Margin']:.2%}")
    print(f"NPV:                        ${results['NPV']:,.0f}")
    print(f"IRR:                        {results['IRR']:.2%}\n")

    print("Cash Flows:")
    for i, cf in enumerate(results['Cash Flows'], 1):
        print(f"Year {i}: ${cf:,.0f}")

    print("\n==================== DECISION ====================")
    print(f"NPV Requirement:            > $0")
    print(f"IRR Requirement:            > {required_irr:.2%}")
    print(f"Program Status:             {decision}")
    print("=================================================\n")
