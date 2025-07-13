pipeline{
    agent any

    stages{
        stage("Cloning from GitHub"){
            steps {
                script{
                    echo 'Cloning from Github'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/maskedwolf4/Anime-Recommender-System']])
                }
            }
        }
    }
}