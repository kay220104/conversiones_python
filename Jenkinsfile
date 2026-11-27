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

        stage('Instalar dependencias') {
            steps {
                sh 'python3 -m pip install pytest'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh 'python3 -m pytest test_conversiones.py -v'
            }
        }
    }
}
