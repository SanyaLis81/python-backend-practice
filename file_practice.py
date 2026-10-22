import json

with open("balance.txt", "w", encoding="utf-8") as file:
    file.write("2500")
with open("balance.txt", "w", encoding="utf-8") as file:
    file.write("3000")
account = {
    "account_number" : "98765",
    "balance" : 4000
}

with open("account.json", "w", encoding="utf-8") as file:
    json.dump(account, file, indent=4)
with open("account.json", "r", encoding="utf-8") as file:
    loaded_account = json.load(file)
print(loaded_account["balance"])
loaded_account["balance"] += 500
with open("account.json", "w", encoding="utf-8") as file:
    json.dump(loaded_account, file, indent=4)
try:
    with open("account.json", "r", encoding="utf-8") as file:
        json_loaded = json.load(file)
    print(json_loaded["account_number"])
    print(json_loaded["balance"])
except FileNotFoundError:
    print("Файл не найден")
except json.decoder.JSONDecodeError:
    print("Файл содержит некорректный JSON")
with open("account.json", "w", encoding="utf-8") as file:
    json.dump(account, file, indent=4)

def find_account(lst, key, amount):
    for i in lst:
        if "account_number" in i and "balance" in i and i["account_number"] == key:
            i["balance"] += amount
            return True, i["balance"]
    return False, None

def load_accounts(filename):
    with open(filename, "r", encoding="utf-8") as file:
        loaded_account = json.load(file)
        return loaded_account

def save_accounts(accounts, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(accounts, file, indent=4)

accounts = [
    {
        "account_number": "101",
        "balance": 4000
    },
    {
        "account_number": "102",
        "balance": 2500
    },
    {
        "account_number": "103",
        "balance": 7000
    }
]
save_accounts(accounts, "account.json")
accounts_file = load_accounts("account.json")
print(accounts_file)
if find_account(accounts_file, "102", 500):
    print("Счёт успешно пополнен")
    save_accounts(accounts_file, "account.json")
else:
    print("Счёт не найден")
