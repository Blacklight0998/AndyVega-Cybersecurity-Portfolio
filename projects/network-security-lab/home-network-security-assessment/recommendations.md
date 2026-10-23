# Recommendations

## 1. Segment IoT and Multimedia Devices

Place smart speakers, smart TVs and similar devices on a guest network or dedicated VLAN when the router supports segmentation.

Goal:

- Reduce direct communication between less-trusted IoT devices and trusted user endpoints
- Limit the impact of a device compromise

## 2. Maintain Router Firmware

Keep the primary router updated with supported firmware releases.

Goal:

- Reduce exposure to known vulnerabilities
- Receive security and stability fixes

## 3. Strengthen Wireless Access

Recommended wireless-security practices:

- Use a strong Wi-Fi password
- Avoid reusing passwords from other services
- Disable WPS when it is not needed
- Periodically review connected devices
- Use newer wireless security standards when supported by the equipment

## 4. Maintain an Alternative Internet Connection

The assessed network depended on one ISP and one router.

A mobile hotspot or similar backup method can provide temporary Internet connectivity during an outage.

## 5. Consider QoS for Critical Applications

The assessment did not identify configured service prioritization.

If congestion becomes a problem, QoS could be evaluated for applications sensitive to latency, including:

- Video calls
- Online classes
- Gaming

## 6. Review Connected Devices Periodically

Regularly checking the client list can help identify:

- Unknown devices
- Devices that should no longer have access
- Unexpected changes in the network environment

## 7. Establish a Basic Traffic Baseline

Periodic Wireshark captures can help build familiarity with normal traffic patterns.

A baseline makes unusual behavior easier to recognize during future troubleshooting or security investigations.

## Proposed Security Improvement

```text
Current design

Internet
   |
Router
   |
All devices on the same LAN

            ↓

Recommended design

Internet
   |
Router / Firewall
   |
   +-- Trusted Network
   |     +-- Laptop
   |     +-- Smartphones
   |
   +-- IoT / Guest Network
         +-- Smart Speaker
         +-- TV / Set-top Box
```

The primary improvement is logical separation between trusted personal devices and IoT/multimedia systems.
