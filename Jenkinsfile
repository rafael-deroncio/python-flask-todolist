pipeline {
    agent any

    stages {
        stage("Teste 1") {
            step("step 1") {
                echo 'Pipeline OK'
            }

            step("step 2") {
                echo 'Pipeline OK'
            }

            step("step 3") {
                echo 'Pipeline OK'
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