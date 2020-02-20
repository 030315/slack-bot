import pandas as pd
import mysql.connector
import datetime

conn = None

def main():
  # mysql 接続
  connect()
  # メンバー取得
  members_df = getMembers()
  # 最大のグループIDを取得
  max_group_id = members_df['group_id'].max()
  # 現在のグループIDを取得
  group_id = getGroup()

  next_group_id = 0
  if max_group_id < (group_id + 1):
    next_group_id = 1
  else:
    next_group_id = group_id + 1

  next_clean_members = members_df[members_df['group_id'] == next_group_id]
  slack_user_names = next_clean_members['slack_user_name'].values.tolist()

  user_list = ''
  for slack_user_name in slack_user_names:
    user_list += '@' + slack_user_name + ' '

  updateGroup(next_group_id)

  print('次週の掃除当番は ' + user_list + 'です。頑張ってください。')

def connect():
  global conn
  conn = mysql.connector.connect(user='root', password='', host='localhost', database='useful')

def getMembers():
  cur = conn.cursor()
  cur.execute('select * from useful_members')

  members = []
  for row in cur.fetchall():
      members.append({
        'id': row[0],
        'name1': row[1],
        'name2': row[2],
        'slack_user_name': row[3],
        'group_id': row[4]
      })

  cur.close

  df = pd.DataFrame(members)
  return df

def getGroup():
  cur = conn.cursor()
  cur.execute('select * from useful_clean')

  row = cur.fetchone()
  cur.close

  return row[2]

def updateGroup(next_group_id):
  cur = conn.cursor()
  now =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  sql = 'update useful_clean set clean_group_id = ' + str(next_group_id) + ', updated = \'' + now + '\' where id = 1'
  cur.execute(sql)
  conn.commit()
  cur.close

if __name__ == "__main__":
    main()

    conn.close

