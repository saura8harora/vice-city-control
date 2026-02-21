import numpy as np
import pandas as pd
from constants import INITIAL_POPULATION

def create_population():
    data = {
        "respect": np.random.uniform(40, 60, INITIAL_POPULATION),
        "trust": np.random.uniform(40, 60, INITIAL_POPULATION),
        "chaos": np.random.uniform(30, 50, INITIAL_POPULATION),
        "influence": np.random.uniform(0, 1, INITIAL_POPULATION)
    }
    return pd.DataFrame(data)

def apply_rumor(df, impact):
    df["chaos"] += np.random.uniform(0.5, 1.5, len(df)) * impact
    df["trust"] -= np.random.uniform(0.2, 0.7, len(df)) * impact
    return df

def apply_mission(df, boost):
    df["respect"] += np.random.uniform(0.5, 1.5, len(df)) * boost
    df["trust"] += np.random.uniform(0.5, 1.2, len(df)) * boost
    df["chaos"] -= np.random.uniform(0.2, 0.6, len(df)) * boost
    return df

