import re
from urllib.parse import urlparse


def inspect_url(url):
    findings = []

    if not url.strip():
        return ["No URL entered."]

    try:
        parsed = urlparse(url.strip())

        if not parsed.scheme or not parsed.hostname:
            return ["Could not identify a valid URL hostname."]

        hostname = parsed.hostname.lower()

    except ValueError:
        return ["Could not identify a valid URL hostname."]

    # Check 1: IP address in hostname
    ip_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    if re.match(ip_pattern, hostname):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    # Check 2: @ symbol
    if "@" in url:
        findings.append(
            "Contains an @ symbol, which can hide the actual destination."
        )

    # Check 3: HTTP instead of HTTPS
    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    # Check 4: Many hostname segments
    if len(hostname.split(".")) >= 5:
        findings.append(
            "Hostname contains many dot-separated segments."
        )

    # Check 5: Punycode-style hostname
    if "xn--" in hostname:
        findings.append(
            "Contains a punycode-style hostname."
        )

    # Check 6: Suspicious words in URL
    suspicious_words = [
        "verify",
        "password",
        "banking",
        "wallet",
        "confirm"
    ]

    if any(word in url.lower() for word in suspicious_words):
        findings.append(
            "Contains words commonly used in misleading links."
        )

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def main():
    print("=" * 45)
    print("       PHISHING URL AWARENESS CHECKER")
    print("=" * 45)
    print("Text checks only - this program does not open URLs.")

    while True:
        url = input("\nEnter a sample URL (or type exit): ").strip()

        if url.lower() in ("q", "quit", "exit"):
            print("\nThank you for using the checker!")
            break

        findings = inspect_url(url)

        print("\nRESULT:")
        for finding in findings:
            print("-", finding)

        if findings and not findings[0].startswith(
            ("No URL entered", "Could not identify",
             "No listed warning signs")
        ):
            print("\nReview carefully before trusting this link.")


if __name__ == "__main__":
    main()