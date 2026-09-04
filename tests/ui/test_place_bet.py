from decimal import Decimal

from config import BASE_URL, USER_ID
from pages.betting_page import BettingPage


ODDS_BUTTON_ID = (
    "odds-ligue-1-nice-psg-2026-09-19-away"
)

STAKE = Decimal("10.00")


def _assert_mapping_matches(
    actual: dict[str, object],
    expected: dict[str, object],
    context: str,
):
    mismatches = [
        (
            f"- {field}: expected {expected[field]}, "
            f"actual {actual[field]}"
        )
        for field in expected
        if actual[field] != expected[field]
    ]

    assert not mismatches, (
        f"{context} mismatch:\n" + "\n".join(mismatches)
    )


def test_user_can_place_single_bet(
    driver,
    api_client,
):
    """
    Covers the critical E2E betting journey.

    Verifies payout calculation, successful placement,
    receipt consistency and balance update.
    """

    # Arrange
    reset_response = api_client.reset_balance()
    assert reset_response.status_code == 200, (
        "Failed to reset balance before UI test"
    )

    page = BettingPage(
        driver=driver,
        base_url=BASE_URL,
        user_id=USER_ID,
    )

    page.open()

    balance_before = page.get_balance()

    # Act
    selected_odds = page.select_odds(
        ODDS_BUTTON_ID
    )

    page.enter_stake(STAKE)

    expected_payout = (
        STAKE * selected_odds
    ).quantize(
        Decimal("0.01")
    )

    bet_slip_payout = (
        page.get_potential_payout()
    )

    page.place_bet()

    receipt = page.get_receipt()
    success_title = page.get_success_title()

    page.close_receipt()

    balance_after = page.get_balance()

    expected_balance = (
        balance_before - STAKE
    ).quantize(
        Decimal("0.01")
    )

    expected_financials = {
        "Bet Slip payout": expected_payout,
        "Receipt stake": STAKE,
        "Receipt odds": selected_odds,
        "Receipt payout": expected_payout,
        "Receipt payout consistency": bet_slip_payout,
        "Balance after bet": expected_balance,
    }

    actual_financials = {
        "Bet Slip payout": bet_slip_payout,
        "Receipt stake": receipt.stake,
        "Receipt odds": receipt.odds,
        "Receipt payout": receipt.payout,
        "Receipt payout consistency": receipt.payout,
        "Balance after bet": balance_after,
    }

    # Assert critical flow
    assert success_title == "Bet Placed Successfully!", (
        f"Unexpected success title: {success_title!r}"
    )

    assert receipt.bet_id.startswith("#B-"), (
        f"Unexpected receipt bet id format: {receipt.bet_id!r}"
    )

    assert receipt.match, "Receipt match should not be empty"
    assert receipt.placed_at, "Receipt placed_at should not be empty"

    _assert_mapping_matches(
        actual=actual_financials,
        expected=expected_financials,
        context="Financial verification",
    )

