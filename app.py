import numpy as np
import matplotlib.pyplot as plt
import streamlit as st 
from src.black_scholes import bs_call_price, bs_put_price

st.set_page_config(page_title='Black Scholes Heatmap', layout='wide')
st.title("Black Scholes Options price and Heatmap")

with st.sidebar:
    
    st.subheader("Base Parameters")
    S = st.number_input("Spot (S)", value=100.0, step=1.0)
    K = st.number_input("Strike (K)", value=100.0, step=1.0)
    T = st.number_input("TIme to expiry (years, T)", value=1.0, step=0.01)
    r = st.number_input("Risk-free rate (r, as a decimal)", value=0.03, step=0.001, format="%.4f")
    sigma = st.number_input("Volatility (σ, e.g. 0.20 = 20%)", value=0.20, step=0.01, format="%.4f")
    q = st.number_input("Dividend yield (q)", value=0.0, step=0.001, format="%.4f")

    st.subheader("Heatmap Ranges")
    spot_min = st.number_input("Min Spot price", value=80.0, step=1.0)
    spot_max = st.number_input("Max Spot price", value=120.0, step=1.0)

    vol_min = st.number_input("Min Volatility of σ", value=0.10, step=0.01, format="%.4f")
    vol_max = st.number_input("Max Volatility of σ", value=0.40, step=0.01, format="%.4f")

    n_spots = st.slider("Spot grid size", min_value=10, max_value=60, value=30, step=5)
    n_vols  = st.slider("Vol grid size",  min_value=10, max_value=60, value=30, step=5)

    generate = st.button("Generate Heatmaps")

def compute_grids(K, T, r, q, spot_min, spot_max, vol_min, vol_max, n_spots, n_vols):

    spots = np.linspace(spot_min, spot_max, n_spots)
    
    vols = np.linspace(vol_min, vol_max, n_vols)

    call = np.empty((n_vols, n_spots))
    put = np.empty_like(call)

    for i, v in enumerate(vols):
        for j, s in enumerate(spots):
            call[i, j] = bs_call_price(s, K, T, r, v, q)
            put[i,  j] = bs_put_price (s, K, T, r, v, q)

    return spots, vols, call, put

def plot_heatmap(Z, spots, vols, title, cbar_label):
    
    fig, ax = plt.subplots()  
    im = ax.imshow(Z, extent=[spots.min(), spots.max(), vols.min(), vols.max()], origin="lower", aspect="auto", cmap="viridis",)
    
    ax.set_xlabel("Spot Price")
    ax.set_ylabel("Volatility (σ)")
    ax.set_title(title)
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label(cbar_label)  # Label on the color scale
    return fig   

if generate:
    if spot_max <= spot_min or vol_max <= vol_min:
        st.error("Max must be greater than Min for both Spot and Volatility.")
        st.stop()
    elif T <= 0:
        st.error("Time to maturity T must be > 0.")
        st.stop()

    spots, vols, call_Z, put_Z = compute_grids(K, T, r, q, spot_min, spot_max, vol_min, vol_max, n_spots, n_vols)

    c1, c2 = st.columns(2)
    with c1:
            st.subheader("Call Price Heatmap")
            st.pyplot(plot_heatmap(call_Z, spots, vols, "Call Price", "Call Value"))

    with c2:
            st.subheader("Put Price Heatmap")
            st.pyplot(plot_heatmap(put_Z, spots, vols, "Put Price", "Put Value"))

    with st.expander("Single-point check at base S and mid σ"):
        sig_mid = (vol_min + vol_max) / 2

        
        st.write(f"σ(mid) = {sig_mid:.4f}")
        st.write(f"Call(S={S}): **{bs_call_price(S,K,T,r,sig_mid,q):.4f}**")
        st.write(f"Put (S={S}): **{bs_put_price (S,K,T,r,sig_mid,q):.4f}**")

else:
    st.info("Set parameters in the sidebar, then click **Generate Heatmaps**.")    
