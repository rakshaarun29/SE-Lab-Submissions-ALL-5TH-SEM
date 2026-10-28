# Lab 5: Static Code Analysis

## Project
**Program:** `tax_calculator.py`

This lab uses Pylint, Bandit, and Flake8 to identify and address code quality, security, and formatting issues in a Python tax calculator.

## Tools Used
- **Pylint:** Checks code quality and maintainability.
- **Bandit:** Identifies common security weaknesses.
- **Flake8:** Checks Python style and formatting.

## Changes Made
- Replaced AES-ECB encryption with AES-GCM encryption using a random nonce.
- Increased the RSA key size to 2048 bits.
- Replaced standard XML parsing with `defusedxml`.
- Removed the unused CGI handler.
- Improved PAN input validation.
- Improved function naming, code structure, and formatting.
- Corrected the tax-regime selection to choose the lower calculated tax.

## Reports
- `pylint_before.txt`
- `pylint_after.txt`
- `bandit_before.txt`
- `bandit_after.txt`
- `flake8_before.txt`
- `flake8_after.txt`

## Other Deliverables
- `issues.md` — Summary of identified issues and fixes.
- `reflection.md` — Reflection on the static analysis exercise.

## Running the Program
Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python tax_calculator.py
```

## Note
The tax calculations are for educational purposes only and should not be treated as tax advice. The hard-coded encryption key is a lab limitation and must be replaced with secure key management before production use.   