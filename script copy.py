import subprocess
import datetime
last_time=None
import os
def perform_backup():

    # 定义数据库信息
    db_user = "debian-sys-maint"
        #>??????????????????

    db_password = "RjI7wk8AMqrG9GCD"

    db_name = "test"
    current_directory='/home/yjy'
    ls=os.listdir(current_directory+"/sql")
    exist_date=[]
    exist_date2=[]
    today=datetime.datetime.today()
    exist_date.append(today.strftime("%Y-%m-%d")+".sql")
    exist_date2.append(today.strftime("%Y-%m-%d")+".sql")
    one_day=datetime.timedelta(days=1)
    for i in range(0,6):
        today= today - one_day
        exist_date.append(today.strftime("%Y-%m-%d")+".sql")
        if i>=2:
            continue
        exist_date2.append(today.strftime("%Y-%m-%d")+".sql")
    for file in ls:
        if file.endswith(".sql"):
            if file in exist_date:
                continue
            os.remove(current_directory+"/sql/"+file)



    # # # 定义备份文件名，包含当前日期
    backup_file = datetime.datetime.now().strftime('%Y-%m-%d')+".sql"
    subprocess.run('export MYSQL_PWD=RjI7wk8AMqrG9GCD',shell=True)
    # 构建 mysqldump 命令
    command = f"mysqldump -u "+db_user+"  "+db_name+" > "+current_directory+"/sql/"+backup_file

    # 使用 subprocess 执行命令
    subprocess.run(command, shell=True)

# 创建一个调度器
# scheduler = BlockingScheduler()

# 设置每天凌晨的定时任务
# scheduler.add_job(perform_backup, 'interval', days=1, start_date='2023-08-30 15:28:00')
# scheduler.add_job(perform_backup, 'interval', minutes=1, start_date='2023-08-30 15:28:00')

# 启动调度器
# scheduler.start()
perform_backup()
