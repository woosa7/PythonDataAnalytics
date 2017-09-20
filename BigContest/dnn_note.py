# ----------------------------------------------------------------------------
def predict_with_network(input_data):
    # Calculate node 0 in the first hidden layer
    node_0_0_input = (input_data * weights['node_0_0']).sum()
    node_0_0_output = relu(node_0_0_input)

    # Calculate node 1 in the first hidden layer
    node_0_1_input = (input_data * weights['node_0_1']).sum()
    node_0_1_output = relu(node_0_1_input)

    # Put node values into array: hidden_0_outputs
    hidden_0_outputs = np.array([node_0_0_output, node_0_1_output])

    # Calculate node 0 in the second hidden layer
    node_1_0_input = (hidden_0_outputs * weights['node_1_0']).sum()
    node_1_0_output = relu(node_1_0_input)

    # Calculate node 1 in the second hidden layer
    node_1_1_input = (hidden_0_outputs * weights['node_1_1']).sum()
    node_1_1_output = relu(node_1_1_input)

    # Put node values into array: hidden_1_outputs
    hidden_1_outputs = np.array([node_1_0_output, node_1_1_output])

    # Calculate model output: model_output
    model_output = (hidden_1_outputs * weights['output']).sum()

    # Return model_output
    return(model_output)

output = predict_with_network(input_data)
print(output)

# ----------------------------------------------------------------------------
from keras.utils import to_categorical

# Convert the target to categorical: target
target = to_categorical(df.survived)

model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(n_cols,)))
model.add(Dense(2, activation='softmax'))
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(predictors, target)
predictions = model.predict(pred_data)
# Calculate predicted probability of survival: predicted_prob_true
predicted_prob_true = predictions[:,1]

# ----------------------------------------------
from keras.optimizers import SGD
my_optimizer = SGD(lr=lr)
model.compile(optimizer=my_optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(predictors, target, validation_split=0.3)

# ----------------------------------------------
# Early stopping: Optimizing the optimization
from keras.callbacks import EarlyStopping
# Stop optimization when the validation loss hasn't improved for 2 epochs
early_stopping_monitor = EarlyStopping(patience=2)
model.fit(predictors, target, epochs=30, validation_split=0.3, callbacks=[early_stopping_monitor])

# ----------------------------------------------
model_2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model_1_training = model_1.fit(predictors, target, epochs=15, validation_split=0.2, callbacks=[early_stopping_monitor], verbose=False)
model_2_training = model_2.fit(predictors, target, epochs=15, validation_split=0.2, callbacks=[early_stopping_monitor], verbose=False)

plt.plot(model_1_training.history['val_loss'], 'r', model_2_training.history['val_loss'], 'b')
plt.xlabel('Epochs')
plt.ylabel('loss')
plt.show()



# ----------------------------------------------------------------------------
