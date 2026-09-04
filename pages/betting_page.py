from dataclasses import dataclass
from decimal import Decimal

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@dataclass(frozen=True)
class BetReceipt:
    bet_id: str
    match: str
    stake: Decimal
    odds: Decimal
    payout: Decimal
    placed_at: str


class BettingPage:
    # Bet slip
    STAKE_INPUT = (
        By.ID,
        "bet-slip-stake-input",
    )

    PLACE_BET_BUTTON = (
        By.ID,
        "bet-slip-place-bet",
    )

    BET_SLIP_PAYOUT = (
        By.ID,
        "bet-slip-potential-payout",
    )

    # Header
    HEADER_BALANCE = (
        By.CSS_SELECTOR,
        "#header-balance span:last-child",
    )

    # Success modal
    SUCCESS_MODAL = (
        By.CSS_SELECTOR,
        "div.modalBody",
    )

    SUCCESS_TITLE = (
        By.CSS_SELECTOR,
        "div.modalBody h2.modalTitle",
    )

    RECEIPT_BET_ID = (
        By.ID,
        "modal-success-bet-id",
    )

    RECEIPT_MATCH = (
        By.ID,
        "modal-success-match",
    )

    RECEIPT_STAKE = (
        By.ID,
        "modal-success-stake",
    )

    RECEIPT_ODDS = (
        By.ID,
        "modal-success-odds",
    )

    RECEIPT_PAYOUT = (
        By.ID,
        "modal-success-payout",
    )

    RECEIPT_PLACED_AT = (
        By.ID,
        "modal-success-placed-at",
    )

    RECEIPT_CLOSE_BUTTON = (
        By.ID,
        "modal-success-close",
    )

    def __init__(
        self,
        driver,
        base_url: str,
        user_id: str,
        timeout: int = 10,
    ):
        self.driver = driver
        self.url = f"{base_url}/?user-id={user_id}"
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.url)

    def select_odds(
        self,
        odds_button_id: str,
    ) -> Decimal:
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, odds_button_id)
            )
        )

        odds_text = button.find_element(
            By.CSS_SELECTOR,
            ".oddsButtonValue",
        ).text

        odds = Decimal(odds_text)

        button.click()

        return odds

    def enter_stake(
        self,
        stake: Decimal,
    ):
        stake_input = self.wait.until(
            EC.visibility_of_element_located(
                self.STAKE_INPUT
            )
        )

        stake_input.clear()
        stake_input.send_keys(
            f"{stake:.2f}"
        )

    def get_potential_payout(self) -> Decimal:
        payout_text = self.wait.until(
            EC.visibility_of_element_located(
                self.BET_SLIP_PAYOUT
            )
        ).text

        return self._parse_money(
            payout_text
        )

    def get_balance(self) -> Decimal:
        balance_text = self.wait.until(
            EC.visibility_of_element_located(
                self.HEADER_BALANCE
            )
        ).text

        return self._parse_money(
            balance_text
        )

    def place_bet(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.PLACE_BET_BUTTON
            )
        ).click()

    def get_success_title(self) -> str:
        return self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_TITLE
            )
        ).text

    def get_receipt(self) -> BetReceipt:
        self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_MODAL
            )
        )

        return BetReceipt(
            bet_id=self.driver.find_element(
                *self.RECEIPT_BET_ID
            ).text,

            match=self.driver.find_element(
                *self.RECEIPT_MATCH
            ).text,

            stake=self._parse_money(
                self.driver.find_element(
                    *self.RECEIPT_STAKE
                ).text
            ),

            odds=Decimal(
                self.driver.find_element(
                    *self.RECEIPT_ODDS
                ).text
            ),

            payout=self._parse_money(
                self.driver.find_element(
                    *self.RECEIPT_PAYOUT
                ).text
            ),

            placed_at=self.driver.find_element(
                *self.RECEIPT_PLACED_AT
            ).text,
        )

    def close_receipt(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.RECEIPT_CLOSE_BUTTON
            )
        ).click()

        self.wait.until(
            EC.invisibility_of_element_located(
                self.SUCCESS_MODAL
            )
        )

    @staticmethod
    def _parse_money(
        value: str,
    ) -> Decimal:
        amount = value.split("€")[-1].strip()

        return Decimal(amount)