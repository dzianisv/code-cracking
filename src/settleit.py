# A group of people go camping together and buy a lot of stuff.

# Rose rents a car for the trip for $400. The car is used by
# Averi, Ishaan, Jayce and herself. Later in the trip, Ishaan bought
# groceries for $100. Only Averi and Jayce consumed the groceries.

# Now the trip is over, and everyone wants to get paid back what
# they're owed.

# Write a program that produces transactions which settle each 
# person's debt.
from dataclasses import dataclass
from typing import List

@dataclass
class Transaction:
    person: str
    amount: float
    debtors: List[str]

def update(balancesheet, name, amount):
    if name not in balancesheet:
        balancesheet[name] = amount
    else:
        balancesheet[name] += amount
    
# [{"Rose", 400, ["Rose", "Averi", "Isham", "Jaye"]}, {"Isham", 100, ["Averi", "Jaye"]}]
# Dict 
# {
#    "Rose": 300,
#    "Averi", -150,
#    "Isham", 0,
#    "Jaye", -150
#}
def compute_balancesheet(transactions: List[Transaction]):
    balancesheet = dict()
    
    for tx in transactions:
        update(balancesheet, tx.person, tx.amount)        
        amount = tx.amount / len(tx.debtors)
        for debtor in tx.debtors:
            update(balancesheet, debtor, -amount)
        
    return balancesheet

    
    
b = compute_balancesheet(
    [
        Transaction("Rose", 400, ["Rose", "Averi", "Isham", "Jaye"]), 
        Transaction("Isham", 100, ["Averi", "Jaye"])
    ])
    
assert b == {'Rose': 300.0, 'Averi': -150.0, 'Isham': 0.0, 'Jaye': -150.0}

# {
#   'Sarah': 125,
#   'John': 50,
#   'Katie': 15,
#   'Sam': -7,
#   'Joseph': -6,
#   'Ben': -9,
#   'Charlie': -43,
#   'Fred': -125
# }

@dataclass
class SettleTransaction:
    debtor:  str
    creditor: str
    amount: float


def settle_balances(balancesheet):
    names = list(balancesheet.keys())
    settlelist = list()
    
    for i in range(len(names)):
        creditor = names[i]
        if balancesheet[creditor] > 0:
            for j in range(i+1, len(names)):
                debitor = names[j]
                if  balancesheet[debitor] < 0:
                    amount = min(abs(balancesheet[debitor]),  balancesheet[creditor])
                    settlelist.append(SettleTransaction(debtor=debitor, creditor=creditor, amount=amount))
                    balancesheet[creditor] -= amount
                    balancesheet[debitor] += amount
                
                if balancesheet[creditor] == 0:
                    break
                    
    return settlelist

assert settle_balances(b) == [SettleTransaction("Averi", "Rose", 150), SettleTransaction("Jaye", "Rose", 150)]

assert settle_balances({
   'Sarah': 125,
   'John': 50,
   'Katie': 15,
   'Sam': -7,
   'Joseph': -6,
   'Ben': -9,
   'Charlie': -43,
   'Fred': -125
}) == [
    SettleTransaction("Sam", "Sarah", 7),
    SettleTransaction("Joseph", "Sarah", 6),
    SettleTransaction("Ben", "Sarah", 9),
    SettleTransaction("Charlie", "Sarah", 43),
    SettleTransaction("Fred", "Sarah", 60),
    SettleTransaction("Fred", "John", 50),
    SettleTransaction("Fred", "Katie", 15)
]

def settle(transactions: List[Transaction]) -> List[SettleTransaction]:
    b = compute_balancesheet(transactions)
    return settle_balances(b)

assert settle([
        Transaction("Rose", 400, ["Rose", "Averi", "Isham", "Jaye"]), 
        Transaction("Isham", 100, ["Averi", "Jaye"])
    ]) == [
        SettleTransaction("Averi", "Rose", 150), 
        SettleTransaction("Jaye", "Rose", 150)
    ]

assert settle([
        Transaction("Rose", 400, ["Rose", "Averi", "Isham", "Jaye"]), 
        Transaction("Isham", 100, ["Averi", "Jaye"])
    ]) == [
        SettleTransaction("Averi", "Rose", 150), 
        SettleTransaction("Jaye", "Rose", 150)
    ]
