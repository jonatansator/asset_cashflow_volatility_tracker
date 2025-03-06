# asset_cashflow_volatility_tracker

- This Python tool tracks historical and projected volatility in cash flows from a lending portfolio’s assets (e.g., residential mortgages, commercial loans).
- It uses rolling standard deviation of cash flow data and flags assets with high volatility for closer monitoring, outputting a simple dashboard for risk oversight.

---

## Files
- `asset_cashflow_vol_tracker.py`: Main script for calculating cash flow volatility, projecting future trends, and visualizing results with Plotly.
- `output.png`: Plot

---

## Libraries Used
- `pandas`
- `numpy`
- `plotly`

---

## Features
- **Data Setup**: Generates synthetic monthly cash flow data for assets like Mortgages, AutoLoans, and CommLoans (replaceable with real data).
- **Volatility Calculation**: Computes rolling standard deviation over a 12-month window to measure historical cash flow volatility.
- **High-Volatility Flags**: Identifies assets in the top 25% of volatility for monitoring.
- **Projection**: Extrapolates future volatility for 12 months using the last historical value with random noise.
- **Visualization**: Plots historical (solid red lines) and projected (dashed teal lines) volatility for each asset using Plotly.
