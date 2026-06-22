# CI Integration Approach

## Objective

Integrate the automation suite into a Continuous Integration (CI) pipeline to ensure automated validation of application functionality on every code change.

## Proposed Workflow

1. Trigger the pipeline on:

   * Push to main branch
   * Pull Request creation or update

2. Provision a clean execution environment.

3. Install Python dependencies from `requirements.txt`.

4. Install Playwright browsers and required system dependencies.

5. Execute the complete PyTest automation suite.

6. Generate execution reports:

   * Console Report
   * HTML Report

7. Publish reports as CI artifacts for download and review.

8. Fail the pipeline when any critical test case fails.

---

## CI Technology

The implementation uses **GitHub Actions** as the CI platform.

### Workflow Steps

```text
Checkout Repository
        ↓
Setup Python Environment
        ↓
Install Dependencies
        ↓
Install Playwright Browsers
        ↓
Execute PyTest Suite
        ↓
Generate HTML Report
        ↓
Upload Report Artifact
```

---

## Reporting Strategy

The pipeline automatically generates:

* PyTest Console Results
* HTML Test Execution Report
* Build Status (Pass / Fail)

Reports are uploaded as GitHub Actions artifacts and can be downloaded directly from the workflow run.

---

## Benefits

* Early detection of regressions
* Consistent execution environment
* Automated validation for every change
* Improved release confidence
* Centralized reporting and traceability

---

## Current Implementation

A GitHub Actions workflow has been implemented for this assignment.

The workflow automatically:

* Installs project dependencies
* Installs Playwright browsers
* Executes the automated test suite
* Generates HTML reports
* Uploads reports as downloadable artifacts

Workflow File:

```text
.github/workflows/ci.yml
```

This approach ensures that the automation suite remains maintainable, reproducible, and ready for future scalability.
