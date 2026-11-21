import pytest

from models.provider_ids import GenericProviderID, ModelProviderID


def test_rejects_full_form_id_with_trailing_newline() -> None:
    with pytest.raises(ValueError, match="Invalid plugin id"):
        GenericProviderID("langgenius/openai/gpt\n")


def test_rejects_short_form_id_with_trailing_newline() -> None:
    with pytest.raises(ValueError, match="Invalid plugin id"):
        GenericProviderID("openai\n")


def test_full_form_id_without_newline_parses() -> None:
    provider = GenericProviderID("langgenius/openai/gpt")
    assert provider.organization == "langgenius"
    assert provider.plugin_name == "openai"
    assert provider.provider_name == "gpt"


def test_short_form_id_without_newline_parses() -> None:
    provider = ModelProviderID("google")
    assert provider.organization == "langgenius"
    assert provider.provider_name == "google"


def test_rejects_embedded_newline() -> None:
    with pytest.raises(ValueError, match="Invalid plugin id"):
        GenericProviderID("langgenius/openai\n/gpt")
