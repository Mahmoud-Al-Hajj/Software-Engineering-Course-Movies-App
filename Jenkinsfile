pipeline {
  agent any
  triggers {
    pollSCM('H/2 * * * *')
  }
  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/Mahmoud-Al-Hajj/Software-Engineering-Course-Movies-App'
      }
    }

    stage('Ensure Minikube is running') {
      steps {
        bat '''
          REM start minikube if not already running
          minikube status || minikube start --driver=docker
        '''
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        bat '''
          REM create and call a docker_env script (more reliable than FOR loop)
          minikube docker-env --shell=cmd > "%WORKSPACE%\\docker_env.bat"
          call "%WORKSPACE%\\docker_env.bat"

          REM confirm we're using minikube docker (optional debug)
          docker info
          docker images

          REM build the image inside minikube's docker daemon
          docker build -t website:latest .
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat '''
          REM apply manifests using minikube's kubectl to be certain of context
          minikube kubectl -- apply -f deployment.yaml
          minikube kubectl -- apply -f service.yaml

          REM If using "latest" tag, force a rollout restart to ensure new image is used
          minikube kubectl -- rollout restart deployment/django-deployment || echo "rollout restart may not be supported; continuing"

          REM wait for rollout
          minikube kubectl -- rollout status deployment/django-deployment
        '''
      }
    }
  }
}
