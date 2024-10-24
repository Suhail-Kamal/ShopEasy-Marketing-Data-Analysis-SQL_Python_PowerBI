import pandas as pd
import pyodbc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Download the VADER lexicon for sentiment analysis if not already present
nltk.download('vader_lexicon')

# Define a function to fetch data from a SQL database using a SQL query
def fetch_data_from_sql():
    # Define the connection string with parameters for the database connection
    conn_str = (
        "Driver={SQL Server};"
        "Server=MSI\\SQLEXPRESS;"
        "Database=PortfolioProject_MarketingAnalytics;"
        "Trusted_Connection=yes;"
    )
    # Establish the connection to the database
    conn = pyodbc.connect(conn_str)

    # Define the SQL query to fetch customer reviews data
    query = "SELECT ReviewID, CustomerID, ProductID, ReviewDate, Rating, ReviewText FROM customer_reviews"

    # Execute the query and fetch the data into a DataFrame
    df = pd.read_sql(query, conn)

    # Close the connection to free up resources
    conn.close()

    # Return the fetched data as a DataFrame
    return df

# Fetch the customer reviews data from the SQL database
customer_reviews_df = fetch_data_from_sql()

# Initialize the VADER sentiment intensity analyzer for analyzing the sentiment of text data
sia = SentimentIntensityAnalyzer()

# Define a function to calculate sentiment scores using VADER
def calculate_sentiment(review):
    sentiment = sia.polarity_scores(review)
    return sentiment['compound']

# Define a function to categorize sentiment using both the sentiment score and the review rating
def categorize_sentiment(score, rating):
    if score > 0.05: #positive sentiment score
        if rating >= 4:
            return 'Positive' # High rating and positive sentiment
        elif rating == 3:
            return 'Mixed Positive' # Neutral rating but positive sentiment
        else:
            return 'Mixed Negative'
    elif score < -0.05:
        if rating <= 2:
            return 'Negative'
        elif rating ==3:
            return 'Mixed Negative'
        else:
            return 'Mixed Positive'
    else:
        if rating >= 4:
            return 'Positive'
        elif rating <= 2:
            return 'Negative'
        else:
            return 'Neutral'
        
# Define a function to bucket sentiment scores into text ranges
def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0'
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'
    else:
        return '-1.0 to -0.5'
# Apply sentiment analysis to calculate sentiment scores for each review
customer_reviews_df['SentimentScore'] = customer_reviews_df['ReviewText'].apply(calculate_sentiment)
# Apply sentiment categorization using both text and rating
customer_reviews_df['SentimentCategory'] = customer_reviews_df.apply(
    lambda row: categorize_sentiment(row['SentimentScore'], row['Rating']), axis=1)

# Apply sentiment bucketing to categorize scores into defined ranges
customer_reviews_df['SentimentBucket'] = customer_reviews_df['SentimentScore'].apply(sentiment_bucket)

print(customer_reviews_df.head())

# Save the DataFrame with sentiment scores, categories, and buckets to a new CSV file
customer_reviews_df.to_csv('fact_customer_reviews_with_sentiment.csv', index=False)




