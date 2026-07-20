# Part 2 – Test Automation Framework Design

# Objective

Design a scalable, maintainable, and reusable automation framework for a B2B SaaS platform that supports multiple browsers, mobile devices, multiple tenants, API testing, and CI/CD integration.

---

# Technology Stack

| Component | Tool |
|----------|------|
| Language | Python |
| Test Framework | Pytest |
| UI Automation | Playwright |
| API Testing | Requests |
| Cross Browser Testing | BrowserStack |
| Reporting | Allure |
| Parallel Execution | pytest-xdist |
| CI/CD | GitHub Actions |
| Configuration | YAML |
| Logging | Python Logging |
| Version Control | Git |

---

# Framework Architecture

```
                           GitHub

                              │

                       GitHub Actions

                              │

                           Pytest

             ┌────────────────────────────────┐
             │                                │
             │                                │

        API Tests                       UI Tests

             │                                │

         Requests                     Playwright

             │                                │

             └──────────────┬─────────────────┘

                            │

                      BrowserStack

                            │

                     Test Reports

                            │

                         Allure
```

---

# Project Structure

```
workflowpro-qa-automation-case-study/

automation/

│

├── api/

├── config/

├── fixtures/

├── pages/

├── testdata/

├── tests/

│      api/

│      ui/

│      integration/

├── utils/

└── conftest.py

docs/

reports/

screenshots/

logs/
```

---

# Design Principles

The framework follows the following software engineering principles.

- Page Object Model
- Single Responsibility Principle
- Reusability
- Separation of Concerns
- Configuration Driven Execution
- External Test Data
- Independent Test Cases
- Easy CI/CD Integration

---

# Configuration Management

Environment specific configuration is stored in YAML files.

Example:

QA

Staging

Production

Browser configuration includes:

- Chromium
- Firefox
- WebKit

Execution mode:

- Headless
- Headed

Viewport:

- Desktop
- Tablet
- Mobile

---

# Test Data Management

Test data is separated from test logic.

Example:

users.json

projects.json

Benefits

- Reusable
- Easier maintenance
- No hardcoded values
- Supports multiple tenants

---

# Multi-Tenant Strategy

The application supports multiple companies.

Each tenant has:

- Separate users
- Separate projects
- Separate permissions
- Separate data

Automation validates:

- User only sees own company data.
- Cross-tenant access is denied.
- Tenant isolation is preserved.

---

# User Roles

Admin

- Create Project
- Delete Project
- Manage Users

Manager

- Create Tasks
- Update Tasks
- View Reports

Employee

- View Assigned Tasks
- Update Task Status

Separate test users should exist for each role.

---

# API Testing Strategy

API tests validate:

- Authentication
- Project Creation
- Project Update
- Project Deletion
- Authorization
- Tenant Isolation

UI tests should never create test data manually if an API can create it faster.

---

# BrowserStack Strategy

Cross-browser execution:

- Chrome
- Firefox
- Safari

Mobile devices:

- Android
- iPhone

Benefits:

- Real devices
- Cross-platform validation
- Responsive UI verification

---

# Logging Strategy

Framework logs:

- Test Start
- Test End
- Browser Launch
- API Calls
- Failures
- Exceptions

---

# Screenshot Strategy

Take screenshots:

- On Failure
- On Assertion Failure
- On Unexpected Exception

Store under:

screenshots/

---

# Reporting Strategy

Use Allure Reports.

Reports include:

- Passed Tests
- Failed Tests
- Execution Time
- Attachments
- Screenshots
- Logs

---

# CI/CD Strategy

Every code push triggers:

1. Install dependencies
2. Install Playwright browsers
3. Run API tests
4. Run UI tests
5. Run Integration tests
6. Generate Allure Report
7. Upload reports as artifacts

---

# Parallel Execution

Framework supports:

pytest -n auto

Benefits:

- Faster execution
- Better CI performance

---

# Error Handling

Framework handles:

- Network failures
- Timeout
- Retry
- Screenshot capture
- Logging

---

# Security

Sensitive information is never stored in source code.

Secrets stored in:

- .env
- GitHub Secrets
- BrowserStack Secrets

---

# Missing Requirements

The case study intentionally leaves some information unspecified.

Before implementation I would clarify the following:

1. Is MFA mandatory for every login?
2. Are dedicated QA environments available?
3. How is test data cleaned after execution?
4. Is database access available?
5. Are API tokens generated dynamically?
6. Which browsers are officially supported?
7. Which mobile devices should be tested?
8. Is visual regression testing required?
9. Is accessibility testing part of the scope?
10. What reporting format is preferred?
11. How many parallel executions are allowed?
12. What are the execution time expectations?
13. Are BrowserStack credentials already available?
14. Can API responses be mocked?
15. Are there rate limits on the APIs?

---

# Future Improvements

- Dockerized execution
- Kubernetes-based test execution
- Visual Regression Testing
- Accessibility Testing
- Contract Testing
- Performance Testing using k6
- Security Testing using OWASP ZAP
- Slack Notifications
- Self-healing locators
- AI-assisted flaky test detection