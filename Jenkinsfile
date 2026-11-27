pipeline {
    agent {
        label 'python'
    }

    stages {
        stage('Verificar Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh 'python3 -m unittest test_conversiones.py'
            }
        }
    }
}
