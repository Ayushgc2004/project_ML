from sklearn.preprocessing import LabelEncoder

# Sample data
gender = ['Male', 'Female', 'Female', 'Male', 'Male']

print("Original Gender Data:", gender)

# Create encoder
le = LabelEncoder()

# Fit and transform
encoded_gender = le.fit_transform(gender)

print("Encoded Gender Data:", encoded_gender)