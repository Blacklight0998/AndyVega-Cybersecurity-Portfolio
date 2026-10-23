# Network Security Lab

This project groups two university networking activities that cover different parts of the same topic: understanding a network and designing one.

## 1. Home Network Security & Traffic Analysis

[View project](./home-network-security-assessment/)

A university group project based on a real residential network. It covers IPv4 and DHCP, gateway and DNS testing, Wi-Fi security review, Wireshark captures, and security findings and recommendations. The main recommendation was to separate IoT and multimedia devices from trusted devices.

The findings are based on configuration review and a limited packet capture. I did not run a vulnerability scan or test the recommendations.

## 2. Packet Tracer VLSM Network Lab

[View project](./packet-tracer-vlsm-lab/)

A university group exercise in Cisco Packet Tracer. I divided `10.10.0.0/21` with VLSM into six LANs and three point-to-point router links, configured the router interfaces and tested connectivity between PCs and their gateways and between routers.

## How they connect

The first project found that a flat network was the main weakness. The second shows I can plan and configure addressing from scratch. A natural next step is to combine both: build a segmented network with a firewall or ACLs, scan it before and after, and show that the isolation works. This is not done yet.
