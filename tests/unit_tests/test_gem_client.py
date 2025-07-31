import pytest

def test_get_fact_checked_answer(genai_setup, mocker):

    g_client, search_mock, genai_mock = genai_setup

    mock_api_response = mocker.Mock()
    mock_api_response.text = '{"title": "Success"}'
    genai_mock.models.generate_content.return_value = mock_api_response

    search_mock.get_fresh_summaries.return_value = ["fact"]

    result = g_client.get_fact_checked_answer(query='Who is the best developer in the world')

    assert result['title'] == 'Success'
    search_mock.get_fresh_summaries.assert_called_once()
    genai_mock.models.generate_content.assert_called_once()



def test_empty_query_string(genai_setup):

    g_client, _, _= genai_setup

    with pytest.raises(ValueError):
        g_client.get_fact_checked_answer(query='')


def test_query_is_none(genai_setup):
    g_client, _, _= genai_setup

    with pytest.raises(ValueError):
        g_client.get_fact_checked_answer(query=None)


def test_empty_summaries_list(genai_setup, mocker):

    g_client, search_mock, genai_mock = genai_setup

    mock_api_response = mocker.Mock()
    mock_api_response.text = '{"title": "Success"}'
    genai_mock.models.generate_content.return_value = mock_api_response

    search_mock.get_fresh_summaries.return_value = []

    result = g_client.get_fact_checked_answer(query='Who is the best developer in the world')

    assert result['title'] == 'Success'
    search_mock.get_fresh_summaries.assert_called_once()
    genai_mock.models.generate_content.assert_called_once()


#TO-DO - need to add more tests later - not_json_response, for example
