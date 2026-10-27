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
    if not isinstance(loaded_account, list):
        raise ValueError("Файл должен содержать список счетов")
    if not loaded_account:
        raise ValueError("Список счетов пуст")
    for account in loaded_account:
        if not isinstance(account, dict):
            raise ValueError("Каждый счёт должен быть словарём")
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

def deposit_to_account(filename, key, amount):
    try:
        file_account = load_accounts(filename)
    except json.JSONDecodeError:
        raise ValueError("Файл содержит некорректный JSON")
    except FileNotFoundError:
        raise ValueError("Файл не найден")
    result = find_account(file_account, key, amount)
    if result[0]:
        save_accounts(file_account, filename)
        return True
    return False

with open("account.json", "w", encoding="utf-8") as file:
    json.dump(accounts, file, indent=4)

tm_file = [
    {"account_number": "102"}
]
with open("tm_file.json", "w", encoding="utf-8") as file:
    json.dump(tm_file, file, indent=4)

def get_account_info(accounts, account_number):
    for account in accounts:
        if account["account_number"] == account_number:
            return account
    return None

def get_account_info_from_file(filename, account_number):
    return get_account_info(load_accounts(filename), account_number)

def withdraw_from_account(filename, account_number, amount):
    file_account = load_accounts(filename)
    info_account = get_account_info(file_account, account_number)
    if info_account != None:
        if "balance" in info_account and info_account["balance"] >= amount:
            info_account["balance"] -= amount
            save_accounts(file_account, filename)
            return True
    return False
