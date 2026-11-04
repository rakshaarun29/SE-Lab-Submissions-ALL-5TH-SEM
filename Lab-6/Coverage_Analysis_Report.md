# Lab 6: Code and Branch Coverage Analysis

## Objective

The objective of this lab was to measure code coverage and branch coverage for the self-storage application, then write tests for its key decision paths and edge cases.

## Application Under Test

`self_storage.py` contains three functions:

- `rent_due` calculates rent based on unit size, months, climate control, and membership.
- `access_allowed` decides whether an owner or visitor can access a storage unit.
- `payment_status` returns the payment state based on the due date, autopay, and prior late payments.

## Test Approach

Two separate test files were used:

- `CodeCoverageTest_51_application.py` measures execution of the application’s statements.
- `BranchCoverageTest_51_application.py` exercises the true and false outcomes of its decisions.

The tests cover valid and invalid rent inputs, membership and climate pricing, rent discounts, owner and visitor access, and the current, grace, and lien payment states.

## Results

| Coverage Run | Tests Passed | Application Coverage |
|---|---:|---:|
| Code coverage | 6 | 100% |
| Branch coverage | 7 | 100% |

The code coverage report showed that all 37 statements in `self_storage.py` were executed, with no missed statements.

The branch coverage report showed that all 26 branches in `self_storage.py` were covered, with no partial branches. The terminal reports are saved as `CodeCoverage_Results.png` and `BranchCoverage_Results.png`.

## Analysis

The code coverage result indicates that the tests executed every statement in the application. The branch coverage result goes further: it indicates that both outcomes of each reported decision were exercised during the branch test run.

For example, the tests cover rent validation and pricing decisions, allowed and denied access paths, and all three payment status outcomes. The separate reports distinguish statement execution from decision-path testing.

## Conclusion

The tests achieved 100% code coverage and 100% branch coverage for the tested version of `self_storage.py`. These results show that the application’s statements and reported decision branches were exercised by the test suites. Coverage measures execution; it does not by itself prove that every possible input or behavior is correct.