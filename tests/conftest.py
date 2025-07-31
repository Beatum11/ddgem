import pytest
from pytest_mock import MockerFixture
from src.ddgem.utils.ddsearch import DDSearch
from google import genai
from src.ddgem.utils.gem import GeminiClient


@pytest.fixture
def genai_setup(mocker: MockerFixture):

    genai_mock = mocker.Mock(spec=genai)
    search_mock = mocker.Mock(spec=DDSearch)
    g_client = GeminiClient(search_client=search_mock, genai_client=genai_mock)

    return g_client, search_mock, genai_mock

