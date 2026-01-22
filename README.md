# 🔍 LLM-Based Input Validator

> **LLM-powered user profile validation with strict schema enforcement and automated evaluations**

**Tech Stack:** Python · Large Language Models · Prompt Engineering · Promptfoo  
**Context:** AI/ML Internship Assignment

---

## Overview

This project implements a **Large Language Model (LLM)–based input validation system** that validates user profile data using **prompt engineering only**.

All validation logic is delegated entirely to an LLM:
- No regex
- No traditional validation libraries
- No hardcoded rules

The system enforces **strict structured JSON output**, includes **retry logic**, and supports **automated evaluations**.

---

## Key Features

- **LLM-only validation logic**
- **Prompt-engineered constraints** (E.164, ISO-2, email validity, etc.)
- **Strict output schema enforcement**
- **Automatic retries** for malformed LLM responses
- **Automated evals** using Promptfoo
- **Secure API key handling** via environment variables

---

## Input Format

The validator accepts a JSON file with the following structure:

```json
{
  "name": "string | null",
  "email": "string | null",
  "age": "number | null",
  "country": "string | null",
  "phone": "string | null"
}
