#!/bin/python
# _*_ coding:utf-8 _*_

"""
    simple-ansible

    A simple Ansible-api example
    TODO: simple ui base flask

    :copyright: (c) 2018 by wqz
"""
from __future__ import (absolute_import, division, print_function)


class BaseModule(object):
    def __init__(self, tasks):
        self.tasks = tasks

    def get_tasks(self):
        return self.tasks
