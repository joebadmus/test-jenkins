@Library("shared-library") _
pipeline {
//   agent { label "linux" }
  agent any
  environment {
    // SECRET_KEY = credentials('mrjoejenkins')
    kv_url = 'https://mrjoekeyvault.vault.azure.net/'
  }
  parameters{
      string(name: 'ENVIRONMENT', defaultValue: '')
  }
  stages {
    stage('Set env from') {
        steps {
          script{
           def env = getEnvironment()
           echo "config loaded for test ${env}"
          }
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
            def env = getEnvironment()
            echo "env - $env from getEnvironment()"
            // if("${env}" != null){
            //     env.CONFIG = "$env"
            //     echo "config loaded from shared library"
            // }else{                
                if ("${params.ENVIRONMENT}" == "test"){
                env.CONFIG = TEST_SEC
                echo "config loaded for test env - ${env.CONFIG}"
                }
                else if ("${params.ENVIRONMENT}" == "dev"){
                env.CONFIG = DEV_SEC
                echo "config loaded for dev env  - ${env.CONFIG}"
                }
                else if ("${params.ENVIRONMENT}" == "pre"){
                env.CONFIG = PRE_SEC
                echo "config loaded for pre env  - ${env.CONFIG}"
                }
                else{
                    error("the env ${params.ENVIRONMENT} is ot allowed")
                }
            // }
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