from decimal import Decimal

transaction_fees = {
    (Decimal("0.00"), Decimal("500.00")): 3,
    (Decimal("500.01"), Decimal("1000.00")): 5,
    (Decimal("1000.01"), Decimal("2000.00")): 10,
    (Decimal("2000.01"), Decimal("10000.00")): 30,
    (Decimal("10000.01"), Decimal("15000.00")): 55,
    (Decimal("15000.01"), Decimal("25000.00")): 80,
    (Decimal("25000.01"), Decimal("50000.00")): 135,
    (Decimal("50000.01"), Decimal("inf")): 190,
}

#if deciding to add "etf leader" feature, take fee structure from "etf_leader_fees"
etf_leader_fees = {
    (Decimal("0.00"), Decimal("500.00")): 3,
    (Decimal("500.01"), Decimal("1000.00")): 5,
    (Decimal("1000.01"), Decimal("inf")): 9,
}

depot_fees = {
    (Decimal("0.00"), Decimal("50000.00")): 20,
    (Decimal("50000.01"), Decimal("100000.00")): 25,
    (Decimal("100000.01"), Decimal("150000.00")): 37.50,
    (Decimal("150000.01"), Decimal("inf")): 50,
}

def get_transaction_fees(amount):
    amount = Decimal(str(amount))
    for key, value in transaction_fees.items():
        if amount >= key[0] and amount <= key[1]:
            return value

def get_leader_fees(amount):
    amount = Decimal(str(amount))
    for key, value in etf_leader_fees.items():
        if amount >= key[0] and amount <= key[1]:
            return value

def get_depot_fees(portfolio_value):
    pass

def get_stamp_fees(transaction_amount):
    pass

def get_exchange_fees(transaction_amount):
    pass

