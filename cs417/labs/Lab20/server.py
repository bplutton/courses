"""Lab 20: Build the Other Side — Server

Your FastAPI grading server. Build each section as you work
through the tasks. The TODOs tell you what to add and where.
"""

from fastapi import FastAPI
from grading import grade
import json

app = FastAPI()

@app.post("/echo")
def echo(data: dict):
    return {"you_sent": data}


# ---------------------------------------------------------------------------
# Task 1: The Naive Server
# ---------------------------------------------------------------------------
# Import the grade function from grading.py, then create a POST /grade
# endpoint that accepts {"student": ..., "lab": ...} and returns the score.

# TODO: import grade from grading

# TODO: POST /grade endpoint

@app.post("/grade")
def grade_endpoint(data: dict):
    student = data["student"]
    lab = data["lab"]
    score = grade(student, lab)
    # return json{"student": student, "lab": lab, "score": score}
    return {"student": student, "lab": lab, "score": score}


# ---------------------------------------------------------------------------
# Task 2: Retries Reveal a Problem
# ---------------------------------------------------------------------------
# Add a grading_log list that records every grading event.
# Update POST /grade to (1) accept an optional "slow" field and pass it
# to grade(), and (2) append each grading event to the log.
# Add GET /log and POST /reset-log endpoints.

# TODO 1

grading_log = []

completed = {}

# TODO: update POST /grade to log events and support "slow"

@app.post("/grade")
def grade_endpoint(data: dict, submission_id: str | None = None):
    if (submission_id is not None) and (submission_id in completed):
        return completed.get(submission_id)
    else:
        student = data["student"]
        lab = data["lab"]
        slow = data.get("slow", False)
        score = grade(student, lab, slow=slow) # Use three values in the grading_log
        grading_log.append([{"student": student, "lab": lab, "score": score, "slow": slow}]) # Add dictionary containing four values
        if submission_id is not None:
            completed.append({submission_id: 
                            {"student": student, "lab": lab, "score": score}
                            })
            return completed[submission_id]
        return {"student": student, "lab": lab, "score": score}

# TODO: GET /log endpoint

@app.get("/log")
def get_log():
    return {"entries": grading_log}

# TODO: POST /reset-log endpoint

@app.post("/reset-log")
def reset_log():
    grading_log.clear()
    return {"message": "Grading log reset."}


# ---------------------------------------------------------------------------
# Task 3: Idempotency Makes Retries Safe
# ---------------------------------------------------------------------------
# Add a completed dict that maps submission IDs to results.
# Update POST /grade to check for an optional "submission_id" field —
# if the ID is already in completed, return the cached result without
# grading again or logging.
# Add POST /reset-completed endpoint.

# TODO: POST /reset-completed endpoint

@app.post("/reset-completed")
def reset_completed():
    completed.clear()
    return {"message": "Completed submissions reset."}


# ---------------------------------------------------------------------------
# Task 4: Honest About Time
# ---------------------------------------------------------------------------
# You'll need: from fastapi import BackgroundTasks
#              from fastapi.responses import JSONResponse
#
# Add jobs dict, job_submission_map dict, and a job ID generator.
# Create POST /grade-async (returns 202, runs grading in background).
# Create a run_grade_job helper that does the actual grading.
# Create GET /grade-jobs/{job_id} to check job status.

# TODO: jobs = {}
# TODO: job_submission_map = {}

# TODO: POST /grade-async endpoint

# TODO: run_grade_job helper function

# TODO: GET /grade-jobs/{job_id} endpoint
