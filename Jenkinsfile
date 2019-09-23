pipeline{
    agent any
    
    options { buildDiscarder(logRotator(numToKeepStr: '5')) }

    environment {
        slack_icon = ":fred_zoom:"
        slack_channel = "#alerts"
    }

    stages{
        stage("Install Python requirements"){
            steps{
                script{
                    sh "pip3 install -r requirements.txt --user"
                }
            }
        }
        stage("Run ElasticSearch checks"){
            steps{
                script{
                    sh "./curl_wrap.sh | ./check.py"
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