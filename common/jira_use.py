# -*- coding: utf-8 -*-
"""
Time:2022/8/30 8:58
Author:CAOZHENG
File:jira_use.py
"""

from datetime import datetime
from jira import JIRA
from config import jira_cfg


class JiraUse:
    def __init__(self, project_name, jira_server=jira_cfg.JIRA_SERVER,
                 project_user=jira_cfg.JIRA_USER, project_pwd=jira_cfg.JIRA_PWD):
        """

        :param project_name: 项目名
        :param jira_server: jira地址
        :param project_user: jira用户名
        :param project_pwd: jira密码
        """
        self.project_name = project_name
        self.jira_server = jira_server
        self.project_user = project_user
        self.project_pwd = project_pwd
        self.jira = JIRA(server=jira_server, basic_auth=(self.project_user, self.project_pwd))

    def search_issues(self):
        """
        # 按照 jql查询 issues
        :return:
        """
        issues_list = []
        issues = self.jira.search_issues(jql_str=jira_cfg.JIRA_JQL, maxResults=-1)
        for issue in issues:
            issues_list.append({"issue_key": issue.key,
                                "summary": str(issue.fields.summary).replace("'", "\\'"),
                                "status": str(issue.fields.status),
                                "priority": str(issue.fields.priority),
                                "severity": str(issue.fields.customfield_10600),
                                "recurrence": str(issue.fields.customfield_10601),
                                "labels": " ".join(issue.fields.labels),
                                "assignee": str(issue.fields.assignee),
                                "reporter": str(issue.fields.reporter),
                                "updated": datetime.strptime((issue.fields.updated[0:10]), '%Y-%m-%d').date(),
                                "created": datetime.strptime((issue.fields.created[0:10]), '%Y-%m-%d').date()})
        # print(issues_list)
        for i in range(len(issues_list)):
            print(issues_list[i])

        return issues_list
        # for item in range(len(issues_list)):
        #     print(issues_list[item])
        # for i in item:
        #     print(item[i].values())


if __name__ == "__main__":
    jira = JiraUse('ES400v')
    jira.search_issues()
