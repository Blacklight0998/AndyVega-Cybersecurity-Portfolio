# Python Security & Automation Labs

This section groups the Python work that is most relevant to cybersecurity.

Most of these started as separate learning exercises. I keep them together because they show how I have been applying Python to networking, cryptography, authentication and web analysis without pretending they were all built as one application.

## 1. Python Network Reconnaissance Tool

[View project](./python-network-reconnaissance-tool/)

This is the most complete Python project in the portfolio right now.

It grew from two earlier exercises: a DNS enumeration script and a Scapy TCP SYN scanner. Since both are part of the same discovery process, I combined them into one workflow and added JSON reporting.

```text
Target domain
    |
    v
DNS enumeration
    |
    v
Resolved IP addresses
    |
    v
TCP port scanning
    |
    v
JSON report
```

What I am practicing here:

- Python structure and functions
- DNS resolution
- TCP/IP and TCP flags
- Scapy
- dnspython
- wordlist-based enumeration
- error handling
- JSON output

## 2. AES-EAX Cryptography Lab

[View lab](./cryptography-lab/)

This stays separate because it has a different purpose. The two exercises in this folder were made to understand AES-EAX, nonces, authentication tags and integrity verification.

I do not consider it a full cryptography project; it is a small learning lab that I kept because it shows another way I have used Python in security-related coursework.

## 3. Web Security & Scraping Exercise

[View exercise](./web-security-scraping-exercise/)

This university exercise combines login validation, random password generation, password hashing, regex and web scraping in one command-line program.

For the portfolio version I kept the code close to the original work and changed only the password encryption section to demonstrate hashing instead.

> Network testing in this repository is intended only for systems I own or have explicit permission to test.
