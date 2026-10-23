# VLSM Subnetting Plan

The starting network for the lab was:

`10.10.0.0/21`

The LANs were ordered from the highest host requirement to the lowest before assigning address space.

| Subnet | Hosts | Mask | Network | First usable | Last usable | Broadcast |
|---|---:|---|---|---|---|---|
| A | 240 | 255.255.255.0 | 10.10.0.0 | 10.10.0.1 | 10.10.0.254 | 10.10.0.255 |
| B | 192 | 255.255.255.0 | 10.10.1.0 | 10.10.1.1 | 10.10.1.254 | 10.10.1.255 |
| C | 150 | 255.255.255.0 | 10.10.2.0 | 10.10.2.1 | 10.10.2.254 | 10.10.2.255 |
| D | 120 | 255.255.255.128 | 10.10.3.0 | 10.10.3.1 | 10.10.3.126 | 10.10.3.127 |
| E | 85 | 255.255.255.128 | 10.10.3.128 | 10.10.3.129 | 10.10.3.254 | 10.10.3.255 |
| F | 40 | 255.255.255.192 | 10.10.4.0 | 10.10.4.1 | 10.10.4.62 | 10.10.4.63 |
| R1-R2 | 2 | 255.255.255.252 | 10.10.4.64 | 10.10.4.65 | 10.10.4.66 | 10.10.4.67 |
| R2-R3 | 2 | 255.255.255.252 | 10.10.4.68 | 10.10.4.69 | 10.10.4.70 | 10.10.4.71 |
| R1-R3 | 2 | 255.255.255.252 | 10.10.4.72 | 10.10.4.73 | 10.10.4.74 | 10.10.4.75 |

## Why VLSM was used

The LANs did not need the same number of hosts. Using one fixed mask for every subnet would waste more addresses.

The /30 networks were used for the router-to-router connections because each point-to-point link only needed two usable addresses.
