
#  Health Dashboard Web App (Flask)

A multi-page health analytics web application built with Flask.  
This project simulates a personal health tracking system inspired by Apple Health UI design.

---

##  Features

### Sleep Analysis
- 24-hour sleep timeline visualization
- Inputs: bed time, sleep time, wake time, get-up time
- Night awakenings tracking
- Sleep duration and sleep quality calculation
- Automated feedback comments (e.g. late sleep, early wake, frequent awakenings)

---

###  Advanced Health Analysis
- BMI calculation (height & weight)
- Blood pressure evaluation (optional input)
- Blood glucose evaluation (optional input)
- Risk classification system:
  - 🟢 Normal (Good)
  - 🟡 Warning
  - 🔴 High Risk
- Overall health score generation

---

##  UI Design

- Apple Health–inspired interface
- Card-based layout system
- Color-coded health status:
  - 🟢 Good
  - 🟡 Warning
  - 🔴 Danger
- Clean multi-page navigation (dashboard style)
- Minimal and responsive design

---

##  Tech Stack

- Python (Flask)
- HTML / CSS
- Jinja2 Templates
- Rule-based scoring system
- Basic data visualization (timeline UI)

---

##  System Architecture

User Input → Flask Backend → Rule-based Health Engine → HTML Dashboard Output

---

##  Project Structure

```

project/
├── app.py
├── utils.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── sleep.html
│   ├── results_analyse.html
│   ├── advanced.html
│   └── advanced_result.html
└── static/ (optional)

````

---

##  How to Run Locally

```bash
pip install -r requirements.txt
python app.py
````

Then open:

```
[http://127.0.0.1:5000](https://info102-final-ys523-health-dashboard.onrender.com/)
```

---

##  Deployment

This project can be deployed using:

* Render (recommended)
* PythonAnywhere
* Any Flask-compatible hosting service

---

##  Key Learnings

* Multi-page Flask application design
* Form handling and request processing
* Rule-based scoring system design
* UI design inspired by Apple Health
* Basic health metric calculations (BMI, sleep quality, risk levels)

---

##  Future Improvements

* Add database storage (historical tracking)
* Improve visualization (charts / graphs)
* Mobile-friendly responsive design
* AI-based health recommendations
* User login system

---

##  Author

Built as a personal academic project focused on health data visualization and web development fundamentals.
