import pandas as pd

def recommend_hospital(df, emergency_type):

    def emergency_match(specialists):
        specialists = specialists.lower()

        if emergency_type == "Heart Attack" and "cardiology" in specialists:
            return 10

        elif emergency_type == "Stroke" and "neurology" in specialists:
            return 10

        elif emergency_type == "Accident" and "trauma" in specialists:
            return 10

        elif emergency_type == "Pregnancy" and "pediatrics" in specialists:
            return 10

        return 5

    df = df.copy()

    df["score"] = (
        df["available_beds"] * 0.4
        + df["available_icu"] * 0.3
        + df["ambulances"] * 0.2
        + df["specialists"].apply(emergency_match) * 0.1
    )

    return df.sort_values(by="score", ascending=False).iloc[0]