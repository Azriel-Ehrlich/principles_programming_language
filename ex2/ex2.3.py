from datetime import datetime, timedelta

def generate_dates(date_str, n, k):
    # Convert the input string into a datetime object
    start_date = datetime.strptime(date_str, "%d/%m/%Y")
    
    # Build a list of n dates, each k days apart, using map (functional style)
    return list(
        map(lambda i: (start_date + timedelta(days=i*k)).strftime("%d/%m/%Y"),
            range(n))
    )

# Example usage
dates = generate_dates("01/01/2024", 10, 5)
print(dates)