pipeline{
    agent any
    environment{
        IMAGE_NAME = "my_image"
        CONTAINER_NAME = "my_container"
    }
    
    stages{
        stage('Clone'){
            steps{
                git branch: 'main', url: 'https://github.com/mohdajeem/jenkins_practice2.git'
            }
        }

        stage("Build"){
            steps{
                script{
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }
        
        stage('Run'){
            steps{
                script{
                    sh 'docker rm -r $CONTAINER_NAME || true'
                    sh 'docker run -d -p 8080:80 --name $CONTAINER_NAME $IMAGE_NAME'
                }
            }
        }
    }

    post{
        success {
            echo "Success"
        }
        failure{
            echo "Fail"
        }
    }
}


