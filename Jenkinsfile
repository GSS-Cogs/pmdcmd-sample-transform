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
        stage('echo received source url') { 
            agent {docker { image 'gsscogs/databaker:latest' } }
            steps {
               sh "echo recieved source url: ${params.source}"
            }
        }

        stage('unzip all the things') { 
            agent {docker { image 'gsscogs/databaker:latest' } }
            steps {
                withCredentials([[$class: 'FileBinding', credentialsId:"ons_source_bucket_credentials", variable: 'GOOGLE_APPLICATION_CREDENTIALS']]) {
                    sh "python3 getunzipsource.py ${params.source}"
                }
            }
        }

       stage('echo received files') { 
            agent {docker { image 'gsscogs/databaker:latest' } }
            steps {
               sh "ls -l ./source"
            }
        }

    }
}
