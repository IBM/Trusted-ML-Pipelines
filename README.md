# Building a secure and transparent ML pipeline using open source technologies
The application of AI algorithms in domains such as criminal justice, credit scoring, and hiring holds unlimited promise. At the same time, it raises legitimate concerns about algorithmic fairness. There’s a growing demand for fairness, accountability, and transparency from ML systems. And we need to remember that training data isn’t the only source of possible bias and adversarial contamination. It can also be introduced through inappropriate data handling, inappropriate model selection, or incorrect algorithm design. We need a pipeline that’s open, transparent, secure, and fair, and that fully integrates into the AI lifecycle. Such a pipeline requires a robust set of bias and adversarial checkers, debiasing and defense algorithms, and explanations.

Animesh Singh, Svetlana Levitan, and Tommy Li demonstrate how to build an ML pipeline that’s open, secure, and fair and that fully integrates into the AI lifecycle, using open source tools like AIF360, ART, Model Asset Exchange (MAX).

## Get Started 
- Sign up for free IBM Cloud account: http://ibm.biz/oscon2019
- Watson Studio:  https://dataplatform.cloud.ibm.com/


## Instructions
### 1. Create a Jupyter notebook on Watson Studio or on the local machine
To start with this tutorial, we need to first get an instance of Jupyter notebook running either on the Cloud using Watson Studio or on the local machine. 

* To set it up on Watson Studio, visit the [Watson Studio tutorial](https://github.com/IBM/pytorch-on-watson-studio) and follow all the steps to learn about how to create a Notebook on Watson Studio and use it to train with the MNIST PyTorch Model.

* To run it on local Machine, clone this repository and start a local Jupyter Server.
```shell
git clone https://github.com/IBM/ML-Pipelines-101.git
cd ML-Pipelines-101
pip install -r requirements.txt
jupyter notebook
```

### 2. Run the ART, AIF360, ML Pipeline Notebook
We will be going over the following three Jupyter notebooks. The first two notebooks will 
go over the concepts behind Adversarial Robustness Toolbox (ART) and AI Fairness 360 (AIF360). Then the last notebook will create a Machine Learning Pipeline using the open source project,
KubeFlow Pipeline, to leverage the concepts we learned from the previous two notebooks as an end to end pipeline scenario. 

#### 2.1. ART: MNIST Adversarial training
[This notebook](notebooks/adversarial-training-mnist.ipynb) will use an attack method called fast gradient attack to generate adversarial samples. Then go over some 
concepts of Adversarial training and showcase how this kind of training can better persist attacks from adversarial samples.

If you are using Watson Studio, you can load this notebook with the below URL link.
```shell
https://raw.githubusercontent.com/IBM/ML-Pipelines-101/master/notebooks/adversarial-training-mnist.ipynb
```

#### 2.2. AIF360: Gender Classification
[This notebook](notebooks/tutorial_gender_classification.ipynb) will train a Gender Classification model using PyTorch. Then it will showcase how AIF360 can detect the bias
from the dataset and mitigate the dataset using a preprocessing algorithm called reweighting.

If you are using Watson Studio, you can load this notebook with the below URL link.
```shell
https://raw.githubusercontent.com/IBM/ML-Pipelines-101/master/notebooks/tutorial_gender_classification.ipynb
```

#### 2.3. End to End ML Pipeline with Gender Classification
In [this notebook](notebooks/ml-pipeline.ipynb) we will create an End to End Machine Learning Pipeline that preprocesses the data and trains the PyTorch Gender Classification model. Then, it applies the fast gradient attack
and AIF360 bias detection that generate metrics for this model to evaluate its robustness and fairness. Finally, it deploys the model 
using KFServing which leverages KNative in the background to serve models in a serverless environment.

If you are using Watson Studio, you can load this notebook with the below URL link.
```shell
https://raw.githubusercontent.com/IBM/ML-Pipelines-101/master/notebooks/ml-pipeline.ipynb
```


## Learn more

- **Adversarial Robustness Toolbox**: https://github.com/IBM/adversarial-robustness-toolbox
- **AI Fairness 360**: https://github.com/IBM/AIF360
- **Model Asset Exchange**: https://developer.ibm.com/exchanges/models/
- **KNative**: https://github.com/knative
- **KubeFlow**: https://github.com/kubeflow
