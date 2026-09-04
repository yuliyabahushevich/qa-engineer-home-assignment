Test plan: Test scenirious

TS1 - Placing a single bet on the platform and validating the bet placement and the balance update.
Priority: Critical

Risk Rationale: Placing a bet is a critical functionality of the platform, and any issues with this feature can lead to financial losses for users and damage to the platform's reputation. Validating the bet placement and balance update ensures that users can trust the platform to handle their bets accurately and securely.
Steps:
1. Log in to the platform with valid credentials.
2. Navigate to the betting section and select upcoming match to place a bet on.
3. Select odds "1" and enter a valid stake "2" amount.
4. Validate Potential Payout calculation and ensure that it is accurate based on the selected odds and stake amount.
4. Click on the "Place Bet" button 
5. Verify that the success receipt is displayed and contains the correct match, selection, stake, odds, potential payout and bet ID.
6. Check the user's balance to ensure that it has been updated correctly after the bet placement.
Expected Result: The bet is successfully placed, and the user's balance is updated correctly to reflect the bet amount.

TS2 - Successfully place a bet with the maximum allowed stake (€100.00)
Priority: High

Risk Rationale: Validating the bet placement with different stake values ensures that the platform can handle various betting scenarios and that users can place bets with different amounts without encountering issues. This helps to ensure that the platform is flexible and user-friendly, allowing users to customize their betting experience according to their preferences.
Steps:
1. Log in to the platform with valid credentials.
2. Navigate to the betting section and select an upcoming match to place a bet on.
3. Select odds "X" and enter different valid stake amounts "100"
4. Validate Potential Payout calculation and ensure that it is accurate based on the selected odds and stake amount.
4. Click on the "Place Bet" button
5. Verify that the bet is successfully placed and a confirmation message is displayed.
6. Check the user's balance to ensure that it has been updated correctly after the bet placement.
Expected Result: The bet is successfully placed, and the user's balance is updated correctly to reflect the bet amount for each stake value tested.

TS3 - Prevent bet placement when stake exceeds available balance
Priority: Critical

Risk Rationale: Preventing bet placement when the stake exceeds the available balance is crucial to avoid financial losses for users and maintain the integrity of the betting process. Validating this functionality ensures that users cannot place bets that they cannot afford, which helps to protect their financial interests and maintain trust in the platform. ID 4
Precondition:
Available balance is below €100.00
Steps:
1. Log in to the platform with valid credentials.
2. Navigate to the betting section and select an upcoming match to place a bet on.
3. Select odds "X" and enter a stake amount that exceeds the user's available balance.
4. Click on the "Place Bet" button
5. Verify that the bet placement is prevented, and an appropriate error message is displayed indicating that the stake exceeds the available balance.
6. Check the user's balance to ensure that it remains unchanged after the attempted bet placement.
Expected Result: The bet placement is prevented, and an appropriate error message is displayed indicating that the stake exceeds the available balance. The user's balance remains unchanged after the attempted bet placement

TS4 - Validate invalid stake values and error messages
Priority: Medium

Risk Rationale: Validating invalid stake values and error messages ensures that the platform can handle user input errors gracefully and provide clear feedback to users. This helps to prevent confusion and frustration, allowing users to correct their input and successfully place bets. Ensuring that the platform can handle invalid stake values also helps to maintain the integrity of the betting process and protect users from potential financial losses due to incorrect input           
Steps:
1. Log in to the platform with valid credentials.
2. Navigate to the betting section and select an upcoming match to place a bet on.
3. Select odds "2" and enter invalid stake values such as less than 1 and more than 100, 0, non-numeric values, 3 decimal places, negative values and special characters:
test data: -1, 0, 100.01, 10.001, abc, !@#
Note: Minimum boundary is excluded from deterministic validation because the specification is inconsistent regarding €1.00 vs €1.01.
Expected Result: The platform should prevent bet placement for invalid stake values and display appropriate error messages indicating the nature of the input error. The user's balance should remain unchanged after the attempted bet placement.

TS5 - Selecting another odds option replaces previous selection
Priority: Medium

Risk Rationale: Ensuring that selecting another odds option replaces the previous selection is important for maintaining a clear and intuitive user experience. Validating this functionality ensures that users can easily change their bet selections without confusion or errors, allowing them to make informed decisions about their bets. This helps to enhance the overall usability of the platform and improve user satisfaction.
Steps:
1. Log in to the platform with valid credentials.
2. Navigate to the betting section and select an upcoming match to place a bet on.
3. Select odds "1" and enter a valid stake amount.
4. Verify that HOME selection appears in the Bet Slip.
5. Select a different odds option "2" for the same match. 
6. Verify that the previous odds selection is replaced with the new selection - AWAY, and the potential payout is updated accordingly based on the new odds and stake amount.
7. Enter a valid stake amount for the new odds selection.
8. Click on the "Place Bet" button
9. Verify that the bet is successfully placed with the new odds selection and that a confirmation message is displayed.
10. Check the user's balance to ensure that it has been updated correctly after the bet placement with the new odds selection.
Expected Result: The previous odds selection is replaced with the new selection, and the potential payout is updated accordingly. The bet is successfully placed with the new odds selection, and the user's balance is updated correctly to reflect the bet amount for the new odds selection.      
