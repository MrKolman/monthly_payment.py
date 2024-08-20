def calculate_monthly_payment(principal, annual_rate, years):

    r = (annual_rate / 12) / 100
    n = years * 12
    # calculate your monthly payment
    monthly_payment = (principal * r) / (1 - (1 + r) ** -n)
    return monthly_payment

principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))
monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {monthly_payment:.2f} kr")