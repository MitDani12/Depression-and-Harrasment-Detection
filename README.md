# Depression-and-Harrasment-Detection
## Introduction
Internet is considered as a major storehouse of information in today’s world. No single work can be done without help. It has become one of the major ways of communication. Out of all communication methods available, Social Media is one of the most common forms. Social media has changed the world. The number of internet users worldwide in 2019 is 4.388 billion, up 9.1% year-on-year. The number of social media users worldwide in 2019 is 3.484 billion, up 9% year-on-year. Social media has been blamed for promoting social ills. People have a need to fit in to be visible praised in this new digital world. Social Media has many ill effects such as Cyber-bullying, Harassment and Depression. Evidence is mounting that there is a link between social media and depression. It is an almost undisputable truth that access to a cloak of anonymity and a large, large microphone brings the worst out in some people. Today, this is particularly true on social media. Online harassment and hate- messaging is a growing trend and a growing security concern for anyone on social media today. In fact, 40% of Internet users say they have personally experienced online harassment. Researchers have found that the longer you spend on social media, the more likely you are to be depressed. Hence we have come up with this project in which we will be developing a system that helps in detecting a depressive and harassment text. The user of this system will not have to login or do any registration. The user simply has to put the textual post in the form and submit. On submitting the post the system will detect whether the post is depressive or harassment or neither.
## Objective
The proposed system aims at providing automation for detecting depression and harassment on social media platforms. The system will assist the authorities with certain features added in tackling the problem of depression and harassment that is going on in social media through alerts.
## Problem Statement
Due to lack of proper systems for detecting depression and harassment, people nowadays are harassed on social media. People expression depression are also not identified and hence they get lonelier and worse. The prime impediment of implementing a Depression and Harassment Detection on Social Media System is the social and psychological help of the individuals themselves.
##  Methodology
### Naive bayes classifier
Naïve bayes classifiers are highly used for text based classification. It is a probabilistic learning model that applies bayes theorem.
The dataset is first subjected to pre-processing stage.Pre-processing consist of following steps:
1.	Tokenization: This process splits the given text into relevant tokens like characters, words, phrases etc Here word –level tokenization is used.
2.	Bag-of-words: BoW counts the number of times a particular token appears in the given text. To achieve this a class called Count Vectorizer from scikit-learn is used.
### Artificial Neural Network(ANN)
An artificial neuron network (ANN) is a computational model based on biological neural network architecture and functions. ANNs are known to be nonlinear statistical data analysis methods where modeling or patterns are found for the complex relationships between inputs and outputs
We created a multi-layer neural network with two hidden layers ,’relu’ activation function and adam optimizer. The model was trained on depression dataset for 50 epochs with a batch size of 10. After 50 epochs model gave 96.5% accuracy
### Long Short Term Memory(LSTM)
Recurrent Neural Networks (RNN) is a neural network that takes inputs from previous steps and uses the next step as an output. Building blocks for the layers of a recurrent neural network (RNN) are long-term memory (LSTM) modules.
Traditional neural networks are unable to remember past tests and documents. This problem is solved by LSTM. In addition to the current input, it uses previous outputs to make better decisions. The LSTM unit is equipped with a cell, an input gate, an output gate and a gate. To order to make more rational choices, the cell remembers information over large intervals. Bidirectional LSTMs are traditional LSTM 
extensions that train two in the input sequence instead of one LSTM.

###Conclusion
Thus we have implemented naïve Bayes classifier and artificial neural network and LSTM over our depression and harassment dataset. Compared to ANN, naïve Bayes are simple to implement. For large dataset like the one we used performance of naive Bayes tends to plateau after a certain point thus the highest accuracy obtained for naive Bayes is approximately 93%.In contrast, ANN because of its complex nature tend to  learn from huge datasets and its performance improves. Thus ANN provides us an accuracy of approximately 96%. Furthermore, simplicity of naïve Bayes prevents it from overfitting whereas ANN because of its complex architecture if trained  unnecessary for large time can lead to overfitting.
Deep learning models like LSTM’s are best suited for text classification and they provide high accuracy of approximately 98% among all three model.