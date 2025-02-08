from collections import defaultdict
import json


class Splitwise:
    def __init__(self):
        self.expenses = []

    def add_expense(self, paid_by, amount, participants):
        split_amount = amount / len(participants)
        for participant in participants:
            if participant != paid_by:
                # Add the amount owed by the participant to the paid_by
                self.expenses.append((participant, paid_by, split_amount))

    def simplify_debts(self):
        # Calculate net balances
        balances = defaultdict(float)

        # Calculate how much each person owes or is owed
        for payer, payee, amount in self.expenses:
            balances[payer] -= amount  # payer owes money
            balances[payee] += amount  # payee is owed money

        # Separate creditors and debtors based on balances
        creditors = [(person, amount) for person, amount in balances.items() if amount > 0]
        debtors = [(person, -amount) for person, amount in balances.items() if amount < 0]

        creditors.sort(key=lambda x: x[1], reverse=True)
        debtors.sort(key=lambda x: x[1], reverse=True)

        # Settle debts
        transactions = []
        i = 0
        j = 0

        while i < len(debtors) and j < len(creditors):
            debtor, debt_amount = debtors[i]
            creditor, credit_amount = creditors[j]

            # Settling amount
            settle_amount = min(debt_amount, credit_amount)
            transactions.append((debtor, creditor, settle_amount))

            # Update amounts
            debtors[i] = (debtor, debt_amount - settle_amount)
            creditors[j] = (creditor, credit_amount - settle_amount)

            # Move to the next debtor or creditor if their amounts are settled
            if debtors[i][1] == 0:
                i += 1
            if creditors[j][1] == 0:
                j += 1

        # Display results
        if not transactions:
            print("No debts to settle.")
        else:
            print("\nSimplified Debts:")
            for debtor, creditor, amount in transactions:
                print(f"{debtor} owes {creditor}: ${amount:.2f}")

    def __repr__(self):
        return json.dumps(self.expenses, indent=2)


# Example usage:
s = Splitwise()

# Adding various expenses involving multiple participants
s.add_expense('Alice', 1200, ['Alice', 'Bob', 'Charlie', 'Dave'])  # 1200 / 4 = 300 each
s.add_expense('Bob', 500, ['Bob', 'Charlie', 'Dave'])  # 500 / 3 = 166.67 each
s.add_expense('Charlie', 800, ['Alice', 'Charlie', 'Dave'])  # 800 / 3 = 266.67 each
s.add_expense('Dave', 100, ['Alice', 'Bob'])  # 100 / 2 = 50 each
s.add_expense('Alice', 900, ['Alice', 'Charlie'])  # 900 / 2 = 450 each
s.add_expense('Dave', 300, ['Bob', 'Dave'])  # 300 / 2 = 150 each

print("Initial Expenses:")
print(s)
s.simplify_debts()

