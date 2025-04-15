node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        // Using your Docker Hub repo name and tagging with branch + build number
        app = docker.build("edirizvani/djangoexercise:${env.BRANCH_NAME}-${env.BUILD_NUMBER}")
    }

    stage('Push image') {
        // Only push Docker image if we're on 'dev' branch
        if (env.BRANCH_NAME == 'dev') {
            docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                app.push("${env.BRANCH_NAME}-${env.BUILD_NUMBER}")
                app.push("${env.BRANCH_NAME}-latest")
            }
        } else {
            echo "Not pushing Docker image. Branch '${env.BRANCH_NAME}' is not 'dev'."
        }
    }
}
