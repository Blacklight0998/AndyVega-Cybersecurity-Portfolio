from pathlib import Path

import dns.resolver


def enumerate_subdomains(domain, wordlist, dns_server):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]

    results = []

    with Path(wordlist).open("r", encoding="utf-8") as wordlist_file:
        for line in wordlist_file:
            subdomain = line.strip()
            if not subdomain:
                continue

            target = f"{subdomain}.{domain}"

            try:
                answers = resolver.resolve(target, "A")
                addresses = [answer.address for answer in answers]
                results.append({"hostname": target, "addresses": addresses})
                print(f"[DNS] {target}: {', '.join(addresses)}")
            except (
                dns.resolver.NXDOMAIN,
                dns.resolver.NoAnswer,
                dns.resolver.NoNameservers,
                dns.resolver.LifetimeTimeout,
            ):
                print(f"[DNS] {target}: not found")

    return results
