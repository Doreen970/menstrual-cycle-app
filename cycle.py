import datetime

def period_info():
    # get day one and last day from user
    previous_day_one = input("Enter the first day of your previous period (YYYY-MM-DD): ")
    day_one = input("Enter first day of your recent period (YYYY-MM-DD): ")
    #parse dates
    start_date = datetime.datetime.strptime(day_one, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(previous_day_one, "%Y-%m-%d").date()
    #calculate period length
    period_length = end_date - start_date
    #calculate days before next period
    next_period_date = start_date - period_length
    current_date = datetime.date.today()
    days_before_next_period = next_period_date - current_date
    #print period info
    print(f"Your next period starts on {next_period_date}")
    print(f"Your cycle length is {period_length.days} days")
    print(f"There are {days_before_next_period} days before next period")

period_info()