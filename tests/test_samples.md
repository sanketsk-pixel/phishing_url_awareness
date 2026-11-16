# Test Results

**Project Name:** Phishing URL Awareness Checker  
**Programming Language:** Python  
**Python Version:** 3.13  
**Operating System:** Windows 10  
**Testing Type:** Manual Testing  

## 1. Test Cases

| No. | Sample URL | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | `http://192.0.2.10/account` | IP address and HTTP warning | IP address warning and HTTP warning displayed. | PASS |
| 3 | `http://example.com@sample.invalid/login` | @ symbol and HTTP warning | @ symbol warning and HTTP warning displayed. | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments warning | Many dot-separated hostname segments warning displayed. | PASS |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname warning | Punycode-style hostname warning displayed. | PASS |

## 2. Test Summary

- Total Test Cases: 5
- Passed: 5
- Failed: 0
- Testing Status: Completed

## 3. Testing Notes

- All five sample URLs were tested successfully.
- The program checks URL text only.
- No websites were opened or scanned.
- The program displays warning messages based on URL patterns.
- No warning signs found does not guarantee that a URL is safe.

## 4. Conclusion

The Phishing URL Awareness Checker successfully completed all five sample test cases. It identifies selected URL warning signs and displays appropriate messages to help users review suspicious links carefully.

The tool is intended for educational awareness purposes and does not guarantee URL safety.