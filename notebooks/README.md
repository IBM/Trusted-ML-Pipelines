# ML Pipelines Notebooks

In this tutorial we will be going over the following three Jupyter notebooks. The first two notebooks will 
go over the concept behind ART and AIF360. Then the last notebook will create a Machine Learning Pipeline using 
KubeFlow Pipeline to leveage the concepts we learned from the previous two notebooks as a end to end pipeline scenario. 

## 1. ART MNIST Adversarial training
`TODO`: This notebook will use an attack method called fast gradent attack to generate adversarial samples. Then go over the 
concept of Adversarial training and showcase how this kind of training can better presist the attack from the adversarial samples.

## 2. AIF360 Gender Classification
`TODO`: This notebook will train a Gender Classification using PyTorch. Then it will showcase how AIF360 can detect the bias
from the dataset and mitigate the dataset using a preprocessing reweighting algorithm.

## 3. End to End ML Pipeline with Gender Classification
`TODO`: In this notebook we will create a ML Pipeline that trains the PyTorch Gender Classification, the apply the fast gradent attack
and AIF360 bias detection to generate metrics on this model's robustness and fairness. Then finally it will deploy the model 
using KFServing which leveages KNative in the background to serve the models in a serverless environment.
