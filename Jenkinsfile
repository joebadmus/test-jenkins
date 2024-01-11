@Library("shared-library") _
pipeline {
//   agent { label "linux" }
  agent any
  environment {
    // SECRET_KEY = credentials('mrjoejenkins')
    kv_url = 'https://mrjoekeyvault.vault.azure.net/'
    settingsFile = "${env.WORKSPACE}/environment.json"
  }
  parameters{
      string(name: 'ENVIRONMENT', defaultValue: 'test')
  }
  stages {
    stage('Set env version') {
        steps {
          script {

                // sh 'python main.py hello'
                // sh 'ls -ltr'
                // setVersion(env.BRANCH_NAME)
                // def currentVersion = getVersion()
                echo "Set env version"
          }
        }
    }
    stage('Testing Jenkins file') {
        steps {
          script{
            testJenkinsBuild()
          }
      }
    }
  }
 }