````md
# 🩺 Health Dashboard Web App (Flask)  
### README with AI Creative Practices Documentation

---

# 1. Project Overview

This project is a multi-page health analytics web application built using Flask. It simulates a lightweight personal health monitoring system inspired by Apple Health UI design.

The application includes two major modules:

### 💤 Sleep Analysis
Users input:
- Bed time
- Sleep time
- Wake time
- Get-up time
- Night awakenings

Outputs:
- Sleep duration
- Bed duration
- Sleep quality score
- Overall sleep score
- Automated comments
- Sleep timeline visualization

### 🧬 Advanced Health Analysis
Users input:
- Height
- Weight
- Blood pressure (optional)
- Blood glucose (optional)

Outputs:
- BMI
- Blood pressure classification
- Glucose classification
- Overall health score

---

# 2. How to Run the Project

## Local Reproduction (under 10 minutes)

### Step 1: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/health-dashboard.git
cd health-dashboard
````

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Application

```bash
python app.py
```

### Step 4: Open Browser

```text
http://127.0.0.1:5000
```

---

# 3. Python Environment

## Python Version

```text
Python 3.11.x
```

## Required Packages

Included in:

```text
requirements.txt
```

Recommended contents:

```txt
Flask==3.0.0
gunicorn==21.2.0
```

## Operating System

Tested on:

* Windows 10
* macOS (compatible)
* Linux (compatible)

## Data Files

No external dataset required.
All project data is user input collected through web forms.

## API Keys / Credentials

No external APIs used.
No credentials required.

---

# 4. Project Structure

```text
health-dashboard/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── sleep.html
│   ├── results_analyse.html
│   ├── advanced.html
│   └── advanced_result.html
└── README.md
```

---

# 5. AI Creative Practices — Prompt and Collaboration Log

---

# A. AI Tools Used

## 1. ChatGPT (OpenAI GPT-5 series)

Used for:

* Flask debugging
* UI redesign suggestions
* HTML/CSS generation
* Deployment guidance
* README drafting

## 2. GitHub Copilot

README automic commit message


---

# B. Agentic Workflow Description

AI was used through multi-step iterative collaboration rather than single-turn generation.

Example workflow:

### Phase 1 — Functional Scaffolding

Prompted AI to create Flask routes, forms, and templates.

### Phase 2 — Debugging Loop

When template variables or routes failed, I iteratively supplied error messages and revised code manually.

### Phase 3 — UI Redesign

Used AI to transform plain HTML pages into Apple Health-inspired card interfaces.

### Phase 4 — Deployment Pipeline

Used AI guidance for GitHub setup, requirements.txt generation, and Render deployment.

This process resembled agentic software development: scaffold → test → critique → revise.

---

# C. Selected Prompt–Response Pairs

---

## Example 1 — Sleep Scoring Logic

### Prompt

> My plan is to use bedtime, sleep time, wake time, get-up time, and awakenings as input. Calculate sleep duration and sleep quality.

### AI Response Summary

Suggested formulas:

* Sleep duration = wake time - sleep time
* Sleep quality = sleep duration / bed duration × score

### Critical Review

What AI got right:

* Correct separation of sleep duration vs bed duration.
* Good basis for efficiency metric.

What AI missed:

* Did not consider midnight crossover.
* Needed manual handling for times after midnight.

My correction:
Implemented custom time conversion logic so 23:30 → 07:00 works correctly.

---

## Example 2 — UI Redesign

### Prompt

> Upgrade this project into portfolio-level Apple Health UI.

### AI Response Summary

Suggested:

* Card layout
* Soft shadows
* Green/yellow/red risk colors
* Dashboard navigation

### Critical Review

What AI got right:

* Strong design direction.
* Clear modular structure.

What AI missed:

* Some HTML examples were incomplete.
* CSS needed manual cleanup.

My correction:
Adjusted spacing, alignment, and merged CSS into existing templates.

---

## Example 3 — Deployment

### Prompt

> Deploy publish and ensure everyone can use it.

### AI Response Summary

Suggested Render deployment using:

```bash
gunicorn app:app
```

### Critical Review

What AI got right:

* Correct Flask deployment flow.
* Correct need for requirements.txt.

What AI missed:

* Did not initially mention email verification delay.
* Needed repo conflict troubleshooting.

My correction:
Resolved GitHub push conflicts and completed deployment manually.

---

# D. Review and Correction Record 

---

## Case 1 — Midnight Time Calculation Error

Problem:
Naive subtraction caused negative values.

Correction:
Converted times into minutes and added 24h rollover logic.

Reasoning:
Sleep sessions often cross midnight.

---

## Case 2 — Template Variable Error

Problem:
index page error with misplaced CSS parts and template error from wrong variable name

Correction:
Matched backend variable names and changed CSS into other doc.

Reasoning:
Flask templates require exact variable consistency.

---

## Case 3 — GitHub Push Conflict

Problem:

```text
failed to push some refs as there were previous work from other course in my github
```

Correction:
Created a clean repository workflow and synced remote branch properly.

Reasoning:
Remote repo contained previous unrelated history.

---

# E. Original Contributions

The following parts reflect my own original design and decisions beyond AI-generated output:

## Product Design

* Chose health dashboard concept.
* Decided to combine sleep + BMI + BP + glucose into one platform.

## Sleep Metrics Logic

* Selected inputs: bedtime, sleep onset, wake time, get-up time.
* Decided sleep quality should reflect efficiency and awakenings.

## UX Decisions

* Requested Apple Health visual identity.
* Decided to split modules into Sleep and Advanced Health.

## Debugging Decisions

* Corrected routing, variable mismatches, deployment issues manually.

## Scope Control

* Chose not to overcomplicate with databases or APIs.

---

# 6. Reflection

AI significantly accelerated early-stage development by generating Flask scaffolding, HTML structures, deployment instructions, and design ideas. Tasks that would normally require repeated documentation lookup were completed quickly through interactive prompting.

there was a great change in my work in the end about tha dashboard editition,and AI deleted part of my original CSS code and the website failed to work. The problem was fixed with a long-time debugging process.

However, AI outputs often required technical judgment. Some code examples were incomplete, inconsistent with my existing project, or ignored edge cases such as midnight time calculations. The final product depended on my own debugging, testing, and design decisions rather than direct copy-paste outputs.

If repeating this project, I would use AI earlier for structured planning, but I would modularize backend logic sooner and introduce automated tests to validate scoring formulas.

---

# 7. Live Demo

```text
https://info102-final-ys523-health-dashboard.onrender.com/
```

---

# 8. Author

Built as an academic project focused on health data visualization, Flask web development, and transparent AI-assisted software creation.

```
```
