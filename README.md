<h1 align="center">🔍 LLM-Based Input Validator</h1>

<p align="center">
  <b>LLM-powered user profile validation with strict schema enforcement and automated evaluations</b><br/>
  <i>Tech Stack: Python · Large Language Models · Prompt Engineering · Promptfoo</i><br/>
  <i>Context: AI/ML Internship Assignment</i>
</p>

<hr/>

<h2>1. Overview</h2>

<p>
This project implements a <b>Large Language Model (LLM)–based input validation system</b> that validates
user profile data using <b>prompt engineering only</b>.
</p>

<p>
All validation logic is delegated entirely to an LLM:
</p>

<ul>
  <li>❌ No regex</li>
  <li>❌ No traditional validation libraries</li>
  <li>❌ No hardcoded rules</li>
</ul>

<p>
The system enforces <b>strict structured JSON output</b>, includes <b>retry logic</b>, and supports
<b>automated evaluations</b>.
</p>

<hr/>

<h2>2. Key Features</h2>

<ul>
  <li>✅ LLM-only validation logic</li>
  <li>✅ Prompt-engineered constraints (E.164, ISO-2, email validity, etc.)</li>
  <li>✅ Strict output schema enforcement</li>
  <li>✅ Automatic retries for malformed LLM responses</li>
  <li>✅ Automated evaluations using Promptfoo</li>
  <li>✅ Secure API key handling via environment variables</li>
</ul>

<hr/>

<h2>3. Input Format</h2>

<p>The validator accepts a JSON file with the following structure:</p>

<pre>
{
  "name": "string | null",
  "email": "string | null",
  "age": "number | null",
  "country": "string | null",
  "phone": "string | null"
}
</pre>

<h3>Input Rules</h3>

<ul>
  <li>Missing fields are ignored</li>
  <li>No data is inferred or fabricated</li>
  <li>Validation applies only to provided fields</li>
</ul>

<hr/>

<h2>4. Output Format (Strict)</h2>

<p>The validator <b>always</b> returns output in the following schema:</p>

<pre>
{
  "is_valid": true,
  "errors": [],
  "warnings": []
}
</pre>

<h3>Field Description</h3>

<ul>
  <li><b>is_valid</b> → boolean</li>
  <li><b>errors</b> → list of strings</li>
  <li><b>warnings</b> → list of strings</li>
</ul>

<p>
Any malformed output from the LLM is <b>automatically retried</b> until it conforms to this schema.
</p>

<hr/>

<h2>5. Validation Rules (High-Level)</h2>

<h3>Errors</h3>

<ul>
  <li>Name must be present and non-empty</li>
  <li>Email must be a valid email address</li>
  <li>Age must be a positive number</li>
  <li>Country must be a valid ISO-2 country code (e.g. IN, US)</li>
  <li>Phone number must be present and in E.164 format</li>
</ul>

<h3>Warnings</h3>

<ul>
  <li>Age below 18</li>
  <li>Name shorter than 3 characters</li>
  <li>Disposable or temporary email address</li>
  <li>Phone country code does not align with country</li>
</ul>

<p>
All rules are expressed at a <b>high level in the prompt</b> and interpreted entirely by the LLM.
</p>

<hr/>

<h2>6. Setup Instructions</h2>

<h3>Clone the Repository</h3>

<pre>
git clone https://github.com/&lt;your-username&gt;/llm-input-validator.git
cd llm-input-validator
</pre>

<h3>Create and Activate Virtual Environment</h3>

<pre>
python -m venv venv
</pre>

<p><b>macOS / Linux</b></p>

<pre>
source venv/bin/activate
</pre>

<p><b>Windows</b></p>

<pre>
venv\Scripts\activate
</pre>

<h3>Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<hr/>

<h2>7. API Key Configuration</h2>

<p>Create a <code>.env</code> file locally (do <b>not</b> commit it):</p>

<pre>
OPENAI_API_KEY=your_openai_api_key_here
</pre>

<p><b>OR</b></p>

<pre>
GROQ_API_KEY=your_groq_api_key_here
</pre>

<h3>Security Notes</h3>

<ul>
  <li>API keys are intentionally not committed</li>
  <li>Evaluators must provide their own keys</li>
  <li>Environment-variable–based secrets follow production best practices</li>
</ul>

<hr/>

<h2>8. Running the Validator</h2>

<pre>
python validate_user.py tests/invalid.json
</pre>

<h3>Example Output</h3>

<pre>
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
</pre>

<hr/>

<h2>9. Automated Evaluations (Promptfoo)</h2>

<p>
This project includes <b>Promptfoo evaluations</b> to verify output correctness and schema discipline.
</p>

<h3>Install Promptfoo</h3>

<pre>
npm install -g promptfoo
</pre>

<h3>Run Evaluations</h3>

<pre>
promptfoo eval -c evals/promptfoo.yaml
</pre>

<h3>Evaluation Notes</h3>

<ul>
  <li>Promptfoo requires a live LLM provider</li>
  <li>Accounts with zero API credit may encounter 429 rate-limit errors</li>
  <li>This does not indicate incorrect configuration</li>
  <li>Evaluations run reliably on Linux and CI environments</li>
</ul>

<hr/>

<h2>10. Project Structure</h2>

<pre>
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
</pre>

<hr/>

<h2>11. Design Decisions</h2>

<ul>
  <li>LLM-driven validation avoids brittle rule duplication</li>
  <li>Prompt engineering captures real-world standards</li>
  <li>Schema enforcement with retries ensures deterministic outputs</li>
  <li>Promptfoo evaluations provide automated correctness checks</li>
  <li>Secure secret handling mirrors real-world production systems</li>
</ul>
