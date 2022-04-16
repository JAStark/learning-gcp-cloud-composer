"""Code from https://cloud.google.com/composer/docs/run-apache-airflow-dag#airflow-1
Google tutorial, using the Airflow 1 version
"""

import datetime

import airflow
from airflow.operators import bash_operator

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

with airflow.DAG(
    "composer_sample_dag",
    catchup=False,
    default_args=default_args,
    schedule_interval=datetime.timedelta(days=1),
) as dag:

    print_dag_run_conf = bash_operator.BashOperator(
        task_id="print_dag_run_conf", bash_command="echo {{ dag_run.id }}"
    )
