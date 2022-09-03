import pytest
from main import hello

#def test_hello():
#  assert hello() == 'Hello CodePipeline!'
  
  
@pytest.mark.parametrize(('expected',), [
  ('Hello CodePipeline.',),
])
def test_hello(expected):
  assert hello() == expected