// Jenkinsfile
pipeline {
    agent {
        docker {
            image 'python:3.9-slim' // Use a Python image as our environment
            args '-u 0:0' // To avoid permission issues in some Docker environments
        }
    }

    environment {
        PYTHONUNBUFFERED = '1' // Ensures Python output is unbuffered in Jenkins console
        // If you were using a production database, you'd define DB variables here, e.g.:
        # DATABASE_URL = 'sqlite:///db.sqlite3'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/panwars186/customer-churn-predictor.git'
                // Replace <your-username> with your actual GitHub username
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Migrations (for test database)') {
            steps {
                // Django automatically sets up a separate test database for `manage.py test`
                // but running makemigrations ensures everything is up-to-date
                // This step is more crucial if you actually had models and needed to create tables
                sh 'python manage.py makemigrations --noinput'
                sh 'python manage.py migrate --noinput'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python manage.py test myapp' // Run tests for your specific app
                // Or sh 'python manage.py test' to run all tests
            }
        }

        stage('Run Application (for demonstration/integration test)') {
            steps {
                // For a quick demonstration, run the server in the background
                // In a real CI/CD, you might deploy to a temporary environment instead
                sh 'nohup python manage.py runserver 0.0.0.0:8000 > django_app.log 2>&1 &'
                sh 'sleep 10' // Give Django time to start up (can take longer than Flask)
                sh 'curl -v http://localhost:8000/' // Make a request to verify it's running
                sh 'echo "Django app started. Check console output for URL and curl output."'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
            // If you ran the app in the background, you might want to stop it here
            // sh 'pkill -f "python manage.py runserver"' // Use with caution
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}