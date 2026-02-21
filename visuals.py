import matplotlib.pyplot as plt
import numpy as np


def city_pulse_meter(value):
    value = max(min(value, 100), 0)

    fig, ax = plt.subplots(figsize=(3, 3))

    # Make transparent
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    theta = np.linspace(0, 2*np.pi, 200)

    # Neon ring outline
    ax.plot(np.cos(theta), np.sin(theta), linewidth=3, color="#00f0ff")

    # Fill arc
    fill_angle = 2*np.pi * (value / 100)
    t_fill = np.linspace(0, fill_angle, 200)
    ax.fill(
        np.cos(t_fill),
        np.sin(t_fill),
        color="#ff2bd6",
        alpha=0.5
    )

    # Center text
    ax.text(
        0, 0,
        f"{int(value)}%",
        ha="center",
        va="center",
        fontsize=18,
        color="white",
        fontweight="bold"
    )

    ax.set_title("CITY PULSE", fontsize=12, color="white")

    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")

    # Remove borders
    for spine in ax.spines.values():
        spine.set_visible(False)

    return fig


def influencer_network(df):
    fig, ax = plt.subplots(figsize=(4, 3))

    # Make transparent
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    ax.scatter(
        df["influence"],
        df["respect"],
        alpha=0.7,
        s=25,
        color="#00f0ff"
    )

    ax.set_title("INFLUENCER NETWORK", fontsize=11, color="white")
    ax.set_xlabel("Influence", color="white")
    ax.set_ylabel("Respect", color="white")

    # White ticks
    ax.tick_params(colors="white")

    # Remove borders
    for spine in ax.spines.values():
        spine.set_visible(False)

    return fig