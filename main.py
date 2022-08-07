import aivle_login
import os
import conf
import execute_util as exe
os.chdir(os.getcwd())

if conf.execute_teams == 'True':
    exe.execute(conf.teams_file_name, conf.teams_path)

if conf.execute_jupyter == 'True':
    exe.execute(conf.jupyter_file_name)

if conf.execute_vs == 'True':
    print('vs 실행')
    exe.execute(conf.vs_file_name, conf.vs_path)

if conf.execute_aivle == 'True':
    aivle_login.run()
