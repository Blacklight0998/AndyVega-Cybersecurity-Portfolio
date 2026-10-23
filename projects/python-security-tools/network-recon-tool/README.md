# Python Network Reconnaissance Tool

This is a Python learning project for basic reconnaissance in authorized lab environments.

It started from two small exercises I had already built: one for DNS subdomain enumeration and another for TCP SYN scanning with Scapy. Keeping them as separate scripts worked for practice, but combining them into one workflow made more sense and gave me a better reason to organize the code.

## Current workflow

```text
Target domain
    |
    v
DNS enumeration
    |
    v
Resolved hosts / IP addresses
    |
    v
TCP port scan
    |
    v
JSON report
```

## What the program does

1. Reads possible subdomains from a wordlist.
2. Queries their DNS `A` records through a configurable DNS resolver.
3. Collects the IP addresses it finds.
4. Runs a SYN scan against a small list of common ports on those discovered hosts.
5. Saves the results to a JSON report.

The default port list is intentionally small because this is a learning project, not an attempt to build a replacement for tools such as Nmap.

## Project structure

```text
network-recon-tool/
├── main.py
├── modules/
│   ├── dns_enum.py
│   ├── port_scan.py
│   └── reporting.py
├── data/
│   └── subdomains.txt
├── reports/
└── requirements.txt
```

`main.py` controls the flow, while the DNS, scanning and reporting functions are kept in separate modules. This was one of the main changes from the original standalone scripts.

## What I practiced

- Python functions and modules
- DNS resolution and `A` records
- Reading a wordlist from a file
- TCP SYN scanning
- TCP flags and basic response interpretation
- Scapy
- Error handling
- JSON reporting

## Where it came from

The DNS part came from a university exercise where the first version was not returning useful results. I changed the resolver, expanded the wordlist and added clearer error output while troubleshooting it.

The scanner came from a separate Scapy exercise that originally scanned localhost. I reused the same basic SYN-scan logic as one stage of this project.

## Limitations / next improvements

Right now the tool is intentionally basic. Some improvements I would like to work on later are better input validation, configurable port lists, cleaner summaries and more useful reporting.

This is a learning project and should only be used against systems I own or have explicit permission to test.
