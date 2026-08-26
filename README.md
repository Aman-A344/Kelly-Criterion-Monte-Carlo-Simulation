# Kelly Criterion Wealth Growth Simulation

A Python simulation exploring the Kelly Criterion in coin-tossing games over 1,000 rounds across 10,000 runs. It demonstrates optimal capital growth, compares experimental median paths with theoretical compounding rates, and visualizes how log-wealth optimization protects against long-term risk of ruin.

Simulator.png

## Overview

When trading or betting with an edge, risking too much leads to catastrophic loss, while risking too little underutilizes the edge. The **Kelly Criterion** determines the optimal fraction of total wealth to wager on each trial to maximize expected logarithmic wealth over time:

$$f^* = p - q = 2p - 1$$

Where:
* $p = 0.52$ (Win Probability)
* $q = 0.48$ (Loss Probability)
* Optimal Fraction $f^* = 0.04$ (4% of current bankroll per wager)

## Key Concepts Demonstrated

* **Median vs. Mean Divergence:** Shows how the exponential right skew of wealth distributions makes the mean misleading due to extreme high-earning outliers, whereas the median closely tracks theoretical expectations.
* **Theoretical Growth Rate ($g$):** Computes the expected compound growth per round using log-returns:
  $$g = p \ln(1 + f) + (1 - p) \ln(1 - f)$$
* **Monte Carlo Visualizations:** Uses `matplotlib` to graph the 99th-percentile final wealth distribution alongside the geometric path progression against theoretical bounds.
