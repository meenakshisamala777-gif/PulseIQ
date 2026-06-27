def get_priority(emergency):

    if emergency in ["Heart Attack", "Stroke"]:
        return "🔴 Critical"

    elif emergency in ["Accident", "Burn Injury"]:
        return "🟠 High"

    elif emergency == "Pregnancy":
        return "🟡 Medium"

    else:
        return "🟢 Low"