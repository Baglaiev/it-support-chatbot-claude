# Tests

This directory contains test files for the IT Support Chatbot.

## Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_chatbot.py

# Run with verbose output
pytest -v
```

## Test Structure

```
tests/
├── __init__.py
├── test_chatbot.py          # Main chatbot tests
├── test_document_processing.py  # Document loading tests
├── test_rag_chain.py        # RAG chain tests
└── conftest.py              # Pytest configuration and fixtures
```

## Writing Tests

Example test:

```python
import pytest
from src.it_support_chatbot_claude_api import load_llm

def test_load_llm():
    """Test LLM loading"""
    llm = load_llm(
        model_name="claude-sonnet-4-20250514",
        temperature=0.7
    )
    assert llm is not None
    assert llm.model_name == "claude-sonnet-4-20250514"
```

## Test Coverage

Aim for:
- 80%+ code coverage
- All critical paths tested
- Edge cases covered

## CI/CD Integration

Tests run automatically on:
- Every push to main/develop
- Every pull request
- Via GitHub Actions

---

For more information, see CONTRIBUTING.md
