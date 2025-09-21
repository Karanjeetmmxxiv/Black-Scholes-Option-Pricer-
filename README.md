# Black–Scholes Option Pricer

An interactive **Python/Streamlit** app to price European call and put options using the **Black–Scholes model**.

## Features
- Calculate call & put prices with Black–Scholes formula  
- Interactive inputs for spot, strike, maturity, volatility, risk-free rate, and dividend yield  
- Heatmaps of option values across ranges of spot price × volatility  
- P&L heatmaps (green = profit, red = loss) based on purchase price  

## Live Demo
👉 [Open in Streamlit Cloud](https://ftwbr6tv3bjwrbnfwmg6cx.streamlit.app/)

##vRun Locally
Clone this repo and install dependencies:

```bash
git clone https://github.com/Karanjeetmmxxiv/Black-Scholes-Option-Pricer-.git
cd Black-Scholes-Option-Pricer-
pip install -r requirements.txt
streamlit run app.py
