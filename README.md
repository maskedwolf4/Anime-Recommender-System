End to End Anime Hybrid Recommender System

Overview

This project presents a comprehensive, end-to-end Machine Learning application: an Anime Hybrid Recommender System. It's designed to provide personalized anime recommendations to users by combining the strengths of both user-based and content-based recommendation techniques. This full-stack application adheres to modern MLOps principles, ensuring robust development, deployment, and monitoring.

The system aims to enhance user experience by suggesting anime titles that are highly relevant to their preferences, whether those preferences are inferred from similar users or from the characteristics of anime they've enjoyed previously.
Recommendation Approach: Hybrid Model

Our recommender system employs a hybrid approach to deliver superior recommendations:

User-Based Recommendation (Collaborative Filtering): This component identifies users with similar viewing histories or preferences to the current user. If similar users have enjoyed certain anime, those titles are recommended. This captures community trends and serendipitous discoveries.

Content-Based Recommendation: This component analyzes the features (genres, themes, studios, tags, etc.) of anime that a user has liked. It then recommends other anime that share similar characteristics, ensuring relevance based on the item's intrinsic properties.

By combining these two methods, the system overcomes the limitations of each individual approach (e.g., cold-start problem for new users in collaborative filtering, or over-specialization in content-based methods), leading to more accurate and diverse recommendations.
Benefits

 Personalized Experience: Delivers highly tailored anime suggestions, improving user satisfaction.

  Reduced Discovery Effort: Helps users find new anime quickly and efficiently, expanding their watchlists.

  Robust Recommendations: The hybrid approach provides more accurate and diverse recommendations compared to single-method systems.

  Scalable & Maintainable: Built with MLOps principles, ensuring the system can handle growing user bases and evolving models.

  Data-Driven Insights: Provides a foundation for understanding user preferences and anime trends.

Architecture and Technologies

This project is built as a full-stack, end-to-end Machine Learning application, following robust MLOps principles. The technology stack is designed for scalability, reliability, and efficient operations:

  Machine Learning Model Training:

  TensorFlow: Used for building and training the deep learning models that power both the user-based and content-based recommendation engines.

  Backend Application:

  Flask: A lightweight and powerful Python web framework serving as the API layer for the recommender system, handling user requests and delivering recommendations.

  MLOps & Application Tracking:

  Comet ML: Integrated for comprehensive application tracking, experiment management, model versioning, and performance monitoring. This provides visibility into the ML lifecycle.

  Data Versioning:

  DVC (Data Version Control): Utilized for versioning datasets and machine learning models, ensuring reproducibility of experiments and traceability of data changes. This allows for tracking large files and directories alongside Git.

  Source Code Management:

  GitHub: The primary platform for source code management, enabling version control, collaboration, and code reviews.

  CI/CD Pipeline:

  Jenkins: Orchestrates the Continuous Integration and Continuous Delivery pipeline.

  Docker-in-Docker (DinD): Jenkins is configured to run inside a Docker container, with the ability to build other Docker images within its environment, providing an isolated and consistent build process. This automates testing, building, and pushing new versions.

  Containerization:

  Docker: Used to containerize the Flask backend application and the ML model, ensuring consistent environments from development to production.

  Container Registry:

  Google Container Registry (GCR): Securely stores and manages the Docker images built by the CI/CD pipeline, making them readily available for deployment.

  Cluster Management & Deployment:

  Google Kubernetes Engine (GKE): Manages the deployment and scaling of the containerized application. GKE provides a robust and scalable environment for running the recommender system, handling load balancing, auto-scaling, and self-healing.



Screenshots

Here are some screenshots demonstrating the application in action:

![Dashboard of Anime Recommender](https://github.com/maskedwolf4/Anime-Recommender-System/blob/main/example_use.png)
