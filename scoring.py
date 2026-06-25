def calculate_score(candidate_skills, required_skills):

    matched = set(candidate_skills).intersection(
        set(required_skills)
    )

    score = (len(matched) / len(required_skills)) * 100

    return round(score, 2), list(matched)