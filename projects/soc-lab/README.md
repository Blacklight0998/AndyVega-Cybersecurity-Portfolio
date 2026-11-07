# SOC Lab & Incident Analysis

This section collects the work that is closest to what a SOC analyst does: reading logs, separating normal from suspicious activity, and writing down findings and next steps.

## 1. Linux Log Audit & Security Review

[View case](./linux-log-audit-case/)

A university case with a simulated Linux server: repeated failed SSH logins from one source, a user reading `/etc/shadow` with `sudo` in the early morning, backup failures and files with `777` permissions. I extracted the evidence from `auth.log` and the backup log with command-line tools and wrote findings with mitigations.

This is simulated data, not a production incident.

## 2. Enterprise SOC Lab

[View repository](https://github.com/Blacklight0998/Blacklight-Enterprise-Lab)

A long-term homelab in VirtualBox (Windows and Linux) that I am building to practice monitoring and incident investigation. It is an early build. What exists today:

- a SOC alert triage template (v1.0) with sections for evidence, indicators, disposition, ATT&CK mapping and escalation
- an Azure Sentinel SIEM pipeline (Azure Monitor Agent → Log Analytics → Sentinel) with KQL-based detections
- two closed cases: [`BL-ALT-2026-001`](https://github.com/Blacklight0998/Blacklight-Enterprise-Lab/blob/main/incident-response/cases/BL-ALT-2026-001/triage.md) (four failed Windows logons from an incorrect PIN, investigated with the Security log) and [`BL-ALT-2026-002`](https://github.com/Blacklight0998/Blacklight-Enterprise-Lab/blob/main/incident-response/cases/BL-ALT-2026-002/triage.md) (a simulated RDP brute-force attack, detected end-to-end by a custom Sentinel Analytics Rule)

## Next steps

- rewrite the SSH log audit as a triage report using the lab template
- a third case testing a valid account with a wrong password, to compare against case 002's non-existent-account scenario
- document more cases with evidence, disposition and ATT&CK mapping only where the evidence supports it
