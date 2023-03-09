# Medical-Insurance-Price-Prediction
![Alt text](vector_graphics/OKY6FW0.jpg)

Overview 
--------
This end-to-end machine learning project is focused on predicting medical insurance price using regression. Data was collected from Kaggle and cleaned for Exploratory Data Analysis using Statistical Analysis and Feature Engineering. A Custom Transformer was also built for Feature Engineering. Transformation pipelines were implemented for convenient preprocessing of existing and new data. Machine Learning techniques such as Linear Regression, Polynomial Regression, Decision Tree Regression, Support Vector Regression and Random Forest Regression were applied for creation of models and cross-validation was used to evaluate their performance. Hyperparameter Tuning was applied using GridSearchCV to improve performance of some models. The Random Forest classification model was deployed using Flask on Render Cloud Hosting.

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
To develop regression models that predict the medical insurance cost for an individual based on their personal information like age, sex, BMI, number of children, region and their lifestyle habits such as smoking using the dataset available on Kaggle. R^2 score will be used to evaluate model performance and the best performing model will be deployed for educational purposes.

Results 
-------
|Model|Trainset accuracy|Testset accuracy|Inference|
|:-|:-|:-|:-|
|poly_reg|0.8419|0.8665|Good performance|
|tree_reg|0.8670|0.8641|Good performance|
|forest_reg|0.8739|0.8737|Good performance|

Since Random Forest Classification model achieved the highest R^2 score (0.8737) on test set without any signs of overfitting on the training data after Hyperparameter Tuning, it was chosen for deployment.

Installation 
------------ 
**Prerequisites**:

- Anaconda Python Distribution
- python 3.9.13

Note: The steps below for installing packages involve 'requirements.txt' file. This file contains only those packages that were necessary for deployment of the flask app and therefore doesn't include all the packages that were used for the development of the project.

1. **Install Conda**: If you do not have Conda installed on your system, you can download and install the appropriate version for your operating sytem from the official Conda Website (https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
2. **Clone the repository**: To clone this repository on your local machine,  open Terminal or Git Bash CLI (for Windows), navigate to a folder where you want to clone the repository, type this command `git clone https://github.com/shre-db/Medical-Insurance-Price-Prediction.git` and press Enter. The repository will be cloned to your local machine.
3. **Create an environment**: To avoid conflicts between packages, create a new environment. You can create one using the following command: `conda create -n ENVNAME python=3.9.16`. Replace `ENVNAME` with the name of your choice, for example: `medi-dep`, `medi-dev`.
4. **Activate the environment**: Once you have created the environment, you need to activate it to start using it. You can activate the environment using the following command: `conda activate ENVNAME`.
5. **Install packages**: You can now install the required packages in the environment using the either of the following commands:`conda install --yes --file requirements.txt` or `conda install --file requirements.txt`. The former automatically answers "yes" to all prompts during installation, while the latter requires user to manually confirm each installation prompt. If you're on a windows computer, you may have issues while running the above command because of gunicorn package. Since gunicorn is not needed for running an app locally, I recommend removing it from requirements.txt file before running the command mentioned earlier in this step.
6. **Deactivate the environment**: Once you are done working with the environment, you can deactivate using `conda deactivate` and then close the prompt using `exit`. That's it! You have now installed the packages using Conda.

Usage 
----- 
You can access the deployed project by following the link: https://medical-insurance-price-prediction.onrender.com/. Alternatively, after installation you can run the project locally by following the steps below:

1. Open Anaconda prompt.
2. Navigate to the project folder.
3. Run this command: `python main.py`.
4. Copy the url (http://localhost:5000 or similar) generated in the prompt.
5. Open a web browser and paste the url to access the web application.

Contributing 
------------ 
Thank you for your interest in this project! At this time we are not accepting contribution from external collaborators. If you have any feedback or suggestions, please feel free to create an issue or contact us directly.

Credits
-------
- Data for this project was collected from [Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance).
- Cover Image in this project was <a href="http://www.freepik.com">Designed by Vilmosvarga / Freepik</a>.
- Flowcharts in this project were made with the help of https://app.diagrams.net/.

License
-------
This project is licensed under the [MIT License](LICENSE.txt) - see the [LICENSE.txt](LICENSE.txt) file for details.

Contact
-------
- **Name**: Shreyas
- **Email**: shreyasdb99@gmail.com
- **GitHub**: [shre-db](https://github.com/shre-db)
- **Instagram**: [shryzium](https://www.instagram.com/shryzium/)
