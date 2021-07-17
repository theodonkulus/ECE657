# import required packages
import utils
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow import keras



# YOUR IMPLEMENTATION
# Thoroughly comment your code to make it easy to follow


if __name__ == "__main__": 
    verbose=True
    # 1. Load your saved model
    model = keras.models.load_model('models/NLP_model')

    # 2. Load your testing data
    try:
        print("attempting to find previously preproceed test set")
        test_data = pd.read_csv(os.path.join(os.getcwd(), 'data/test_NLP_Preproc.csv'))
        print("DATA FOUND YEEEE BOII")
        print(train_data)
    except IOError:
        raw_test_data = utils.load_NLP_data('data/aclImdb/test/', verbose=False)

        # Preprocess data - I gotchu boo
        test_data = utils.preprocess_NLP_data(raw_test_data, verbose=False)

        #Save preprocessed data to save time between runs/tuning (~2 min per run)
        test_data.to_csv(os.path.join(os.getcwd(), 'data/_test_NLP_Preproc.csv'))

    # 3. Run prediction on the test data and print the test accuracy
    score = model.evaluate(test_data, test_labels, batch_size=1, verbose=True)

    scores = []
    predictions = []
    # cycle through each test point to get loss at each point
    for ii in range(0, test_data.shape[0]):
        # reshape to maintain dimensionality
        dat = np.expand_dims(test_data[ii], 0)
        lab = np.expand_dims(np.asarray(test_labels[ii]), 0)
        # scores.append(model.evaluate(dat, lab, verbose=verbose))
        predictions.append(model.predict(dat, verbose=verbose))
        scores.append(predictions[ii]-lab)
    plt.figure()
    plt.subplot(211)
    plt.title('RNN Test Predictions')
    plt.plot(np.squeeze(predictions), label='predicitons')
    plt.plot(test_labels, label='ground truth')
    plt.legend()
    plt.subplot(212)
    plt.title('RNN Prediction Difference')
    plt.plot(np.squeeze(scores))
    plt.legend()
    plt.show()

    #TODO need to extract predictions and plot them against GT
    # probably should just use the predit instead of the evaluate function
