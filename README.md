# Bitcoin Runes ETCH & DEPLOY & TARGET 840,000th BLOCK

This Python script provides an environment for generating Partially Signed Bitcoin Transactions (PSBT) targeting specific blocks on the Bitcoin blockchain. This script is designed for educational and development purposes, offering users a hands-on experience with Bitcoin transactions.

We thought that specific API keys for a premium subscription but decided launch it free. Enjoy! 

## Features

- **PSBT Generation**: Execute the creation of a Bitcoin transaction aimed at a specific block (block 840,000).
- **API Request**: Send transaction details to Magic Runes Etch & Deployment service.
- **Customizable Token Properties**: Input parameters for Runes, such as ticker, decimals, and supply limits.

## Prerequisites

Ensure you have the following requirements installed before starting:
- Python 3.8 or above
- Pip for Python package management

## Installation

Follow these steps to get your development environment ready:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/magicrunesbtc/etch-runes.git

2. **Install necessary Python packages:**
   ```bash
   pip install requests

**Configuration**
Open the config.py file and set the following configurations:

API_URL: Magic Runes API for etching & deploying Runes
WALLET_SECRET_PHRASE: Secret phrase for your wallet 

**USAGE**
Just execute by this command: python main.py

You will be prompted to enter the following token properties when you run the script:

etch_rune_ticker: Unique identifier for the token (e.g., "MAGICRUNES").
decimals: Number of decimal places for token precision (0 to 38).
symbol: A single-character symbol for the token (e.g., "M").
max_supply: The maximum number of tokens that can be minted.
limit_per_mint: The number of tokens allowed per mint event.
