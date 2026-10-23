# Home Network Security & Traffic Analysis

This project came from a university group assignment where we analyzed a real residential network. For the portfolio, I kept the technical work and screenshots that are useful to show what we actually tested, and removed identifying information that was not needed.

## What we looked at

The project covered the home network from a few different angles:

- device inventory and network layout
- IPv4 and DHCP configuration
- local and Internet connectivity
- DNS resolution
- Wi-Fi security
- bandwidth testing
- Wireshark traffic captures
- basic security findings and recommendations

## Network topology

![Original home network topology](./screenshots/11_network_topology.png)

The environment used one router for Internet access, Wi-Fi and DHCP. The network included a laptop, mobile devices, a smart speaker and TV equipment.

## Real traffic capture

![Wireshark traffic capture](./screenshots/07_wireshark_capture_1.png)

I kept the original capture instead of recreating something cleaner for GitHub. More notes are in the [Wireshark analysis](./wireshark-analysis.md).

## Project notes

| Section | What is there |
|---|---|
| [Network Architecture](./network-architecture.md) | Topology, addressing, DHCP and Wi-Fi details |
| [Connectivity & Performance](./connectivity-tests.md) | Gateway, Internet, DNS and `tracert` testing |
| [Wireshark Analysis](./wireshark-analysis.md) | Packet captures and protocols seen during the test |
| [Security Findings](./security-findings.md) | Main risks we identified |
| [Recommendations](./recommendations.md) | Improvements proposed after the review |

## Main results

The connectivity tests confirmed access to the local gateway, Internet connectivity and DNS resolution.

The Wi-Fi connection used WPA2-Personal with CCMP on 5 GHz and 802.11ac.

The documented Speedtest result was about:

- 155.20 Mbps download
- 157.18 Mbps upload
- 4 ms latency

In Wireshark we saw TCP, TLS 1.2, SSDP, IGMP and ICMPv6 traffic. We did not see an obvious malicious pattern during the capture window, but the sample was limited and I would not treat that as proof that the network was completely clean.

## Security observations

The biggest issue was that trusted devices and IoT/multimedia devices were all on the same LAN. That is simple for a home network, but it also means a compromised IoT device would have more direct access to other local systems.

Other points we reviewed were WPS, router firmware maintenance and the fact that one router/ISP was a single point of failure.

The main recommendation was to separate IoT and multimedia devices from trusted endpoints using a guest network or VLAN when the equipment supports it.

## What I got from this project

This was one of the first activities where networking stopped feeling like only subnetting and theory. I had to look at a real configuration, test connectivity, inspect actual packets and then explain what the results meant from a security point of view.

## Context

The original assignment was completed as a group for a networking course. This GitHub version is a technical summary of that work and does not try to present the entire group project as individual work.

Personal and network-specific identifiers such as SSIDs, MAC addresses and similar values were censored before publishing.
