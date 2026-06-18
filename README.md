# RR QA Automation Assignment

Automation suite for TMDB Discover application.

## Documentation Portal

This project includes a documentation portal that provides access to:

* Test Strategy
* Test Cases
* Defect Report
* CI Integration Approach
* Test Execution Reports

### Launch Documentation Portal

Start a local web server from the project root:

```bash
python3 -m http.server 8000
```

Open the documentation portal:

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

### Why a Local Web Server?

The documentation portal dynamically renders Markdown documents using JavaScript. Modern browsers block local file access (`file://`) for security reasons, so a lightweight local web server is required to correctly display the documentation.

### Documentation Structure

```text
docs/
├── index.html
├── viewer.html
├── TestStrategy.md
├── TestCases.md
├── DefectReport.md
└── CIApproach.md
```

## Framework

- Python
- PyTest
- Playwright
- Loguru
- pytest-html

## Run Tests

pytest

## Generate Report

pytest

Report:

reports/report.html


