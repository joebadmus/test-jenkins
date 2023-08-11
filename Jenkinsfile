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
      string(name: 'ENVIRONMENT', defaultValue: '')
  }
  stages {
    stage('Set env version') {
        steps {
          script{
           def version = readFile file: "version.txt"
           echo "Application version is ${version}"
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