import warnings

import pytest


@pytest.fixture(autouse=True)
def suppress_warnings():
    """Suprime warnings desnecessários durante os testes."""
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=PendingDeprecationWarning)
