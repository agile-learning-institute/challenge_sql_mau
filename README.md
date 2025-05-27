# SQL MAU/DAU Challenge

SQL Challenge for Monthly/Daily Active User Analysis and Visualization

## Overview
Modern identity management systems provide event streams of login attempts, which are crucial for measuring user engagement through metrics like Daily Active Users (DAU) and Monthly Active Users (MAU). This challenge focuses on analyzing login data to create meaningful visualizations of user engagement patterns.

## Data Structure
The project includes two main data files:

### users.csv
- Contains user information including:
  - user_id: Unique identifier for each user
  - user_name: Username
  - street: User's street address
  - city: User's city
  - state: User's state
  - zip: User's zip code

### logins.csv
- Contains login event data including:
  - timestamp: Login attempt timestamp (UTC)
  - user_id: Reference to users.csv
  - login_status: Success/failure status
  - Additional metadata (IP, user agent, etc.)

## Challenge Requirements

### Primary Goals
1. Create a visualization showing DAU trends over the two-month period
2. Create a visualization showing MAU trends, use a moving 30-day window to show MAU over the prior 30 days.
3. Ensure proper handling of multiple logins per user per day/month (no double counting)

### Success Criteria
- Accurate DAU/MAU calculations
- Clear, readable visualizations
- Proper handling of edge cases (time zones, missing data)
- Documentation of your approach and findings

### Bonus Challenges
1. **Geographic Analysis**
   - MAU by State visualization
   - User distribution heat map
   - Regional engagement patterns

2. **Engagement Analysis**
   - DAU/MAU ratio trends
   - User retention analysis
   - Login time pattern analysis (morning vs evening users)

3. **Advanced Metrics**
   - User session duration analysis
   - Login frequency patterns
   - User churn prediction

## Implementation Approaches
You are free to choose any tools, languages, or frameworks to complete this challenge. Here are some example approaches, but feel free to use any method you prefer:

### Example 1: DBeaver and Spreadsheet Analysis
Probably the simplest possible visualization would be
1. Connect to your database using DBeaver
2. Run your DAU/MAU queries
3. Export results to CSV
4. Open in your preferred spreadsheet software (Excel, Google Sheets, etc.)
5. Create visualizations using the built-in charting tools

### Example 2: Python with Data Analysis Libraries
If you wanted to exercise your python skills a nice approach would be to use pandas and matplot. Your code might look something like this:
```python
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("example.db")
df = pd.read_sql_query("SELECT date, value FROM timeseries", conn)

plt.plot(df['date'], df['value'])
plt.title("Line Graph")
plt.xlabel("Date")
plt.ylabel("Value")
plt.show()
```

### Example 3: Grafana Dashboard
If you want to take your skills to the next level, Let's create a live interactive dashboard using open source observability tools That are commonly used in IT operations. You want to run grafana and your database in containers, Your doctor compose file might look something like this:
```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15
    container_name: postgres
    environment:
      POSTGRES_USER: grafana
      POSTGRES_PASSWORD: grafana
      POSTGRES_DB: metrics
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    depends_on:
      - postgres
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana-storage:/var/lib/grafana

volumes:
  pgdata:
  grafana-storage:
```

### Example 4: Custom Solution
Create your own unique approach using any combination of tools and techniques.

## Submission Requirements
1. Create a branch of this repository for your work
1. Update this README with information about your solution
1. Include instructions on how to duplicate your solution
4. Provide any additional analysis or insights

## Tips for Success
- Consider timezone handling in your calculations
- Think about how to handle edge cases
- Focus on creating clear, meaningful visualizations
- Document your approach and reasoning
- Consider scalability and performance
- Think about how your solution could be extended
