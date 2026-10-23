# Phase 1: Linux Infrastructure, Administration & Monitoring

This is the first part of the [Linux Security Lab](../).

For this university activity we worked with three Linux virtual machines on the same network. I used it to practice the basic administration work I need before doing anything more security-focused.

## Lab setup

- installed and cloned three Ubuntu VMs on the same network
- configured a static IPv4 address on each one with Netplan
- validated the configuration and tested connectivity between machines with `ping`
- troubleshot basic Linux network configuration

## Administration practice

- **Files and directories:** `cp`, `mv`, `rm`, `rmdir`, `mkdir`, `tar`, `less`, `head`, `tail`
- **Shell:** adding a directory to `PATH`, aliases, redirection (`>`, `>>`), pipes
- **Text processing and search:** `grep`, basic and extended regular expressions, `find`, `xargs`
- **Users and groups:** creating users and groups, changing membership, reviewing existing users and active sessions

## Monitoring

- `dmesg` for recent kernel messages
- `ps aux`, `top` and `free -h` for processes, CPU and memory
- `ip a`, `ping` and `ss -tunlp` to inspect interfaces, connectivity, and listening ports and services
- a `cron` job that runs every hour and writes CPU, memory and disk usage to a log file, which turned manual checks into a repeatable task

## Proposal, not deployed: Netdata, Prometheus and Grafana

The academic project also included a monitoring design. I did not deploy it, so I document it as a proposal and not as completed work.

```text
Server 1: Netdata + Prometheus + Grafana
Server 2: Netdata
Server 3: Netdata

Netdata agents → Prometheus (15 s scrape) → Grafana dashboards
```

Proposed alert thresholds:

| Resource | Threshold | Duration |
|---|---:|---:|
| CPU | > 80% | 5 min |
| Memory | > 85% | 5 min |
| Disk | > 90% | 10 min |
| Availability | `up = 0` | 2 min |

The design also noted that monitoring interfaces (Netdata listens on TCP `19999`) should not be exposed to the Internet unnecessarily.

A future upgrade would be to deploy this in the three-VM lab, build dashboards and trigger a controlled alert.

## What I learned

Commands for users, processes, networking and logs make more sense once I have used them to manage a system instead of memorizing them for an exam.

Screenshots for this phase are not included in the portfolio yet.
