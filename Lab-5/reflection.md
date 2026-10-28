# Lab 5: Static Code Analysis — Reflection

## 1. What did I learn about static code analysis?

I learned that static code analysis examines source code to identify potential problems without requiring the program to execute. Pylint focuses on code quality and maintainability, Flake8 checks formatting and PEP 8 compliance, and Bandit detects common security weaknesses.

## 2. Which issues were the most important to fix?

The security findings were the highest priority. I replaced AES ECB encryption with AES-GCM, increased the RSA key size from 1024 to 2048 bits, switched to defusedxml for XML parsing, and removed the unsafe CGI handler. I also improved PAN validation and corrected the regime-selection comparison so that it selects the lower calculated tax.

## 3. How did the three tools complement one another?

Bandit identified security risks that could be overlooked by ordinary execution tests. Pylint identified naming and code-structure problems, while Flake8 identified formatting violations. Using all three provided broader coverage than relying on only one tool.

## 4. What did I learn about verification and maintainability?

I learned that fixing warnings is not enough; the program must also be tested after changes. The final program executed successfully, Pylint reported 10.00/10, Bandit reported no issues, and Flake8 produced an empty report. These results improve confidence in the code, although they do not prove that the program is free of every defect or security risk. The hard-coded encryption key still needs secure key management before this code could be used in production.
