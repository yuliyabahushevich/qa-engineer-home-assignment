import requests


class BettingClient:
    def __init__(self, base_url: str, user_id: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "x-user-id": user_id
        })

    def get_matches(self):
        return self.session.get(
            f"{self.base_url}/api/matches"
        )

    def get_balance(self):
        return self.session.get(
            f"{self.base_url}/api/balance"
        )

    def place_bet(
        self,
        match_id: str,
        selection: str,
        stake: float,
    ):
        payload = {
            "matchId": match_id,
            "selection": selection,
            "stake": stake,
        }

        return self.session.post(
            f"{self.base_url}/api/place-bet",
            json=payload,
        )

    def reset_balance(self):
        return self.session.post(
            f"{self.base_url}/api/reset-balance"
        )