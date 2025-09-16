import math

def norm_cdf(x: float) -> float:
    return 0.5*(1.0 + math.erf(x/math.sqrt(2.0)))

def bs_call_price(S, K, T, r, sigma, q=0.0):

    if T <= 0:
        return max(0.0, S - K)
    if sigma <= 0:
        max(0.0, S*math.exp(-q*T) - K*math.exp(-r*T))

    d1 = (math.log(S/K) + (r - q + 0.5*sigma*sigma)*T) / (sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)

    call = S * math.exp(-q*T) * norm_cdf(d1) - K*math.exp(-r * T) * norm_cdf(d2)
    return call

def bs_put_price(S, K, T, r, sigma, q=0.0):
    if T <= 0:
        return max(0.0, K - S)
    if sigma <= 0:
        return max(0.0, K*math.exp(-r*T) - S*math.exp(-q*T))

    d1 = (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    put = K * math.exp(-r * T) * norm_cdf(-d2) - S * math.exp(-q * T) * norm_cdf(-d1)
    return put