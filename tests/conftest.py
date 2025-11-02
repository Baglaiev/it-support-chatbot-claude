"""
Test configuration and fixtures for pytest
"""

import pytest
import os
from pathlib import Path


@pytest.fixture
def mock_api_key():
    """Mock API key for testing"""
    return "sk-ant-test-key-12345"


@pytest.fixture
def setup_env(mock_api_key):
    """Setup test environment variables"""
    os.environ["ANTHROPIC_API_KEY"] = mock_api_key
    yield
    # Cleanup
    if "ANTHROPIC_API_KEY" in os.environ:
        del os.environ["ANTHROPIC_API_KEY"]


@pytest.fixture
def temp_documents_dir(tmp_path):
    """Create temporary documents directory"""
    docs_dir = tmp_path / "documents"
    docs_dir.mkdir()
    return docs_dir


@pytest.fixture
def sample_pdf_path(temp_documents_dir):
    """Create a sample PDF path (not actual PDF content)"""
    pdf_path = temp_documents_dir / "test_document.pdf"
    return pdf_path


@pytest.fixture
def mock_retriever():
    """Mock retriever for testing"""
    class MockRetriever:
        def invoke(self, query):
            return [{"content": "Mock document content"}]
    
    return MockRetriever()
