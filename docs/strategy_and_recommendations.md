Strategy and Recommendations

1. Automation Strategy

I selected two high-value tests for automation: one end-to-end UI test covering the critical bet placement journey and one API test covering a core business validation rule.

E2E UI: Successful single bet placement

This scenario represents the main user journey of the feature: selecting an outcome, entering a valid stake, placing the bet, receiving a success receipt, and verifying that the balance is updated.

I selected this scenario because it validates the integration between the main UI components and the backend through the most business-critical flow. It also provides good regression value because a failure in this journey would directly prevent a user from placing a bet.

API: Maximum stake validation

The API test validates that a stake above the allowed maximum of €100.00 is rejected.

I selected this scenario because the maximum stake is an explicit business rule and can be validated more efficiently and reliably at the API layer than through the UI. Testing it directly through the API also provides faster feedback and isolates backend validation from browser-specific behavior.

2. Scenarios Intentionally Left Manual

The following areas were intentionally kept manual for this scoped assignment:

Minimum stake boundary — the specification contains conflicting requirements for the minimum allowed stake, so the expected result is not unambiguous enough to use as a stable automated assertion.

Error modal and retry behavior — useful to verify manually during exploratory testing because the failure state may require controlled backend conditions or mocking to reproduce reliably.

Date and odds filters — important functionality, but lower priority than the core bet placement flow for a two-test automation scope.

Selection replacement behavior — straightforward to verify manually and lower business risk than successful placement and server-side validation.

Repeated bets on the same match/selection — the specification does not explicitly define whether a user may place another bet on the same match and the same outcome after a previous bet has completed. This should be clarified before stable automated coverage is added.

3. Recommendations

3.1 Clarify and align business requirements

Before expanding automated coverage, I would recommend resolving several ambiguities in the specification.

Minimum stake inconsistency

The minimum stake is defined differently in different sections:

Business Rules: €1.00

Stake Validation: €1.01

Expected UI validation message: “Minimum stake is €1.00”

This creates ambiguity for both implementation and testing. The minimum accepted value should be defined once and used consistently across UI validation, API validation, documentation, and automated tests.

Repeated bets on the same match and selection

The specification states that only one active selection can exist in the bet slip at a time and that a new selection replaces the current one. However, it does not define the expected behavior after a bet has already completed.

The following business rules should be clarified:

Can a user place multiple sequential bets on the same match?

Can the same outcome (HOME, DRAW, or AWAY) be selected again after a successful bet?

Are there any limits on repeated bets for the same event?

If repeated bets are restricted, what response and user-facing message should be expected?

Clarifying these rules would prevent inconsistent UI/API behavior and allow deterministic test coverage.

3.2 Add CI/CD and layered automated coverage

If the project scaled, I would run the automated suite in CI on every pull request and on the main branch.

The test suite should remain layered:

API tests for business rules, validation, authentication, and error responses

a smaller set of UI E2E tests for critical user journeys

targeted component/integration tests where appropriate

This would provide faster feedback while keeping the more expensive browser-based suite focused.
