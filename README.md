🔍 LLM-Based Input Validator

LLM-powered user profile validation with strict schema enforcement and automated evaluations

Tech Stack: Python · Large Language Models · Prompt Engineering · Promptfoo
Context: AI/ML Internship Assignment

1. Overview

This project implements a Large Language Model (LLM)–based input validation system that validates user profile data using prompt engineering only.

All validation logic is delegated entirely to an LLM:

❌ No regex

❌ No traditional validation libraries

❌ No hardcoded rules

The system enforces strict structured JSON output, includes retry logic, and supports automated evaluations.

2. Key Features

✅ LLM-only validation logic

✅ Prompt-engineered constraints (E.164, ISO-2, email validity, etc.)

✅ Strict output schema enforcement

✅ Automatic retries for malformed LLM responses

✅ Automated evaluations using Promptfoo

✅ Secure API key handling via environment variables

3. Input Format

The validator accepts a JSON file with the following structure:

{
  "name": "string | null",
  "email": "string | null",
  "age": "number | null",
  "country": "string | null",
  "phone": "string | null"
}

Input Rules

Missing fields are ignored

No data is inferred or fabricated

Validation applies only to provided fields

4. Output Format (Strict)

The validator always returns output in the following schema:

{
  "is_valid": true,
  "errors": [],
  "warnings": []
}

Field Description

is_valid → boolean

errors → list of strings

warnings → list of strings

Any malformed output from the LLM is automatically retried until it conforms to this schema.

5. Validation Rules (High-Level)
Errors

Name must be present and non-empty

Email must be a valid email address

Age must be a positive number

Country must be a valid ISO-2 country code (e.g. IN, US)

Phone number must be present and in E.164 format

Warnings

Age below 18

Name shorter than 3 characters

Disposable or temporary email address

Phone country code does not align with country

Rule Interpretation

All rules are expressed at a high level in the prompt and interpreted entirely by the LLM.

6. Setup Instructions
Clone the Repository
git clone https://github.com/<your-username>/llm-input-validator.git
cd llm-input-validator

Create and Activate Virtual Environment
python -m venv venv


macOS / Linux

source venv/bin/activate


Windows

venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

7. API Key Configuration

Create a .env file locally (do not commit it):

OPENAI_API_KEY=your_openai_api_key_here


OR

GROQ_API_KEY=your_groq_api_key_here

Security Notes

API keys are intentionally not committed

Evaluators must provide their own keys

Environment-variable–based secrets follow production best practices

8. Running the Validator
python validate_user.py tests/invalid.json

Example Output
{
  "is_valid": false,
  "errors": [
    "name is required",
    "email is not a valid email address"
  ],
  "warnings": [
    "age is below recommended minimum"
  ]
}

9. Automated Evaluations (Promptfoo)

This project includes Promptfoo evaluations to verify output correctness and schema discipline.

Install Promptfoo
npm install -g promptfoo

Run Evaluations
promptfoo eval -c evals/promptfoo.yaml

Evaluation Notes

Promptfoo requires a live LLM provider

Accounts with zero API credit may encounter 429 rate-limit errors

This does not indicate incorrect configuration

Evaluations run reliably on Linux and CI environments

10. Project Structure
llm-input-validator/
├── validate_user.py
├── prompts/
│   └── validator_prompt.txt
├── evals/
│   └── promptfoo.yaml
├── tests/
│   ├── invalid.json
│   └── valid.json
├── requirements.txt
├── .env.example
└── README.md

11. Design Decisions

LLM-driven validation avoids brittle rule duplication

Prompt engineering captures real-world standards

Schema enforcement with retries ensures deterministic outputs

Promptfoo evaluations provide automated correctness checks

Secure secret handling mirrors real-world production systems
