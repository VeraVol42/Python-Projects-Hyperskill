import argparse
from math import ceil, log

parser = argparse.ArgumentParser(description="This program is a credit calculator.")
parser.add_argument('--type', choices=['annuity', 'diff'], required=True, help='Type of payment: "annuity" or "diff"')
parser.add_argument('--payment', type=int, help='Monthly payment amount')
parser.add_argument('--principal', type=int, help='Loan principal amount')
parser.add_argument('--periods', type=int, help='Number of periods')
parser.add_argument('--interest', type=float, help='Loan interest rate')

args = parser.parse_args()

if args.type == 'diff' and args.principal is not None and args.principal > 0 and args.interest is not None and args.interest > 0.0 and args.periods is not None and args.periods > 0:
    m = 1  # month_number
    total_payment = 0
    i = args.interest / (12 * 100)
    while m <= args.periods:
        diff_payment = ceil(args.principal / args.periods + i * (args.principal - ((args.principal * (m - 1)) / args.periods)))
        print(f"Month {m}: payment is {diff_payment}")
        m += 1
        total_payment += diff_payment
    print(f"Overpayment = {total_payment - args.principal}")


elif args.type == 'annuity' and args.principal is not None and args.principal > 0 and args.interest is not None and args.interest > 0.0 and args.periods is not None and args.periods > 0:
    i = args.interest / (12 * 100)
    m = i * ((1 + i) ** args.periods) / (((1 + i) ** args.periods) - 1)
    payment = ceil(args.principal * m)
    print(f"Your monthly payment = {payment}!")
    print(f"Overpayment = {payment * args.periods - args.principal}")


elif args.type == 'annuity' and args.interest is not None and args.interest > 0.0 and args.periods is not None and args.periods > 0 and args.payment is not None and args.payment > 0:
    i = float(args.interest / (12 * 100))
    m = (1 + i) ** args.periods
    principal = args.payment / ((i * m) / (m - 1))
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {args.payment * args.periods - principal}")

elif args.type == 'annuity' and args.principal is not None and args.principal > 0 and args.interest is not None and args.interest > 0.0 and args.payment is not None and args.payment > 0:
    i = float(args.interest / (12 * 100))
    x = args.payment / (args.payment - i * args.principal)
    n = ceil(log(x, 1 + i))
    if n < 12 > 1:
        print(f"It will take {n} months to repay this loan!")
    elif n == 1:
        print(f"It will take {n} month to repay this loan!")
    elif n == 12:
        print(f"It will take {1} year to repay this loan!")
    elif n > 12 and n % 12 > 1:
        print(f"It will take {ceil(n // 12)} years and {ceil(n % 12)} months to repay this loan!")
    elif n > 12 and ceil(n % 12) == 1:
        print(f"It will take {ceil(n // 12)} years and {1} month to repay this loan!")
    else:
        print(f"It will take {ceil(n // 12)} years to repay this loan!")

        print(f"Overpayment = {args.payment * n - args.principal}")

else:
    print("Incorrect parameters")
