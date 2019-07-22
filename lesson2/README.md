##  Jenkins Workshop (Part2)

### Build Triggers

1. Install "GitHub Pull Request Builder" Plugin

  * Manage Jenkins --> Manage Plugins --> Available --> GitHub Pull Request Builder


2. Configure plugin access to Git Repository

  * Manage Jenkins --> Configure System --> GitHub Pull Request Builder
  * Credential --> Add --> Secret text --> put `GitHub personal token` --> Add --> Test Credentials
  ```
  https://github.com/settings/tokens
  ```

3. Enable GitHub Pull Request Builder

  * Open Freestyle Job created in previous lesson -->
  Configure --> General --> set `GitHub project Url`

  * Freestyle Job --> Configure --> Build Triggers --> set GitHub Pull Request Builder


  In opened configuration tab set

  * Trigger phrase --> `build_training`
  * Crontab line --> `H/2 * * * *`
  * Build every pull request automatically without asking
  * Whitelist Target Branches --> `master`

4. Test build triggering

  * Create new git branch
  ```
  git checkout -b trigger
  ```
  * Edit README file or create a new one
  ```
  echo "Testing Build Trigger" > test_trigger.txt
  git add test_trigger.txt
  git commit -m "testing build trigger"
  git push
  ```
  * Create Pull Request from newly created branch to `master`
  * Wait a minute and check Jenkins Job
  * Trigger job from PR comment `build_training` and check in Jenkins UI


### HomeWork. Create Pipeline Job

1. New Item --> Enter an item name ex. `Pipeline` --> Ok.

  You can use and modify Jenkinsfile created with BlueOcean job.

  * Use environment variables in Pipeline for git url and credentialsId
  ```
  environment {
        giturl = 'https://github.com/pavlobornia/training-ci'
        credentials = 'abf15cef-c50d-426c-bd68-01efff095f62'
    }
  ```
  https://jenkins.io/doc/pipeline/tour/environment/

  * Use parallel stages in your pipeline. You can replace running tests step with shell step `echo "Running Tests"`
  ```
  stage('Parallel') {
      parallel {
        stage('Run Unit Tests') {
          steps {
            sh 'flask-app pytest'
          }
        }
        stage('Run Smoke Tests') {
          steps {
            echo "Tests 2"
          }
        }
      }
  }
  ```

  * Force your parallel stages to all be aborted when one of them fails  
    ```
    options { parallelsAlwaysFailFast() }
    ```
    ```
    failFast true
    ```

  * Use Post Condition Actions for archiving test results
  ```
  post {
      success {
        junit 'flask-app/junit-report/report.xml'
      }
  }
  ```
  * Delete workspace when build is done
  ```
  sh 'sudo rm -rf flask-app/junit-report'
  cleanWs()
  ```

See details https://jenkins.io/doc/book/pipeline/syntax/
