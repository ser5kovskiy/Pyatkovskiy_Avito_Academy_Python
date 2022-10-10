import pytest
from what_is_year_now import what_is_year_now
from unittest.mock import MagicMock, patch


@patch("what_is_year_now.urllib.request.urlopen")
@patch("what_is_year_now.json.load")
def test_first_format(json_load_mock, openurl_mock):
    resp_mock = MagicMock()
    openurl_mock.return_value = resp_mock
    resp_mock.__enter__.return_value = resp_mock
    json_load_mock.return_value = {"currentDateTime": '2022-10-10'}
    assert what_is_year_now() == 2022


@patch("what_is_year_now.urllib.request.urlopen")
@patch("what_is_year_now.json.load")
def test_second_format(json_load_mock, openurl_mock):
    resp_mock = MagicMock()
    openurl_mock.return_value = resp_mock
    resp_mock.__enter__.return_value = resp_mock
    json_load_mock.return_value = {"currentDateTime": '10.10.2022'}
    assert what_is_year_now() == 2022


@patch("what_is_year_now.urllib.request.urlopen")
@patch("what_is_year_now.json.load")
def test_unusual_second_format(json_load_mock, openurl_mock):
    resp_mock = MagicMock()
    openurl_mock.return_value = resp_mock
    resp_mock.__enter__.return_value = resp_mock
    json_load_mock.return_value = {"currentDateTime": '0001-01-01'}
    assert what_is_year_now() == 1


@patch("what_is_year_now.urllib.request.urlopen")
@patch("what_is_year_now.json.load")
def test_unusual_second_format(json_load_mock, openurl_mock):
    resp_mock = MagicMock()
    openurl_mock.return_value = resp_mock
    resp_mock.__enter__.return_value = resp_mock
    json_load_mock.return_value = {"currentDateTime": '01.01.0001'}
    assert what_is_year_now() == 1


@patch("what_is_year_now.urllib.request.urlopen")
@patch("what_is_year_now.json.load")
def test_first_format_exception(json_load_mock, openurl_mock):
    resp_mock = MagicMock()
    openurl_mock.return_value = resp_mock
    resp_mock.__enter__.return_value = resp_mock
    json_load_mock.return_value = {"currentDateTime": '2022.10.10'}
    with pytest.raises(ValueError):
        what_is_year_now()


@patch("what_is_year_now.urllib.request.urlopen")
@patch("what_is_year_now.json.load")
def test_second_format_exception(json_load_mock, openurl_mock):
    resp_mock = MagicMock()
    openurl_mock.return_value = resp_mock
    resp_mock.__enter__.return_value = resp_mock
    json_load_mock.return_value = {"currentDateTime": '10-10-2022'}
    with pytest.raises(ValueError):
        what_is_year_now()
