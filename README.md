# QA Engineer Home Assignment

Automated test suite for a betting application using API and UI coverage.

## Tech Stack
- Python 3
- `pytest`
- Selenium WebDriver
- `requests`
- `python-dotenv` (`config.py` imports `dotenv`)

## Project Structure

```text
qa-engineer-home-assignment/
├── api/
│   └── betting_client.py
├── docs/
│   ├── execution_results.md
│   ├── strategy_and_recommendations.md
│   └── test_plan.md
├── pages/
│   └── betting_page.py
├── tests/
│   ├── api/
│   │   └── test_place_bet_validation.py
│   └── ui/
│       └── test_place_bet.py
├── config.py
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## What the suite covers
- `tests/api/test_place_bet_validation.py`
  - verifies the API rejects a bet when the stake exceeds the maximum allowed value
- `tests/ui/test_place_bet.py`
  - covers the critical end-to-end flow for placing a single bet
  - validates success messaging, receipt fields, payout consistency, and balance behavior

## Prerequisites
- Python 3 available on your machine
- Internet access to reach the target application at `https://qae-assignment-tau.vercel.app`
- A valid `USER_ID`
- Google Chrome installed locally for UI tests

Note: the `driver` fixture in `conftest.py` creates `webdriver.Chrome()`, so UI tests depend on a local Chrome-capable Selenium setup.

## Setup

On this macOS machine, `python3` is available while `python` is not, so use `python3` to create the virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install python-dotenv
```

Why the extra install?
- `config.py` imports `from dotenv import load_dotenv`
- the current `requirements.txt` does not list `python-dotenv`

## Configuration

Create a `.env` file in the project root:

```dotenv
USER_ID=<candidate-user-id>
```

Alternatively, you can export the variable in your shell:

```bash
export USER_ID=<candidate-user-id>
```

## Running the tests

Run all tests:

```bash
pytest
```

Run API tests only:

```bash
pytest tests/api -q
```

Run UI tests only:

```bash
pytest tests/ui -q
```

Run the main UI scenario directly:

```bash
pytest tests/ui/test_place_bet.py -q
```

## Validation notes
- `pytest tests/api -q` was validated in this workspace and passes.
- The UI test currently exposes known application issues documented in `docs/execution_results.md`, including:
  - balance not updating after bet placement
  - payout in the success receipt not matching the bet slip payout

## Documentation
- `docs/test_plan.md`
- `docs/execution_results.md`
- `docs/strategy_and_recommendations.md`
