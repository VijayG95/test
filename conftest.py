import pytest
import requests

@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network calls not allowed during testing!")
    monkeypatch.setattr(requests,"get",lambda *args,**kwargs:stunted_get())