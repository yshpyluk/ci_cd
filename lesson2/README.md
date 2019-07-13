##  Jenkins Workshop (Part2)

### Build Triggers

1. Install "GitHub Pull Request Builder" Plugin

  * Manage Jenkins --> Manage Plugins --> Available --> GitHub Pull Request Builder
  * Access to Git Repository !!!!!!!!!!!!!!!!!!


2. Enable GitHub Pull Request Builder

  * Open Freestyle Job created in previous lesson -->
    Configure --> Build Triggers --> set GitHub Pull Request Builder


  In opened configuration tab set

  * Trigger phrase --> `build_training`
  * Crontab line --> `H/1 * * * *`
  * Build every pull request automatically without asking
  * Whitelist Target Branches --> `master`

3. Test build triggering

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

4. Install `ngrok` software

  * Download from https://ngrok.com/download
  * `unzip ngrok-*.zip`
  * `./ngrok http 8080`


5. Configure web hooks for triggering Jenkins Job

  *  Open Jenkins Freestyle Job --> Configure --> Build Triggers --> GitHub Pull Request Builder --> set `Use github hooks for build triggering`

  * Open GitHub Repository Settings -->
  Webhooks --> Add webhook
  * Set Payload URL, example
  `http://b9a0f2dc.ngrok.io/ghprbhook/`
  * select individual events `Issue comments`, `Pull requests`
  * Add Webhook and test it with Pull Request comment or push event
