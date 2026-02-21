def calculate_respect(df):
    return df["respect"].mean()

def calculate_trust(df):
    return df["trust"].mean()

def calculate_chaos(df):
    return df["chaos"].mean()

def calculate_heat(chaos):
    return min(max(chaos * 1.2, 0), 100)

def calculate_civic_points(respect, trust):
    return (respect + trust) / 2
def misinfo_radar(chaos, trust):
    """
    Returns (level, score) where level is one of:
    'STABLE', 'TENSION', 'WAVE'
    """
    # Score rises when chaos high and trust low
    score = (chaos * 1.2) + ((100 - trust) * 0.8)
    score = max(min(score, 200), 0)

    if score >= 140:
        return "WAVE", score
    elif score >= 90:
        return "TENSION", score
    return "STABLE", score


def crisis_playbook(level):
    """
    Simple, judge-friendly recommended actions.
    """
    if level == "WAVE":
        return [
            "Deploy trusted micro-influencers with consistent messaging",
            "Launch a Civic Quest to convert panic into participation",
            "Push transparency updates (facts + next steps) every 15 min"
        ]
    if level == "TENSION":
        return [
            "Boost community leaders’ visibility (trusted voices)",
            "Post 'myth vs fact' mini-bullets in Vice Radio ticker",
            "Reward cooperation with civic points"
        ]
    return [
        "Maintain steady comms cadence",
        "Keep missions running to sustain civic engagement",
        "Monitor trust trend for sudden drops"
    ]