@Library("shared-library") _
pipeline {
    agent any

    stages {
        stage('Check if branch is deleted') {
            steps {
                script {
                    // Define the Git remote and branch name
                    def gitRemote = 'origin'
                    def gitBranch = 'test-new-branch'

                    // List all the remote references and check if the branch is present
                    def remoteRefs = sh(returnStdout: true, script: "git ls-remote --heads ${gitRemote}").trim()
                    def branchRef = "refs/heads/${gitBranch}"
                    def isDeleted = !remoteRefs.contains(branchRef)

                    // Print the result for debugging purposes
                    echo "Branch ${gitBranch} is ${isDeleted ? 'deleted' : 'not deleted'}"
                }
            }
        }
    }
}