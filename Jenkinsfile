pipeline {
  agent any
  stages {
    stage('source') {
      steps {
        git(url: 'git@github.com:ctsictai/cts_drf_project_test.git', branch: 'master', credentialsId: 'ctsictai')
      }
    }

    stage('build') {
      steps {
        tool 'gradle'
      }
    }

    stage('deploy') {
      steps {
        sh 'echo "deploy success"'
      }
    }

  }
}