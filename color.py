import os 
from dotenv import load_dotenv
import psycopg2


load_dotenv()

# Extracted from the HTML table
data = {
    "Monday": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    "Tuesday": ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
    "Wednesday": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
    "Thursday": ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    "Friday": ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]
}

# Database connection details
conn = psycopg2.connect(
    # dbname=os.getenv('DB_NAME'),
    # user=os.getenv('DB_USER'),
    # password=os.getenv('DB_PASSWORD'),
    # host=os.getenv('DB_HOST'),
    # port=5433
    os.getenv('URL')
)
cur = conn.cursor()

from collections import Counter

# Flatten the list of colors to form one list
all_colors = [color for day in data.values() for color in day]

# Count the frequencies
color_counts = Counter(all_colors)

# Get the most worn color
most_worn_color = color_counts.most_common(1)[0][0]

# Median color calculation
sorted_colors = sorted(color_counts.items(), key=lambda item: item[1])
mid_index = len(sorted_colors) // 2
median_color = sorted_colors[mid_index][0] if len(sorted_colors) % 2 != 0 else (sorted_colors[mid_index - 1][0], sorted_colors[mid_index][0])

# Get the variance of colors
mean_frequency = sum(color_counts.values()) / len(color_counts)
variance = sum((count - mean_frequency) ** 2 for count in color_counts.values()) / len(color_counts)

# Find the probability of having a red
total_colors = sum(color_counts.values())
red_count = color_counts.get('RED', 0)
probability_red = red_count / total_colors


# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS colors (
        color VARCHAR(50),
        frequency INT
    )
""")

# Insert data
for color, frequency in color_counts.items():
    cur.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color, frequency))

conn.commit()
cur.close()
conn.close()


print("Most worn color:", most_worn_color)
print("Median color:", median_color)
print("Variance of colors:", variance)
print("Probability of red:", probability_red)
