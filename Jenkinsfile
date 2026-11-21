// PR 智能检视流水线（Jenkins multibranch + GitHub PR 触发）
pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 30, unit: 'MINUTES')
    }

    environment {
        GITHUB_TOKEN = credentials('github-token')
        DB_PATH = '/tmp/review_sessions.db'
    }

    stages {
        stage('PR Review') {
            when {
                expression { env.CHANGE_ID != null && env.CHANGE_ID != '' }
            }
            steps {
                script {
                    def repo = "zisang0210/pr-review-demo"
                    def pr = env.CHANGE_ID
                    echo "==> Jenkins triggered review for ${repo}#${pr}"
                }
                sh '''
                    cd /root/whzs/jenkins/demo
                    python3 -m src.review first-review \
                        --repo "zisang0210/pr-review-demo" \
                        --pr "${CHANGE_ID}"
                '''
            }
        }
    }

    post {
        success {
            echo "检视流水#视成功"
        }
        failure {
            echo "检视流水线失败"
        }
    }
}
