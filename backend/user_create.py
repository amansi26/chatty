import phonenumbers

def create_user_db(conn, user_num, pwd):
    try:
        num = phonenumbers.parse(user_num, 'IN')
        if not phonenumbers.is_valid_number(num):
            return
        user_num = int(user_num)
        user_entry = conn.execute('INSERT INTO user(user_number,passwd) VALUES (?,?);', (user_num, pwd,))
        conn.commit()
        conn.close()
        return True
    except:
        return

def remove_user_db(conn, user_num):
    try:
        cur = conn.cursor()
        user_num = int(user_num)
        cur.execute("SELECT user_number FROM user WHERE user_number=?", (user_num,))
        data = cur.fetchall()
        if data is None:
            return
        else:
            user_entry = conn.execute('DELETE FROM user WHERE user_number=?;', (user_num,))
            conn.commit()
            conn.close()
            return True
    except:
        return

