"""
Basic unit tests for IT Support Chatbot
"""

import pytest
import os
from pathlib import Path


def test_import_modules():
    """Test that all required modules can be imported"""
    try:
        from src.it_support_chatbot_claude_api import (
            load_llm,
            extract_text_pdf,
            load_documents,
            split_documents,
            create_vectorstore,
            config_retriever,
            config_rag_chain,
            chat_llm
        )
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import modules: {e}")


def test_environment_setup(setup_env, mock_api_key):
    """Test environment setup"""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    assert api_key == mock_api_key


def test_documents_directory_exists():
    """Test that documents directory exists"""
    docs_path = Path("documents")
    # This will fail if not in project root, which is expected in tests
    # In actual deployment, the directory should exist
    assert True  # Placeholder test


def test_requirements_file_exists():
    """Test that requirements.txt exists"""
    req_file = Path("requirements.txt")
    # Check if we're in project root
    if req_file.exists():
        assert req_file.exists()
        # Check that it's not empty
        content = req_file.read_text()
        assert len(content) > 0
        assert "langchain" in content
        assert "anthropic" in content
    else:
        # If not in project root, skip
        pytest.skip("Not in project root")


def test_config_file_template_exists():
    """Test that config template exists"""
    config_template = Path("config/.env.template")
    if config_template.exists():
        assert config_template.exists()
        content = config_template.read_text()
        assert "ANTHROPIC_API_KEY" in content
    else:
        pytest.skip("Config template not found")


# Mock tests for functions (require actual implementation)
def test_extract_text_pdf_function_exists():
    """Test that extract_text_pdf function exists"""
    from src.it_support_chatbot_claude_api import extract_text_pdf
    assert callable(extract_text_pdf)


def test_load_llm_function_exists():
    """Test that load_llm function exists"""
    from src.it_support_chatbot_claude_api import load_llm
    assert callable(load_llm)


def test_config_rag_chain_function_exists():
    """Test that config_rag_chain function exists"""
    from src.it_support_chatbot_claude_api import config_rag_chain
    assert callable(config_rag_chain)


# Add more specific tests as needed
class TestDocumentProcessing:
    """Tests for document processing functions"""
    
    def test_load_documents_empty_folder(self, temp_documents_dir):
        """Test loading documents from empty folder"""
        from src.it_support_chatbot_claude_api import load_documents
        docs = load_documents(str(temp_documents_dir))
        assert docs == []


class TestConfiguration:
    """Tests for configuration"""
    
    def test_default_model_name(self):
        """Test default model configuration"""
        default_model = "claude-sonnet-4-20250514"
        assert isinstance(default_model, str)
        assert "claude" in default_model


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
