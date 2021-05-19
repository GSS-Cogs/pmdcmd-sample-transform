pipeline {
    agent none

    parameters{
        string (
            defaultValue: "-not-specified-",
            description: 'The source url as passed to the Jenkins job',
            name: 'source'
            )
    }

    stages {
        stage('log out python packages') {
            agent { docker { image 'gsscogs/allure-test-generator:latest' } }
            steps {
                sh 'pip freeze'
            }
        }

        stage('echo received source url') { 
            agent {docker { image 'gsscogs/databaker:latest' } }
            steps {
               sh 'echo recieved source url: "${params.source}"'
            }
        }
    }
}