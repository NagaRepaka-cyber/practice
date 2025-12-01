pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                echo 'Hello World'
                def sum(x,y):
                    print(x+y)

                sum(2,4)
            }
        }
        stage('build') {
            steps {
                echo 'Hello Hi'
            }
        }
        stage('deploy') {
            steps {
                echo 'Hello, how are you?'
            }
        }
    }
}
