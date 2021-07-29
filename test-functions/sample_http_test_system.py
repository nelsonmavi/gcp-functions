import os
import uuid

import requests


def test_no_args():
    base_url = os.getenv('BASE_URL')
    assert base_url is not None

    res = requests.get('{}/hello_http'.format(base_url))
    assert res.text == 'Hello, World'


def test_args():
    base_url = os.getenv('BASE_URL')
    assert base_url is not None

    name = str(uuid.uuid4())
    res = requests.post(
        '{}/hello_http'.format(base_url),
        json={'name': name}
    )
    assert res.text == 'Hello, {}!'.format(name)

