import main


def test_print(capsys):
    name = 'test'
    data = {'objectId': name}

    # Call tested function
    main.hello_gcs(data, None)
    out, err = capsys.readouterr()
    assert out == 'File: {}.\n'.format(name)
