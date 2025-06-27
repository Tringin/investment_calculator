from decimal import Decimal

transaction_fees = {
    (Decimal("0"), Decimal("500.00")): 3,
    (Decimal("500.01"), Decimal("1000.00")): 5,
    (Decimal("1000.01"), Decimal("2000.00")): 10,
    (Decimal("2000.01"), Decimal("10000.00")): 30,
    (Decimal("10000.01"), Decimal("15000.00")): 55,
    (Decimal("15000.01"), Decimal("25000.00")): 80,
    (Decimal("25000.01"), Decimal("50000.00")): 135,
    (Decimal("50000.01"), Decimal("2000.00")): 190,
}

def get_transaction_fees(amount):
