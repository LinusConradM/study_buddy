import pytest

from parsers import extract_text


def test_extract_text_unsupported_extension():
    with pytest.raises(ValueError):
        extract_text('notes.txt')