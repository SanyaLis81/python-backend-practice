transactions = [
    {"type": "deposit", "amount": 100},
    {"type": "withdraw", "amount": 30},
    {"type": "deposit", "amount": 50},
    {"type": "withdraw", "amount": 20},
    {"type": "deposit", "amount": 100},
]
operation_types = set()
total_deposits = 0
total_withdrawals = 0
for i in transactions:
    operation_types.add(i["type"])
    if i["type"] == "deposit":
        total_deposits += i["amount"]
    elif i["type"] == "withdraw":
        total_withdrawals += i["amount"]
difference = total_deposits - total_withdrawals
print("Пополнения:", total_deposits)
print("Снятия:", total_withdrawals)
print("Разница:", difference)
print("Типы операций:", operation_types)
