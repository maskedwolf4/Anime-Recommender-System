pipeline{
    agent any

    environment{
        VENV_DIR = 'venv'
    }

    stages{

        stage("Cloning from GitHub"){
            steps {
                script{
                    echo 'Cloning from Github'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/maskedwolf4/Anime-Recommender-System']])
                }
            }
        }

        stage("Making a Virtual Environment"){
            steps {
                script{
                    echo 'Making a Virtual Environment'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip3 install --upgarde pip
                    pip3 install -e .
                    pip3 install dvc
                    '''
                    
                }
            }
        }

        stage("DVC Pull"){
            steps {
                script{
                    
                    withCredentials([file(credentialsId:'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                        script{
                            echo 'DVC Pull'
                            sh'''
                            . ${VENV_DIR}/bin/activate
                            dvc pull
                            '''

                        }
                    

                    }
                    
                    
                }
            }
        }




    }
}