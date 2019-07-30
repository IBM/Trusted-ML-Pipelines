# Introduction to deep learning with Watson Studio


Svetlana Levitan and David Nichols will provide an introduction to neural networks, convolutional and recurrent networks, model deployment strategies, AI Fairness 360 and Adversarial Robustness Toolbox, Model Asset Exchange.

Key Open Source Projects Used:

* Keras: keras.io
* PMML:  dmg.org/pmml
* ONNX:  onnx.ai
* AI Fairness 360: https://github.com/IBM/AIF360
* Adversarial Robustness Toolbox: https://github.com/IBM/adversarial-robustness-toolbox
* Model Asset Exchange: https://developer.ibm.com/exchanges/models/

## Get Started 
If you have a notebook server (e.g. from Anaconda3), you can run notebooks locally for convolutional networks, AIF360 and ART. For running the R scripts, you will need R Studio. Or you can run all that and a flow editor in Watson Studio, that requires a free IBM Cloud account.

- Sign up for free IBM Cloud account: http://ibm.biz/Bd2whP
- Watson Studio:  https://dataplatform.cloud.ibm.com/


To create a project in Watson Studio:

Click New project on the Watson Studio home page or your My Projects page.
Choose a Deep Learning project type, that will automatically create Cloud Object Storage and Watson Machine Learning services for the project.
On the New project screen, add a name and optional description for the project.
Select the Restrict who can be a collaborator check box to restrict collaborators to members of your organization or integrate with a catalog. The check box is selected by default if you are a member of a catalog. You can’t change this setting after you create the project.

Click Create. You can start adding resources. 
Go to Assets tab


### 1. Create a Jupyter notebook on Watson Studio or on the local machine.
To start with this tutorial, we need to first get an instance of Jupyter notebook running either on the Cloud using Watson Studio or on the local machine. 



* To run it on local Machine, clone this repository and start a local Jupyter Server.
```shell
git clone https://github.com/IBM/Trusted-ML-Pipelines.git
cd Trusted-ML-Pipelines
pip install -r requirements.txt
jupyter notebook
```

### 2. Run Keras, AIF360, ART
We suggest going over the following Jupyter notebooks. The first notebook will 
go over a small deep learning model in Keras, the others explore concepts behind Adversarial 
Robustness Toolbox (ART) and AI Fairness 360 (AIF360). 

If you are using Watson Studio, we recommend to use runtime `Default Python 3.6 S (4 vCPU and 16 GB RAM)`.

#### 2.1. A Keras model for MNIST handwritten digit classification.
Use the notebook 
https://github.com/IBM/Trusted-ML-Pipelines/blob/master/conf/JSM2019/notebooks/MNIST%20Keras%20CNN%20Example.ipynb


#### 2.2. ART: MNIST Adversarial training
[This notebook](notebooks/adversarial-training-mnist.ipynb) will use an attack method called fast gradient attack to generate adversarial samples. Then go over some 
concepts of Adversarial training and showcase how this kind of training can better persist attacks from adversarial samples.

If you are using Watson Studio, you can load this notebook with the below URL link.
```shell
https://raw.githubusercontent.com/IBM/Trusted-ML-Pipelines/master/notebooks/adversarial-training-mnist-WS.ipynb
```
To run locally use the notebook `adversarial-training-mnist.ipynb`

#### 2.3. AIF360: Gender Classification
[This notebook](notebooks/tutorial_gender_classification.ipynb) will train a Gender Classification model using PyTorch. Then it will showcase how AIF360 can detect the bias
from the dataset and mitigate it in the dataset using a preprocessing algorithm called reweighting.

If you are using Watson Studio, you can load this notebook with the below URL link.
```shell
https://raw.githubusercontent.com/IBM/Trusted-ML-Pipelines/master/notebooks/tutorial_gender_classification.ipynb
```


### 3. (Optional) Advanced deep learning models for app developers
If you are interested in how to create and use open source deep learning models for app developers, you can use the below workshop to learn more about how to wrap models into container, using TensorFlowJS and NodeRed.
https://github.com/CODAIT/max-workshop-oscon-2019

Due to the limitation of network connectivity on the workshop, you can use the below link to try out the object-detector models API.
http://max-object-detector.max.us-south.containers.appdomain.cloud/
