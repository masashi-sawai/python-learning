# ファイル名リネーム簡易ツール
# Win環境にてファイル名を「フォルダ名_連番.拡張子」にリネームする
# リネーム時は対象フォルダのコピーを利用する

import os
import glob
import shutil
import datetime

today = datetime.datetime.utcnow().date()
now = datetime.datetime.now().time()

dr_org = os.getcwd() + '/Image/'
dr = os.getcwd() + '\\' + \
    dr_org.split('/')[-2] + '_' + str(today) + '_' + str(now).replace(':', '')
shutil.copytree(dr_org, dr)
dr_list = glob.glob(dr + '/*')

for no in dr_list:
    file_list = glob.glob(no + '\\*.*')
    file_list.sort()
    for cnt, path in enumerate(file_list):
        path_array = path.replace('\\', '/').split('/')
        new_filename = path_array[-2] + '_' + \
            str(cnt + 1) + '.' + path_array[-1].split('.')[-1]
        new_path_array = path_array
        new_path_array[-1] = new_filename
        new_path = ','.join(new_path_array).replace(',', '/')
        print(path.replace('\\', '/'))
        print('⇒ Rename：' + new_path)
        print('----')
        os.rename(path, new_path)

print('* complate *')
