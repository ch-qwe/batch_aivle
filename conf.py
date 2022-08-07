import os
import json

conf = ''
with open('config.json', 'r') as conf_json:
    conf = json.load(conf_json)

execute_teams = conf['execute_teams']
"""_summary_\n
    teams 프로그램 실행 여부
    실행 시 True 문자열 
"""
teams_path = conf['teams_path']
"""_summary_\n
    teams 프로그램 절대 경로 입니다.
"""
teams_file_name = conf['teams_file_name']
"""_summary_\n
    teams 프로그램 확장자를 포함한 이름 입니다
"""

execute_jupyter = conf['execute_jupyter']
"""_summary_\n
    jupyter 프로그램 실행 여부
    실행 시 True 문자열 
"""
jupyter_path = conf['jupyter_path']
"""_summary_\n
     jupyter 프로그램 절대 경로 입니다.
"""
jupyter_file_name = conf['jpuyter_file_name']
"""_summary_\n
    jupyter 프로그램 확장자를 포함한 이름 입니다
"""

execute_vs = conf['execute_vs']
"""_summary_\n
    visual_code 프로그램 실행 여부
    실행 시 True 문자열 
"""
vs_path = conf['vs_path']
"""_summary_\n
    vs_code 프로그램 절대 경로 입니다.
"""

vs_file_name = conf['vs_file_name']
"""_summary_\n
    jupyter 프로그램 확장자를 포함한 이름 입니다
"""

execute_aivle = conf['execute_aivle']
"""_summary_\n
    aivle_edu 로그인 프로세스 실행 여부
    실행 시 True 문자열 
"""
id = conf['id']
"""_summary_\n
    aivle_edu 로그인 아이디 입니다.
"""
pw = conf['pw']
"""_summary_\n
    aivle_edu 로그인 비밀번호 입니다.
"""
chrome_path = conf['chrome_path']
"""_summary_\n
    크롬 실행경로 입니다.\n
    chrome.exe 를 제외한 절대 경로입니다.\n
    X 크롬 드라이버가 아님니다.
"""
chromedriver_path = conf['chromedriver_path']
"""_summary_\n
    크롬 드라이버 실행 경로입니다.\n
    chromedriver.exe 를 포함한 절대경로 입니다.
"""
run_cmd = conf['run_cmd']
"""_summary_\n
    크롬 디버그 모드 실행 명려어 입니다.\n
    start chrome.exe --remote-debugging-port=9222 --user-data-dir=C:/Chrome_temp
"""
url_aivle = conf['url_aivle']
"""_summary_\n
    aivle_edu url 주소 입니다.
"""
id_path = conf['id_path']
"""_summary_\n
    aivle_edu 아이디 input 태그 css 셀렉터 경로 입니다.
"""
pw_path = conf['pw_path']
"""_summary_\n
    aivle_edu 비밀번호 input 태그 css 셀렉터 경로 입니다.
"""
btn_path = conf['btn_path']
"""_summary_\n
    aivle_edu 확인버튼 button 태그 css 셀렉터 경로 입니다.
"""

otp_path = conf['otp_path']
"""_summary_\n
    aivle_edu otp input 태그 css 셀렉터 경로 입니다.
"""
