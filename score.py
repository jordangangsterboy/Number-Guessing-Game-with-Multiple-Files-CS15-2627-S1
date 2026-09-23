def update_score(score:int):
    if score > 10:
        return score - 10
    return 0

def get_rating(score:int):
    if score >= 80:
        return "Excellent"
    if score >= 50:
        return "Good"
    return "Keep Practicing"

if __name__ == "__main__":
    pass