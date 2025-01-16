pipeline {
    agent any

    environment {
        APP_DIR = "/home/ubuntu/app-flask"
        VENV_DIR = "${APP_DIR}/env"
        GIT_REPO = "git@github.com:seu_usuario/seu_repositorio.git"
        SERVICE_NAME = "appflask"
    }

    stages {
        stage('Clonar Repositório') {
            steps {
                git url: "${GIT_REPO}", branch: 'main'
            }
        }

        stage('Instalar Dependências') {
            steps {
                script {
                    sh """
                        sudo source ${VENV_DIR}/bin/activate
                        pip install -r ${APP_DIR}/requirements.txt
                    """
                }
            }
        }

        stage('Iniciar Testes') {
            steps {
                sh """
                    pytest ${APP_DIR}/tests.py
                """
            }
        }

        stage('Reiniciar Serviço') {
            steps {
                script {
                    sh """
                        sudo systemctl restart ${SERVICE_NAME}
                    """
                }
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