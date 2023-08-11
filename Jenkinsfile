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
                  // def currentVersion = readFile file: "features/version.txt"
                setVersion(env.BRANCH_NAME)
                
                def currentVersion = getVersion()

                echo "Current Application version is ${currentVersion}"
          }
        }
    }
    stage('Set env from') {
          steps {
            script{
            def env = getEnvironment("${env.WORKSPACE}/features/environment.json")
            echo "config loaded for test ${env}"
            }
        }
    }
    stage('lists env variables') {
        steps {
          sh 'ls -la'
      }
    }
    stage('Print env variables') {
        steps {
          sh 'printenv'
      }
    }
  }
 }