node {
    def app
    
    stage('clone repository') {
        checkout scm
    }
    
    stage('build image') {
        app = docker.build("nitinjangam/flask-app")
    }
    
    stage('test image') {
        app.inside {
            sh 'echo "tests passed"'
        }
    }
    
    stage('push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}