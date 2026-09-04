def test_rejects_bet_when_stake_exceeds_maximum(api_client):
    """
    Selected because maximum stake is a core financial business rule
    that should be enforced directly by the API.
    """

    reset_response = api_client.reset_balance()
    assert reset_response.status_code == 200

    balance_before_response = api_client.get_balance()
    assert balance_before_response.status_code == 200
    balance_before = balance_before_response.json()["balance"]

    matches_response = api_client.get_matches()
    assert matches_response.status_code == 200

    matches = matches_response.json()
    assert matches, "No matches returned by API"

    match_id = matches[0]["id"]

    response = api_client.place_bet(
        match_id=match_id,
        selection="HOME",
        stake=100.01,
    )

    assert response.status_code == 422

    balance_after_response = api_client.get_balance()
    assert balance_after_response.status_code == 200
    balance_after = balance_after_response.json()["balance"]

    assert balance_after == balance_before