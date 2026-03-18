# Decentralized Identity Verification Tool

## Overview
The Decentralized Identity Verification Tool is a robust application designed to streamline and secure the process of identity verification. By leveraging a decentralized approach, this tool ensures that users can verify their identities in a secure and user-friendly manner. It is particularly beneficial for organizations and services that require identity verification for onboarding new users, such as financial institutions, government agencies, and online service providers. The application provides a seamless interface for users to upload their identity documents and check the status of their verification requests.

## Features
- **User-Friendly Interface**: A clean and intuitive web interface for users to submit their identity documents and check verification status.
- **Secure Document Upload**: Supports secure upload of identity documents using FastAPI's file handling capabilities.
- **Real-Time Status Updates**: Allows users to check the status of their identity verification in real-time.
- **API Documentation**: Comprehensive API documentation available for developers to integrate the tool into other systems.
- **Responsive Design**: The web interface is fully responsive, ensuring compatibility across devices.
- **Database-Driven**: Utilizes SQLite for storing user identities and verification statuses, ensuring data persistence.
- **CORS Support**: Configured to allow cross-origin requests, facilitating integration with other applications.

## Tech Stack
| Technology   | Description                                    |
|--------------|------------------------------------------------|
| Python       | Programming language used for backend logic    |
| FastAPI      | Web framework for building APIs                |
| Uvicorn      | ASGI server for running FastAPI applications   |
| Jinja2       | Templating engine for rendering HTML templates |
| SQLite       | Lightweight database for storing user data     |
| HTML/CSS/JS  | Frontend technologies for the user interface   |
| Docker       | Containerization for deployment                |

## Architecture
The project is structured as a FastAPI application that serves both frontend and backend functionalities. The backend handles API requests and serves HTML templates, while the frontend provides a user interface for interacting with the application.

### Project Structure
```plaintext
/
├── app.py                 # Main application file
├── Dockerfile             # Docker configuration file
├── requirements.txt       # Python dependencies
├── start.sh               # Script for starting the application
├── static/                # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css      # Stylesheet for the application
│   └── js/
│       └── main.js        # JavaScript for client-side interactions
├── templates/             # HTML templates
│   ├── api_docs.html      # API documentation page
│   ├── index.html         # Home page
│   ├── status.html        # Status checking page
│   └── verify.html        # Identity verification page
└── identity_verification.db # SQLite database file
```

### Data Flow
```plaintext
[User] -> [Frontend (HTML/CSS/JS)] -> [FastAPI Backend] -> [SQLite Database]
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Docker (for containerized deployment)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/decentralized-identity-verification-tool-auto.git
   cd decentralized-identity-verification-tool-auto
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
To start the application, run the following command:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```
Visit `http://localhost:8000` in your web browser to access the application.

## API Endpoints
| Method | Path                        | Description                                      |
|--------|-----------------------------|--------------------------------------------------|
| GET    | /                           | Home page                                        |
| GET    | /verify                     | Identity verification page                       |
| GET    | /status                     | Check verification status page                   |
| GET    | /api-docs                   | API documentation page                           |
| POST   | /api/verify                 | Submit identity details and documents for verification |
| GET    | /api/status/{user_id}       | Retrieve verification status for a given user ID |
| GET    | /api/documents/{user_id}    | Fetch uploaded documents for a specific user     |

## Screenshots
![Home Page](screenshots/home.png)
![Verify Identity Page](screenshots/verify.png)
![Check Status Page](screenshots/status.png)

## Docker Deployment
To deploy the application using Docker:
1. Build the Docker image:
   ```bash
   docker build -t identity-verification-tool .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 identity-verification-tool
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

---
Built with Python and FastAPI.