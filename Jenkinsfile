pipeline{
    agent any

    environment{
        VENV_DIR = 'venv'
        GCP_PROJECT = 'western-will-465217-v8'
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
        KUBECTL_AUTH_PLUGIN = "/usr/lib/google-cloud-sdk/bin"
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
                    python -m pip install --upgrade pip
                    pip3 install -e .
                    pip3 install dvc
                    '''
                    
                }
            }
        }

        stage("DVC Pull"){
            steps {
                script{
                    // This block correctly sets GOOGLE_APPLICATION_CREDENTIALS for DVC
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


        stage("Build and Push image to GCR"){
            steps {
                script{
                    
                    withCredentials([file(credentialsId:'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                        script{
                            echo 'Build and Push image to GCR'
                            sh'''
                            export PATH=$PATH:${GCLOUD_PATH}
                            # Use quotes around the variable and a space or equals sign
                            gcloud auth activate-service-account --key-file="${GOOGLE_APPLICATION_CREDENTIALS}"
                            gcloud config set project ${GCP_PROJECT}
                            gcloud auth configure-docker --quiet # Fixed typo: --quite -> --quiet
                            docker build -t gcr.io/${GCP_PROJECT}/ars-project:latest .
                            docker push gcr.io/${GCP_PROJECT}/ars-project:latest
                            '''
                        }
                    }
                }
            }
        }


        stage("Deploying to Kubernetes"){
            steps {
                script{
                    
                    withCredentials([file(credentialsId:'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                        script{
                            echo 'Deploying to Kubernetes'
                            sh'''
                            export PATH=$PATH:${GCLOUD_PATH}:${KUBECTL_AUTH_PLUGIN}
                            # Use quotes around the variable and a space or equals sign
                            gcloud auth activate-service-account --key-file="${GOOGLE_APPLICATION_CREDENTIALS}"
                            gcloud config set project ${GCP_PROJECT}
                            gcloud container clusters get-credentials ars-app-cluster-1 --region us-central1 --project=${GCP_PROJECT} # Added --project for clarity, though gcloud config set project helps
                            kubectl apply -f deployment.yaml
                            '''
                        }
                    }
                }
            }
        }
    }
}