import os

# 현재 디렉토리
current_directory = os.getcwd()
print(current_directory)

# 현재 디렉토리의 파일 목록 가져오기
for filename in os.listdir(current_directory):
    # 공백 또는 쉼표가 포함된 파일 처리
    if " " in filename or "," in filename:
        # 공백과 쉼표를 언더바로 대체
        new_filename = filename.replace(" ", "_").replace(",", "_")
        
        # 파일 이름 변경
        os.rename(os.path.join(current_directory, filename), os.path.join(current_directory, new_filename))
        print(f'Renamed: "{filename}" -> "{new_filename}"')

# 다시 파일 목록 가져오기
for filename in os.listdir(current_directory):
    # 연속된 언더바를 단일 언더바로 정리
    if "__" in filename:
        new_filename = filename
        while "__" in new_filename:
            new_filename = new_filename.replace("__", "_")
        
        # 파일 이름 변경
        os.rename(os.path.join(current_directory, filename), os.path.join(current_directory, new_filename))
        print(f'Cleaned: "{filename}" -> "{new_filename}"')

print("All files processed and cleaned!")
