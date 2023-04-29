import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# BASADO EN CORRELACION

# Compute the correlation matrix
corr = iris.corr()

# Plot the correlation matrix
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

# Perform feature selection based on correlation
threshold = 0.5
corr_features = set()
for i in range(len(corr.columns)):
    for j in range(i):
        if abs(corr.iloc[i, j]) > threshold:
            corr_features.add(corr.columns[i])

print('Selected features:', list(corr_features))   #['petal_length', 'petal_width']

# Create a new dataframe with the selected features
selected_features_df = iris[list(corr_features)]

# Display the new dataframe
print('\nNew dataframe with selected features:')  
print(selected_features_df.head())  


# CHI CUADRADA
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# Separate features and target variable
X = iris.iloc[:, :-1]  # features
y = iris.iloc[:, -1]   # target variable

# Apply chi-squared feature selection
k = 3  # number of top features to select
selector = SelectKBest(chi2, k=k)
selector.fit(X, y)

# Get the selected features
selected_features = X.columns[selector.get_support()]

print('Selected features:', list(selected_features)) #['sepal_length', 'petal_length', 'petal_width']

 # BACKWARD ELIMINATION
from sklearn.feature_selection import f_regression
from sklearn.linear_model import LinearRegression

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing = pd.read_csv(url, sep='\s+', header=None)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Compute the correlation matrix
corr2 = housing.corr()

# Plot the correlation matrix
sns.set (rc = {'figure.figsize':(9, 8)}, font_scale=0.5)
sns.heatmap(corr2, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Perform backward feature elimination
n_features = 3  # number of features to select
estimator = LinearRegression()
selected_features = set(X.columns)

while len(selected_features) > n_features:
    worst_score = float('inf')
    worst_feature = None
    
    for feature in selected_features:
        selected_features.remove(feature)
        X_selected = X[list(selected_features)]
        scores, _ = f_regression(X_selected, y)
        score = scores.mean()
        
        if score < worst_score:
            worst_score = score
            worst_feature = feature
                
        selected_features.add(feature)
            
    selected_features.remove(worst_feature)

print('Selected features:', list(selected_features)) #['CHAS', 'B', 'DIS']