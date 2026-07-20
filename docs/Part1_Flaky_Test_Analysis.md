# Part 1 – Debugging Flaky Test Code

## Objective

The objective of this task is to identify the causes of flaky Playwright tests, explain why they occur, and propose a reliable solution suitable for CI/CD environments.

---

# Flakiness Issues Identified

| Issue | Explanation |
|-------|-------------|
| No explicit wait after login | The dashboard loads asynchronously, causing assertions to execute before navigation completes. |
| Direct URL assertion | Redirect timing varies depending on browser and network conditions. |
| No wait for dashboard elements | Dynamic content may not be rendered immediately. |
| Hardcoded credentials | Difficult to maintain across multiple environments. |
| Browser is always Chromium | Does not validate Firefox or WebKit behaviour. |
| No retry strategy | Temporary network failures immediately fail the test. |
| No screenshots or logs | Makes debugging difficult in CI pipelines. |
| Uses default viewport | Different resolutions may produce different layouts. |
| No Page Object Model | UI logic and test logic are tightly coupled. |
| Test data hardcoded | Poor scalability for multi-tenant environments. |

---

# Why These Issues Occur in CI/CD

Local execution is usually faster and more stable.

CI environments differ because:

- Shared CPU resources
- Slower network
- Different browsers
- Different operating systems
- Different screen resolutions
- Higher execution latency

These conditions expose race conditions that may never appear locally.

---

# Improvements Applied

- Page Object Model
- Explicit waits
- Configuration-driven framework
- Logging
- Screenshot capture
- Test data externalization
- Browser configuration
- Parallel execution support
- Environment configuration
- API/UI separation

---

# Expected Benefits

- Reduced flaky failures
- Easier maintenance
- Better debugging
- Reusable framework
- CI/CD compatibility

---

# Best Practices Followed

- Used Page Object Model
- Removed duplicated locators
- Used reusable configuration
- Externalized test data
- Added logging
- Supported multiple browsers
- Added screenshot capability
- Designed framework for CI/CD execution
- Enabled parallel execution
- Kept tests independent

---

# Assumptions

Since WorkflowPro is a fictional application, the following assumptions were made:

- Login endpoint exists.
- Dashboard redirects to `/dashboard`.
- User credentials are valid.
- Authentication is handled through username and password.
- Project cards contain tenant names.
- BrowserStack configuration is available.