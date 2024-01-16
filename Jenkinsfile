@Library("shared-library") _
pipeline {
//   agent { label "linux" }
  agent none

  parameters{
      string(name: 'ENVIRONMENT', defaultValue: 'test')
  }
  stages {
    // stage('Set env version') {
    //     steps {
    //       script {

    //             // sh 'python main.py hello'
    //             // sh 'ls -ltr'
    //             // setVersion(env.BRANCH_NAME)
    //             // def currentVersion = getVersion()
    //             echo "Set env version"
    //       }
    //     }
    // }
    stage('Testing Jenkins file') {
        steps {
            sh 'echo "Testing enn variable"'
            sh ' printenv | sort '
      }
    }
  }
 }