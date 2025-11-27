
import sys
if len(sys.argv) != 3:
    initial_balance = float(sys.argv[1])
    deposit_amount = float(sys.argv[2])
else:
  
  initial_balance=1000
  deposit_amount=200


updated_balance = initial_balance + deposit_amount

# Display result
print(f"Initial Balance: {initial_balance}")
print(f"Deposit Amount: {deposit_amount}")
print(f"Updated Balance: {updated_balance}")
