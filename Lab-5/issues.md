# Lab 5: Static Code Analysis — Issues and Fixes

| Issue | Type | Original line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Unsafe CGI handler (B412) | Security — High | 6, 92 | CGIHandler has security implications. | Removed the unused CGI handler and its function. |
| AES ECB mode (B305) | Security — Medium | 77 | ECB does not provide semantic security for repeated plaintext blocks. | Replaced ECB encryption with AES-GCM using a fresh random nonce for each encryption. |
| Weak RSA key size (B505) | Security — Medium | 83 | The original RSA key size was 1024 bits. | Increased the RSA key size to 2048 bits. |
| Unsafe XML parsing (B408, B318) | Security — Low/Medium | 5, 86 | Standard minidom parsing can expose applications to XML attacks. | Replaced it with defusedxml and added checks for required elements and values. |
| Invalid PAN validation | Input validation | 68 | The original regular expression could accept a valid-looking prefix followed by extra characters. | Used `re.fullmatch` and checked that the input is a string. |
| Non-standard function names (C0103) | Code quality | Multiple | CamelCase names did not follow Python naming conventions. | Renamed functions to snake_case and updated their call sites. |
| Excessive return statements (R0911) | Code quality | 25 | The original slab-rate function used too many return statements. | Used a bracket list and loop to select the applicable rate. |
| Unused variables and imports | Code quality/style | Multiple | Unused variables and imports added unnecessary clutter. | Removed unused variables and imports. |
| Formatting violations | Style | Multiple | The original code had long lines and inconsistent formatting. | Reformatted the code to satisfy Flake8. |
