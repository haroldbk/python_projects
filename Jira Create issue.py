#Jira Create issue
#https://pythonjira.com/create-a-jira-ticket-with-python/
from jira import JIRA

jira_connection = JIRA(server='https://omolaragreen.atlassian.net',
   basic_auth=('haroldbk@taki.onmicrosoft.com','ATATT3xFfGF0M4KF5uJKgmD_re_sK9L_-_InFq5u4TnMid_kzMVexhYqJVxBBk6_r7ku8Wf_-HySW4J4xQUPxfEBpXdkprNuRehrHhgiVqq6u26M7Jia9w9uCSH-DJcxUrng6JfeRX2_nttPMqIQXTeVCpuddefmHT19Q3pY3zPPPwdh214NcxM=A84FDF30'
))



issue_dict={
    "project": {
      "key": "HT"
    },
    "summary": "Issue Summary501",
    "description": "Python This needs to be done",
    "issuetype": {
      "name": "Task"
    }
}

new_issue=jira_connection.create_issue(fields=issue_dict)

print(new_issue.key)