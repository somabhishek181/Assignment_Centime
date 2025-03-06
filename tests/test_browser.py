import pytest


@pytest.mark.usefixtures("setup")
class TestBrowserIniti:
    def test_title(self, setup):
        assert "Automation Practice Site" in setup.title
