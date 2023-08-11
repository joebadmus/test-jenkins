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
                  def currentVersion = readFile file: getVersion()
                  echo "Current Application version is ${currentVersion}"
                // Split the version into major, minor, and patch components
                  def versionParts = currentVersion.split('\\.')
                  def majorVersion = versionParts[0].toInteger()
                  def minorVersion = versionParts[1].toInteger()
                  def patchVersion = versionParts[2].toInteger()
                    // If we're on the main branch, increment the major version
                  if (env.BRANCH_NAME == 'master') {
                      majorVersion++
                      minorVersion = 0
                      patchVersion = 0
                  }
                    // Construct the new version string
                  def newVersion = "${majorVersion}.${minorVersion}.${patchVersion}"
                    // Write the new version to a file or environment variable
                    // writeVersionToFileOrEnv(newVersion)
                  writeFile file: 'version.txt', text: newVersion
                    // Print the new version for debugging purposes
                  echo "New version: ${newVersion}"
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