import pytest
from main import hello
  
@pytest.mark.parametrize(('expected',), [
  ('Hello CodePipeline.',),
])
def test_hello(expected):
  assert hello() == expected
