pipeline {
    agent any

    stages {
        stage('Clonar Repositório') {
            steps {
                git url: "${GIT_REPO}", branch: 'main'
            }
        }

    //     stage('Instalar Dependências') {
    //         steps {
    //             script {
    //                 sh """
    //                     sudo source ${VENV_DIR}/bin/activate
    //                     pip install -r ${APP_DIR}/requirements.txt
    //                 """
    //             }
    //         }
    //     }

    //     stage('Iniciar Testes') {
    //         steps {
    //             sh """
    //                 pytest ${APP_DIR}/tests.py
    //             """
    //         }
    //     }

    //     stage('Reiniciar Serviço') {
    //         steps {
    //             script {
    //                 sh """
    //                     sudo systemctl restart ${SERVICE_NAME}
    //                 """
    //             }
    //         }
    //     }
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