pipeline {
    agent any

    environment {
        SERVICE_NAME = "appflask"
    }

    stages {

        stage('Instalar Dependências') {
            steps {
                echo 'Instalar dependências'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Rodar testes'
            }
        }

        stage('Reiniciar Serviço') {
            steps {
                echo 'Reiniciar o service'
            }
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