# Copyright (c) 2014 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import mock

from sahara import conductor as cond
from sahara.utils import edp


conductor = cond.API

_java_main_class = "org.apache.hadoop.examples.WordCount"
_java_opts = "-Dparam1=val1 -Dparam2=val2"


def create_job_exec(type, configs=None):
    b = create_job_binary('1', type)
    j = _create_job('2', b, type)
    e = _create_job_exec(j.id, type, configs)
    return j, e


def _create_job(id, job_binary, type):
    job = mock.Mock()
    job.id = id
    job.type = type
    job.name = 'special_name'
    if edp.compare_job_type(type, edp.JOB_TYPE_PIG, edp.JOB_TYPE_HIVE):
        job.mains = [job_binary]
        job.libs = None
    else:
        job.libs = [job_binary]
        job.mains = None
    return job


def create_job_binary(id, type):
    binary = mock.Mock()
    binary.id = id
    binary.url = "internal-db://42"
    if edp.compare_job_type(type, edp.JOB_TYPE_PIG):
        binary.name = "script.pig"
    elif edp.compare_job_type(type, edp.JOB_TYPE_MAPREDUCE, edp.JOB_TYPE_JAVA):
        binary.name = "main.jar"
    else:
        binary.name = "script.q"
    return binary


def create_cluster(plugin_name='vanilla', hadoop_version='1.2.1'):
    cluster = mock.Mock()
    cluster.plugin_name = plugin_name
    cluster.hadoop_version = hadoop_version
    return cluster


def create_data_source(url):
    data_source = mock.Mock()
    data_source.url = url
    if url.startswith("swift"):
        data_source.type = "swift"
        data_source.credentials = {'user': 'admin',
                                   'password': 'admin1'}
    elif url.startswith("hdfs"):
        data_source.type = "hdfs"
    return data_source


def _create_job_exec(job_id, type, configs=None):
    j_exec = mock.Mock()
    j_exec.job_id = job_id
    j_exec.job_configs = configs
    if edp.compare_job_type(type, edp.JOB_TYPE_JAVA):
        j_exec.job_configs['configs']['edp.java.main_class'] = _java_main_class
        j_exec.job_configs['configs']['edp.java.java_opts'] = _java_opts
    return j_exec
