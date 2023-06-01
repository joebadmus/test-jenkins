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
    stage('Get KV Config'){
      options {
            azureKeyVault(credentialID: 'mrjoejenkins', 
            keyVaultURL: 'https://mrjoekeyvault.vault.azure.net/', 
            secrets: [
                [envVariable: "TEST_SEC" , name: "test", secretType: 'Secret'],
                [envVariable: "DEV_SEC" , name: "dev", secretType: 'Secret'],
                [envVariable: "PRE_SEC" , name: "pre", secretType: 'Secret']
                ]
            )
            }
      steps{
        script{
            // def env = getEnvironment()
            echo "Testing!!!!!!!!!! "
            echo "${env.WORKSPACE}s/environment.json"
            TEST_ENV = "${params.ENVIRONMENT}" == '' ? getEnvironment("${env.WORKSPACE}/features/environment.json") : "${params.ENVIRONMENT}"   
            // if ("${params.ENVIRONMENT}" == "test"){
            if ("$TEST_ENV" == "test"){
                env.CONFIG = TEST_SEC
                echo "config loaded for test env - ${env.CONFIG}"
            }
            // else if ("${params.ENVIRONMENT}" == "dev"){
            else if ("$TEST_ENV" == "dev"){
                env.CONFIG = DEV_SEC
                echo "config loaded for dev env  - ${env.CONFIG}"
            }
            // else if ("${params.ENVIRONMENT}" == "pre"){
            else if ("$TEST_ENV" == "pre"){
                env.CONFIG = PRE_SEC
                echo "config loaded for pre env  - ${env.CONFIG}"
                }
            else{
                error("the env ${params.ENVIRONMENT} is not allowed")
            }
            }
      }
    }
    stage('Print kv config') {
          steps{
          script{
              echo "=======stage 2========"
              echo "{$env.CONFIG}"
          }
        }
      }
    stage('Print test env') {
        steps {
          script {
            echo "=======stage 4========"
              echo "${params.ENVIRONMENT}"
              echo "${env.BRANCH_NAME}"
          }
        }
    }
    stage('Print env variables') {
        steps {
          sh 'printenv'
      }
    }
  }
 }