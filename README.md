# amazon_recommendation_system_bda
The semester project of the Big Data Analytics course taught by Dr. Kifayat Ullah Khan and Mr. Humayoun Mustafa Mazhar.

# BDA Project: amazon.com product recommendation system

## Team Members
- Yahya Qureshi
- Maaz Khaled
- Eman Tahir

## Introduction
This project is divided into three major parts:
1. Model Training
2. Flask Setup and Connection to Frontend and Backend
3. Kafka Producer and Consumer for Real-Time Recommendations

## 1. Model Training
The first part of the project involved selecting and training a machine learning algorithm to predict user preferences based on their past behaviors. For this, we chose the Alternating Least Squares (ALS) algorithm, which is particularly well-suited for customer order data due to its ability to handle large, sparse datasets effectively and generate high-quality recommendations.

### Why ALS?
ALS is a collaborative filtering technique that factors the user-item interaction matrix into two low-rank matrices, representing user preferences and item features. It alternates between fixing the user matrix and solving for the item matrix and vice versa, minimizing the reconstruction error at each step. This approach is ideal for:
- Handling large datasets with many missing values.
- Providing personalized recommendations based on user behavior.
- Scaling well with increasing data size, making it suitable for real-time applications.

### Key Steps:
- **Algorithm Selection**: ALS was chosen for its robustness in handling large-scale recommendation tasks.
- **Data Preparation**: Cleaning and pre-processing the dataset to ensure high-quality inputs.
- **Model Training**: Training the ALS model on user interaction data to predict preferences accurately.

## 2. Flask Setup and Connection to Frontend and Backend
The second part of the project involved setting up a Flask web application framework and establishing connections between the frontend and backend using RESTful API endpoints.

### Key Steps:
- **Frontend Development**: Using HTML and CSS to design a user-friendly interface.
- **Backend Integration**: Developing backend services with Python and connecting them using Flask.
- **API Development**: Creating RESTful API endpoints to handle requests and responses efficiently.

## 3. Kafka Producer and Consumer for Real-Time Recommendations
The final part of the project focused on implementing Kafka producer and consumer to stream real-time recommendations based on user preferences.

### Key Steps:
- **Kafka Setup**: Setting up Kafka producer and consumer for data streaming.
- **Real-Time Data Processing**: Collecting user behavior data through the producer and processing it to generate recommendations.
- **Recommendation Delivery**: Sending personalized recommendations to the frontend via Flask.

## Member Contributions
- **Yahya Qureshi**: Responsible for training the machine learning model used to generate user recommendations.
- **Maaz Khaled & Eman Tahir**: Set up the Flask application, connected the server to the frontend interface, and developed the Kafka producer and consumer for real-time recommendation streaming.

## Appendix A: Data Upload to MongoDB
To enhance our recommendation system, we attempted to integrate detailed product information from the Amazon API. Due to the requirement for a seller account, this integration was put on hold. Instead, we uploaded our data to MongoDB for better management and accessibility, despite facing several technical challenges.

### Lessons Learned:
- **Complexity of Real-World Data**: Handling and processing large, complex datasets requires significant time and effort.
- **Importance of Preparation**: Allocating sufficient time for data management tasks is crucial for project success.

## Conclusion
Despite challenges, we successfully built a robust recommendation system combining ALS and Content-Based Filtering. This project provided valuable insights into handling advanced features and real-world data complexities, which will guide our future endeavors.
