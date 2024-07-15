import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Read the CSV file
    csv_path = "Hospital Patient Records/hospital.csv"
    df = pd.read_csv(csv_path)
    
    # Print the first few rows of the DataFrame and column names
    print("Columns in the dataset:", df.columns)
    print(df)
    
    # Visualizations
    
    # Bar chart of counts by gender
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Gender', data=df)
    plt.title('Distribution of Patients by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.show()
    
    # Box plot of bill amounts by gender
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Gender', y='Bill Amount', data=df)
    plt.title('Bill Amount Distribution by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Bill Amount')
    plt.show()
    
    # Bar chart of medical conditions by gender
    plt.figure(figsize=(12, 8))
    sns.countplot(x='Date of Birth', hue='Gender', data=df)
    plt.title('Number of Patients per Medical Condition by Gender')
    plt.xlabel('Medical Condition')
    plt.ylabel('Count')
    plt.legend(title='Gender')
    plt.show()


main()
