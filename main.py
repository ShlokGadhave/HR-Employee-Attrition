import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
df=pd.read_csv('Customer Churn.csv')
print(df)
df.head()
df.info()
# Replacing blanks with zero as the tenure is zero 
df['TotalCharges']=df['TotalCharges'].replace(' ','0') 
df['TotalCharges']=df['TotalCharges'].astype(float) #convertng data type 
df.info()
print(df.isnull().sum())
print(df.describe())
print(df['customerID'].duplicated().sum())

# Conversion of values of senior citizen to Yes and No 
def conv(value):
    if value==1:
        return 'Yes'
    else:
        return 'No'
df['SeniorCitizen']=df['SeniorCitizen'].apply(conv)
print(df.head(30))
# Churn Visualization
count=sns.countplot(x=df['Churn'])
count.bar_label(count.containers[0])
plt.title('Count of customers by churn')
plt.show()
plt.figure(figsize=(3,4))
gp=df.groupby('Churn').agg({'Churn':'count'})
print(gp)
ar=plt.pie(gp['Churn'],labels=gp.index,autopct="%1.2f%%")
plt.title("Percentage of churn customers")
plt.show()
# From the given pie chart it clear that total 26.51% of customers have churned out 

#Percentage of Churn based on Gender 
plt.figure(figsize=(4,4))
kr=sns.countplot(x=df['gender'],data=df,hue='Churn')
kr.bar_label(kr.containers[0])
plt.title('Churn By Gender')
plt.show()

# Percentage of Churn based on senior citizen 
plt.figure(figsize=(4,4))
kr = sns.countplot(x=df['SeniorCitizen'], data=df, hue='Churn')
# percentage labels
total = len(df)
for container in kr.containers:
    labels = [f'{(v.get_height()/total)*100:.1f}%' for v in container]
    kr.bar_label(container, labels=labels)
plt.title('Churn By Senior Citizen')
plt.show()

#Churn using Tenure 
plt.figure(figsize=(9,4))
sns.histplot(x=df['tenure'],data=df,bins=50,hue='Churn')
plt.title('Churn By Tenure ')
plt.show()

# People who had used our services for longer period time had stayed 
# whereas people who had recently joined the services are leftout 

#Churn Analysis using contract of the person 

sns.countplot(x=df['Contract'],data=df,hue='Churn')
plt.title('Count of Customers based on the contracts')
plt.show()

#It is seen that persons with one month contract are larger as compared to person with one to two years of contract 

# SubPlots of Following Category 

columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 
           'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

# Number of columns for the subplot grid (you can change this)
n_cols = 3
n_rows = (len(columns) + n_cols - 1) // n_cols  # Calculate number of rows needed

# Create subplots
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 4))  # Adjust figsize as needed

# Flatten the axes array for easy iteration (handles both 1D and 2D arrays)
axes = axes.flatten()

# Iterate over columns and plot count plots
for i, col in enumerate(columns):
    sns.countplot(x=col, data=df, ax=axes[i], hue = df["Churn"])
    axes[i].set_title(f'Count Plot of {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')

# Remove empty subplots (if any)
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

# The majority of customers who do not churn tend to have services like PhoneService, InternetService (particularly DSL), and OnlineSecurity enabled. For services like OnlineBackup, TechSupport, and StreamingTV, churn rates are noticeably higher when these services are not used or are unavailable.

plt.figure(figsize=(5,4))
ax=sns.countplot(x='PaymentMethod',data=df,hue='Churn')
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title('Count of Payment Method Used')
plt.show()