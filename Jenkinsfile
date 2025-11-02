pipeline {
  agent any
  triggers {
    // Poll GitHub every 2 minutes
    pollSCM('H/2 * * * *')
  }
  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/Mahmoud-Al-Hajj/Software-Engineering-Course-Movies-App'
      }
    }
    stage('Build in Minikube Docker') {
      steps {
        bat '''
          REM === Switch Docker to Minikube Docker ===
          @FOR /f "tokens=*" %%i IN ('minikube docker-env --shell=cmd') DO @%%i
          REM === Build Django image inside Minikube Docker ===
          docker build -t website:latest .
        '''
      }
    }
    stage('Deploy to Minikube') {
      steps {
        bat '''
          REM === Apply the updated deployment manifest ===
          kubectl apply -f deployment.yaml
          REM === Ensure the rollout completes ===
          kubectl rollout status deployment/django-deployment
        '''
      }
    }
  }
}