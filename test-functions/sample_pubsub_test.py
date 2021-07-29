import base64

import main


def test_print_hello_world(capsys):
    data = {}

    # Call tested function
    main.hello_pubsub(data, None)
    out, err = capsys.readouterr()
    assert out == 'Hello World!\n'


def test_print_name(capsys):
    name = 'test'
    data = {'data': base64 .b64encode(name.encode())}

    # Call tested function
    main.hello_pubsub(data, None)
    out, err = capsys.readouterr()
    assert out == 'Hello World {}!\n'.format(name)
