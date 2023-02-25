import math
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import r2_score

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


n =50000
x_values = np.arange(1, n+1, dtype=np.int32)

y_values = np.array([phi(x) for x in x_values])

model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mse', optimizer='adam', metrics=['mse'])

model.fit(x_values, y_values, epochs=1, batch_size=32)
model.save('Totient.h5')
test_x = 8


test_y = model.predict([test_x])

print(test_y)
