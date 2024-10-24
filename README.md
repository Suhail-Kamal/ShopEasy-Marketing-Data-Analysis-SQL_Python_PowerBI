# ShopEasy Marketing Data Analysis 
### Project Overview

This data analysis project aims to provide insights into the Marketing performance of ShopEasy, an online retail business, which is facing reduced customer engagement and conversion rates despite launching several new online marketing campaigns. 

- <a href="https://github.com/Suhail-Kamal/ShopEasy-Marketing-Data-Analysis-SQL_Python_PowerBI/blob/main/Dashboard.pbix">PowerBI Dashboard</a>



### Dataset used
- <a href="https://github.com/Suhail-Kamal/ShopEasy-Marketing-Data-Analysis-SQL_Python_PowerBI/blob/main/PortfolioProject_MarketingAnalytics.bak">Dataset</a>

### Questions to focus on (KPIs) :

- **Reduced Customer Engagement:** The number of customer interactions and engagement with the site and marketing content has declined.
- **Decreased Conversion Rates:** Fewer site visitors are converting into paying customers.
- **High Marketing Expenses:** Significant investments in marketing campaigns are not yielding expected returns.
- **Need for Customer Feedback Analysis:** Understanding customer opinions about products and services is crucial for improving engagement and conversions.

### Tools Used

- SQL Server Express 2022 - Database engine that i used to Restore and attach the Marketing Data Analysis Backup Database file.
- SQL Server Management Studio - Tool that i used to interact with my SQL Server to run queries and manage database.
- VS Code - Used to do Sentimental Analysis Using Python (By using customer Reviews)
- PowerBI - Used to Create Dashboards.

### Process

- **Data cleaning :** includes Normalizing, Putting Average Values into NULL rows in the Duration Column, Clearing Whitespaces, Tag Duplicate Records using SQL Queries,Selecting Cleaned and Standardized data for the analysis

- **Sentiment Analysis Using Python:**
By determining the review text whether it is positive or negative and determiness what's the great of positivity or negativity in the texts,
Defining a function to categorize sentiment using both the sentiment score and the review rating,
Putting the score in a bucket categorises as Strongly Positive,Mildly Positive,Mildly Negative ,Strongly Negative.

- **Creating Dashboards Using PowerBI:** to find insights for the Business Problem

###  Data Analysis
Include some interesting code/features worked with
```sql
-- Common Table Expression (CTE) to identify and tag duplicate records
WITH DuplicateRecords AS (
SELECT
JourneyID,
CustomerID,
ProductID,
VisitDate,
Stage,
Action,
Duration,
-- Using ROW_NUMBER() to assign a unique row number to each record within the partition defined below
ROW_NUMBER() OVER (
PARTITION BY CustomerID, ProductID, VisitDate, Stage, Action
ORDER BY JourneyID
) AS row_num
FROM
dbo.customer_journey
)

-- Select all records from the CTE where row_num > 1, which indicates duplicate entries
SELECT *
FROM DuplicateRecords
WHERE row_num >1
ORDER BY JourneyID;

```
### Project Insights

- **Decreased Conversion Rates:** The conversion rate demonstrated a strong rebound in December, reaching 10.2%, despite a notable dip to 5.0% in October.
- **Reduced Customer Engagement:** There is a decline in overall social media engagement, with views dropping throughout the year.
While clicks and likes are low compared to views, the click-through rate    stands at 15.37%, meaning that engaged users are still interacting effectively.
- **Customer Feedback Analysis:**
Customer ratings have remained consistent, averaging around 3.7 throughout the year.
Although stable, the average rating is below the target of 4.0, suggesting a need for focused improvements in customer satisfaction, for products below 3.5.

### Project Insights Overview
![Overview](https://github.com/user-attachments/assets/e110b055-1ebe-4504-bcb1-47796a7b7800)

### Actions
- **Increase Conversion Rates:** Target High-Performing Product Categories: Focus marketing efforts on products with demonstrated high conversion rates, such as Kayaks, Ski Boots, and Baseball Gloves. Implement seasonal promotions or personalized campaigns during peak months (e.g., January and September) to capitalize on these trends.

- **Enhance** **Customer** **Engagement:** Revitalize Content Strategy: To turn around declining views and low interaction rates, experiment with more engaging content formats, such as interactive videos or user-generated content. Additionally, boost engagement by optimizing call-to-action placement in social media and blog content, particularly during historically lower-engagement months (September-December).

- **Improve** **Customer Feedback Scores:** Address Mixed and Negative Feedback: Implement a feedback loop where mixed and negative reviews are analyzed to identify common issues. Develop improvement plans to address these concerns. Consider following up with dissatisfied customers to resolve issues and encourage re-rating, aiming to move average ratings closer to the 4.0 target.






