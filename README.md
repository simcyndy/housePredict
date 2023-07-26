# Simple House Price Predictor

This is a beginner-friendly project that introduces the basic concepts of Machine Learning. We generate a synthetic dataset representing house prices and sizes, and use a simple linear regression model to predict house prices based on size.

# Getting Started

These instructions will guide you on how to set up and run the project.

# Prerequisites
<ol>
  <li>Python 3.x</li>
  <li>pip (Python package installer)</li>
</ol>

# Installation 
* Clone the repository:

```git clone https://github.com/simcyndy/housePredict.git```


* Navigate into the cloned repository:

``` cd housePredict ```

* Create a Python virtual environment and Activate the virtual environment:

``` python3 -m venv env ```

``` source env/bin/activate```

* Install the required packages:

```pip install -r requirements.txt```

* Running the Project
After installing the required packages, you can run the project:
 ``python generate_data.py``

# About the Dataset
The dataset used in this project is synthetic and generated using numpy. It represents house prices in relation to house sizes. Each house size is randomly generated between 1000 and 3500 square feet. The corresponding price for each house is roughly calculated as the size of the house * $200, with some added noise for realism.

# Model
The project uses a simple linear regression model from Scikit-Learn to predict house prices based on size. The data is split into an 80% training set and a 20% testing set. The model is trained on the training set and then used to predict prices in the testing set.

