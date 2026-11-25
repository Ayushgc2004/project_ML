import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D'],
    'City': ['Pune', 'Mumbai', 'Pune', 'Delhi'],
    'Age': [22, 25, 23, 24]
})

le = LabelEncoder()

df['City_encoded'] = le.fit_transform(df['City'])

print(df)