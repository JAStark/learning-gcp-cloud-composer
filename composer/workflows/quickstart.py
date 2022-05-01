"""Code from https://cloud.google.com/composer/docs/run-apache-airflow-dag#airflow-1
Google tutorial
Updated to use the Airflow 2 version https://cloud.google.com/composer/docs/composer-2/run-apache-airflow-dag
Make sure using conda env `gcp-python-foxling` for local testing
"""

import datetime

from airflow import models
from airflow.operators import bash

YESTERDAY = datetime.datetime.now() - datetime.timedelta(days=1)

default_args = {
    "owner": "Composer Example",
    "depends_on_past": False,
    "email": [""],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=5),
    "start_date": YESTERDAY,
}

#### AIRFLOW 1
# with airflow.DAG(
#     "composer_sample_dag",
#     catchup=False,
#     default_args=default_args,
#     schedule_interval=datetime.timedelta(days=1),
# ) as dag:
#
#     print_dag_run_conf = bash_operator.BashOperator(
#         task_id="print_dag_run_conf", bash_command="echo {{ dag_run.id }}"
#     )

#### AIRLFLOW 2
with models.DAG(
    "composer_quickstart",
    catchup=False,
    default_args=default_args,
    schedule_interval=datetime.timedelta(days=1),
) as dag:

    # Print the dag_run id from the Airflow logs
    print_dag_run_conf = bash.BashOperator(
        task_id="print_dag_run_conf", bash_command="echo {{ dag_run.id }}"
    )
