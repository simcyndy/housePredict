import numpy as np

num_houses = 50

np.random.seed(0)
sizes = np.random.randint(low=1000, high=3500, size=num_houses)

prices = sizes * 200 + np.random.randint(low=20000, high=70000, size=num_houses)

# for i in range(5):
#     print(f"House {i+1} - Size : {sizes[i]}'sq ft, Price: ${prices[i]}")

import matplotlib.pyplot as plt
# plt.scatter(sizes, prices)
# plt.xlabel('House Size(sq ft)')
# plt.ylabel('Price ($)')
# plt.title('House prices based on Price')
# plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Reshape data since skleran expects 2D array
sizes = sizes.reshape(-1,1)
prices = prices.reshape(-1, 1)

# Split data into training and test set
sizes_train, sizes_test, prices_train, prices_test = train_test_split(sizes, prices, test_size=0.2, random_state=0)

model = LinearRegression()

# Train model using training data
model.fit(sizes_train, prices_train)

# Predict house price with test datat
prices_pred = model.predict(sizes_test)

# Print predicted and actual prices for the first 5 houses in the test set
for i in range(5):
    print(f"House {i+1} - Actual price: ${prices_test[i][0]}, Predicted price: ${prices_pred[i][0]}")

plt.scatter(sizes_train, prices_train, color='blue', label='Actual Price')  # Plot actual prices for the training set
plt.plot(sizes_train, model.predict(sizes_train), color='red', label='Predicted Price')  # Plot predicted prices for the training set
plt.xlabel('Size (sq ft)')
plt.ylabel('Price ($)')
plt.title('Actual vs Predicted Prices (Training Set)')
plt.legend()
plt.show()
