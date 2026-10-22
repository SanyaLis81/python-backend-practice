transactions = [
    {"type": "deposit", "amount": 100},
    {"type": "withdraw", "amount": "abc"},
    {"type": "deposit", "amount": 50},
]
def transaction_summary(transactions):
    dct = {"types" : set(),
    "deposits" : 0,
    "withdrawals" : 0,
    "difference" : 0
           }

    for i in transactions:
        if not isinstance(i["amount"], (int, float)):
            continue
        if i["type"] == "deposit":
            dct["deposits"] += i["amount"]
        elif i["type"] == "withdraw":
            dct["withdrawals"] += i["amount"]
        dct["types"].add(i["type"])
    dct["difference"] = dct["deposits"] - dct["withdrawals"]
    return dct
print(transaction_summary(transactions))
