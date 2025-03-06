import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Sample data (replace with real portfolio cash flow data)
dates = pd.date_range(start='2020-01-01', end='2024-01-01', freq='M')
assets = ['Mortgages', 'AutoLoans', 'CommLoans']
df = pd.DataFrame(index=dates, columns=assets)
df['Mortgages'] = np.random.normal(1000, 50, len(dates))  # Simulated cash flows
df['AutoLoans'] = np.random.normal(800, 70, len(dates))
df['CommLoans'] = np.random.normal(1200, 100, len(dates))

# Step 1: Prepare cash flow data
cf = df.copy()
window = 12  # Rolling window in months

# Step 2: Calculate rolling volatility
vol = cf.rolling(window=window).std()

# Step 3: Identify high-volatility assets
threshold = vol.quantile(0.75)  # Top 25% as "high volatility"
flags = vol > threshold

# Step 4: Project future volatility (simple extrapolation)
future_dates = pd.date_range(start=dates[-1], periods=13, freq='M')[1:]
last_vol = vol.iloc[-1]
proj_vol = pd.DataFrame(index=future_dates, columns=assets)
for asset in assets:
    proj_vol[asset] = last_vol[asset] * (1 + np.random.normal(0, 0.05, len(future_dates)))

# Step 5: Combine historical and projected volatility
full_vol = pd.concat([vol.dropna(), proj_vol])

# Step 6: Build visualization
fig = go.Figure()
for asset in assets:
    fig.add_trace(go.Scatter(
        x=vol.index, y=vol[asset], mode='lines', name=f'{asset} Hist',
        line=dict(color='#FF6B6B', width=2)  # Reddish for historical
    ))
    fig.add_trace(go.Scatter(
        x=proj_vol.index, y=proj_vol[asset], mode='lines', name=f'{asset} Proj',
        line=dict(color='#4ECDC4', width=2, dash='dash')  # Teal dashed for projected
    ))

# Step 7: Apply dark theme and layout
fig.update_layout(
    title='Asset Cashflow Volatility Tracker',
    xaxis_title='Date',
    yaxis_title='Volatility (Std Dev)',
    plot_bgcolor='rgb(40, 40, 40)',
    paper_bgcolor='rgb(40, 40, 40)',
    font=dict(color='white'),
    xaxis=dict(gridcolor='rgba(255, 255, 255, 0.1)', gridwidth=0.5),
    yaxis=dict(gridcolor='rgba(255, 255, 255, 0.1)', gridwidth=0.5),
    legend=dict(font=dict(color='white')),
    margin=dict(l=50, r=50, t=50, b=50)
)

# Step 8: Display flagged assets
high_vol_assets = flags.iloc[-1][flags.iloc[-1]].index.tolist()
print(f"Assets with high volatility as of {dates[-1].date()}: {high_vol_assets}")

# Step 9: Show plot
fig.show()