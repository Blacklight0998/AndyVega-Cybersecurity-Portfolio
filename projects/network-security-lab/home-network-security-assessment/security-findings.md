# Security Findings and Risk Assessment

## Summary

The residential network provided adequate connectivity and basic wireless protection, but the assessment identified several security and availability concerns that could be improved.

| Finding | Potential Impact | Risk Level | Recommended Action |
|---|---|---:|---|
| All devices on one LAN | A compromised device could communicate with other local devices | Medium | Separate IoT / less-trusted devices |
| Single router and ISP | Loss of connectivity if the router or ISP fails | Low | Maintain an alternative connection method |
| WPA2-Personal in use | Acceptable protection, but dependent on strong credentials | Low | Use strong credentials and consider newer security when supported |
| Possible unused WPS functionality | Could increase wireless attack surface if enabled | Medium | Disable WPS if not required |
| Router firmware may become outdated | Known vulnerabilities may remain unpatched | Medium | Keep firmware updated |
| IoT devices share trusted LAN | IoT compromise could increase lateral exposure | Medium | Use guest network or VLAN segmentation |

## Finding 1: Lack of Network Segmentation

All assessed devices were connected to the same local network.

### Why it matters

A flat network allows endpoints on the same segment to communicate more freely. If a less-trusted device such as an IoT endpoint were compromised, other devices could be exposed to additional risk.

### Recommendation

Separate smart devices and multimedia equipment from laptops and personal devices using a guest network or VLAN when supported.

---

## Finding 2: Single Point of Failure

The household depended on one Internet provider and one primary router.

### Why it matters

Failure of either component would remove Internet access for all connected devices.

### Recommendation

Maintain an alternative temporary connection method, such as mobile tethering, for outages.

---

## Finding 3: Wireless Security

The network used WPA2-Personal with CCMP encryption.

### Assessment

This provides a reasonable level of protection for a residential network when combined with a strong password and properly maintained equipment.

### Recommendations

- Use a strong Wi-Fi password
- Change credentials when necessary
- Keep router firmware updated
- Disable WPS if it is not needed
- Review connected devices periodically

---

## Finding 4: IoT Exposure

Smart and multimedia devices were connected to the same LAN as user devices.

### Why it matters

IoT devices can increase the number of endpoints that must be trusted and maintained.

### Recommendation

Move IoT devices to a guest or isolated network segment so that a compromise has less opportunity to affect trusted systems.

## Overall Assessment

The project did not identify an active attack or obvious malicious traffic during the assessment period. The main opportunities for improvement were preventive: segmentation, firmware maintenance, stronger wireless hygiene and basic redundancy.
