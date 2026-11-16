# Phishing URL Awareness Checker

## 1. Project Overview

The Phishing URL Awareness Checker is a beginner-friendly Python project designed to identify selected warning signs in URL text.

It helps users understand common characteristics that may appear in suspicious URLs.

## 2. Objectives

- Learn basic Python programming.
- Understand common URL warning signs.
- Identify selected URL patterns using Python.
- Promote phishing awareness.

## 3. Features

The program checks for six warning signs:

1. Presence of the `@` symbol.
2. URL length greater than 100 characters.
3. IP address instead of a domain name.
4. Five or more hostname segments.
5. Punycode-style hostname containing `xn--`.
6. Use of HTTP scheme.

## 4. Additional Improvements

- Multiple URL checking using a loop.
- Type `exit` to stop the program.
- Clear result summary when warning signs are detected.
- Empty input handling.

## 5. Technologies Used

- Python 3.13
- Regular Expressions (`re`)
- URL Parsing (`urllib.parse`)
- Visual Studio Code

## 6. Project Structure

```text
phishing_url_awareness/
├── phishing_checker.py
├── README.md
├── requirements.txt
├── tests/
│   └── test_samples.md
└── screenshots/
    ├── sample_run.png
    └── test_results.png
```

## 7. Installation and Execution

### Requirements
- Python 3.13 or compatible version.
- Visual Studio Code.

### Run the Project

Open the project folder in VS Code Terminal and execute:

```bash
python phishing_checker.py
```

Enter a sample URL when prompted.

To stop the program, type:

```text
exit
```

## 8. How It Works

The program accepts a URL as text and uses Python built-in libraries to inspect its structure.

It checks the URL against six predefined warning signs and displays the findings in the terminal.

Users can check multiple sample URLs without restarting the program.

## 9. Testing

Five sample test cases will be documented in `tests/test_samples.md`.

Actual results will be recorded after testing the program.

## 10. Limitations

- The program does not open or visit websites.
- It does not send network requests.
- It does not scan websites.
- It cannot confirm whether a URL is safe or malicious.
- It only checks selected text-based warning signs.

## 11. Ethical Use

This project is developed for educational and cybersecurity awareness purposes.

Only use the sample URLs provided for this project.

Never enter passwords or confidential information on unexpected websites.

## 12. Future Improvements

- Add more URL pattern checks.
- Improve terminal output formatting.
- Add more beginner-friendly explanations.

## 13. Disclaimer

A URL with no detected warning signs is not necessarily safe. Always verify unexpected links through trusted sources.