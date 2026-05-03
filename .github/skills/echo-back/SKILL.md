---
title: Echo-back Skill
name: echo-back
description: Returns verbatim the provided `this` parameter prefixed with a fixed phrase.
version: 1.0.0
created: 2026-05-02
---

# Echo-back Skill

## When to use
Use this skill when you want the agent to return verbatim the value provided in the `this` parameter.

## Behavior / Instructions
1. Look for a parameter named `this` in the incoming request, prompt, or call context.
2. If `this` is present, respond with the exact phrase: `Hey buddy, you wanted to echo back ` followed immediately by the `this` value. Preserve the `this` value's characters and formatting, but do not add any other text, explanation, or commentary.
3. If `this` is missing or empty, ask a single concise clarifying question requesting the value for `this`.

## Examples
- Input: `this=hello` → Output: `Hey buddy, you wanted to echo back `hello`
- Input: `this: {"a": 1}` → Output: `Hey buddy, you wanted to echo back `{"a": 1}`
- Input: `this: ```\nline1\nline2\n``` ` → Output: `Hey buddy, you wanted to echo back ```\nline1\nline2\n``` `

## Constraints
- Never prepend or append additional commentary.
- Preserve the exact characters and formatting of the `this` value.

## Minimal Answer Policy
When `this` is present, return only the phrase `Hey buddy, you wanted to echo back ` followed immediately by the `this` value (no extra commentary). When prompting for a missing `this`, ask exactly one short question such as: "What should `this` be?"

