# WorkflowPro QA Automation Case Study

## Overview

This repository contains my solution for the QA Automation Engineering Case Study provided by Bynry.

The project demonstrates:

- UI Test Automation using Playwright
- API Testing using Requests
- Pytest Framework
- BrowserStack Cross Browser Testing
- Multi-Tenant Testing
- CI/CD Integration
- Test Framework Design

---

## Tech Stack

- Python
- Playwright
- Pytest
- BrowserStack
- Requests
- GitHub Actions
- Allure Reports

---

## Project Structure

```
automation/

api/

config/

fixtures/

pages/

tests/

ui/

api/

integration/

utils/

testdata/

docs/

reports/

screenshots/
```

---

## Installation

Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/workflowpro-qa-automation-case-study.git
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browsers

```bash
playwright install
```

---

## Run Tests

Run all tests

```bash
pytest
```

Run UI tests

```bash
pytest automation/tests/ui
```

Run API tests

```bash
pytest automation/tests/api
```

Run Integration tests

```bash
pytest automation/tests/integration
```

---

## Features

- Page Object Model
- API + UI Integration Testing
- Multi-Tenant Validation
- BrowserStack Ready
- Environment Configuration
- Parallel Execution
- Allure Reporting
- CI/CD Ready

---

## Assumptions

The application used in this assignment is fictional.

The implementation focuses on demonstrating automation framework design and testing strategy rather than execution against a live application.

---

## Author

S M Musharraf Perwez