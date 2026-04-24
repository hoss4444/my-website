# Skill: Secure & Scalable Data Handling

## 1. Data Validation & Sanitization
- **Input Rule:** Never trust client-side data. All inputs must be sanitized to prevent XSS (Cross-Site Scripting).
- **Type Checking:** Ensure data matches expected types (e.g., email strings must be validated, numbers must be checked for ranges).
- **Empty States:** Always define "Null" or "Empty" states for UI elements to prevent site crashes when data is missing.

## 2. API & Fetch Operations
- **Error Handling:** Every fetch request must have a `.catch()` block or `try/catch` wrapper.
- **Loading States:** UI must provide visual feedback (spinners, skeletons) while data is "In-Flight."
- **Timeouts:** Implement a timeout of 10 seconds for all external API calls to prevent hanging processes.

## 3. Storage Standards
- **Local Storage:** Use `localStorage` only for non-sensitive UI preferences (e.g., Theme: Dark/Light).
- **Sensitive Data:** Never store passwords, personal IDs, or private keys in client-side code or local storage.
- **JSON Structure:** When creating local data mocks, use a flat hierarchy where possible to simplify mapping.

## 4. Performance
- **Debouncing:** Any data-fetching triggered by user input (like a search bar) must be debounced by 300ms.
- **Caching:** Cache expensive API results in memory if the data is unlikely to change during the user session.
