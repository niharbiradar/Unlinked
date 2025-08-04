# RULES.md — Anti-LinkedIn Development Guidelines

---

## 1. Code Quality & Maintainability

- Write **clean, modular, and reusable** code with clear separation of concerns.  
- Use **descriptive, consistent naming** for variables, functions, and components.  
- Follow **DRY principles**; avoid duplication.  
- Add **comments and docstrings** where clarity is needed, but don’t over-comment obvious code.  
- Keep functions and components **small and focused**.

---

## 2. Security Best Practices

- **Always validate and sanitize all user inputs** on the backend before processing or storing.  
- Protect against common web vulnerabilities:  
  - Prevent **NoSQL injection** in MongoDB queries.  
  - Prevent **Cross-Site Scripting (XSS)** by escaping outputs as needed.  
  - Implement proper **CORS policies** — whitelist only required origins.  
  - Securely handle **authentication tokens and secrets**; never hardcode them in code. Use environment variables or secret managers.  
- Use **HTTPS** for all communications (assumed in deployment).  
- Ensure **passwords or sensitive data** (if any) are properly hashed/encrypted.

---

## 3. Performance & Scalability

- Use **async/await** for non-blocking backend operations (FastAPI + Motor).  
- Cache repeated data fetches on the frontend with React Query’s caching strategies.  
- Add appropriate **indexes** in MongoDB to speed up frequent queries.  
- Lazy load React components and split code bundles when necessary.  
- Avoid premature optimization or adding complexity before justified by use cases.

---

## 4. Testing & Reliability

- Write **unit tests** for all critical backend logic and frontend components.  
- Write **integration tests** for API endpoints.  
- Use mocks or stubs to isolate dependencies in tests.  
- Run tests frequently during development and before deployments.  
- Handle errors gracefully; provide meaningful messages and status codes.

---

## 5. Consistency & Standards

- Follow standard **style guides**:  
  - Python: **PEP8**  
  - JavaScript/TypeScript: **Airbnb** or similar  
- Use formatting tools: **Black** for Python, **ESLint + Prettier** for JS/TS.  
- Make **small, atomic commits** with clear descriptive messages.  
- Keep dependencies updated and monitor for security patches.

---

## 6. Documentation & Communication

- Maintain a **project log** documenting architectural decisions and major code changes.  
- Before starting new code, **confirm current project state and requirements** to avoid conflicts.  
- Document APIs, components, and complex logic clearly but concisely.  
- Refactor code regularly to keep the codebase clean and manageable.

---

## 7. Development Process Guidelines

- Do not **hallucinate or assume** requirements beyond defined specs.  
- Always **reference the current project plan and rules** before writing new code.  
- Prioritize **simplicity and clarity**; avoid overengineering.  
- Ensure all code is **scalable, secure, and efficient**, but no unnecessary complexity.  
- Use **Docker** for consistent development and production environments.

---

*End of Rules.md*
