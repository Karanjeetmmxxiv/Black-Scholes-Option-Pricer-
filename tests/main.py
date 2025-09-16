import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.black_scholes import bs_call_price, bs_put_price


S,K,T,r,sigma = 100,100,1.0,0.03,0.20
print("Call:", bs_call_price(S,K,T,r,sigma))
print("Put :", bs_put_price(S,K,T,r,sigma))