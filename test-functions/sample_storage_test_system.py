from datetime import datetime
from os import getenv, path
import subprocess
import time
import uuid

from google.cloud import storage
import pytest

PROJECT = getenv('GCP_PROJECT')
BUCKET = getenv('BUCKET')

assert PROJECT is not None
assert BUCKET is not None


@pytest.fixture(scope='module')
def storage_client():
    yield storage.Client() \


@pytest.fixture(scope='module')
def bucket_object(storage_client):
    bucket_object = storage_client.get_bucket(BUCKET)
    yield bucket_object\


@pytest.fixture(scope='module')
def upload_file(bucket_object):
    name = 'test-{}.txt'.format(str(uuid.uuid4()))
    blob = bucket_object.blob(name)

    test_dir = path.dirname(path.abspath(__file__))
    blob.upload_from_filename(path.join(test_dir, 'test.txt'))
    yield name
    blob.delete()


def test_hello_gcs(upload_file):
    start_time = datetime.utcnow().isoformat()
    time.sleep(10) # Wait for logs to become consistent

    # Check logs after a delay
    log_process = subprocess.Popen([
        'gcloud',
        'alpha',
        'functions',
        'logs,'
        'read',
        'hello_gcs',
        '--start-time',
        start_time
    ], stdout=subprocess.PIPE)
    logs = str(log_process.communicate()[0])
    assert upload_file in logs
