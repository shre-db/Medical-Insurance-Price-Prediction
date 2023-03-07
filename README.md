# Medical-Insurance-Price-Prediction

Overview 
--------

This projects is focused on predicting medical insurance price using regression. Data was collected from Kaggle and cleaned for Exploratory Data Analysis 
using Statistical Analysis and Feature Engineering. Transformation pipelines were implemented for convenient preprocessing of existing and new data. Machine
Learning techniques such as Linear Regression, Polynomial Regression, Decision Tree Regression, Support Vector Regression and Random Forest Regression were
applied for creation of models and cross-validation was used to evaluate their performance. Hyperparameter Tuning was applied to improve performance of some
of the models. Finally the project aims to deploy the trained models, although this step is not yet completed.

Table of contents 
----------------- 

1. Primary Objective
2. Results
3. Installation
4. Usage
5. Contributing
6. Credits
7. License
8. Contact

Primary Objective 
----------------- 

To develop regression models that accurately predict the medical insurance cost for an individual based on their personal information like age, sex, BMI, number of children, region and their lifestyle habits such as smoking using the dataset available on Kaggle. R^2 score will be used to evaluate model performance and the best performing model will be deployed for educational purposes.

Results 
------- 

No results yet.

Installation 
------------ 

**Prerequisites**:

- Anaconda Python Distribution
- python 3.9.16

Note: The steps below for installing packages involve 'requirements.txt' file. This file contains only those packages that were necessary for deployment of the flask app and therefore doesn't include all the packages that were used for the development of the project.


1. **Install Conda**: If you do not have Conda installed on your system, you can download and install the appropriate version for your operating sytem from the official Conda Website (https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
2. **Create an environment**: To avoid conflicts between packages, create a new environment. You can create one using the following command: conda create -n ENVNAME python=3.9.16. Replace ENVNAME with the name of your choice, for example: medi-dep, medi-dev.
3. **Activate the environment**: Once you have created the environment, you need to activate it to start using it. You can activate the environment using the following command: conda activate ENVNAME.
4. **Install packages**: You can now install the required packages in the environment using the either of the following commands:conda install --yes --file requirements.txt or conda install --file requirements.txt. The former automatically answers "yes" to all prompts during installation, while the latter requires user to manually confirm each installation prompt. If you're on a windows computer, you may have issues while running the above command because of gunicorn package. Since it is not needed for running an app locally, I recommend removing the 'gunicorn' package from requirements.txt file before running the command mentioned earlier in this step.
5. **Deactivate the environment**: Once you are done working with the environment, you can deactivate using conda deactivate and then close the prompt using exit. That's it! You have now installed the packages using Conda.
