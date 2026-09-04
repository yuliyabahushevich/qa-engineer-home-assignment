Bugs:

BG1 - Available balance is not updated in the UI after successful bet placement
Severity: High
Steps to reproduce:
1. Log in to the platform with valid credentials.
2. Navigate to the betting section and select an upcoming match to place a bet on.
3. Select odds and enter a valid stake amount.
4. Click on the "Place Bet" button.
5. Verify that the bet is successfully placed and a confirmation message is displayed.
6. Check the user's balance to ensure that it has been updated correctly after the bet placement.
Expected Result:
The bet is successfully placed, and the user's balance is updated correctly to reflect the bet amount.
Actual Result:
The bet is successfully placed, but the user's balance is not updated correctly
Business Impact:
Users may lose trust in the platform if their balance is not updated correctly after placing a bet, leading to potential financial losses and damage to the platform's reputation.
Evidence:see screenshots

BG2 - Past matches are shown in the matches section
Severity: Medium
Steps to reproduce:
1. Log in to the platform with valid credentials.
2. Navigate to the matches section.
3. Verify that only upcoming matches are displayed.
Expected Result:
Only upcoming matches should be displayed in the matches section.
Actual Result:
Past matches are displayed in the matches section.
Business Impact:
Users may be confused or frustrated if they see past matches in the matches section, leading to a poor user experience and potential loss of engagement with the platform.
Evidence: see screenshots

BG3 -  Bet can be successfully placed on a past match
Severity: Critical
Steps to reproduce:
1. Log in to the platform with valid credentials.
2. Navigate to the matches section and select a past match.
3. Attempt to place a bet on the past match.
Expected Result:
Users should not be able to place bets on past matches.
Actual Result:
The bet on a past match is successfully processed and a success receipt is displayed.
Business Impact:
Allowing users to place bets on past matches can lead to financial losses for users and damage to the platform's reputation, as it undermines the integrity of the betting process.
Evidence: see screenshots

BG4 - Odds filter does not support the full specified odds range
Severity: Medium
Steps to reproduce:
1. Log in to the platform with valid credentials.
2. Navigate to the betting section with matches to place a bet on.
3. Click on the filter for odds and select a valid min - max odds value: 1,01- 1000.
Expected Result:
The odds filter should support the full valid range from 1.01 to 1000.00.
Actual Result:
The odds filter only allows values from 1 to 10, so the full specified odds range cannot be configured.
Business Impact:
Users cannot filter matches using the full supported odds range defined by the product requirements, which limits the functionality of the filter.

BG5 - Potential payout in success receipt does not match the calculated payout
Severity: High
Steps to reproduce:
1. Open the application using a valid user ID.
2. Select an upcoming match and an outcome with odds 1.70.
3. Enter a stake of €10.00.
4. Verify that the Bet Slip shows a potential payout of €17.00.
5. Place the bet.
6. Check the potential payout displayed in the success receipt.
Expected Result:
The success receipt should display a potential payout of €17.00
(€10.00 × 1.70), consistent with the Bet Slip value.
Actual Result:
The Bet Slip displays €17.00, but the success receipt displays €20.00.
Business Impact:
Users receive inconsistent financial information after placing a bet,
which may misrepresent their potential return and reduce trust in the platform.

BG6 - Available balance is not shown in bet slip
Severity: Medium

BG7 - No validation feedback for invalid odds filter range
Severity: Medium

BG8 - No selection is displayed in success message after placing a bet
Severity: Medium
