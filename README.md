# RR QA Automation Assignment

Automation test suite for the TMDB Discover application using Playwright and PyTest.

## Framework Stack

* Python
* PyTest
* Playwright
* Loguru
* pytest-html
* GitHub Actions (CI)

---

## Project Structure

```text
.
├── pages/
├── tests/
├── utils/
├── reports/
├── docs/
├── scripts/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Prerequisites

* Python 3.12+
* Git
* Playwright

Verify installation:

```bash
python3 --version
pip --version
```

---

## Setup

### Clone Repository

```bash
git clone <repository-url>
cd rr-qa-automation-assignment
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

---

## Run Tests

### Run Entire Test Suite

```bash
pytest -v
```

### Run Tests in Headed Mode

```bash
pytest -v -s --headed
```

### Run Specific Test File

```bash
pytest tests/test_search.py -v
```

### Run Specific Test Case

```bash
pytest tests/test_search.py::test_tc018_verify_search_with_valid_movie_title -v
```

---

## Test Reports

Generate report:

```bash
pytest
```

Report location:

```text
reports/report.html
```

Open report in browser:

```bash
open reports/report.html
```

---

## Documentation Portal

The project includes a documentation portal containing:

* Test Strategy
* Test Cases
* Defect Report
* CI Integration Approach
* Test Execution Reports

### Launch Documentation Portal

Start a local web server:

```bash
python3 -m http.server 8000
```

Open:

```text
http://localhost:8000/docs/index.html
```

### Alternative Using Shell Script

```bash
chmod +x scripts/start_docs.sh
./scripts/start_docs.sh
```

Then open:

```text
http://localhost:8000/docs/index.html
```

---

## Why a Local Web Server?

The documentation portal dynamically renders Markdown files using JavaScript.

Modern browsers restrict local file access (`file://`) for security reasons, so a lightweight local web server is required for proper rendering.

---

## Documentation Structure

```text
docs/
├── index.html
├── viewer.html
├── TestStrategy.md
├── TestCases.md
├── DefectReport.md
└── CIApproach.md
```

---

## Continuous Integration

GitHub Actions is configured to:

* Install dependencies
* Install Playwright browsers
* Execute PyTest suite
* Generate HTML reports
* Upload reports as build artifacts

CI workflow file:

```text
.github/workflows/ci.yml
```

---

## Known Defects Identified

### TC002 - Direct Access / Refresh on Popular Route

**Expected:** Application should load successfully.

**Actual:** Direct navigation or browser refresh on `/popular` returns HTTP 404.

**Severity:** High

**Priority:** High

This defect was identified during automation execution and documented in the defect report.
