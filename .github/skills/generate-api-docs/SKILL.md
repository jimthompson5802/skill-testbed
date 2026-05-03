---
name: generate-api-docs
description: "Generate API documentation from source code. Use when the user asks to document API routes, generate endpoint docs, or create a summary of HTTP methods and paths from code."
---

# Generate API Documentation

## When to use
When the user asks to generate API documentation from code.

## Instructions
1. Scan all files under /app
2. Identify API routes
3. Extract:
   - HTTP method
   - Route path
   - Function name
4. Generate Markdown documentation
5. Include a summary table of endpoints