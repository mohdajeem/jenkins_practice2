pipeline{
    agent any

    environment{
        IMAGE_NAME = 'flask_app2'
        CONTAINER_NAME = 'flask_app_container_jenkins'
    }

    stages{
        stage('clone'){
            steps{
                git branch: 'main', url:'https://github.com/mohdajeem/jenkins_practice2.git'
            }
        }
        stage('Build'){
            steps{
                script{
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }
        stage('Run'){
            steps{
                script{
                    sh 'docker rm -f $CONTAINER_NAME || true'
                }
                script{
                    sh 'docker run -itd --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME'
                }
            }
        }
    }
}

post{
    success {
        echo "success fully done"
    }
    failure{
        echo "failed...  "
    }
}
