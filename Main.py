import random
import numpy as np
import matplotlib.pyplot as plt

# Simulation Parameters
starting_wealth = 100
win_probability = 0.52
num_rounds = 1000
num_simulations = 10000

# Kelly Criterion for symmetric/even-money bet
f = 2 * win_probability - 1

# Theoretical Expected Wins
expected_wins = win_probability * num_rounds

# Run Simulations
wealth_paths = []
experimental_wins = []

for simulation in range(num_simulations):

    # Start each simulation at $100
    wealth_path = [starting_wealth]
    num_wins = 0

    for round in range(num_rounds):

        random_int = random.randint(1, 100)

        if random_int <= win_probability * 100:
            num_wins += 1
            new_wealth = wealth_path[-1] * (1 + f)
        else:
            new_wealth = wealth_path[-1] * (1 - f)

        wealth_path.append(new_wealth)

    # Save the complete wealth path
    wealth_paths.append(wealth_path)

    # Save number of wins for this simulation
    experimental_wins.append(num_wins)

# Final Wealth of Each Simulation
final_wealths = []

for path in wealth_paths:
    final_wealths.append(path[-1])

# Median Wealth Path
median_wealth_path = []

for i in range(num_rounds + 1):

    wealth_at_round = []

    for path in wealth_paths:
        wealth_at_round.append(path[i])

    median = np.median(wealth_at_round)
    median_wealth_path.append(median)

# Theoretical Kelly Growth Path

# Expected logarithmic growth per round
g = (win_probability * np.log(1 + f) + (1 - win_probability) * np.log(1 - f)
)

theoretical_wealth_path = []

for i in range(num_rounds + 1):
    theoretical_wealth = starting_wealth * np.exp(g * i)
    theoretical_wealth_path.append(theoretical_wealth)

# Log Final Wealth
log_final_wealths = np.log(final_wealths)

# Results
print("Kelly fraction:", f)
print("Theoretical expected wins:", expected_wins)
print("Average simulated wins:", np.mean(experimental_wins))
print("Median final wealth:", np.median(final_wealths))
print("Mean final wealth:", np.mean(final_wealths))
print("Mean log final wealth:", np.mean(log_final_wealths))
print("Theoretical final wealth:", theoretical_wealth_path[-1])

# Plots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Distribution of Final Wealth
mean_final_wealth = np.mean(final_wealths)
median_final_wealth = np.median(final_wealths)

axes[0].hist(
    final_wealths,
    bins=100,
    edgecolor="black",
    linewidth=0.5,
    alpha=0.75
)

# Mean and median lines
axes[0].axvline(
    mean_final_wealth,
    color="red",
    linestyle="--",
    linewidth=2.5,
    zorder=10,
    label=f"Mean = ${mean_final_wealth:,.0f}"
)

axes[0].axvline(
    median_final_wealth,
    color="blue",
    linestyle="--",
    linewidth=2.5,
    zorder=10,
    label=f"Median = ${median_final_wealth:,.0f}"
)

# Keep the useful x-axis range
axes[0].set_xlim(0, np.percentile(final_wealths, 99))

axes[0].set_title("Distribution of Final Wealth")
axes[0].set_xlabel("Final Wealth ($)")
axes[0].set_ylabel("Number of Simulations")
axes[0].legend()

# Plot 2: Median Path + Kelly Growth Path
axes[1].plot(median_wealth_path, label="Median Simulated Wealth")
axes[1].plot(theoretical_wealth_path, label="Kelly Theoretical Growth")
axes[1].set_title("Median Wealth Path vs. Kelly Growth")
axes[1].set_xlabel("Round")
axes[1].set_ylabel("Wealth ($)")
axes[1].legend()

plt.tight_layout()
plt.show()
