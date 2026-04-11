def explain_threat(log):

    log = log.lower()

    if "failed login" in log:
        return "Multiple failed login attempts detected. Possible brute force attack."

    elif "brute force" in log:
        return "Brute force attack pattern detected. Attacker trying many passwords."

    elif "reset" in log:
        return "Multiple password reset attempts. Suspicious account activity."

    elif "sql injection" in log:
        return "SQL Injection attack detected. Malicious database query attempt."

    elif "normal login" in log:
        return "Normal user login activity. No threat detected."

    else:
        return "Unknown activity. Monitoring recommended."