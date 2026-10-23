# Python Security Tools

Python work with a security purpose.

## Python Network Reconnaissance Tool

[View project](./network-recon-tool/)

The most complete Python project in the portfolio. It grew from two earlier exercises, a DNS enumeration script and a Scapy TCP SYN scanner, which I combined into one workflow.

```text
Target domain → DNS enumeration → resolved IPs → TCP SYN scan → JSON report
```

It is a learning project, not a replacement for tools such as Nmap.

## Next ideas

These are not built yet:

- a script that reads `auth.log`, counts failed SSH logins per source IP and flags brute-force patterns (the automated version of my [log audit case](../soc-lab/linux-log-audit-case/))
- a simple detector for SYN scans like the one this tool produces
- scope checks and input validation in the recon tool

> Network testing in this repository is intended only for systems I own or have explicit permission to test.

Smaller Python exercises (AES-EAX and a scraping program) are in the [coursework archive](../../coursework-archive/).
