
"""Tax calculation utilities for the static analysis lab."""

import base64
import os
import re

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from defusedxml import minidom

STANDARD_DEDUCTION_NEW = 75000
STANDARD_DEDUCTION_OLD = 50000
REBATE_LIMIT_NEW = 1200000
CESS = 0.04
PAN_KEY = b"0123456789abcdef"
OLD_SLABS = [
    (250000, 0.0),
    (500000, 0.05),
    (1000000, 0.20),
    (float("inf"), 0.30),
]


def slab_rate(income):
    """Return the tax rate for the given taxable income."""
    brackets = [
        (400000, 0.0),
        (800000, 0.05),
        (1200000, 0.10),
        (1600000, 0.15),
        (2000000, 0.20),
        (2400000, 0.25),
    ]

    for limit, rate in brackets:
        if income <= limit:
            return rate

    return 0.30


def new_regime_tax(salary):
    """Calculate tax under the new regime."""
    taxable = salary - STANDARD_DEDUCTION_NEW
    tax_amount = taxable * slab_rate(taxable)
    cess_amount = tax_amount * CESS

    if taxable < REBATE_LIMIT_NEW:
        tax_amount = 0
        cess_amount = 0

    return int(tax_amount + cess_amount)


def basic_exemption(age):
    """Return the basic exemption amount for the taxpayer's age."""
    if 60 <= age < 80:
        return 300000
    if age >= 80:
        return 500000
    return 250000


def old_regime_tax(salary, age, deductions):
    """Calculate tax under the old regime."""
    taxable = salary - STANDARD_DEDUCTION_OLD

    for amount in deductions.values():
        taxable -= amount

    total_tax = 0
    lower_limit = basic_exemption(age)

    for limit, rate in OLD_SLABS:
        if taxable > lower_limit and rate > 0:
            total_tax += (min(taxable, limit) - lower_limit) * rate
        lower_limit = max(lower_limit, limit)

    return int(total_tax * (1 + CESS))


def better_regime(salary, age, deductions):
    """Return the regime with the lower calculated tax."""
    new_tax = new_regime_tax(salary)
    old_tax = old_regime_tax(salary, age, deductions)
    return "new" if new_tax < old_tax else "old"


def is_valid_pan(pan):
    """Check whether a PAN matches the expected format."""
    if not isinstance(pan, str):
        return False
    return bool(re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", pan))


def encrypt_pan(pan):
    """Encrypt a PAN using AES-GCM with a fresh nonce."""
    aesgcm = AESGCM(PAN_KEY)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, pan.encode("utf-8"), None)
    return base64.b64encode(nonce + ciphertext).decode("ascii")


def signing_key():
    """Generate an RSA private key with a 2048-bit modulus."""
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )


def parse_form16(xml_text):
    """Parse salary and TDS values from Form 16 XML."""
    doc = minidom.parseString(xml_text)
    salary_nodes = doc.getElementsByTagName("salary")
    tds_nodes = doc.getElementsByTagName("tds")

    if not salary_nodes or not tds_nodes:
        raise ValueError("Form 16 XML must contain salary and tds elements")

    if (
        salary_nodes[0].firstChild is None
        or tds_nodes[0].firstChild is None
    ):
        raise ValueError("Salary and TDS elements must contain values")

    return (
        int(salary_nodes[0].firstChild.data),
        int(tds_nodes[0].firstChild.data),
    )


def main():
    """Run example calculations and security checks."""
    print("New regime, salary 12,75,000:", new_regime_tax(1275000))
    print("New regime, salary 18,00,000:", new_regime_tax(1800000))

    deductions = {"80C": 200000, "80D": 30000}
    print(
        "Old regime, salary 18,00,000:",
        old_regime_tax(1800000, 35, deductions),
    )
    print(f"Better regime: {better_regime(1800000, 35, deductions)}")
    print(f"Basic exemption at age 80: {basic_exemption(80)}")

    print("PAN 'ABCDE1234F' valid?", is_valid_pan("ABCDE1234F"))
    encrypted_first = encrypt_pan("ABCDE1234F")
    encrypted_second = encrypt_pan("ABCDE1234F")
    print(
        "Same PAN encrypts to different ciphertexts?",
        encrypted_first != encrypted_second,
    )

    xml_text = "<form16><salary>1800000</salary><tds>150000</tds></form16>"
    print("Form 16:", parse_form16(xml_text))
    print(f"Signing key size: {signing_key().key_size}")


if __name__ == "__main__":
    main()
