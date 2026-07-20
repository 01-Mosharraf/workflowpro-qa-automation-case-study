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

## Framework Highlights

- Page Object Model
- API + UI Integration Testing
- BrowserStack Cross Browser Support
- Multi-Tenant Test Design
- Environment Based Configuration
- Parallel Test Execution
- GitHub Actions CI/CD
- Allure Reporting
- External Test Data
- Screenshot on Failure

---

## Test Coverage

- Login
- Multi-Tenant Validation
- API Project Creation
- UI Verification
- BrowserStack Mobile Strategy
- Tenant Isolation
- CI/CD Ready Framework

---

## CI/CD Pipeline

This project includes a GitHub Actions workflow.

Pipeline stages:

1. Checkout code
2. Setup Python
3. Install dependencies
4. Install Playwright browsers
5. Execute tests
6. Upload artifacts

---

## Project Highlights

- Playwright Automation
- Pytest Framework
- API Testing
- BrowserStack Ready
- Page Object Model
- Parallel Execution
- YAML Configuration
- GitHub Actions
- Multi-Tenant Testing
- CI/CD Integration

---

## Execution Notice

This repository was created as part of the Bynry QA Automation Case Study.

WorkflowPro is a fictional SaaS application used only for framework design.

The framework demonstrates:

- Playwright architecture
- API abstraction
- Page Object Model
- CI/CD
- BrowserStack integration
- Multi-tenant design

Network execution is intentionally disabled because no real WorkflowPro environment is provided.

---

## Assumptions

The application used in this assignment is fictional.

The implementation focuses on demonstrating automation framework design and testing strategy rather than execution against a live application.

---

## Author

S M Musharraf Perwez