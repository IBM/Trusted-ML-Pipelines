# Building a secure and transparent ML pipeline using open source technologies
The application of AI algorithms in domains such as criminal justice, credit scoring, and hiring holds unlimited promise. At the same time, it raises legitimate concerns about algorithmic fairness. There’s a growing demand for fairness, accountability, and transparency from ML systems. And we need to remember that training data isn’t the only source of possible bias and adversarial contamination. It can also be introduced through inappropriate data handling, inappropriate model selection, or incorrect algorithm design. We need a pipeline that’s open, transparent, secure, and fair, and that fully integrates into the AI lifecycle. Such a pipeline requires a robust set of bias and adversarial checkers, debiasing and defense algorithms, and explanations.

Animesh Singh, Svetlana Levitan, and Tommy Li demonstrate how to build an ML pipeline that’s open, secure, and fair and that fully integrates into the AI lifecycle, using open source tools like AIF360, ART, Model Asset Exchange (MAX).

## Get Started 
- Sign up for free IBM Cloud account: http://ibm.biz/oscon2019
- Watson Studio:  https://dataplatform.cloud.ibm.com/


## Instructions
### 1. Create a Jupyter notebook on Watson Studio or on the local machine
To start with this tutorial, we need to first get an instant of Jupyter notebook running either on the Cloud using Watson Studio or on the local machine. To set it up on Watson Studio, go to https://github.com/IBM/pytorch-on-watson-studio to follow all the steps to learn about how to create a Notebook on Watson Studio and use it to train and test a MNIST PyTorch Model

### 2. Run the ART, AIF360, ML Pipeline Notebook
We will be going over the following three Jupyter notebooks. The first two notebooks will 
go over the concept behind ART and AIF360. Then the last notebook will create a Machine Learning Pipeline using 
KubeFlow Pipeline to leveage the concepts we learned from the previous two notebooks as a end to end pipeline scenario. 

#### 2.1. ART MNIST Adversarial training
[This notebook](notebooks/adversarial-training-mnist.ipynb) will use an attack method called fast gradent attack to generate adversarial samples. Then go over the 
concept of Adversarial training and showcase how this kind of training can better presist the attack from the adversarial samples.

If you are loading this notebook using Watson Studio, you can load it with the below URL link.
```shell
https://raw.githubusercontent.com/IBM/ML-Pipelines-101/master/notebooks/adversarial-training-mnist.ipynb
```

#### 2.2. AIF360 Gender Classification
[This notebook](notebooks/tutorial_gender_classification.ipynb) will train a Gender Classification using PyTorch. Then it will showcase how AIF360 can detect the bias
from the dataset and mitigate the dataset using a preprocessing reweighting algorithm.

If you are loading this notebook using Watson Studio, you can load it with the below URL link.
```shell
https://raw.githubusercontent.com/IBM/ML-Pipelines-101/master/notebooks/tutorial_gender_classification.ipynb
```

#### 2.3. End to End ML Pipeline with Gender Classification
In [this notebook](notebooks/ml-pipeline.ipynb) we will create a ML Pipeline that trains the PyTorch Gender Classification, the apply the fast gradent attack
and AIF360 bias detection to generate metrics on this model's robustness and fairness. Then finally it will deploy the model 
using KFServing which leveages KNative in the background to serve the models in a serverless environment.

If you are loading this notebook using Watson Studio, you can load it with the below URL link.
```shell
https://raw.githubusercontent.com/IBM/ML-Pipelines-101/master/notebooks/ml-pipeline.ipynb
```

