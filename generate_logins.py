import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from faker import Faker
import sys

def generate_login_times(date, num_logins):
    """Generate random login times for a given day."""
    start_time = datetime.combine(date, datetime.min.time())
    end_time = datetime.combine(date, datetime.max.time())
    time_delta = (end_time - start_time).total_seconds()
    
    login_times = []
    for _ in range(num_logins):
        random_seconds = random.randint(0, int(time_delta))
        login_time = start_time + timedelta(seconds=random_seconds)
        login_times.append(login_time)
    
    return sorted(login_times)

def generate_hack_attempts(date, num_attempts=3):
    """Generate failed login attempts that look like hack attempts."""
    start_time = datetime.combine(date, datetime.min.time())
    end_time = datetime.combine(date, datetime.max.time())
    time_delta = (end_time - start_time).total_seconds()
    
    attempts = []
    for _ in range(num_attempts):
        random_seconds = random.randint(0, int(time_delta))
        attempt_time = start_time + timedelta(seconds=random_seconds)
        attempts.append(attempt_time)
    
    return sorted(attempts)

def main():
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python generate_logins.py <output_file> <start_date> <end_date>")
        print("Example: python generate_logins.py logins.csv 2024-01-01 2024-01-31")
        sys.exit(1)

    output_file = sys.argv[1]
    start_date_str = sys.argv[2]
    end_date_str = sys.argv[3]

    try:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Error: Dates must be in YYYY-MM-DD format")
        sys.exit(1)

    # Read user data
    users_df = pd.read_csv('users.csv')
    faker = Faker()

    # Initialize lists to store login data
    login_data = []

    # Generate data for each day
    current_date = start_date
    while current_date <= end_date:
        # Process each user
        for _, user in users_df.iterrows():
            # Determine if user will login today based on propensity
            if random.random() < user['login_propensity']:
                # Generate number of logins for today
                num_logins = random.randint(1, 10)
                login_times = generate_login_times(current_date, num_logins)
                
                # Generate logins
                for login_time in login_times:
                    # Determine if IP should change (1 in 100 chance)
                    ip_address = faker.ipv4() if random.random() < 0.01 else user['ip_address']
                    
                    # Determine if user agent should change (1 in 1000 chance)
                    user_agent = faker.user_agent() if random.random() < 0.001 else user['user_agent']
                    
                    login_data.append({
                        'timestamp': login_time,
                        'user_id': user['user_id'],
                        'ip_address': ip_address,
                        'user_agent': user_agent,
                        'success': True
                    })

        # Generate hack attempts for this day
        hack_attempts = generate_hack_attempts(current_date)
        for attempt_time in hack_attempts:
            # Generate random user ID that doesn't exist
            fake_user_id = faker.uuid4()
            login_data.append({
                'timestamp': attempt_time,
                'user_id': fake_user_id,
                'ip_address': faker.ipv4(),
                'user_agent': faker.user_agent(),
                'success': False
            })

        current_date += timedelta(days=1)

    # Convert to DataFrame and sort by timestamp
    logins_df = pd.DataFrame(login_data)
    logins_df = logins_df.sort_values('timestamp')

    # Save to CSV
    logins_df.to_csv(output_file, index=False)
    print(f"Generated {len(logins_df)} login records in {output_file}")

if __name__ == "__main__":
    main() 