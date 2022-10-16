from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import datetime as dt
default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2022,10,16),
    'retries': 30
    'retry_delay': dt.timedelta(minutes=3),
}

dag = DAG('DashPlot',
          default_args=default_args,
          schedule_interval='0 * * * *', # minutes '0 1 * * *' hours
          catchup=False
          )

command_t1 = 'python /Users/admin/pppavlov.github.io/BokehDash.py'
t1 = BashOperator(
          task_id = 'BokehDash',
          bash_command = command_t1
          dag = dag
)

command_t2 = 'python /Users/admin/pppavlov.github.io/git_push.py '
t2 = BashOperator(
                  task_id = 'gitPush',
                  bash_command = command_t2,
                  dag = dag
)


t1 >> t2 