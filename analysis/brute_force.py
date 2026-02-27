def estimate_cracking_time(entropy):

    guesses_per_second = 10**10
    
    total_combinations = 2**entropy
    
    seconds = total_combinations / guesses_per_second
    
    if seconds < 60:
        return f"{round(seconds, 2)} Seconds"
    elif seconds < 3600:
        return f"{round(seconds/60, 2)} Minutes"
    elif seconds < 86400:
        return f"{round(seconds/3600, 2)} Hours"
    elif seconds < 31536000:
        return f"{round(seconds/86400, 2)} Days"
    else:
        return f"{round(seconds/31536000, 2)} Years"
