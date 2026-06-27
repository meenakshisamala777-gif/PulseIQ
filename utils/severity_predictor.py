def predict_severity(emergency_type):

    if emergency_type == "Heart Attack":
        return "🔴 Critical"

    elif emergency_type == "Stroke":
        return "🔴 Critical"

    elif emergency_type == "Accident":
        return "🟠 High"

    elif emergency_type == "Burn Injury":
        return "🟠 High"

    elif emergency_type == "Pregnancy":
        return "🟡 Medium"

    else:
        return "🟢 Low"