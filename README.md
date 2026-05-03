
### :crown:PRONE - Crypto Alert System

> **SIGNAL EDITION** | `>_CRYPTO MONITOR ONLINE`

![Status](https://img.shields.io/badge/STATUS-TELEGRAM_OPERATIONAL-green)
![Python](https://img.shields.io/badge/PYTHON-3.13-blue)
![Platform](https://img.shields.io/badge/PLATFORM-Linux%20|%20macOS-black)
![Version](https://img.shields.io/badge/VERSION-0.6.0-red)
![Mode](https://img.shields.io/badge/MODE-HEADLESS_TERMINAL-00FF41)

- SYSTEM: Prone v0.6.0 online
- MISSION: Monitor Crypto Signals
- PROTOCOL: HTTP API -> Telegram Dispatch
- ARCHITECTURE: Modular | GitFlow | Terminal-Driven

---

#### :rocket:QUICK START
```
# Clone repository
git clone https://github.com/KotaroGa/Prone.git
cd prone

# Checkout stable release
git checkout v0.6.0

# Create virtual enviroment
python -m venv .venv

# Activate (Linux-MacOS)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create enviroment file
nano .env
Add `TELEGRAM_BOT_TOKEN=your_token`
    `TELEGRAM_CHAT_ID=your_chat_id`

# Run
python src/main.py
```

---
#### :satellite:CURRENT CAPABILITIES
* Real-time cryptocurrency price monitoring
* CoinGecko API price retrieval
* Configurable cryptocurrency list
* Threshold-based alert system
* Stateful alert logic (anti-spam notifications)
* Telegram Bot alert dispatch
* Enviroment-based configuration
* Secure token handling(.env ignored)
* Modular notifier class
* GitFlow structured workflow
* Version tagging
* Real time logging in container (PYTHONUNBUFFERED)
* Persistent alert state (no duplicate alerts after restart)
* Dynamic asset configuration via enviroment variable


---
#### :nut_and_bolt:TECH STACK
- >LANGUAGE: Python3.13
- >HTTP: requests
- >ENV: python-dotenv
- >DATA: CoinGecko API
- >NOTIFICATIONS: Telegram Bot API
- >WORKFLOW: GitFlow
- >PLATFORM: Terminal-first development
- >LOGGING: Python logging module


---
> [!TIP]
>##### If you like my work and want to support it, you can do so with cryptocurrencies.
>##### Your contributions help maintain projects and continue creating free content

- 🔴 (BTC): `bc1qlhup35a64qq0e6uc2v07s64tzjrmj8j9e24jmr`
- 🔴 (ETH): `0x6D4DB084eaC2cF9D4BbF04FdCBd3e737FDD36dcc`
- 🔴 (SOL): `51ueAbc6TC52UExxTKRoYSKuiWnLSci2`