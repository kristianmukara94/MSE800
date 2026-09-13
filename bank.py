# Bank Account Management System
# Demonstrates OOP concepts: classes, attributes, methods, and single inheritance.


class BankAccount:
    """Base class: represents a general bank account."""

    def __init__(self, account_number, customer_name, balance):
        # self refers to the specific object being created.
        # These become that object's own attributes (its stored data).
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def display_details(self):
        """Show the account's current details."""
        print("Account Details:")
        print(f"  Account Number : {self.account_number}")
        print(f"  Customer Name  : {self.customer_name}")
        print(f"  Balance        : ${self.balance:,.2f}")

    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount
        print(f"Deposited ${amount:,.2f}. New balance: ${self.balance:,.2f}")

    def withdraw(self, amount):
        """Remove money from the account, but never more than the balance."""
        if amount > self.balance:
            # Conditional validation: block withdrawals that exceed the balance.
            print(f"Withdrawal failed: ${amount:,.2f} exceeds balance of ${self.balance:,.2f}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:,.2f}. New balance: ${self.balance:,.2f}")


class SavingsAccount(BankAccount):
    """
    Child class: a SavingsAccount IS a BankAccount, plus interest features.
    Inherits __init__, deposit, and withdraw directly from BankAccount.
    """

    def calculate_interest(self, interest_rate):
        """Calculate interest earned based on current balance and rate (%)."""
        interest = self.balance * (interest_rate / 100)
        print(f"Interest at {interest_rate}% on ${self.balance:,.2f} = ${interest:,.2f}")
        return interest

    def display_details(self):
        """Extend the base class's display_details with a savings-specific label."""
        print("--- Savings Account ---")
        # super() calls BankAccount's display_details instead of rewriting those lines.
        super().display_details()


if __name__ == "__main__":
    # Step 3: Execution script — John's Savings Account scenario.
    john_account = SavingsAccount("SA1001", "John", 5000)

    print("\n1. Initial account details:")
    john_account.display_details()

    print("\n2. Deposit $1,000:")
    john_account.deposit(1000)

    print("\n3. Withdraw $500:")
    john_account.withdraw(500)

    print("\n4. Calculate interest at 5%:")
    john_account.calculate_interest(5)

    print("\n5. Attempt an invalid withdrawal (more than balance):")
    john_account.withdraw(100000)
