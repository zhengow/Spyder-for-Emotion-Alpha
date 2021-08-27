pipeline {
  agent any
  stages {
    stage('xcheck') {
      steps {
        xcheck(testServer: 'http://dev.xcheck.woa.com', testToken: 'a349ab19-9f8d-47fe-9895-19a32ca3e5be')
      }
    }

  }
}