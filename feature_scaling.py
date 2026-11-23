# Standard Scaler
import numpy as np
from sklearn.preprocessing import StandardScaler

X = np.array([[25, 30000],
              [30, 32000],
              [45, 70000],
              [50, 90000]])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(X_scaled.round(2))
# [[-0.98 -0.74]
#  [-0.39 -0.67]
#  [ 1.37  1.41]]

print(scaler.mean_)   # [   33.33 50666.67]
print(scaler.scale_)  # [    8.5  27885.  ]  (std used for scaling)

# Min-Max Scaler
# import numpy as np
# from sklearn.preprocessing import MinMaxScaler

# X = np.array([[25, 30000],
#               [30, 32000],
#               [45, 70000],
#               [50, 90000]])

# scaler = MinMaxScaler()              # default feature_range=(0, 1)
# X_scaled = scaler.fit_transform(X)

# print(X_scaled.round(3))
# # [[0.    0.   ]
# #  [0.25  0.033]
# #  [1.    1.   ]]

# # Custom range, e.g. -1 to 1
# scaler = MinMaxScaler(feature_range=(-1, 1))