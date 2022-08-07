import os


def execute(file_name, file_path="."):
    """_summary_
        프로그램 실행 함수 입니다.
    Args:
        file_name (str): 확장자를 포함한 파일 이름.
        file_path (str): 파일 위치를 나타내는 절대 값 경로
    """
    os.chdir(file_path)
    print(os.getcwd())
    print(file_name)
    result_code = os.system("start "+file_name)
    if result_code == 0:
        print('정상 실행')
    else:
        print('실행 오류')
