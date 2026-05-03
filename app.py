from flask import Flask, render_template, request
from utils import compute_sleep_metrics

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sleep")
def sleep():
    return render_template("sleep.html")

@app.route("/result", methods=["POST"])
def result():

    t1 = request.form["bed_time"]
    t2 = request.form["sleep_time"]
    t3 = request.form["wake_time"]
    t4 = request.form["getup_time"]
    w = int(request.form["wake_count"])

    results = compute_sleep_metrics(t1, t2, t3, t4, w)

    
    return render_template("results_analyse.html", **results)

@app.route("/advanced")
def advanced():
    return render_template("advanced.html")


@app.route("/advanced_result", methods=["POST"])
def advanced_result():

    height = float(request.form["height"])
    weight = float(request.form["weight"])

    systolic = request.form.get("systolic")
    diastolic = request.form.get("diastolic")
    glucose = request.form.get("glucose")

    bmi = weight / ((height / 100) ** 2)

    health_score = 100

    if bmi < 18.5:
        bmi_status = "warning"
        health_score -= 10
    elif bmi > 25:
        bmi_status = "danger"
        health_score -= 20
    else:
        bmi_status = "good"

    if systolic and diastolic:
        s = int(systolic)
        d = int(diastolic)

        if s < 120 and d < 80:
            bp_status = "good"
        elif s < 140:
            bp_status = "warning"
            health_score -= 10
        else:
            bp_status = "danger"
            health_score -= 20
    else:
        bp_status = "neutral"

    if glucose:
        g = float(glucose)

        if g < 6.1:
            glucose_status = "good"
        elif g < 7:
            glucose_status = "warning"
            health_score -= 10
        else:
            glucose_status = "danger"
            health_score -= 20
    else:
        glucose_status = "neutral"

    if health_score >= 80:
        overall_status = "good"
    elif health_score >= 60:
        overall_status = "warning"
    else:
        overall_status = "danger"

    return render_template(
        "advanced_result.html",
        bmi=round(bmi, 2),
        bmi_status=bmi_status,
        bp_status=bp_status,
        glucose_status=glucose_status,
        health_score=health_score,
        overall_status=overall_status
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)