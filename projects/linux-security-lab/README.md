# Linux Security Lab

This project groups three Linux activities from university courses. They follow a natural progression: set up and administer Linux systems, manage users and privileges, and then investigate a system when something looks wrong.

The activities were not completed as one continuous lab, and I keep that distinction clear. The screenshots and findings come from the original work.

## Project flow

```text
Phase 1: Setup, administration and monitoring
        ↓
Phase 2: Users, groups and privileges
        ↓
Phase 3: System diagnosis and log analysis
```

## Phase 1: Infrastructure, Administration & Monitoring

[View phase 1](./01-infrastructure-and-monitoring/)

- three Ubuntu virtual machines with static IPv4 addresses (Netplan)
- Linux CLI, file management, pipes, `grep`, regular expressions and `find`
- process and memory monitoring
- listening-port inspection with `ss -tunlp`
- an hourly `cron` monitoring script

The original project also proposed a Netdata → Prometheus → Grafana design. It is documented as a proposal, not as something I deployed.

## Phase 2: Identity & Access Management

[View phase 2](./02-user-access-management/)

- creating and removing users and groups
- `su`, `sudo` and active-session review
- password aging with `chage`
- cleaning up temporary accounts

## Phase 3: System Diagnosis & Log Analysis

[View phase 3](./03-system-diagnosis/)

- `auth.log`, `kern.log` and `dmesg`
- processes, CPU and memory
- separating a suspicious-looking log entry from a confirmed cause

## Related

The log-analysis case with simulated SSH attacks is in the [SOC Lab](../soc-lab/linux-log-audit-case/), because it is closer to alert investigation than to system administration.

## Next step

Add a hardening phase on one of the VMs: run an audit tool such as Lynis, apply SSH, firewall and account hardening, and document the before and after. This is not done yet.
