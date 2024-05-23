The repository of the semester project of the Fundamentals of Big Data Analytics course taught by Dr. Kifayat Ullah Khan and Mr. Humayoun Mustafa Mazhar. An amazing project which contributed to our learning and development, massively. Take a look at the execution, in this repository. Thank you for your time :)

# Amazon.com Product Recommendation System

## Project Overview

**Project Name:** Amazon.com Product Recommendation System   
**Team Members:** Yahya Qureshi, Maaz Khaled, Eman Tahir

## Introduction

This project aimed to develop a sophisticated recommendation system for Amazon.com, leveraging big data technologies and machine learning algorithms. The project was divided into three major parts:
1. **Model Training**
2. **Flask Setup and Connection to Frontend and Backend**
3. **Kafka Producer and Consumer for Real-Time Recommendations**

## 1. Model Training

### Algorithm Selection

For this project, we selected the Alternating Least Squares (ALS) algorithm, a collaborative filtering technique particularly well-suited for handling large, sparse datasets like customer order data.

### Why ALS?

- **Scalability:** Handles large datasets efficiently.
- **Accuracy:** Provides high-quality personalized recommendations by factoring the user-item interaction matrix into two low-rank matrices.
- **Suitability:** Ideal for customer order data due to its robustness and scalability.

### Data Preparation

- **Dataset:** Amazon Review Data (2018) - 233.1 million records, 128GB.
- **Data Cleaning:** Implemented extensive data cleaning and pre-processing to ensure the quality of inputs.

### Model Training

- **Process:** Trained the ALS model on user interaction data, including clicks, cart additions, and purchases, to accurately predict user preferences.

## 2. Flask Setup and Connection to Frontend and Backend

### Frontend Development

- **Technologies Used:** HTML, CSS
- **Design:** Developed a user-friendly interface for seamless interaction.

### Backend Integration

- **Technologies Used:** Python, Flask
- **API Development:** Created RESTful API endpoints to handle requests and responses efficiently.

## Data Upload to MongoDB

To enhance our recommendation system, we attempted to integrate detailed product information from the Amazon API. Due to the requirement for a seller account, this integration was put on hold. Instead, we uploaded our data to MongoDB for better management and accessibility, despite facing several technical challenges.

## 3. Kafka Producer and Consumer for Real-Time Recommendations

### Real-Time Data Processing

- **Setup:** Implemented Kafka producer and consumer for real-time data streaming.
- **Data Collection:** Producer collected user behavior data and pushed it to a Kafka topic.
- **Data Processing:** Consumer processed the data from the Kafka topic and generated personalized recommendations.

### Recommendation Delivery

- **Integration:** Recommendations were sent back to the frontend via Flask.

## Member Contributions

- **Maaz Khaled & Eman Tahir:** Set up the Flask application, connected the server to the frontend interface, and developed the Kafka producer and consumer for real-time recommendation streaming.
- **Yahya Qureshi:** Responsible for training the machine learning model used to generate user recommendations.


### Lessons Learned

- **Complexity of Real-World Data:** Handling and processing large, complex datasets requires significant time and effort.
- **Importance of Preparation:** Allocating sufficient time for data management tasks is crucial for project success.

## Conclusion

Despite challenges, we successfully built a robust recommendation system combining ALS and Content-Based Filtering. This project provided valuable insights into handling advanced features and real-world data complexities, which will guide our future endeavors.

---

## Project Impact

### Complexity and Impact

This project required extensive technical expertise and strategic planning to handle a large-scale dataset and integrate multiple technologies seamlessly. The successful implementation of this recommendation system underscores our ability to manage complex projects, innovate with advanced algorithms, and deliver solutions that drive substantial business value.

### Skills Highlighted

- **Big Data Management:** Demonstrated proficiency in handling and processing vast amounts of data using PySpark and MongoDB.
- **Machine Learning and Algorithms:** Showcased the ability to design and implement advanced recommendation algorithms, such as LSH, to enhance product suggestions.
- **Real-time Processing:** Leveraged Apache Kafka to build a real-time data streaming and processing pipeline, ensuring timely and relevant recommendations.
- **Data Analysis:** Applied comprehensive EDA to derive meaningful insights, aiding in improving the recommendation system and benefiting product owners.

### Impact

By undertaking this project, we have proven our technical prowess and dedication to excellence. Our work on the Amazon.com Product Recommendation System reflects our capability to deliver impactful solutions, our readiness to take on challenging tasks, and our enthusiasm for continuous learning and innovation in the tech field.

---

## How to Use This Project

### Prerequisites

- Python 3.7+
- MongoDB
- Apache Kafka
- PySpark
- Flask

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repository-url
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Start MongoDB:**
   Follow MongoDB installation and start-up guides specific to your operating system.

4. **Start Kafka:**
   Follow Kafka installation and start-up guides specific to your operating system.

5. **Run the bash file to start the app and it's dependencies:**
   ```sh
   ./startproj.sh
   ```

### Running the Project

1. **Data Upload:**
   Upload your dataset to MongoDB following the scripts provided in the `data_upload` directory.

2. **Model Training:**
   Train the ALS model using the provided scripts in the `model_training` directory.

3. **Kafka Setup:**
   Set up Kafka producer and consumer using the scripts in the `kafka` directory.

4. **Start the Web App:**
   Run the Flask application and access the frontend via `http://localhost:5000`.
