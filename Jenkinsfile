/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.14.5-alpine3.23' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                   retry(3){
                          sh 'echo "Gidon"'
                   }
            }
        }
    }
	post {
	        always {
	            echo 'This will always run'
	        }
	        success {
	            echo 'This will run only if successful'
	        }
	        failure {
	            echo 'This will run only if failed'
	        }
	        unstable {
	            echo 'This will run only if the run was marked as unstable'
	        }
	        changed {
	            echo 'This will run only if the state of the Pipeline has changed'
	            echo 'For example, if the Pipeline was previously failing but is now successful'
	        }
	    }
}
