import os
from flask import Flask, render_template, request
from pathlib import Path
from werkzeug.utils import secure_filename

from resume_score import (
    parse_job_description,
    parse_resume,
    read_resume,
    final_score
)

app = Flask(__name__)

# Folder where uploaded resumes
# will be stored temporarily
UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

# HOME PAGE

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

# ANALYZE CANDIDATES

@app.route("/analyze", methods=["POST"])
def analyze():

    # Get job description entered by HR
    job_description = request.form.get(
        "job_description"
    )

    # Get all uploaded resumes
    resumes = request.files.getlist(
        "resumes"
    )

    # Validate Job Description

    if not job_description:
        return "Please enter a job description."
    # Parse Job Description

    job = parse_job_description(
        job_description
    )

    # List for storing candidate results
    all_results = []
    # Process Every Resume

    for resume_file in resumes:

        # Skip empty files
        if resume_file.filename == "":
            continue

        # Get safe filename
        filename = secure_filename(
            resume_file.filename
        )

        # Create file path
        file_path = (
            Path(app.config["UPLOAD_FOLDER"])
            / filename
        )

        # Save uploaded resume temporarily
        resume_file.save(file_path)

        try:

            # Read PDF/DOCX
            resume_text = read_resume(
                file_path
            )

            # Skip unsupported files
            if resume_text is None:
                continue

            # Parse resume using AI
            parsed_resume = parse_resume(
                resume_text
            )

            # Compare resume with job
            result = final_score(
                job,
                parsed_resume
            )

            # Store candidate result
            all_results.append({

                "name":
                    parsed_resume.name,

                "score":
                    result.score,

                "details":
                    result.details.model_dump()

            })

        finally:

            # Delete temporary resume
            # after processing
            if file_path.exists():

                file_path.unlink()

    # Sort Candidates
    # Highest Score First

    all_results.sort(
        key=lambda candidate:
            candidate["score"],
        reverse=True
    )

    # Show Results Page
    
    return render_template(
        "results.html",
        results=all_results
    )

# RUN FLASK APP

if __name__ == "__main__":

    app.run(
        debug=True
    )