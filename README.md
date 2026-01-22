<h1 align="center">LLM-Based Input Validator</h1>

<p align="center">
  User profile validation using prompt-engineered constraints<br/>
  <i>Python · LLMs · Prompt Engineering · Promptfoo</i>
</p>

<hr/>

<h2>Overview</h2>
<p>
This project validates user profile inputs by delegating all validation logic to a Large Language Model.
Instead of hardcoded rules or regex, constraints are described in a prompt and enforced through structured
model outputs.
</p>

<p>
The goal is to explore whether an LLM can reliably perform schema-aware validation when combined with
strict output enforcement and retries.
</p>

<h2>Key Features</h2>
<ul>
  <li>Validation logic handled entirely by an LLM</li>
  <li>Strict JSON output schema with retry mechanism</li>
  <li>No regex or traditional validation libraries</li>
  <li>Automated prompt evaluations using Promptfoo</li>
</ul>

<h2>Input / Output</h2>

<pre>
Input:
{
  "name": string | null,
  "email": string | null,
  "age": number | null,
  "country": string | null,
  "phone": string | null
}
</pre>

<pre>
Output:
{
  "is_valid": boolean,
  "errors": string[],
  "warnings": string[]
}
</pre>

<h2>Validation Logic</h2>
<ul>
  <li>Errors are raised for invalid or missing required fields</li>
  <li>Warnings are used for suspicious but acceptable inputs</li>
  <li>No values are inferred or fabricated by the system</li>
</ul>

<h2>Running</h2>
<pre>
python validate_user.py tests/invalid.json
</pre>

<h2>Evaluation</h2>
<p>
Promptfoo is used to automatically check output correctness and schema consistency across test cases.
</p>

<pre>
promptfoo eval -c evals/promptfoo.yaml
</pre>

<h2>Design Notes</h2>
<ul>
  <li>Prompt-based validation reduces duplicated rule logic</li>
  <li>Schema enforcement ensures predictable downstream use</li>
  <li>Evaluations help catch prompt regressions early</li>
</ul>
