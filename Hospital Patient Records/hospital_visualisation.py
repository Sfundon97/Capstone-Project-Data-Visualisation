import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Read the CSV file
    df = pd.read_csv("Hospital Patient Records/hospital.csv")
    print('Dataframe Contents')
    print('==================================================================')
    print(df)
    print('------------------------------------------------------------------')
    print()
    print('Summary of the DataFrame, including the number of non-null records and data types')
    print('==================================================================')
    print(df.info())
    print('------------------------------------------------------------------')
    print()
    print('Summary statistics (like count, mean, min, max, etc.)')
    print('==================================================================')
    print(df.describe())
    print('------------------------------------------------------------------')
    print()
    print('The Number of Missing Data represented by 1 = True and 0 = False:')
    print('=================================================================')
    print(df.isnull().sum())
    print('------------------------------------------------------------------')

  
    # Bar chart of counts by gender
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Gender', data=df)
    plt.title('Distribution of Patients by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Patient Count')
    plt.show()
    
    # Pie chart of total bill amounts by gender
    plt.figure(figsize=(8, 8))
    bill_amounts_by_gender = df.groupby('Gender')['Bill Amount'].sum()
    bill_amounts_by_gender.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['Blue', 'Purple'])
    plt.title('Total Bill Amounts by Gender')
    plt.legend(title='Gender')
    plt.ylabel('')
    plt.show()

    # Number of top medical conditions to display
    top_n = 10
    
    # Get the top N medical conditions
    top_conditions = df['Medical Condition'].value_counts().nlargest(top_n).index
    
    # Filter the dataframe to include only the top N medical conditions
    top_df = df[df['Medical Condition'].isin(top_conditions)]
    
    # Bar chart of top N medical conditions by gender
    plt.figure(figsize=(14, 10))
    sns.countplot(y='Medical Condition', hue='Gender', data=top_df, order=top_conditions)
    plt.title(f'Patients per Medical Condition by Gender (Top {top_n})')
    plt.xlabel('Medical Condition Count')
    plt.ylabel('Medical Condition')
    plt.legend(title='Gender')
    plt.show()

    # Histogram of bill amounts
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Bill Amount'], kde=True)
    plt.title('Distribution of Bill Amounts')
    plt.xlabel('Bill Amount')
    plt.ylabel('Frequency')
    plt.show()

    median_amount = df['Bill Amount'].median(axis=0)
    mode_gender = df['Gender'].mode()
    print('Median Bill: ', median_amount)
    print('Gender that falls sick the most:', mode_gender)
    print('------------------------------------------------------------------')
    print()


main()
