## Introduction to MLOps    
### What is MLOps?
##### MLOps also referred to as Machine Learning Operations, a method of combining software engineering and machine learning to improve speed, quality and reliability of machine learning models in production.

### Why do we need MLOps?
##### MLOPs invovle a set of techniques and tools for management of entire machine learning lifecycle from development to deployment and monitoring. 

##### 1. Scalability: The use of ml models in production is increasing day by day, hence the need for scalability is also increasing. This means we need a way for effective deployment and monitoring of these models.

##### 2. Speed: The scalability of models gives rise to the need for speed at which ML models can be deployed to production environments. MLOps helps streamlines some of the processes involved in this phase and speed up the time-to-market for an ML product.

##### 3. Quality, Reliability and Security: ML models can sometimes be very sensitive to changes in environment and produce unexpected outputs. These models are complex and hard to test and validated rendering them prone to errors thereby reducing quality and reliability. And lastly, with a lot of team collaboration, access privileges, data sharing and security becomes a major concern. MLOps helps in addressing these issues.


### MLOps Lifecycle
##### The MLOps lifecycle is a set of processes that are involved in the development and deployment of ML models.The lifecycle consists of the following phases:

##### 1. Data Collection and Preprocessing - This phase involves collection of data from various sources and preprocessing to make it suitable for training ML models.

##### 2. Model development and training - This phase deals with development of ML model using jupyter notebooks and scikit-learn and training the model using the preprocessed data.

##### 3. Model testing and validation - This phase involves testing and validating the model using test data to ensure that the model is working as expected. 

##### 4. Model deployment - This section involves deploying the ML model using a web service or mobile apps, using tools likes Tensorflow Serving, Flask, Docker, Kubernetes, etc.

##### 5. Model monitoring - Continuous monitoring of the model is needed to ensure that the model is working as expected. This phase involves monitoring the model performance and data drifts.

##### 6. Model management - Models are versioned and tracked to ensure that the right model is deployed to the right environment using tools like git, github, MLflow, etc.

##### 7. Model retraining - Periodic retraining of the model is essential to ensure that the model is working as expected to keep up with current trends and improve model performance.

##### 8. Data management - Future data is collected and stored in a data lake or data warehouse for future use. This data is then used for retraining the model.

#### MLOps Lifecycle
![MLOps Lifecycle](/assets/MLOps_lifecycle.jpg)