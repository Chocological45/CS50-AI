# Traffic

## Experiment Description

Prototyping a convolutional neural network to classify road signs from still images.


## Experiment Aims

The aim of the experiment is to prototype a convolutional neural network (C-NN) with optimal performance (maximized accuracy and minimized loss).

## Method
### Initial Model
Initial network model consisted of the following structure, based on the model provided in the lecture source code:

- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 2x2 pool size
- 1 hidden layer of 128 nodes, utilising ReLU
- Dropout layer with value of 0.5
- Output layer using NUM_CATEGORIES as units and utilising Softmax


### Model Variation 1
- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 3x3 pool size
- 1 hidden layer of 128 nodes, utilising ReLU
- Dropout layer with value of 0.5
- Output layer using NUM_CATEGORIES as units and utilising Softmax


Expected result: The model performance will degrade

### Model Variation 2
- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 2x2 pool size
- 1 hidden layer of 128 nodes, utilising ReLU
- Dropout layer with value of 0.2
- Output layer using NUM_CATEGORIES as units and utilising Softmax

Expected result: The model performance will degrade

### Model Variation 3

- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 2x2 pool size
- 1 hidden layer of 128 nodes, utilising ReLU
- Dropout layer with value of 0.8
- Output layer using NUM_CATEGORIES as units and utilising Softmax

Expected result: The model performance may improve

### Model Variation 4

- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 2x2 pool size
- 1 additional convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 hidden layer of 128 nodes, utilising ReLU
- Dropout layer with value of 0.8
- Output layer using NUM_CATEGORIES as units and utilising Softmax

Expected result: No effect on performance of model

### Model Variation 5

- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 2x2 pool size
- 1 additional convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 hidden layer of 128 nodes, utilising ReLU
- 1 hidden layer of 64 nodes, utilising ReLU
- Dropout layer with value of 0.8
- Output layer using NUM_CATEGORIES as units and utilising Softmax

Expected result: Further increase in time taken. Will increase performance significantly

### Model Variation 6

- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 2x2 pool size
- 1 hidden layer of 128 nodes, utilising ReLU
- 1 hidden layer of 64 nodes, utilising ReLU
- Dropout layer with value of 0.8
- Output layer using NUM_CATEGORIES as units and utilising Softmax

Expected result: Possible improvement to the model performance

### Model Variation 7

- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 2x2 pool size
- 1 additional convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 additional max-pooling layer with a 2x2 pool size
- 1 hidden layer of 128 nodes, utilising ReLU
- Dropout layer with value of 0.5
- Output layer using NUM_CATEGORIES as units and utilising Softmax

Expected result: Definite improvement to the model performance

### Model Variation 8

- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 2x2 pool size
- 1 additional convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 additional max-pooling layer with a 2x2 pool size
- 1 hidden layer of NUM_CATEGORIES * 32 nodes, utilising ReLU
- Dropout layer with value of 0.5
- 1 hidden layer of NUM_CATEGORIES * 16 nodes, utilising ReLU
- 1 hidden layer of NUM_CATEGORIES * 8 nodes, utilising ReLU
- 1 hidden layer of NUM_CATEGORIES * 4 nodes, utilising ReLU
- 1 hidden layer of NUM_CATEGORIES * 2 nodes, utilising ReLU
- Output layer using NUM_CATEGORIES as units and utilising Softmax

Expected result: Slight increase in performance of model

### Model Variation 9

- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 2x2 pool size
- Dropout layer following flatten operation with value of 0.2
- 1 hidden layer of NUM_CATEGORIES * 32 nodes, utilising ReLU
- Dropout layer with value of 0.5
- 1 hidden layer of NUM_CATEGORIES * 16 nodes, utilising ReLU
- 1 hidden layer of NUM_CATEGORIES * 8 nodes, utilising ReLU
- Output layer using NUM_CATEGORIES as units and utilising Softmax

Expected result: Degraded performance from previous model

### Model Variation 10

- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 2x2 pool size
- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 2x2 pool size
- 1 hidden layer of 128 nodes, utilising ReLU
- Dropout layer with value of 0.5
- Output layer using NUM_CATEGORIES as units and utilising Softmax

Expected Result: The optimal performance from all tests so far

### Model Variation 11

- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 2x2 pool size
- 1 convolutional layer, learning 32 filters using a 3x3 kernel utilising ReLU
- 1 max-pooling layer with a 2x2 pool size
- 1 hidden layer of 256 nodes, utilising ReLU
- Dropout layer with value of 0.5
- Output layer using NUM_CATEGORIES as units and utilising Softmax

Expected Result: The optimal performance from all tests so far


## Results

| Model Variation # | Changes Made                                                                     | Loss   | Accuracy |
| ----------------- | -------------------------------------------------------------------------------- | -----: | -------: |
| 0                 | N/A                                                                              | 3.4930 | 0.0566   |
| 1                 | Max-pooling layer was changed to 3x3                                             | 3.4898 | 0.0560   |
| 2                 | Reduced dropout value to 0.2                                                     | 3.5024 | 0.0534   |
| 3                 | Increased dropout value to 0.8                                                   | 3.4994 | 0.0577   |
| 4                 | Added an additional convolutional layer                                          | 0.5262 | 0.8516   |
| 5                 | Added an additional hidden layer with 64 nodes                                   | 3.5020 | 0.0545   |
| 6                 | Removed second convolutional layer                                               | 3.5013 | 0.0554   |
| 7                 | Removed additional hidden layer. Added second conv layer with max-pooling 2x2    | 0.1652 | 0.9622   |
| 8                 | Additional hidden layers in combination with model 7                             | 0.1688 | 0.9570   |
| 9                 | Removal of 2nd conv layer, last two hidden layers. Addition of dropout layer     | 0.2489 | 0.9361   |
| 10                | Model 7 but with 128 node hidden layer                                           | 0.1179 | 0.9674   |
| 11                | Model 10 but with 256 nodes in hidden layer                                      | 0.1684 | 0.9566   |

## Results Analysis

The first four changes made the model took little to no effect on the performance of the model.
Changes made to the Max-Pooling layer degraded performance while increased dropout values led to minor increase in performance though this was shown to be an outlier as later tests showed that a dropout value of 0.5 produced better results.
Learning times for each epoch increased by approximately 10~30s with the addition of a second convolutional layer however it did improve the results significantly though at the cost of time.
The addition of a second hidden layer further increased learning times however degraded performance drastically.
Use of the second hidden layer without the second convolutional layer also produced degraded results though reduced time taken more so than with the second convolutional layer alone.

Reverting to a model using 2 convolutional layers, each followed by a 2x2 max-pooling layer with a single 128 node hidden layer provided greatly improved results to previous variations.
Variation 8 made use of a more complex model and provided a slightly degraded performance.
Removing a convolutional layer, last two hidden layers and adding a dropout layer after the flatten operation led to decent results though a decrease in performance and drastic increase in time taken to learn.


## Conclusion

Following the experiment the results clearly show that the addition of more layers greatly increases the performance of the C-NN model.
The additional convolutional layer increases the overall performance of the C-NN model and as shown by the results gathered, the optimal variation from those that were tested was variation 10.
This model made use of a second convolutional layer with 2x2 max-pooling. This model had the lowest loss value and highest accuracy value thus it is plausible that further convolutional layers may further increase the performance of the model.
This particular model variation also had much lower learning time than other high performing models.
This being said, increasing the number of hidden layers and nodes can also improve the performance of the C-NN model and is a valid way to do so, generally providing accuracies of above 0.9.




