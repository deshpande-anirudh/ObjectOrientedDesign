from collections import defaultdict
import json


class Splitwise:
    def __init__(self):
        self.balances = defaultdict(dict)

    def add_expense(self, paid_by, amount, participants):
        split_amount = amount / len(participants)

        for participant in participants:
            if participant == paid_by:
                continue
            self.balances[paid_by][participant] = self.balances[paid_by].get(participant, 0) + split_amount
            self.balances[participant][paid_by] = self.balances[participant].get(paid_by, 0) - split_amount

    def simplify_debts(self):
        creditors = []
        debtors = []

        # Aggregate net balances for all participants
        net_balances = {}
        for person in self.balances:
            net_balance = sum(self.balances[person].values())
            if abs(net_balance) > 1e-9:  # Avoid precision issues
                net_balances[person] = net_balance

        for person, balance in net_balances.items():
            if balance > 0:
                creditors.append([person, balance])
            elif balance < 0:
                debtors.append([person, -balance])

        debtors.sort(key=lambda x: -x[1])
        creditors.sort(key=lambda x: -x[1])

        i = 0
        j = 0
        transactions = []

        while i < len(debtors) and j < len(creditors):
            creditor, credit_amount = creditors[j]
            debitor, debit_amount = debtors[i]

            settled_amount = min(credit_amount, debit_amount)
            transactions.append((debitor, creditor, settled_amount))

            creditors[j][1] -= settled_amount
            debtors[i][1] -= settled_amount

            if creditors[j][1] < 1e-9:
                j += 1
            if debtors[i][1] < 1e-9:
                i += 1

        print()
        for creditor, debitor, amount in transactions:
            print(f"{creditor} to pay {debitor} the amount ${amount:.2f}")

    def __repr__(self):
        return json.dumps(self.balances)

s = Splitwise()

# Adding various expenses involving multiple participants
s.add_expense('Alice', 1200, ['Alice', 'Bob', 'Charlie', 'Dave'])  # 1200 / 4 = 300 each
s.add_expense('Bob', 500, ['Bob', 'Charlie', 'Dave'])              # 500 / 3 = 166.67 each
s.add_expense('Charlie', 800, ['Alice', 'Charlie', 'Dave'])        # 800 / 3 = 266.67 each
s.add_expense('Dave', 100, ['Alice', 'Bob'])                       # 100 / 2 = 50 each
s.add_expense('Alice', 900, ['Alice', 'Charlie'])                  # 900 / 2 = 450 each
s.add_expense('Dave', 300, ['Bob', 'Dave'])                        # 300 / 2 = 150 each

print("Initial Balances:")
print(s)
s.simplify_debts()

