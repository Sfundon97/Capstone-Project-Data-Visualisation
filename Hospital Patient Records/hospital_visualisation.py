import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Read the CSV file
    df = pd.read_csv("Hospital Patient Records/hospital.csv")
    

    print(df)
    
    
    
    # Visualizations
    
    # Bar chart of counts by gender
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Gender', data=df)
    plt.title('Distribution of Patients by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.show()
    
    # Pie chart of total bill amounts by gender
    plt.figure(figsize=(8, 8))
    bill_amounts_by_gender = df.groupby('Gender')['Bill Amount'].sum()
    bill_amounts_by_gender.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#99ff99'])
    plt.title('Total Bill Amounts by Gender')
    plt.ylabel('')  # Hide the y-label
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
    plt.title(f'Number of Patients per Medical Condition by Gender (Top {top_n})')
    plt.xlabel('Count')
    plt.ylabel('Medical Condition')
    plt.legend(title='Gender')
    plt.show()


main()
