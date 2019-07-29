import pytest
from actions import resolve
from echo import controllers



@pytest.fixture
def expected_action():
    return 'echo'

# @pytest.fixture
# def expected_controller():
#      return controllers.get_echo


def test_resolve_action(expected_action):
    assert resolve(expected_action) == controllers.get_echo # вот тут не ясно, как сделать красиво