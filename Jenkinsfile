pipeline {
    agent any

    stages {
        stage("Teste 1") {
            steps {
                echo 'Step 1: Pipeline OK'
                echo 'Step 2: Pipeline OK'
                echo 'Step 3: Pipeline OK'
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
