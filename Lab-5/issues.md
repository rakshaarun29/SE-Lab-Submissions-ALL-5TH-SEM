# Lab 5: Static Code Analysis — Issues and Fixes

## Issues Identified and Resolved

| Issue | Category | Original Line(s) | Description | Fix Applied |
|---|---|---:|---|---|
| Unsafe CGI handler (B412) | Security — High | 6, 92 | The CGI handler introduced a potential security concern. | Removed the unused CGI handler and its function. |
| AES ECB mode (B305) | Security — Medium | 77 | ECB mode does not adequately protect repeated plaintext patterns. | Replaced ECB encryption with AES-GCM and a fresh random nonce for each encryption. |
| Weak RSA key size (B505) | Security — Medium | 83 | The original RSA key size was 1024 bits. | Increased the RSA key size to 2048 bits. |
| Unsafe XML parsing (B408, B318) | Security | 5, 86 | Standard XML parsing may expose applications to XML-related attacks. | Switched to `defusedxml` and added checks for required elements and values. |
| Invalid PAN validation | Input validation | 68 | The original pattern could accept a valid-looking prefix followed by extra characters. | Used `re.fullmatch()` and checked that the input is a string. |
| Non-standard function names (C0103) | Code quality | Multiple | CamelCase function names did not follow Python naming conventions. | Renamed functions to snake_case and updated their call sites. |
| Excessive return statements (R0911) | Code quality | 25 | The original slab-rate function used too many return statements. | Used a list of brackets and a loop to select the applicable rate. |
| Unused variables and imports | Code quality and style | Multiple | Unused variables and imports made the code harder to maintain. | Removed unused variables and imports. |
| Formatting violations | Style | Multiple | The original code had long lines and inconsistent formatting. | Reformatted the code to satisfy Flake8. |

## Verification

The final reports are saved in the following files:

- `pylint_after.txt`
- `bandit_after.txt`
- `flake8_after.txt`

The recorded results are a Pylint score of 10.00/10, no Bandit findings, and an empty Flake8 report.

**Note:** The line numbers above refer to the original program. Confirm them against your original analysis reports before submission.