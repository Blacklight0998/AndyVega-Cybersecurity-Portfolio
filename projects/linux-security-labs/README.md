# Linux Security Administration & Monitoring Lab

This section groups several Linux activities that originally came from different university exercises.

I decided to keep them under one larger project because they follow a natural progression: first setting up and administering Linux systems, then working with users and privileges, and finally reviewing logs and system activity when something looks wrong.

The activities were not all completed as one continuous lab, so I keep that distinction clear. The screenshots and findings still come from the original work.

## Project flow

```text
Linux setup
   ↓
Administration
   ↓
Users and privileges
   ↓
Monitoring
   ↓
Logs and troubleshooting
   ↓
Security audit
```

## 1. Infrastructure, Administration & Monitoring

[View this section](./linux-infrastructure-monitoring/)

This part covers the Linux environment itself and the day-to-day administration work I practiced.

Main topics:

- three Ubuntu virtual machines
- static IPv4 configuration with Netplan
- connectivity testing
- Linux CLI and file management
- users and groups
- process and memory monitoring
- `ip a` and `ss -tunlp`
- cron-based monitoring

The original academic project also included a proposed Netdata → Prometheus → Grafana monitoring design. I kept it in the portfolio as a proposal, not as something I deployed.

## 2. Identity & Access Management

[View this section](./linux-user-access-management/)

Here the focus was on who has access to the system and how privileges are managed.

I practiced:

- creating and removing users
- reviewing `/etc/passwd` and `/etc/group`
- groups and membership
- `su` and `sudo`
- active-session review with `who` and `w`
- password aging with `chage`
- cleaning up temporary accounts

## 3. System Diagnosis & Log Analysis

[View this section](./linux-system-diagnosis/)

This part was closer to the kind of troubleshooting and basic investigation I want to get better at for Blue Team work.

I reviewed:

- `auth.log`
- `kern.log`
- `dmesg`
- failed authentication attempts
- running processes with `ps`
- CPU/process activity with `top`
- memory usage with `free`

One useful lesson from this activity was not to assume that every warning or failed login explains the problem. I had to compare the logs with process and resource evidence before writing a conclusion.

## 4. Linux Log Audit & Security Review

[View this section](./linux-log-audit-security-review/)

This case used a simulated server with suspicious SSH activity, backup failures and insecure file permissions.

I used command-line tools to extract failed login attempts, count activity by source IP, identify invalid usernames, review `sudo` activity and separate backup warnings and errors.

The part I found most useful was turning the raw log entries into a short set of findings and mitigations instead of stopping at the command output.

## Why this matters to me

Linux is one of the areas I want to be comfortable with before applying for SOC/Blue Team roles. These exercises are still basic, but they gave me hands-on practice with accounts, permissions, logs, processes, services and troubleshooting instead of only reading about them.
