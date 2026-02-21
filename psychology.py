import numpy as np
import pandas as pd
from constants import TRAIT_RANGE, POPULATION_SIZE


# ------------------------------
# CREATE PSYCHOLOGICAL PROFILES
# ------------------------------

def generate_psychological_traits(size=POPULATION_SIZE):
    """
    Generate psychological traits for each citizen.
    All traits are between 0 and 1.
    """

    low, high = TRAIT_RANGE

    traits = pd.DataFrame({
        "fear_sensitivity": np.random.uniform(low, high, size),
        "conformity": np.random.uniform(low, high, size),
        "reactance": np.random.uniform(low, high, size),
        "authority_bias": np.random.uniform(low, high, size),
        "social_proof": np.random.uniform(low, high, size),
        "critical_thinking": np.random.uniform(low, high, size),
    })

    return traits


# ------------------------------
# CITY-WIDE PSYCHOLOGICAL SUMMARY
# ------------------------------

def calculate_psychology_summary(df):
    """
    Returns city-wide average psychological traits.
    """

    summary = {
        "fear_sensitivity": df["fear_sensitivity"].mean(),
        "conformity": df["conformity"].mean(),
        "reactance": df["reactance"].mean(),
        "authority_bias": df["authority_bias"].mean(),
        "social_proof": df["social_proof"].mean(),
        "critical_thinking": df["critical_thinking"].mean(),
    }

    return summary


# ------------------------------
# MANIPULATION VULNERABILITY INDEX
# ------------------------------

def calculate_vulnerability_index(summary):
    """
    Higher score = more psychologically vulnerable city.
    """

    vulnerability = (
        summary["fear_sensitivity"] * 0.4 +
        summary["conformity"] * 0.3 +
        summary["social_proof"] * 0.3 -
        summary["critical_thinking"] * 0.5 -
        summary["reactance"] * 0.2
    )

    # Normalize between 0 and 100
    vulnerability = max(min(vulnerability * 100, 100), 0)

    return vulnerability