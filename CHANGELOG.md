
## Prone
- >_ LOG INITIATED: SIGNAL SYSTEM BOOT
- >_ ALL CHANGES ARE RECORDED HERE
---
### [0.6.0] - 03.05.2026

#### Added
- Dynamic crypto configuration via environment variables
- Support for configurable upper/lower thresholds per asset

#### Refactored
- Removed hardcoded configuration from codebase
- Decoupled alert logic and price fetcher from config module

#### Improved
- Fully configurable system without code changes

---

### [0.5.0] - 01.05.2026

#### Added
- Persistent state management using JSON file
- State loading on startup and saving after each cycle

#### Improved
- Prevent duplicate alerts after restart

---

### [0.4.0] - 25.04.2026

#### Added
- Dockerfile for containerized execution
- .dockerignore for optimized builds

#### Improved
- Real-time logging in container (PYTHONUNBUFFERED)

---

### [0.3.0] - 04.04.2026

#### Added
- Logging system with INFO and ERROR levels
- Centralized logger module

#### Refactored
- Replaced print statements with logging
- Integrated logging across notifier and fetch modules

---

### [0.2.0] - 08.03.2026

#### Added
- Crypto price fetching via CoinGecko API
- Configurable cryptocurrency list
- Threshold-based alert system
- Stateful alert logic to prevent spam
- Continuous monitoring loop

#### Refactored
- Modular architecture (price_fetcher, alert_logic separation)

---

### [v0.1.0] - 15-02-2026

#### ADDED
- `src/notifier.py` - Telegram notifier class
- `src/main.py` - Initialization entry point
- Enviroment-based configuration with `.env`
- GitFlow branch structure
- Version tagging (`v0.1.0`)
- Modular project architecture

#### CHANGED
- Explicit dotenv loading from project root
- Improved error handling for missing enviroment variables

#### FIXED
- Robust token validation on initialization

#### TECHNICAL
- HTTP integration with Telegram bot API
- Fail-fast initialization strategy
- Timeout-based request handling
- Clean separation of concerns

#### NOTES
+ >_STSTEM: TELEGRAM SIGNAL DISPATCH OPERATIONAL
+ >_STATUS: NOTIFIER STABLE
+ >_NEXT: CRYPTO PRICE FETCHER MODULE
+ >_MODE: TERMINAL-FRIST DEVELOPMENT