import json
from datetime import datetime
from pathlib import Path


def save_report(domain, dns_server, dns_results, scan_results):
    reports_dir = Path(__file__).parent.parent / "reports"
    reports_dir.mkdir(exist_ok=True)

    report = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "target_domain": domain,
        "dns_server": dns_server,
        "dns_results": dns_results,
        "tcp_scan": scan_results,
    }

    safe_domain = domain.replace("/", "_").replace("\\", "_")
    output = reports_dir / f"{safe_domain}_report.json"

    with output.open("w", encoding="utf-8") as report_file:
        json.dump(report, report_file, indent=2)

    return output
