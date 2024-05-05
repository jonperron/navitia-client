import pytest

from unittest.mock import MagicMock, patch

from navitia_client.entities.network import Network
from navitia_client.client.apis.public_transportation_apis import NetworkApiClient


@pytest.fixture
def network_apis():
    return NetworkApiClient(
        auth_token="foobar", base_navitia_url="https://api.navitia.io/v1/"
    )


@patch.object(NetworkApiClient, "get_navitia_api")
def test_list_entity_collection_from_region(
    mock_get_navitia_api: MagicMock, network_apis: NetworkApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "networks": [
            {"id": "network:foo", "links": [], "name": "Foo"},
            {"id": "network:bar", "links": [], "name": "Bar"},
        ],
        "pagination": {
            "items_on_page": 25,
            "items_per_page": 25,
            "start_page": 0,
            "total_result": 99,
        },
    }
    mock_get_navitia_api.return_value = mock_response

    # When
    networks, _ = network_apis.list_entity_collection_from_region("tuz")

    # Then
    assert len(networks) == 2
    assert isinstance(networks[1], Network)


@patch.object(NetworkApiClient, "get_navitia_api")
def test_get_entity_by_id(
    mock_get_navitia_api: MagicMock, network_apis: NetworkApiClient
) -> None:
    # Given
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "networks": [
            {"id": "network:foo", "links": [], "name": "Foo"},
        ],
        "pagination": {
            "items_on_page": 25,
            "items_per_page": 25,
            "start_page": 0,
            "total_result": 99,
        },
    }
    mock_get_navitia_api.return_value = mock_response

    # When
    networks, _ = network_apis.get_entity_by_id("tuz", "1")

    # Then
    assert len(networks) == 1
    assert isinstance(networks[0], Network)
