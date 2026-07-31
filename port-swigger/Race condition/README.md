# Race Conditions

Write-ups for the **Race conditions** labs from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/race-conditions).

A race condition arises when the outcome of an operation depends on the timing of other concurrent operations. Web applications are especially exposed to them when a security control relies on a check-then-act sequence that is not atomic, letting an attacker slip several requests through the same check before the state is updated.

## Labs

| Lab | Level | Write-up |
| --- | --- | --- |
| Limit overrun race conditions | Apprentice | [View](./Limit%20overrun%20race%20conditions/README.md) |

## Disclaimer

These write-ups are provided for educational purposes only. All techniques were performed against PortSwigger's intentionally vulnerable Web Security Academy labs. Only ever test systems that you own or have explicit, written permission to test.
