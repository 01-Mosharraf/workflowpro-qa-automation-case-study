# Part 3 – API + UI Integration Test

## Objective

Validate the complete project creation workflow using API, Web UI, and Mobile testing while ensuring tenant isolation.

---

# Test Flow

```
API
 ↓
Create Project
 ↓
Verify Response
 ↓
Login Web UI
 ↓
Search Project
 ↓
Verify Project
 ↓
BrowserStack Mobile
 ↓
Verify Mobile UI
 ↓
Login Different Tenant
 ↓
Verify Project Not Visible
 ↓
Delete Project
```

---

# Step 1 – API

Create project.

Expected Result

- HTTP 201
- Project ID returned

---

# Step 2 – Web UI

Login as Company1 Admin.

Search project.

Expected Result

Project should appear.

---

# Step 3 – Mobile

Launch BrowserStack Android/iPhone.

Login.

Search project.

Expected Result

Project visible.

Responsive layout correct.

---

# Step 4 – Tenant Isolation

Login as Company2.

Search same project.

Expected Result

Project must NOT appear.

---

# Step 5 – Cleanup

Delete project through API.

Expected Result

Environment restored.

---

# Edge Cases

The framework should handle:

- Slow network
- Timeout
- Duplicate project names
- Invalid token
- Invalid tenant
- Browser crash
- Mobile orientation change
- Retry logic
- API 500 errors
- Session expiration

---

# Assumptions

- Authentication endpoint exists.
- API token is available.
- BrowserStack account is configured.
- Test users already exist.
- Project deletion endpoint exists.

---

# Why API + UI?

Using the API to create data is much faster and more reliable than creating it manually through the UI.

The UI is then used only for validation.

This approach reduces execution time and improves test stability.