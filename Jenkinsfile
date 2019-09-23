pipeline{
    agent any
    
    options { buildDiscarder(logRotator(numToKeepStr: '5')) }

    triggers {
        cron("*/14 * * * *")
    }

    environment {
        slack_icon = ":fred_zoom:"
        slack_channel = "#dads-alerts"
        slack_url = "http://slack.imm.corp/api/v1/alert"
    }

    stages{
        stage("Install Python requirements"){
            steps{
                script{
                    sh "/usr/local/bin/pip3 install -r requirements.txt --user"
                }
            }
        }
        stage("Run ElasticSearch checks"){
            steps{
                script{
                    sh """
                    export slack_icon=${slack_icon}
                    export slack_channel=${slack_channel}
                    export slack_url=${slack_url}
                    ./curl_wrap.sh | ./check.py
                    """
                }
            }
        }
    }
    post{
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}
