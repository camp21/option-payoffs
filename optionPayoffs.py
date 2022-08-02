import time
import datetime as dt
from math import sqrt, pi

import numpy as np
import matplotlib as mat

import matplotlib.pyplot as plt
plt.style.use("ggplot")

from mpl_toolkits.mplot3d import Axes3D

#underlying stock price
S = 65.0

# series of underlying stock prices to demonstrate a payoff profile
sSeries = np.arange(S - 10, S + 10, 0.01)

# strike price
K = 65.0

# time to expiration
t = 180.0 / 365.0

# risk free rate
r = 0.015

# volatility 
vol = 0.3

atm_call_prem = 3.30
atm_put_prem = 2.9

otm_call_prem = 1.36
otm_put_prem = 0.90

# def call_payoff(S, K_): 
    # return np.maximum(S - K, 0.0)
call_payoff = lambda S, K: np.maximum(sSeries - K, 0.0)

# def put_payoffs (S, K):
    # return np.maximum(K - S, 0.0)
put_payoff = lambda S, K: np.maximum(K - sSeries, 0.0)

# plot the call payoff
plt.figure(1, figsize=(7, 4))
plt.title("Call option payoff at expiration")
plt.xlabel("Underlying stock price, S")
plt.axhline(y=0, lw=1, c="grey")
plt.plot(sSeries, -atm_call_prem + call_payoff(sSeries, K))

# plot the put payoff
plt.figure(2, figsize=(7, 4))
plt.title("Put option payoff at expiration")
plt.xlabel("Underlying stock price, S")
plt.axhline(y=0, lw=1, c="grey")
plt.plot(sSeries, -atm_put_prem + put_payoff(sSeries, K))

# plot a long straddle payoff
long_straddle = call_payoff(sSeries, K) + put_payoff(sSeries, K)
long_straddle_prem = -atm_call_prem - atm_put_prem
plt.figure(3, figsize=(7,4))
plt.title("Long straddle payoff at expiration")
plt.xlabel("Underlying stock price, S")
plt.axhline(y=0, lw=1, c="grey")
plt.plot(sSeries, long_straddle_prem + long_straddle)

# plot a short straddle payoff
short_straddle = -call_payoff(sSeries, K) - put_payoff(sSeries, K)
short_straddle_prem = atm_call_prem + atm_put_prem
plt.figure(4, figsize=(7, 4))
plt.title("Short straddle payoff at expiration")
plt.xlabel("Underlying stock price, S")
plt.axhline(y=0, lw=1, c="grey")
plt.plot(sSeries, short_straddle_prem - long_straddle)

# plot a short iron condor payoff
short_iron_condor = (
    call_payoff(sSeries, K + 5) 
    - call_payoff(sSeries, K)
    - put_payoff(sSeries, K) 
    + put_payoff(sSeries, K - 5)
)

short_iron_condor_prem = (
    -otm_call_prem + atm_call_prem + atm_put_prem - otm_put_prem
)

plt.figure(5, figsize=(7, 4))
plt.title("Short iron condor payoff at expiration")
plt.xlabel("Underlying stock price, S")
plt.axhline(y=0, lw=1, c="grey")
plt.plot(sSeries, short_iron_condor_prem + short_iron_condor)






