# -*- coding: utf-8 -*-
"""
Time:2022/8/30 9:01
Author:CAOZHENG
File:jira_cfg.py
"""

# jira配置
JIRA_USER = "zcao"
JIRA_PWD = "xxxxxx"
JIRA_SERVER = "http://jira.xxx.com/"

# Jira图片地址


# jql
JIRA_JQL = {
    'project = VA AND issuetype = Bug AND status = Open AND reporter in (zcao) order by created DESC'
}
