import pytest

import json

import atexit

import requests

from memes_service_client import MemesServiceClient

from pact import Consumer, Provider


@pytest.fixture(scope='module')
def pact():
    pact = Consumer('Memes-Website').has_pact_with(
        Provider('Memes-Service')
    )
    pact.start_service()
    atexit.register(pact.stop_service)
    return pact


@pytest.fixture(scope='module')
def meme_client(pact):
    return MemesServiceClient(pact.uri)


def test_get_meme_by_id_with_wrong_id(pact, meme_client):
    meme_id = 1234
    expected = json.dumps({'error': f'Meme with id {meme_id} not found.'})

    pact.given(
        f'Meme with id {meme_id} does not exist'
    ).upon_receiving(
        f'a requests for meme with id {meme_id}'
    ).with_request(
        'get', f'/meme/{meme_id}'
    ).will_respond_with(404, body=expected)

    with pact:
        result = meme_client.get_meme(meme_id=meme_id)

    assert json.dumps(result) == expected


def test_get_meme_by_id_with_correct_id(pact, meme_client):
    meme_id = 0
    expected = json.dumps(
        {
            'id': 0,
            'starts': 4.6,
            'url': 'https://wyncode.co/wp-content/uploads/2014/08/171.jpg'
        }
    )

    pact.given(
        f'Meme with id {meme_id} exists'
    ).upon_receiving(
        f'a requests for meme with id {meme_id}'
    ).with_request(
        'get', f'/meme/{meme_id}'
    ).will_respond_with(200, body=expected)

    with pact:
        result = meme_client.get_meme(meme_id)

    assert json.dumps(result) == expected
