from datetime import datetime, timedelta

# time
def parse_time(t):
    return datetime.strptime(t, "%H:%M")

def diff_hours(t_start, t_end):
    start = parse_time(t_start)
    end = parse_time(t_end)

    # 处理跨午夜
    if end < start:
        end += timedelta(days=1)

    return (end - start).seconds / 3600
def to_hour(t):
    h, m = t.split(":")
    return int(h) + int(m)/60


# rating
def compute_sleep_metrics(t1, t2, t3, t4, w):

    sleep_duration = diff_hours(t2, t3)
    bed_duration = diff_hours(t1, t4)

    bed_duration = max(bed_duration, 0.1)

    sleep_score = min((sleep_duration / 7) * 100, 100)

    awakenings = w
    awaken_penalty = w * 5

    efficiency = (sleep_duration / bed_duration) * 100

    sleep_quality = efficiency - awaken_penalty
    sleep_quality = max(min(sleep_quality, 100), 0)

    overall = (sleep_score + sleep_quality) / 2
    
    comments = []

    if to_hour(t2) > 23.5:
        comments.append("You went to sleep too late (after 23:30). This may affect sleep quality.")

    if to_hour(t4) < 6.5:
        comments.append("You woke up too early (before 6:30).")

    if to_hour(t4) > 8:
        comments.append("You woke up late (after 08:00).")

    if len(comments) == 0:
        comments.append("Your sleep schedule looks stable today.")

    if w > 1:
        comments.append("You woke up more than once during the night, which may reduce sleep quality.")
    sleep_risk = get_risk_level(sleep_score)
    quality_risk = get_risk_level(sleep_quality)
    overall_risk = get_risk_level(overall)
    
    return {
    "sleep_duration": round(sleep_duration, 2),
    "bed_duration": round(bed_duration, 2),
    "sleep_score": round(sleep_score, 2),
    "awakenings": awakenings,
    "sleep_quality": round(sleep_quality, 2),
    "overall": round(overall, 2),

    "t1": time_to_percent(t1),
    "t2": time_to_percent(t2),
    "t3": time_to_percent(t3),
    "t4": time_to_percent(t4),
    
    "comments": comments,
    
    "sleep_risk": sleep_risk,
    "quality_risk": quality_risk,
    "overall_risk": overall_risk,
    }

def get_risk_level(score):
    if score >= 80:
        return "good"
    elif score >= 60:
        return "warning"
    else:
        return "danger"

def time_to_percent(t):
    h, m = t.split(":")
    return (int(h) + int(m)/60) / 24 * 100