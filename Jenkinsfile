pipeline {
    agent any

    stages {
        stage("Teste") {
            echo 'Pipeline falhou!'
        }
    }

    post {
        success {
            echo 'Pipeline executado com sucesso!'
        }

        failure {
            echo 'Pipeline falhou!'
        }
    }
}