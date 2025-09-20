from brownie import DemoToken, accounts

def main():
    acct = accounts.load('my_account')  # load your Brownie account
    token = DemoToken.deploy({'from': acct})
    print(f"Token deployed at {token.address}")
