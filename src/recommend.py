def recommend_resources(cluster):
    if cluster == 0:
        return [
            "Start with basics: Python fundamentals",
            "Watch short concept videos",
            "Practice daily for 30 minutes"
        ]
    elif cluster == 1:
        return [
            "Advanced AI/ML courses",
            "Hands-on projects",
            "Competitive programming challenges"
        ]
    elif cluster == 2:
        return [
            "Intermediate ML tutorials",
            "Focus on weak subjects",
            "Increase practice consistency"
        ]
    else:
        return ["No recommendation available"]
