pipeline {
    agent {
        label 'python'
    }

    stages {
        stage('Entorno') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'python3 -m pip install pytest'
            }
        }

        stage('Descarga') {
            steps {
                git url: 'https://github.com/kay220104/conversiones_python.git', branch: 'main'
            }
        }

        stage('Ejecutar') {
            steps {
                sh 'python3 Conversion.py'
            }
        }

        stage('Probar') {
            steps {
                sh 'python3 -m pytest --junitxml=reports/results.xml'
            }
            post {
                always {
                    junit 'reports/results.xml'
                }
            }
        }
    }
}
