import os

from gh import gh
from packaging import version

# change dir to tests directory to make relative paths possible
os.chdir(os.path.dirname(os.path.realpath(__file__)))


def test_field():
    endpoint = 'repos/dvershinin/lastversion/license'

    output = gh.api_call(endpoint, 'GET', 'path')

    assert output == 'LICENSE'
