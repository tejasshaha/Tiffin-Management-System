import smtplib
from random import randint
from werkzeug.security import generate_password_hash, check_password_hash
from passlib.hash import sha256_crypt
import datetime
import MySQLdb
from flask import Flask, redirect, url_for, render_template, request, json, session

app = Flask(__name__)

db = MySQLdb.connect(host="localhost",  # your host
                     user="root",  # username
                     passwd="root",  # password
                     db="pvg")  # name of the database


@app.route('/golden_customers', methods=['GET', 'POST'])
def golden_customers():
    cur = db.cursor()
    cur.execute("select * from payment where month(curdate())-month(pdate)>=03")
    data = cur.fetchall()
    user = {'first_name': []}
    for row in data:
        user['first_name'].append(row[0])

    return render_template("golden_customers.html",user=user)


@app.route('/account_details', methods=['GET', 'POST'])
def account_details():
    labels = [
        'JAN', 'FEB', 'MAR', 'APR',
        'MAY', 'JUN', 'JUL', 'AUG',
        'SEP', 'OCT', 'NOV', 'DEC'
    ]
    l1 = []
    l = []
    lv = []

    cur = db.cursor()
    cur.execute("select month(pdate) from payment group by month(pdate) order by month(pdate)")
    data = cur.fetchall()

    for row1 in data:
        l.append(row1[0])

    cur = db.cursor()
    cur.execute("select  count(distinct(month(pdate))) from payment")
    data = cur.fetchall()

    for row1 in data:
        m = row1[0]

    for i in range(m):
        l1.append(labels[l[i] - 1])

    cur = db.cursor()
    cur.execute("SELECT sum(amount) FROM payment GROUP BY month(pdate) order by month(pdate)")
    data = cur.fetchall()

    for row in data:
        lv.append(row[0])

    colors = [
        "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
        "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
        "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

    bar_labels = l1
    bar_values = lv

    cur = db.cursor()
    cur.execute("SELECT * from payment")
    data = cur.fetchall()
    print(data)
    user = {'first_name': [], 'pdate': [], 'amount': [], 'type': []}
    for row in data:
        user['first_name'].append(row[0])
        user['pdate'].append(row[1])
        user['amount'].append(row[2])
        user['type'].append(row[3])

    return render_template('bar_chart.html', title='Monthly Collection of money', max=15000, labels=bar_labels,
                           values=bar_values, user=user)


@app.route('/flow', methods=['GET', 'POST'])
def flow():
    return render_template("flow.html")


@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    return render_template("contact_us.html")


@app.route('/todays_order', methods=['GET', 'POST'])
def todays_order():
    cur = db.cursor()
    cur.execute("SELECT * from t where Date=curdate() ")
    data = cur.fetchall()
    print(data)
    user = {'U_name': [], 'Name': [], 'Phone': [], 'Address': [], 'Type': [], 'D_boy_name': []}
    for row in data:
        user['U_name'].append(row[0])
        user['Name'].append(row[1])
        user['Phone'].append(row[2])
        user['Address'].append(row[3])
        user['Type'].append(row[4])
        user['D_boy_name'].append(row[5])

    return render_template("todays_order.html", user=user)


@app.route('/admin_select', methods=['GET', 'POST'])
def admin_select():
    date = datetime.date.today()
    if request.method == 'POST':
        user = {'name': []}
        if request.form.getlist('bhendi_fry'):
            temp = "Bhendi Fry"
            price = 30
            cur = db.cursor()
            query = "INSERT INTO admin_main(Main_Course,Date,price) VALUES(%s,%s,%s)"
            cur.execute(query, (temp, date, price))
            db.commit()

        #            user['name'].append(temp)

        if request.form.getlist('palak_paneer'):
            temp = "Palak Paneer"
            price = 40
            cur = db.cursor()
            query = "INSERT INTO admin_main(Main_Course,Date,price) VALUES(%s,%s,%s)"
            cur.execute(query, (temp, date, price))
            db.commit()

        #           user['name'].append(temp)

        if request.form.getlist('turai'):
            temp = "Turai"
            price = 30
            cur = db.cursor()
            query = "INSERT INTO admin_main(Main_Course,Date,price) VALUES(%s,%s,%s)"
            cur.execute(query, (temp, date, price))
            db.commit()

        #          user['name'].append(temp)

        if request.form.getlist('aloo_lahsuni'):
            temp = "Aloo Lahsuni"
            price = 30
            cur = db.cursor()
            query = "INSERT INTO admin_main(Main_Course,Date,price) VALUES(%s,%s,%s)"
            cur.execute(query, (temp, date, price))
            db.commit()

        #            user['name'].append(temp)

        if request.form.getlist('jain_daal'):
            temp = "Jain Daal"
            price = 30
            cur = db.cursor()
            query = "INSERT INTO admin_main(Main_Course,Date,price) VALUES(%s,%s,%s)"
            cur.execute(query, (temp, date, price))
            db.commit()

        if request.form.getlist('plain_roti'):
            temp = "Plain Roti"
            price = 6
            cur = db.cursor()
            query = "INSERT INTO admin_rotis(Rotis,Date,price) VALUES(%s,%s,%s)"
            cur.execute(query, (temp, date, price))
            db.commit()

        if request.form.getlist('phulkaa'):
            temp = "Phulkaa"
            price = 5
            cur = db.cursor()
            query = "INSERT INTO admin_rotis(Rotis,Date,price) VALUES(%s,%s,%s)"
            cur.execute(query, (temp, date, price))
            db.commit()

        if request.form.getlist('fried_rice'):
            temp = "Fried Rice"
            price = 40
            cur = db.cursor()
            query = "INSERT INTO admin_rice(Rice,Date,price) VALUES(%s,%s,%s)"
            cur.execute(query, (temp, date, price))
            db.commit()

        if request.form.getlist('paneer_pulav'):
            temp = "Paneer Pulav"
            price = 50
            cur = db.cursor()
            query = "INSERT INTO admin_rice(Rice,Date,price) VALUES(%s,%s,%s)"
            cur.execute(query, (temp, date, price))
            db.commit()

        if request.form.getlist('shrikhand'):
            temp = "Shrikhand"
            price = 25
            cur = db.cursor()
            query = "INSERT INTO admin_sweets(Sweets,Date,price) VALUES(%s,%s,%s)"
            cur.execute(query, (temp, date, price))
            db.commit()

        if request.form.getlist('gulab_jamun'):
            temp = "Gulab jamun"
            price = 25
            cur = db.cursor()
            query = "INSERT INTO admin_sweets(Sweets,Date,price) VALUES(%s,%s,%s)"
            cur.execute(query, (temp, date, price))
            db.commit()

        if request.form.getlist('masala_chaas'):
            temp = "Masala Chaas"
            price = 25
            cur = db.cursor()
            query = "INSERT INTO admin_accompaniments(Accompaniments,Date,price) VALUES(%s,%s,%s)"
            cur.execute(query, (temp, date, price))
            db.commit()

        if request.form.getlist('curd'):
            temp = "Curd"
            price = 20
            cur = db.cursor()
            query = "INSERT INTO admin_accompaniments(Accompaniments,Date,price) VALUES(%s,%s,%s)"
            cur.execute(query, (temp, date, price))
            db.commit()

    cur = db.cursor()
    cur.execute(
        "SELECT Main_Course,price from admin_main where Date=curdate() AND Main_Course !='Bhendi Fry' AND Main_Course !='Palak Paneer' AND Main_Course !='Turai' AND Main_Course !='Aloo Lahsuni' AND Main_Course !='Jain Daal'")
    data = cur.fetchall()
    print(data)
    user = {'M_course': [], 'price': []}
    for row in data:
        user['M_course'].append(row[0])
        user['price'].append(row[1])

    cur.execute(
        "SELECT Rice,price from admin_rice where Date=curdate() AND Rice!='Fried Rice' AND Rice!='Paneer Pulav'")
    data = cur.fetchall()
    print(data)
    user1 = {'Rice': [], 'price': []}
    for row in data:
        user1['Rice'].append(row[0])
        user1['price'].append(row[1])

    cur.execute("SELECT Rotis,price from admin_rotis where Date=curdate() AND Rotis!='Plain Roti' AND Rotis!='Phulkaa'")
    data = cur.fetchall()
    print(data)
    user2 = {'Rotis': [], 'price': []}
    for row in data:
        user2['Rotis'].append(row[0])
        user2['price'].append(row[1])

    cur.execute(
        "SELECT Sweets,price from admin_sweets where Date=curdate() AND Sweets!='Shrikhand' AND Sweets!='Gulab Jamun'")
    data = cur.fetchall()
    print(data)
    user3 = {'Sweets': [], 'price': []}
    for row in data:
        user3['Sweets'].append(row[0])
        user3['price'].append(row[1])

    cur.execute(
        "SELECT Accompaniments,price from admin_accompaniments where Date=curdate() AND Accompaniments!='Masala Chaas' AND Accompaniments!='Curd'")
    data = cur.fetchall()
    print(data)
    user4 = {'Accompaniments': [], 'price': []}
    for row in data:
        user4['Accompaniments'].append(row[0])
        user4['price'].append(row[1])

    return render_template("admin_select.html", user=user, user1=user1, user2=user2, user3=user3, user4=user4)


@app.route('/Add_vegetables', methods=['GET', 'POST'])
def Add_vegetables():
    date = datetime.date.today()
    if request.method == 'POST':
        type = request.form['vegetable']
        price = request.form['price']
        cur = db.cursor()
        query = "INSERT INTO admin_main(Main_course,price,Date) VALUES(%s,%s,%s)"
        cur.execute(query, (type, price, date))
        db.commit()

    return render_template("Add_vegetables.html")


@app.route('/Add_accompaniments', methods=['GET', 'POST'])
def Add_accompaniments():
    date = datetime.date.today()
    if request.method == 'POST':
        type = request.form['accompaniments']
        price = request.form['price']
        cur = db.cursor()
        query = "INSERT INTO admin_accompaniments(Accompaniments,price,Date) VALUES(%s,%s,%s)"
        cur.execute(query, (type, price, date))
        db.commit()

    return render_template("Add_accompaniments.html")


@app.route('/Add_rice', methods=['GET', 'POST'])
def Add_rice():
    date = datetime.date.today()
    if request.method == 'POST':
        type = request.form['rice']
        price = request.form['price']
        cur = db.cursor()
        query = "INSERT INTO admin_rice(Rice,price,Date) VALUES(%s,%s,%s)"
        cur.execute(query, (type, price, date))
        db.commit()
    return render_template("Add_rice.html")


@app.route('/Add_sweets', methods=['GET', 'POST'])
def Add_sweets():
    date = datetime.date.today()
    if request.method == 'POST':
        type = request.form['sweet']
        price = request.form['price']
        cur = db.cursor()
        query = "INSERT INTO admin_sweets(Sweets,price,Date) VALUES(%s,%s,%s)"
        cur.execute(query, (type, price, date))
        db.commit()

    return render_template("Add_sweet.html")


@app.route('/Add_rotis', methods=['GET', 'POST'])
def Add_rotis():
    date = datetime.date.today()
    if request.method == 'POST':
        type = request.form['rotis']
        price = request.form['price']
        cur = db.cursor()
        query = "INSERT INTO admin_rotis(Rotis,price,Date) VALUES(%s,%s,%s)"
        cur.execute(query, (type, price, date))
        db.commit()

    return render_template("Add_rotis.html")


@app.route('/add_main_course', methods=['GET', 'POST'])
def add_main_course():
    return render_template("add_main_course.html")


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    count = 0
    date = datetime.date.today()
    cur = db.cursor()

    cur.execute("SELECT * from admin_main where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user = {'name': [], 'price': []}
    # user1={'U_name':a}
    for row in data:
        user['name'].append(row[1])
        user['price'].append(row[2])

    cur.execute("SELECT * from admin_rotis where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user1 = {'name': [], 'price': []}
    for row in data:
        user1['name'].append(row[1])
        user1['price'].append(row[2])

    cur.execute("SELECT * from admin_rice where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user2 = {'name': [], 'price': []}
    for row in data:
        user2['name'].append(row[1])
        user2['price'].append(row[2])

    cur.execute("SELECT * from admin_sweets where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user3 = {'name': [], 'price': []}
    for row in data:
        user3['name'].append(row[1])
        user3['price'].append(row[2])

    cur.execute("SELECT * from admin_accompaniments where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user4 = {'name': [], 'price': []}
    for row in data:
        user4['name'].append(row[1])
        user4['price'].append(row[2])

    return render_template("menu.html", user=user, user1=user1, user2=user2, user3=user3, user4=user4)


@app.route('/aboutus', methods=['GET', 'POST'])
def aboutus():
    return render_template("aboutus.html")


@app.route('/faq', methods=['GET', 'POST'])
def faq():
    return render_template("faqs.html")


@app.route('/add_comment-<a>', methods=['GET', 'POST'])
def add_comment(a):
    cur = db.cursor()
    query = " SELECT * from sign_up where U_name='" + a + "'"
    cur.execute(query)
    data1 = cur.fetchone()
    userr = {'name': data1[0], 'U_name': a}
    date = datetime.date.today()
    if request.method == 'POST':
        comment = request.form['comment']
        cur = db.cursor()
        query = "INSERT INTO comment VALUES(%s,%s)"
        cur.execute(query, (comment, date))
        db.commit()

    return render_template("add_comment.html", userr=userr)


@app.route('/comment', methods=['GET', 'POST'])
def comment():
    cur = db.cursor()
    user = {'comment': []}
    cur.execute("Select * from comment where date=curdate()")
    data = cur.fetchall()
    print(data)
    for row in data:
        user['comment'].append(row[0])
    return render_template("comment.html", user=user)


@app.route('/cust_details2', methods=['GET', 'POST'])
def cust_details2():
    if request.method == 'POST':
        first_name = request.form['fname']
        date = request.form['date']
        cur = db.cursor()
        query = " SELECT * from half_main where Date='" + date + "' AND U_name='" + first_name + "' UNION ALL SELECT * from half_extra_rotis where Date='" + date + "' AND U_name='" + first_name + "'UNION ALL SELECT * from half_extra_rice where Date='" + date + "' AND U_name='" + first_name + "' UNION ALL SELECT * from half_extra_sweets where Date='" + date + "' AND U_name='" + first_name + "' UNION ALL SELECT * from half_extra_accompaniments where Date='" + date + "' AND U_name='" + first_name + "'"
        cur.execute(query)
        data1 = cur.fetchall()
        # print(data1)
        user = {'Main': [], 'Quantity': [], 'Cost': []}
        for row1 in data1:
            user['Main'].append(row1[2])
            user['Quantity'].append(row1[3])
            user['Cost'].append(row1[4])
        return render_template("details_cust.html", user=user)
    return render_template("cust_details.html", )


@app.route('/cust_details1', methods=['GET', 'POST'])
def cust_details1():
    if request.method == 'POST':
        first_name = request.form['fname']
        date = request.form['date']
        cur = db.cursor()
        query = " SELECT * from full_main where Date='" + date + "' AND U_name='" + first_name + "' UNION ALL SELECT * from full_extra_rotis where Date='" + date + "' AND U_name='" + first_name + "'UNION ALL SELECT * from full_extra_rice where Date='" + date + "' AND U_name='" + first_name + "' UNION ALL SELECT * from full_extra_sweets where Date='" + date + "' AND U_name='" + first_name + "' UNION ALL SELECT * from full_extra_accompaniments where Date='" + date + "' AND U_name='" + first_name + "'"
        cur.execute(query)
        data1 = cur.fetchall()
        # print(data1)
        user = {'Main': [], 'Quantity': [], 'Cost': []}
        for row1 in data1:
            user['Main'].append(row1[2])
            user['Quantity'].append(row1[3])
            user['Cost'].append(row1[4])
        return render_template("details_cust.html", user=user)
    return render_template("cust_details.html", )


@app.route('/cust_details-<a>', methods=['GET', 'POST'])
def cust_details(a):
    if request.method == 'POST':
        first_name = request.form['fname']
        date = request.form['date']
        cur = db.cursor()
        query = " SELECT * from guest_main where Date='" + date + "' AND U_name='" + first_name + "' UNION ALL SELECT * from guest_rotis where Date='" + date + "' AND U_name='" + first_name + "'UNION ALL SELECT * from guest_rice where Date='" + date + "' AND U_name='" + first_name + "' UNION ALL SELECT * from guest_sweets where Date='" + date + "' AND U_name='" + first_name + "' UNION ALL SELECT * from guest_accompaniments where Date='" + date + "' AND U_name='" + first_name + "'"
        cur.execute(query)
        data1 = cur.fetchall()
        # print(data1)

        user = {'Main': [], 'Quantity': [], 'Cost': []}

        for row1 in data1:
            user['Main'].append(row1[2])
            user['Quantity'].append(row1[3])
            user['Cost'].append(row1[4])
        return render_template("details_cust.html", user=user)

    return render_template("cust_details.html", user=a)


@app.route('/payh', methods=['GET', 'POST'])
def payh():
    return render_template("payh.html")


@app.route('/payf', methods=['GET', 'POST'])
def payf():
    return render_template("payf.html")


@app.route('/pay', methods=['GET', 'POST'])
def pay():
    return render_template("pay.html")


@app.route('/update_profile-<a>', methods=['GET', 'POST'])
def update_profile(a):
    if request.method == 'POST':
        first_name = request.form['fname']
        email = request.form['email']
        phone = request.form['phone']
        area = request.form['area']
        address = request.form['address']
        password = request.form['password']
        cur = db.cursor()
        cur.execute("UPDATE sign_up set first_name='" + first_name + "' where U_name ='" + a + "'")
        cur.execute("UPDATE sign_up set email='" + email + "' where U_name ='" + a + "'")
        cur.execute("UPDATE sign_up set phone='" + phone + "' where U_name ='" + a + "'")
        cur.execute("UPDATE sign_up set area='" + area + "' where U_name ='" + a + "'")
        cur.execute("UPDATE sign_up set address='" + address + "' where U_name ='" + a + "'")
        cur.execute("UPDATE sign_up set password='" + generate_password_hash(password) + "' where U_name ='" + a + "'")
        db.commit()
    return render_template("update_profile.html",a=a)


@app.route('/view_profile-<a>', methods=['GET', 'POST'])
def view_profile(a):
    cur = db.cursor()
    cur.execute("Select * from sign_up where U_name ='" + a + "'")
    data = cur.fetchone()
    user = {'U_name': a, 'name': data[0], 'email': data[1], 'phone': data[2], 'area': data[3], 'address': data[4]}
    return render_template("view_profile.html", user=user)


@app.route('/successful', methods=['GET', 'POST'])
def successful():
    return render_template("successful.html")


@app.route('/bill2-<a>', methods=['GET', 'POST'])
def bill2(a):
    i = 100
    date = datetime.date.today()
    cur = db.cursor()
    cur.execute("Select * from sign_up where U_name ='" + a + "'")
    data = cur.fetchone()
    # print(data)
    i += 1
    o = ("OR" + str(randint(100, 999)))
    user = {'name': data[0], 'Address': data[4], 'id': o}
    # user1={'U_name':a}

    if cur.execute("Select area from sign_up where U_name ='" + a + "'"):
        user1 = {'area': data[3]}
        trs = {'name': a}
        #   print(user1)
        if cur.execute("Select * from delievery_boy_details where area1 ='" + user1['area'] + "' OR area2 ='" + user1[
            'area'] + "' OR area3 ='" + user1['area'] + "' OR area4 ='" + user1['area'] + "'"):
            data = cur.fetchone()
            #      print(data)
            user2 = {'D_name': data[1], 'Mobile': data[6]}

            cur.execute("Select first_name,phone,type from sign_up where U_name ='" + a + "'")
            data = cur.fetchone()
            std = {'name': data[0], 'phone': data[1], 'type': data[2]}

            query = "INSERT INTO t VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query, ([a], std['name'], std['phone'], user1['area'], std['type'], user2['D_name'], date))
            db.commit()

    # cur.execute("SELECT * from guest_main where where and Date=curdate() U_name ='" + a + "'")
    user3 = {'M_course': [], 'Quantity': [], 'Cost': []}

    cur.execute("Select * from half_extra_rice where U_name ='" + a + "'  AND Date=curdate()")
    data1 = cur.fetchall()
    # print(data1)

    for row1 in data1:
        user3['M_course'].append(row1[2])
        user3['Quantity'].append(row1[3])
        user3['Cost'].append(row1[4])

    cur.execute("Select * from half_extra_rotis where U_name ='" + a + "'  AND Date=curdate()")
    data2 = cur.fetchall()
    # print(data2)

    for row2 in data2:
        user3['M_course'].append(row2[2])
        user3['Quantity'].append(row2[3])
        user3['Cost'].append(row2[4])

    cur.execute("Select * from half_extra_sweets where U_name ='" + a + "'  AND Date=curdate()")
    data3 = cur.fetchall()
    # print(data3)

    for row3 in data3:
        user3['M_course'].append(row3[2])
        user3['Quantity'].append(row3[3])
        user3['Cost'].append(row3[4])

    cur.execute("Select * from half_extra_accompaniments where U_name ='" + a + "'  AND Date=curdate()")
    data4 = cur.fetchall()
    # print(data4)

    for row4 in data4:
        user3['M_course'].append(row4[2])
        user3['Quantity'].append(row4[3])
        user3['Cost'].append(row4[4])

    cur.execute(
        "SELECT SUM(totalHours) Cost FROM ( select sum(Cost) totalHours from half_extra_rice where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from half_extra_rotis where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from half_extra_sweets where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from half_extra_accompaniments where U_name ='" + a + "'  AND Date=curdate()) s")
    data5 = cur.fetchone()
    print(data5)
    user4 = {'Cost': data5[0]}

    def sendNotification():
        cur.execute("Select * from sign_up where U_name ='" + a + "'")
        data = cur.fetchone()

        recepients_list = data[1]
        subject = 'Delivery'
        message = "Hello " + data[0] + ",\n Thank you for ordering.\nYour meal will be delivered soon..."
        sendemail(recepients_list, subject, message)

    def sendemail(to_addr_list, subject, message):
        cur.execute("Select * from sign_up where U_name ='" + a + "'")
        data = cur.fetchone()

        recepients_list = data[1]
        username = 'tejasshaha1998@gmail.com'
        password = 'risingphoenix@123'
        from_addr = 'tejasshaha1998@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        newmessage = '\r\n'.join([
            'To: %s' % recepients_list,
            'From: %s' % from_addr,
            'Subject: %s' % subject,
            '',
            message
        ])
        try:
            server.sendmail(from_addr, to_addr_list, newmessage)

        except:
            print("error sending notification")
        server.quit()

    sendNotification()

    return render_template("bill2.html", trs=trs, user=user, user2=user2, user3=user3, user4=user4)


@app.route('/cancel2-<a>', methods=['GET', 'POST'])
def cancel2(a):
    cur = db.cursor()

    cur.execute("Select * from sign_up where U_name ='" + a + "'")
    data = cur.fetchone()
    # print(data)
    user = {'name': data[0], 'U_name': data[7]}

    cur.execute("Delete from half_main where U_name ='" + a + "'  AND Date=curdate()")
    cur.execute("Delete from half_extra_rice where U_name ='" + a + "'  AND Date=curdate()")
    cur.execute("Delete from half_extra_rotis where U_name ='" + a + "'  AND Date=curdate()")
    cur.execute("Delete from half_extra_sweets where U_name ='" + a + "'AND Date=curdate()")
    cur.execute("Delete from half_extra_accompaniments where U_name ='" + a + "'  AND Date=curdate()")
    cur.execute("Delete from t where U_name ='" + a + "'  AND Date=curdate()")
    #  cur.execute("Delete from payment where first_name ='" + user['name'] + "'  AND pdate=curdate()")
    db.commit()
    #   "<script>alert('Incorrect Username Or Password.Re-Enter it :)')</script>"
    return render_template("cancel2.html", user=user)


@app.route('/download2-<a>', methods=['GET', 'POST'])
def download2(a):
    i = 100
    date = datetime.date.today()
    cur = db.cursor()
    cur.execute("Select * from sign_up where U_name ='" + a + "'")
    data = cur.fetchone()
    # print(data)
    i += 1
    o = ("OR" + str(randint(100, 999)))
    user = {'name': data[0], 'Address': data[4], 'id': o}
    # user1={'U_name':a}

    if cur.execute("Select area from sign_up where U_name ='" + a + "'"):
        user1 = {'area': data[3]}
        trs = {'name': a}
        #   print(user1)
        if cur.execute("Select * from delievery_boy_details where area1 ='" + user1['area'] + "' OR area2 ='" + user1[
            'area'] + "' OR area3 ='" + user1['area'] + "' OR area4 ='" + user1['area'] + "'"):
            data = cur.fetchone()
            #      print(data)
            user2 = {'D_name': data[1], 'Mobile': data[6]}

            cur.execute("Select first_name,phone,type from sign_up where U_name ='" + a + "'")
            data = cur.fetchone()
            std = {'name': data[0], 'phone': data[1], 'type': data[2]}

            query = "INSERT INTO t VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query, ([a], std['name'], std['phone'], user1['area'], std['type'], user2['D_name'], date))
            db.commit()

    # cur.execute("SELECT * from guest_main where where and Date=curdate() U_name ='" + a + "'")
    user3 = {'M_course': [], 'Quantity': [], 'Cost': []}

    cur.execute("Select * from half_extra_rice where U_name ='" + a + "'  AND Date=curdate()")
    data1 = cur.fetchall()
    # print(data1)

    for row1 in data1:
        user3['M_course'].append(row1[2])
        user3['Quantity'].append(row1[3])
        user3['Cost'].append(row1[4])

    cur.execute("Select * from half_extra_rotis where U_name ='" + a + "'  AND Date=curdate()")
    data2 = cur.fetchall()
    # print(data2)

    for row2 in data2:
        user3['M_course'].append(row2[2])
        user3['Quantity'].append(row2[3])
        user3['Cost'].append(row2[4])

    cur.execute("Select * from half_extra_sweets where U_name ='" + a + "'  AND Date=curdate()")
    data3 = cur.fetchall()
    # print(data3)

    for row3 in data3:
        user3['M_course'].append(row3[2])
        user3['Quantity'].append(row3[3])
        user3['Cost'].append(row3[4])

    cur.execute("Select * from half_extra_accompaniments where U_name ='" + a + "'  AND Date=curdate()")
    data4 = cur.fetchall()
    # print(data4)

    for row4 in data4:
        user3['M_course'].append(row4[2])
        user3['Quantity'].append(row4[3])
        user3['Cost'].append(row4[4])

    cur.execute(
        "SELECT SUM(totalHours) Cost FROM ( select sum(Cost) totalHours from half_extra_rice where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from half_extra_rotis where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from half_extra_sweets where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from half_extra_accompaniments where U_name ='" + a + "'  AND Date=curdate()) s")
    data5 = cur.fetchone()
    print(data5)
    user4 = {'Cost': data5[0]}

    return render_template("download.html", trs=trs, user=user, user2=user2, user3=user3, user4=user4)


@app.route('/bill1-<a>', methods=['GET', 'POST'])
def bill1(a):
    i = 100
    date = datetime.date.today()
    cur = db.cursor()
    cur.execute("Select * from sign_up where U_name ='" + a + "'")
    data = cur.fetchone()
    # print(data)
    i += 1
    o = ("OR" + str(randint(100, 999)))
    user = {'name': data[0], 'Address': data[4], 'id': o}
    # user1={'U_name':a}

    if cur.execute("Select area from sign_up where U_name ='" + a + "'"):
        user1 = {'area': data[3]}
        trs = {'name': a}
        #   print(user1)
        if cur.execute("Select * from delievery_boy_details where area1 ='" + user1['area'] + "' OR area2 ='" + user1[
            'area'] + "' OR area3 ='" + user1['area'] + "' OR area4 ='" + user1['area'] + "'"):
            data = cur.fetchone()
            #      print(data)
            user2 = {'D_name': data[1], 'Mobile': data[6]}

            cur.execute("Select first_name,phone,type from sign_up where U_name ='" + a + "'")
            data = cur.fetchone()
            std = {'name': data[0], 'phone': data[1], 'type': data[2]}

            query = "INSERT INTO t VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query, ([a], std['name'], std['phone'], user1['area'], std['type'], user2['D_name'], date))
            db.commit()

    # cur.execute("SELECT * from guest_main where where and Date=curdate() U_name ='" + a + "'")
    user3 = {'M_course': [], 'Quantity': [], 'Cost': []}

    cur.execute("Select * from full_extra_rice where U_name ='" + a + "'  AND Date=curdate()")
    data1 = cur.fetchall()
    # print(data1)

    for row1 in data1:
        user3['M_course'].append(row1[2])
        user3['Quantity'].append(row1[3])
        user3['Cost'].append(row1[4])

    cur.execute("Select * from full_extra_rotis where U_name ='" + a + "'  AND Date=curdate()")
    data2 = cur.fetchall()
    # print(data2)

    for row2 in data2:
        user3['M_course'].append(row2[2])
        user3['Quantity'].append(row2[3])
        user3['Cost'].append(row2[4])

    cur.execute("Select * from full_extra_sweets where U_name ='" + a + "'  AND Date=curdate()")
    data3 = cur.fetchall()
    # print(data3)

    for row3 in data3:
        user3['M_course'].append(row3[2])
        user3['Quantity'].append(row3[3])
        user3['Cost'].append(row3[4])

    cur.execute("Select * from full_extra_accompaniments where U_name ='" + a + "'  AND Date=curdate()")
    data4 = cur.fetchall()
    # print(data4)

    for row4 in data4:
        user3['M_course'].append(row4[2])
        user3['Quantity'].append(row4[3])
        user3['Cost'].append(row4[4])

    cur.execute(
        "SELECT SUM(totalHours) Cost FROM ( select sum(Cost) totalHours from full_extra_rice where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from full_extra_rotis where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from full_extra_sweets where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from full_extra_accompaniments where U_name ='" + a + "'  AND Date=curdate()) s")
    data5 = cur.fetchone()
    print(data5)
    user4 = {'Cost': data5[0]}

    def sendNotification():
        cur.execute("Select * from sign_up where U_name ='" + a + "'")
        data = cur.fetchone()

        recepients_list = data[1]
        subject = 'About Delivery'
        message = "Hello " + data[0] + ",\n Thank you for ordering.\nYour meal will be delivered soon..."
        sendemail(recepients_list, subject, message)

    def sendemail(to_addr_list, subject, message):
        cur.execute("Select * from sign_up where U_name ='" + a + "'")
        data = cur.fetchone()

        recepients_list = data[1]
        username = 'tejasshaha1998@gmail.com'
        password = 'risingphoenix@123'
        from_addr = 'tejasshaha1998@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        newmessage = '\r\n'.join([
            'To: %s' % recepients_list,
            'From: %s' % from_addr,
            'Subject: %s' % subject,
            '',
            message
        ])
        try:
            server.sendmail(from_addr, to_addr_list, newmessage)

        except:
            print("error sending notification")
        server.quit()

    sendNotification()

    return render_template("bill1.html", trs=trs, user=user, user2=user2, user3=user3, user4=user4)


@app.route('/download1-<a>', methods=['GET', 'POST'])
def download1(a):
    i = 100
    date = datetime.date.today()
    cur = db.cursor()
    cur.execute("Select * from sign_up where U_name ='" + a + "'")
    data = cur.fetchone()
    # print(data)
    i += 1
    o = ("OR" + str(randint(100, 999)))
    user = {'name': data[0], 'Address': data[4], 'id': o}
    # user1={'U_name':a}

    if cur.execute("Select area from sign_up where U_name ='" + a + "'"):
        user1 = {'area': data[3]}
        trs = {'name': a}
        #   print(user1)
        if cur.execute("Select * from delievery_boy_details where area1 ='" + user1['area'] + "' OR area2 ='" + user1[
            'area'] + "' OR area3 ='" + user1['area'] + "' OR area4 ='" + user1['area'] + "'"):
            data = cur.fetchone()
            #      print(data)
            user2 = {'D_name': data[1], 'Mobile': data[6]}

            cur.execute("Select first_name,phone,type from sign_up where U_name ='" + a + "'")
            data = cur.fetchone()
            std = {'name': data[0], 'phone': data[1], 'type': data[2]}

            query = "INSERT INTO t VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query, ([a], std['name'], std['phone'], user1['area'], std['type'], user2['D_name'], date))
            db.commit()

    # cur.execute("SELECT * from guest_main where where and Date=curdate() U_name ='" + a + "'")
    user3 = {'M_course': [], 'Quantity': [], 'Cost': []}

    cur.execute("Select * from full_extra_rice where U_name ='" + a + "'  AND Date=curdate()")
    data1 = cur.fetchall()
    # print(data1)

    for row1 in data1:
        user3['M_course'].append(row1[2])
        user3['Quantity'].append(row1[3])
        user3['Cost'].append(row1[4])

    cur.execute("Select * from full_extra_rotis where U_name ='" + a + "'  AND Date=curdate()")
    data2 = cur.fetchall()
    # print(data2)

    for row2 in data2:
        user3['M_course'].append(row2[2])
        user3['Quantity'].append(row2[3])
        user3['Cost'].append(row2[4])

    cur.execute("Select * from full_extra_sweets where U_name ='" + a + "'  AND Date=curdate()")
    data3 = cur.fetchall()
    # print(data3)

    for row3 in data3:
        user3['M_course'].append(row3[2])
        user3['Quantity'].append(row3[3])
        user3['Cost'].append(row3[4])

    cur.execute("Select * from full_extra_accompaniments where U_name ='" + a + "'  AND Date=curdate()")
    data4 = cur.fetchall()
    # print(data4)

    for row4 in data4:
        user3['M_course'].append(row4[2])
        user3['Quantity'].append(row4[3])
        user3['Cost'].append(row4[4])

    cur.execute(
        "SELECT SUM(totalHours) Cost FROM ( select sum(Cost) totalHours from full_extra_rice where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from full_extra_rotis where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from full_extra_sweets where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from full_extra_accompaniments where U_name ='" + a + "'  AND Date=curdate()) s")
    data5 = cur.fetchone()
    print(data5)
    user4 = {'Cost': data5[0]}

    return render_template("download.html", trs=trs, user=user, user2=user2, user3=user3, user4=user4)


@app.route('/cancel1-<a>', methods=['GET', 'POST'])
def cancel1(a):
    cur = db.cursor()

    cur.execute("Select * from sign_up where U_name ='" + a + "'")
    data = cur.fetchone()
    # print(data)
    user = {'name': data[0], 'U_name': data[7]}

    cur.execute("Delete from full_main where U_name ='" + a + "'  AND Date=curdate()")
    cur.execute("Delete from full_extra_rice where U_name ='" + a + "'  AND Date=curdate()")
    cur.execute("Delete from full_extra_rotis where U_name ='" + a + "'  AND Date=curdate()")
    cur.execute("Delete from full_extra_sweets where U_name ='" + a + "'AND Date=curdate()")
    cur.execute("Delete from full_extra_accompaniments where U_name ='" + a + "'  AND Date=curdate()")
    cur.execute("Delete from t where U_name ='" + a + "'  AND Date=curdate()")
    #  cur.execute("Delete from payment where first_name ='" + user['name'] + "'  AND pdate=curdate()")
    db.commit()
    #   "<script>alert('Incorrect Username Or Password.Re-Enter it :)')</script>"
    return render_template("cancel1.html", user=user)


@app.route('/bill-<a>', methods=['GET', 'POST'])
def bill(a):
    i = 100
    date = datetime.date.today()
    cur = db.cursor()
    cur.execute("Select * from sign_up where U_name ='" + a + "'")
    data = cur.fetchone()
    # print(data)
    i += 1
    o = ("OR" + str(randint(100, 999)))
    user = {'name': data[0], 'Address': data[4], 'id': o}
    # user1={'U_name':a}
    trs = {'name': a}
    if cur.execute("Select area from sign_up where U_name ='" + a + "'"):
        user1 = {'area': data[3]}
        #   print(user1)
        if cur.execute("Select * from delievery_boy_details where area1 ='" + user1['area'] + "' OR area2 ='" + user1[
            'area'] + "' OR area3 ='" + user1['area'] + "' OR area4 ='" + user1['area'] + "'"):
            data = cur.fetchone()
            #      print(data)
            user2 = {'D_name': data[1], 'Mobile': data[6]}
            print(user2)

            cur.execute("Select first_name,phone,type from sign_up where U_name ='" + a + "'")
            data = cur.fetchone()
            std = {'name': data[0], 'phone': data[1], 'type': data[2]}

            query = "INSERT INTO t VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query, ([a], std['name'], std['phone'], user1['area'], std['type'], user2['D_name'], date))
            db.commit()

    # cur.execute("SELECT * from guest_main where where and Date=curdate() U_name ='" + a + "'")
    user3 = {'M_course': [], 'Quantity': [], 'Cost': []}
    cur.execute("Select * from guest_main where U_name ='" + a + "'  AND Date=curdate()")
    data = cur.fetchall()
    # print(data)
    for row in data:
        user3['M_course'].append(row[2])
        user3['Quantity'].append(row[3])
        user3['Cost'].append(row[4])

    cur.execute("Select * from guest_rice where U_name ='" + a + "'  AND Date=curdate()")
    data1 = cur.fetchall()
    # print(data1)

    for row1 in data1:
        user3['M_course'].append(row1[2])
        user3['Quantity'].append(row1[3])
        user3['Cost'].append(row1[4])

    cur.execute("Select * from guest_rotis where U_name ='" + a + "'  AND Date=curdate()")
    data2 = cur.fetchall()
    # print(data2)

    for row2 in data2:
        user3['M_course'].append(row2[2])
        user3['Quantity'].append(row2[3])
        user3['Cost'].append(row2[4])

    cur.execute("Select * from guest_sweets where U_name ='" + a + "'  AND Date=curdate()")
    data3 = cur.fetchall()
    # print(data3)

    for row3 in data3:
        user3['M_course'].append(row3[2])
        user3['Quantity'].append(row3[3])
        user3['Cost'].append(row3[4])

    cur.execute("Select * from guest_accompaniments where U_name ='" + a + "'  AND Date=curdate()")
    data4 = cur.fetchall()
    # print(data4)

    for row4 in data4:
        user3['M_course'].append(row4[2])
        user3['Quantity'].append(row4[3])
        user3['Cost'].append(row4[4])

    cur.execute(
        "SELECT SUM(totalHours) Cost FROM ( select sum(Cost) totalHours from guest_main where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from guest_rice where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from guest_rotis where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from guest_sweets where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from guest_accompaniments where U_name ='" + a + "'  AND Date=curdate()) s")
    data5 = cur.fetchone()
    user4 = {'Cost': data5[0]}

    cur.execute("Select * from sign_up where U_name ='" + a + "'")
    data = cur.fetchone()

    query = "Insert into payment values(%s,%s,%s,%s)"
    cur.execute(query, (data[0], date, data5[0], "Guest"))
    db.commit()

    def sendNotification():
        cur.execute("Select * from sign_up where U_name ='" + a + "'")
        data = cur.fetchone()

        recepients_list = data[1]
        subject = 'Delivery'
        message = "Hello " + data[0] + ",\n Thank you for ordering.\nYour meal will be delivered soon..."
        sendemail(recepients_list, subject, message)

    def sendemail(to_addr_list, subject, message):
        cur.execute("Select * from sign_up where U_name ='" + a + "'")
        data = cur.fetchone()

        recepients_list = data[1]
        username = 'tejasshaha1998@gmail.com'
        password = 'risingphoenix@123'
        from_addr = 'tejasshaha1998@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        newmessage = '\r\n'.join([
            'To: %s' % recepients_list,
            'From: %s' % from_addr,
            'Subject: %s' % subject,
            '',
            message
        ])
        try:
            server.sendmail(from_addr, to_addr_list, newmessage)

        except:
            print("error sending notification")
        server.quit()

    sendNotification()

    return render_template("bill.html", trs=trs, user=user, user2=user2, user3=user3, user4=user4)


@app.route('/cancel-<a>', methods=['GET', 'POST'])
def cancel(a):
    cur = db.cursor()

    cur.execute("Select * from sign_up where U_name ='" + a + "'")
    data = cur.fetchone()
    # print(data)
    user = {'name': data[0], 'U_name': data[7]}

    cur.execute("Delete from guest_main where U_name ='" + a + "'  AND Date=curdate()")
    cur.execute("Delete from guest_rice where U_name ='" + a + "'  AND Date=curdate()")
    cur.execute("Delete from guest_rotis where U_name ='" + a + "'  AND Date=curdate()")
    cur.execute("Delete from guest_sweets where U_name ='" + a + "'AND Date=curdate()")
    cur.execute("Delete from guest_accompaniments where U_name ='" + a + "'  AND Date=curdate()")
    cur.execute("Delete from t where U_name ='" + a + "'  AND Date=curdate()")
    #  cur.execute("Delete from payment where first_name ='" + user['name'] + "'  AND pdate=curdate()")
    db.commit()
    #   "<script>alert('Incorrect Username Or Password.Re-Enter it :)')</script>"
    return render_template("cancel.html", user=user)


@app.route('/download-<a>', methods=['GET', 'POST'])
def download(a):
    i = 100
    date = datetime.date.today()
    cur = db.cursor()
    cur.execute("Select * from sign_up where U_name ='" + a + "'")
    data = cur.fetchone()
    # print(data)
    i += 1
    o = ("OR" + str(randint(100, 999)))
    user = {'name': data[0], 'Address': data[4], 'id': o}
    # user1={'U_name':a}
    trs = {'name': a}
    if cur.execute("Select area from sign_up where U_name ='" + a + "'"):
        user1 = {'area': data[3]}
        #   print(user1)
        if cur.execute("Select * from delievery_boy_details where area1 ='" + user1['area'] + "' OR area2 ='" + user1[
            'area'] + "' OR area3 ='" + user1['area'] + "' OR area4 ='" + user1['area'] + "'"):
            data = cur.fetchone()
            #      print(data)
            user2 = {'D_name': data[1], 'Mobile': data[6]}
            print(user2)

            cur.execute("Select first_name,phone,type from sign_up where U_name ='" + a + "'")
            data = cur.fetchone()
            std = {'name': data[0], 'phone': data[1], 'type': data[2]}

            query = "INSERT INTO t VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query, ([a], std['name'], std['phone'], user1['area'], std['type'], user2['D_name'], date))
            db.commit()

    # cur.execute("SELECT * from guest_main where where and Date=curdate() U_name ='" + a + "'")
    user3 = {'M_course': [], 'Quantity': [], 'Cost': []}
    cur.execute("Select * from guest_main where U_name ='" + a + "'  AND Date=curdate()")
    data = cur.fetchall()
    # print(data)
    for row in data:
        user3['M_course'].append(row[2])
        user3['Quantity'].append(row[3])
        user3['Cost'].append(row[4])

    cur.execute("Select * from guest_rice where U_name ='" + a + "'  AND Date=curdate()")
    data1 = cur.fetchall()
    # print(data1)

    for row1 in data1:
        user3['M_course'].append(row1[2])
        user3['Quantity'].append(row1[3])
        user3['Cost'].append(row1[4])

    cur.execute("Select * from guest_rotis where U_name ='" + a + "'  AND Date=curdate()")
    data2 = cur.fetchall()
    # print(data2)

    for row2 in data2:
        user3['M_course'].append(row2[2])
        user3['Quantity'].append(row2[3])
        user3['Cost'].append(row2[4])

    cur.execute("Select * from guest_sweets where U_name ='" + a + "'  AND Date=curdate()")
    data3 = cur.fetchall()
    # print(data3)

    for row3 in data3:
        user3['M_course'].append(row3[2])
        user3['Quantity'].append(row3[3])
        user3['Cost'].append(row3[4])

    cur.execute("Select * from guest_accompaniments where U_name ='" + a + "'  AND Date=curdate()")
    data4 = cur.fetchall()
    # print(data4)

    for row4 in data4:
        user3['M_course'].append(row4[2])
        user3['Quantity'].append(row4[3])
        user3['Cost'].append(row4[4])

    cur.execute(
        "SELECT SUM(totalHours) Cost FROM ( select sum(Cost) totalHours from guest_main where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from guest_rice where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from guest_rotis where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from guest_sweets where U_name ='" + a + "'  AND Date=curdate() UNION ALL select sum(Cost) totalHours from guest_accompaniments where U_name ='" + a + "'  AND Date=curdate()) s")
    data5 = cur.fetchone()
    user4 = {'Cost': data5[0]}

    cur.execute("Select * from sign_up where U_name ='" + a + "'")
    data = cur.fetchone()

    query = "Insert into payment values(%s,%s,%s,%s)"
    cur.execute(query, (data[0], date, data5[0], "Guest"))
    db.commit()

    return render_template("download.html", trs=trs, user=user, user2=user2, user3=user3, user4=user4)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@app.route('/guest_dash-<a>', methods=['GET', 'POST'])
def guest_dash(a):
    if request.method == 'POST':
        date = datetime.date.today()
        type = request.form['type']
        cur = db.cursor()
        # query = "INSERT INTO guest_main(U_name,skip,Date) VALUES(%s,%s,%s)"
        query = "Update guest_main set skip= '" + type + "'WHERE U_name ='" + a + "'"
        cur.execute(query)
        db.commit()
    return render_template('guest_dash.html', a=a)


@app.route('/full_dash-<a>', methods=['GET', 'POST'])
def full_dash(a):
    return render_template('full_dash.html', a=a)


@app.route('/half_dash-<a>', methods=['GET', 'POST'])
def half_dash(a):
    return render_template('half_dash.html', a=a)


@app.route('/try_another_way', methods=['GET', 'POST'])
def try_another_way():
    if request.method == 'POST':
        first_name = request.form['fname']
        phone = request.form['phone']
        cur = db.cursor()
        if cur.execute(
                "Select U_name,phone from sign_up where U_name ='" + first_name + "' AND phone='" + phone + "'"):
            return redirect(url_for('change_password', a=first_name))

    return render_template('try_another_way.html')


@app.route('/forget_username', methods=['GET', 'POST'])
def forget_username():
    if request.method == 'POST':
        phone = request.form['phone']
        email = request.form['email']

        cur = db.cursor()
        # cur.execute("SELECT * FROM sign_up WHERE U_name='" + first_name + "' AND password ='" + password + "'")

        if cur.execute(
                "Select phone,email from sign_up where phone ='" + phone + "' AND email='" + email + "'"):

            return redirect(url_for('change_username', a=email))

        else:
            return "<script>alert('Incorrect Phone Or Username.Re-Enter it :)')</script>"
        #  error = "Incorrect Username Or Password"

    return render_template('forget_username.html')


@app.route('/forget_password', methods=['GET', 'POST'])
def forget_password():
    if request.method == 'POST':
        first_name = request.form['fname']
        email = request.form['email']

        cur = db.cursor()
        # cur.execute("SELECT * FROM sign_up WHERE U_name='" + first_name + "' AND password ='" + password + "'")

        if cur.execute(
                "Select U_name,email from sign_up where U_name ='" + first_name + "' AND email='" + email + "'"):

            return redirect(url_for('change_password', a=first_name))

        else:
            return "<script>alert('Incorrect Username Or Password.Re-Enter it :)')</script>"
        #  error = "Incorrect Username Or Password"

    return render_template('forget_password.html')


@app.route('/change_username-<a>', methods=['GET', 'POST'])
def change_username(a):
    if request.method == 'POST':
        username = request.form['username']

        cur = db.cursor()
        # cur.execute("SELECT * FROM sign_up WHERE U_name='" + first_name + "' AND password ='" + password + "'")
        cur.execute("UPDATE sign_up SET U_name ='" + username + "' WHERE email='" + a + "'")
        db.commit()
        return redirect(url_for('login'))

    return render_template('change_username.html')


@app.route('/change_password/<a>', methods=['GET', 'POST'])
def change_password(a):
    if request.method == 'POST':
        password = request.form['password']

        cur = db.cursor()
        # cur.execute("SELECT * FROM sign_up WHERE U_name='" + first_name + "' AND password ='" + password + "'")

        if cur.execute(
                "UPDATE sign_up SET password ='" + sha256_crypt.encrypt(password) + "' WHERE U_name='" + a + "'"):
            db.commit()
            return redirect(url_for('login'))

    return render_template('change_password.html')


@app.route('/admin_dash', methods=['GET', 'POST'])
def admin_main():
    return render_template("admin_dash.html")


@app.route('/add_delievery_boy', methods=['GET', 'POST'])
def add_delievery_boy():
    if request.method == 'POST':
        id = request.form['id']
        first_name = request.form['fname']
        area1 = request.form['area1']
        area2 = request.form['area2']
        area3 = request.form['area3']
        area4 = request.form['area4']
        mobile = request.form['phone']
        cur = db.cursor()
        query = "Insert into delievery_boy_details(ID,Name,Area1,Area2,Area3,Area4,Mobile) values(%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query, (id, first_name, area1, area2, area3, area4, mobile))
        db.commit()
    return render_template("add_delievery_boy.html")


@app.route('/delievery_boy_detail', methods=['GET', 'POST'])
def delievery_boy_detail():
    cur = db.cursor()
    cur.execute("SELECT * from delievery_boy_details ")
    data = cur.fetchall()
    print(data)
    user = {'name': [], 'area1': [], 'area2': [], 'area3': [], 'area4': [], 'mobile': []}
    for row in data:
        user['name'].append(row[1])
        user['area1'].append(row[2])
        user['area2'].append(row[3])
        user['area3'].append(row[4])
        user['area4'].append(row[5])
        user['mobile'].append(row[6])

    return render_template("ashutosh.html", user=user)


@app.route('/monthly_half_details', methods=['GET', 'POST'])
def monthly_half_details():
    cur = db.cursor()
    cur.execute("SELECT U_name,first_name,email,phone,address from sign_up where type like 'Monthly half tiffin'")
    data = cur.fetchall()
    print(data)
    user = {'f_name': [], 'U_name': [], 'email': [], 'phone': [], 'address': []}
    for row in data:
        user['U_name'].append(row[0])
        user['f_name'].append(row[1])
        user['email'].append(row[2])
        user['phone'].append(row[3])
        user['address'].append(row[4])
    return render_template("c_details.html", user=user)


@app.route('/monthly_full_details', methods=['GET', 'POST'])
def monthly_full_details():
    cur = db.cursor()
    cur.execute("SELECT U_name,first_name,email,phone,address from sign_up where type like 'Monthly full tiffin'")
    data = cur.fetchall()
    print(data)
    user = {'f_name': [], 'U_name': [], 'email': [], 'phone': [], 'address': []}
    for row in data:
        user['U_name'].append(row[0])
        user['f_name'].append(row[1])
        user['email'].append(row[2])
        user['phone'].append(row[3])
        user['address'].append(row[4])
    return render_template("c_details.html", user=user)


@app.route('/guest_details', methods=['GET', 'POST'])
def guest_details():
    cur = db.cursor()
    cur.execute("SELECT U_name,first_name,email,phone,address from sign_up where type like 'Guest'")
    data = cur.fetchall()
    print(data)
    user = {'f_name': [], 'U_name': [], 'email': [], 'phone': [], 'address': []}
    for row in data:
        user['U_name'].append(row[0])
        user['f_name'].append(row[1])
        user['email'].append(row[2])
        user['phone'].append(row[3])
        user['address'].append(row[4])
    return render_template("c_details.html", user=user)


@app.route('/details', methods=['GET', 'POST'])
def details():
    cur = db.cursor()
    cur.execute("SELECT first_name,type,email,phone,address from sign_up ")
    data = cur.fetchall()
    print(data)
    user = {'f_name': [], 'type': [], 'email': [], 'phone': [], 'address': []}
    for row in data:
        user['f_name'].append(row[0])
        user['type'].append(row[1])
        user['email'].append(row[2])
        user['phone'].append(row[3])
        user['address'].append(row[4])
    return render_template("c_details.html", user=user)


@app.route('/guestm-<a>', methods=['GET', 'POST'])
def guestm(a):
    count = 0
    date = datetime.date.today()
    cur = db.cursor()

    cur.execute("SELECT * from admin_main where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user = {'name': [], 'price': []}
    # user1={'U_name':a}
    for row in data:
        user['name'].append(row[1])
        user['price'].append(row[2])

    cur.execute("SELECT * from admin_rotis where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user1 = {'name': [], 'price': []}
    for row in data:
        user1['name'].append(row[1])
        user1['price'].append(row[2])

    cur.execute("SELECT * from admin_rice where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user2 = {'name': [], 'price': []}
    for row in data:
        user2['name'].append(row[1])
        user2['price'].append(row[2])

    cur.execute("SELECT * from admin_sweets where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user3 = {'name': [], 'price': []}
    for row in data:
        user3['name'].append(row[1])
        user3['price'].append(row[2])

    cur.execute("SELECT * from admin_accompaniments where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user4 = {'name': [], 'price': []}
    for row in data:
        user4['name'].append(row[1])
        user4['price'].append(row[2])

    if request.method == 'POST':
        cur.execute("SELECT Main_Course from admin_main where Date=curdate()")
        data = cur.fetchall()
        # print(data)
        price = []
        cur.execute("SELECT price from admin_main where Date=curdate()")
        tejas = cur.fetchall()
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('bhendi_fry'):
            bhendi = data[0]
            type = request.form['type']
            calc = 0

            def bhendi_fry(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_main(U_name,Date,Main_Course,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, bhendi, type, [cost]))
                db.commit()

            if type == "0":
                bhendi_fry(type, calc)

            if type == "1":
                calc = 1 * price[0]
                count = count + calc
                bhendi_fry(type, calc)

            if type == "2":
                calc = 2 * price[0]
                count = count + calc
                bhendi_fry(type, calc)

            if type == "3":
                calc = 3 * price[0]
                count = count + calc
                bhendi_fry(type, calc)

            if type == "4":
                calc = 4 * price[0]
                count = count + calc
                bhendi_fry(type, calc)

            if type == "5":
                calc = 5 * price[0]
                count = count + calc
                bhendi_fry(type, calc)

        if request.form.getlist('palak_paneer'):
            paneer = data[1]
            type = request.form['type1']
            calc = 0

            def palak_paneer(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_main(U_name,Date,Main_Course,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, paneer, type, [cost]))
                db.commit()

            if type == "0":
                palak_paneer(type, calc)

            if type == "1":
                calc = 1 * price[1]
                count = count + calc
                palak_paneer(type, calc)

            if type == "2":
                calc = 2 * price[1]
                count = count + calc
                palak_paneer(type, calc)

            if type == "3":
                calc = 3 * price[1]
                count = count + calc
                palak_paneer(type, calc)

            if type == "4":
                calc = 4 * price[1]
                count = count + calc
                palak_paneer(type, calc)

            if type == "5":
                calc = 5 * price[1]
                count = count + calc
                palak_paneer(type, calc)

        if request.form.getlist('turai'):
            turai = data[2]
            type = request.form['type2']
            calc = 0

            def turai1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_main(U_name,Date,Main_Course,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, turai, type, [cost]))
                db.commit()

            if type == "0":
                turai1(type, calc)

            if type == "1":
                calc = 1 * price[2]
                count = count + calc
                turai1(type, calc)

            if type == "2":
                calc = 2 * price[2]
                count = count + calc
                turai1(type, calc)

            if type == "3":
                calc = 3 * price[2]
                count = count + calc
                turai1(type, calc)

            if type == "4":
                calc = 4 * price[2]
                count = count + calc
                turai1(type, calc)

            if type == "5":
                calc = 5 * price[2]
                count = count + calc
                turai1(type, calc)

        if request.form.getlist('aloo_lahsuni'):
            aloo = data[3]
            type = request.form['type3']
            calc = 0

            def aloo_lahsuni(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_main(U_name,Date,Main_Course,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, aloo, type, [cost]))
                db.commit()

            if type == "0":
                aloo_lahsuni(type, calc)

            if type == "1":
                calc = 1 * price[3]
                count = count + calc
                aloo_lahsuni(type, calc)

            if type == "2":
                calc = 2 * (price[3])
                count = count + calc
                aloo_lahsuni(type, calc)

            if type == "3":
                calc = 3 * price[3]
                # count = count + calc
                aloo_lahsuni(type, calc)

            if type == "4":
                calc = 4 * price[3]
                count = count + calc
                aloo_lahsuni(type, calc)

            if type == "5":
                calc = 5 * price[3]
                count = count + calc
                aloo_lahsuni(type, calc)

        if request.form.getlist('jain_daal'):
            dal = data[4]
            type = request.form['type4']
            calc = 0

            def jain_daal(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_main(U_name,Date,Main_Course,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, dal, type, [cost]))
                db.commit()

            if type == "0":
                jain_daal(type, calc)

            if type == "1":
                calc = 1 * price[4]
                count = count + calc
                jain_daal(type, calc)

            if type == "2":
                calc = 2 * price[4]
                count = count + calc
                jain_daal(type, calc)

            if type == "3":
                calc = 3 * price[4]
                count = count + calc
                jain_daal(type, calc)

            if type == "4":
                calc = 4 * price[4]
                count = count + calc
                jain_daal(type, calc)

            if type == "5":
                calc = 5 * price[4]
                count = count + calc
                jain_daal(type, calc)

        cur.execute("SELECT Rotis from admin_rotis where Date=curdate()")
        data1 = cur.fetchall()
        cur.execute("SELECT price from admin_rotis where Date=curdate()")
        tejas = cur.fetchall()
        price = []
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('masala_puri'):
            puri = data1[0]
            type = request.form['type5']
            calc = 0

            def masala_puri(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_rotis(U_name,Date,Rotis,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, puri, type, [cost]))
                db.commit()

            if type == "0":
                masala_puri(type, calc)

            if type == "1":
                calc = 1 * price[0]
                count = count + calc
                masala_puri(type, calc)

            if type == "2":
                calc = 2 * price[0]
                count = count + calc
                masala_puri(type, calc)

            if type == "3":
                calc = 3 * price[0]
                count = count + calc
                masala_puri(type, calc)

            if type == "4":
                calc = 4 * price[0]
                count = count + calc
                masala_puri(type, calc)

            if type == "5":
                calc = 5 * price[0]
                count = count + calc
                masala_puri(type, calc)

        if request.form.getlist('phulkaa'):
            phulkaa = data1[1]
            type = request.form['type6']
            calc = 0

            def phulkaa1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_rotis(U_name,Date,Rotis,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, phulkaa, type, [cost]))
                db.commit()

            if type == "0":
                phulkaa1(type, calc)

            if type == "1":
                calc = 1 * price[1]
                count = count + calc
                phulkaa1(type, calc)

            if type == "2":
                calc = 2 * price[1]
                count = count + calc
                phulkaa1(type, calc)

            if type == "3":
                calc = 3 * price[1]
                count = count + calc
                phulkaa1(type, calc)

            if type == "4":
                calc = 4 * price[1]
                count = count + calc
                phulkaa1(type, calc)

            if type == "5":
                calc = 5 * price[1]
                count = count + calc
                phulkaa1(type, calc)

        if request.form.getlist('phulkaa_ghee'):
            phulkaa = data1[2]
            type = request.form['type7']
            calc = 0

            def phulkaa_ghee(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_rotis(U_name,Date,Rotis,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, phulkaa, type, [cost]))
                db.commit()

            if type == "0":
                phulkaa_ghee(type, calc)

            if type == "1":
                calc = 1 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

            if type == "2":
                calc = 2 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

            if type == "3":
                calc = 3 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

            if type == "4":
                calc = 4 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

            if type == "5":
                calc = 5 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

        if request.form.getlist('multigrain_roti'):
            roti = data1[3]
            type = request.form['type8']
            calc = 0

            def multigrain_roti(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_rotis(U_name,Date,Rotis,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, roti, type, [cost]))
                db.commit()

            if type == "0":
                multigrain_roti(type, calc)

            if type == "1":
                count = count + calc
                calc = 1 * price[3]
                multigrain_roti(type, calc)

            if type == "2":
                calc = 2 * price[3]
                count = count + calc
                multigrain_roti(type, calc)

            if type == "3":
                calc = 3 * price[3]
                count = count + calc
                multigrain_roti(type, calc)

            if type == "4":
                calc = 4 * price[3]
                count = count + calc
                multigrain_roti(type, calc)

            if type == "5":
                calc = 5 * price[3]
                count = count + calc
                multigrain_roti(type, calc)

        cur.execute("SELECT Rice from admin_rice where Date=curdate()")
        data2 = cur.fetchall()
        price = []
        cur.execute("SELECT price from admin_rice where Date=curdate()")
        tejas = cur.fetchall()
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('fried_rice'):
            f_rice = data2[0]
            type = request.form['type9']
            calc = 0

            def fried_rice(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, f_rice, type, [cost]))
                db.commit()

            if type == "0":
                fried_rice(type, calc)

            if type == "1":
                calc = 1 * price[0]
                count = count + calc
                fried_rice(type, calc)

            if type == "2":
                calc = 2 * price[0]
                count = count + calc
                fried_rice(type, calc)

            if type == "3":
                calc = 3 * price[0]
                count = count + calc
                fried_rice(type, calc)

            if type == "4":
                calc = 4 * price[0]
                count = count + calc
                fried_rice(type, calc)

            if type == "5":
                calc = 5 * price[0]
                count = count + calc
                fried_rice(type, calc)

        if request.form.getlist('plain_rice'):
            p_rice = data2[1]
            type = request.form['type10']
            calc = 0

            def plain_rice(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, p_rice, type, [cost]))
                db.commit()

            if type == "0":
                plain_rice(type, calc)

            if type == "1":
                calc = 1 * price[1]
                count = count + calc
                plain_rice(type, calc)

            if type == "2":
                calc = 2 * price[1]
                count = count + calc
                plain_rice(type, calc)

            if type == "3":
                calc = 3 * price[1]
                count = count + calc
                plain_rice(type, calc)

            if type == "4":
                calc = 4 * price[1]
                count = count + calc
                plain_rice(type, calc)

            if type == "5":
                calc = 5 * price[1]
                count = count + calc
                plain_rice(type, calc)

        if request.form.getlist('veg_pulav'):
            v_pulav = data2[2]
            type = request.form['type11']
            calc = 0

            def veg_pulav(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, v_pulav, type, [cost]))
                db.commit()

            if type == "0":
                veg_pulav(type, calc)

            if type == "1":
                calc = 1 * price[2]
                count = count + calc
                veg_pulav(type, calc)

            if type == "2":
                calc = 2 * price[2]
                count = count + calc
                veg_pulav(type, calc)

            if type == "3":
                calc = 3 * price[2]
                count = count + calc
                veg_pulav(type, calc)

            if type == "4":
                calc = 4 * price[2]
                count = count + calc
                veg_pulav(type, calc)

            if type == "5":
                calc = 5 * price[2]
                count = count + calc
                veg_pulav(type, calc)

        if request.form.getlist('jira_rice'):
            j_rice = data2[3]
            type = request.form['type12']
            calc = 0

            def jira_rice(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, j_rice, type, [cost]))
                db.commit()

            if type == "0":
                jira_rice(type, calc)

            if type == "1":
                calc = 1 * price[3]
                count = count + calc
                jira_rice(type, calc)

            if type == "2":
                calc = 2 * price[3]
                count = count + calc
                jira_rice(type, calc)

            if type == "3":
                calc = 3 * price[3]
                count = count + calc
                jira_rice(type, calc)

            if type == "4":
                calc = 4 * price[3]
                count = count + calc
                jira_rice(type, calc)

            if type == "5":
                calc = 5 * price[3]
                count = count + calc
                jira_rice(type, calc)

        if request.form.getlist('paneer_pulav'):
            p_pulav = data2[4]
            type = request.form['type13']
            calc = 0

            def paneer_pulav(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, p_pulav, type, [cost]))
                db.commit()

            if type == "0":
                paneer_pulav(type, calc)

            if type == "1":
                calc = 1 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

            if type == "2":
                calc = 2 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

            if type == "3":
                calc = 3 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

            if type == "4":
                calc = 4 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

            if type == "5":
                calc = 5 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

        cur.execute("SELECT Sweets from admin_sweets where Date=curdate()")
        data3 = cur.fetchall()
        price = []
        cur.execute("SELECT price from admin_sweets where Date=curdate()")
        tejas = cur.fetchall()
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('gulab_jamun'):
            g_jamun = data3[0]
            type = request.form['type14']
            calc = 0

            def gulab_jamun(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_sweets(U_name,Date,Sweets,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, g_jamun, type, [cost]))
                db.commit()

            if type == "0":
                gulab_jamun(type, calc)

            if type == "1":
                calc = 1 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

            if type == "2":
                calc = 2 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

            if type == "3":
                calc = 3 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

            if type == "4":
                calc = 4 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

            if type == "5":
                calc = 5 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

        if request.form.getlist('shrikhand'):
            shrikhand = data3[1]
            type = request.form['typea']
            calc = 0

            def shrikhand1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_sweets(U_name,Date,Sweets,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, shrikhand, type, [cost]))
                db.commit()

            if type == "0":
                shrikhand1(type, calc)

            if type == "1":
                calc = 1 * price[1]
                count = count + calc
                shrikhand1(type, calc)

            if type == "2":
                calc = 2 * price[1]
                count = count + calc
                shrikhand1(type, calc)

            if type == "3":
                calc = 3 * price[1]
                count = count + calc
                shrikhand1(type, calc)

            if type == "4":
                calc = 4 * price[1]
                count = count + calc
                shrikhand1(type, calc)

            if type == "5":
                calc = 5 * price[1]
                count = count + calc
                shrikhand1(type, calc)

        if request.form.getlist('amrakhand'):
            Amrakhand = data3[2]
            type = request.form['typeb']
            calc = 0

            def Amrakhand1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_sweets(U_name,Date,Sweets,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, Amrakhand, type, [cost]))
                db.commit()

            if type == "0":
                Amrakhand1(type, calc)

            if type == "1":
                calc = 1 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

            if type == "2":
                calc = 2 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

            if type == "3":
                calc = 3 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

            if type == "4":
                calc = 4 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

            if type == "5":
                calc = 5 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

        if request.form.getlist('rabdi'):
            rabdi = data3[3]
            type = request.form['typec']
            calc = 0

            def rabdi1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_sweets(U_name,Date,Sweets,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, rabdi, type, [cost]))
                db.commit()

            if type == "0":
                rabdi1(type, calc)

            if type == "1":
                calc = 1 * price[3]
                count = count + calc
                rabdi1(type, calc)

            if type == "2":
                calc = 2 * price[3]
                count = count + calc
                rabdi1(type, calc)

            if type == "3":
                calc = 3 * price[3]
                count = count + calc
                rabdi1(type, calc)

            if type == "4":
                calc = 4 * price[3]
                count = count + calc
                rabdi1(type, calc)

            if type == "5":
                calc = 5 * price[3]
                count = count + calc
                rabdi1(type, calc)

        cur.execute("SELECT Accompaniments from admin_accompaniments where Date=curdate()")
        data4 = cur.fetchall()
        price = []
        cur.execute("SELECT price from admin_accompaniments where Date=curdate()")
        tejas = cur.fetchall()
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('masala_chaas'):
            chaas = data4[0]
            type = request.form['type16']
            calc = 0

            def Masala_chaas(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_accompaniments(U_name,Date,Accompaniments,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, chaas, type, [cost]))
                db.commit()

            if type == "0":
                Masala_chaas(type, calc)

            if type == "1":
                calc = 1 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

            if type == "2":
                calc = 2 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

            if type == "3":
                calc = 3 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

            if type == "4":
                calc = 4 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

            if type == "5":
                calc = 5 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

        if request.form.getlist('curd'):
            curd = data4[1]
            type = request.form['type17']
            calc = 0

            def curd1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_accompaniments(U_name,Date,Accompaniments,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, curd, type, [cost]))
                db.commit()

            if type == "0":
                curd1(type, calc)

            if type == "1":
                calc = 1 * price[1]
                count = count + calc
                curd1(type, calc)

            if type == "2":
                calc = 2 * price[1]
                count = count + calc
                curd1(type, calc)

            if type == "3":
                calc = 3 * price[1]
                count = count + calc
                curd1(type, calc)

            if type == "4":
                calc = 4 * price[1]
                count = count + calc
                curd1(type, calc)

            if type == "5":
                calc = 5 * price[1]
                count = count + calc
                curd1(type, calc)

        if request.form.getlist('salad'):
            salad = data4[2]
            type = request.form['type18']
            calc = 0

            def salad1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_accompaniments(U_name,Date,Accompaniments,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, salad, type, [cost]))
                db.commit()

            if type == "0":
                salad1(type, calc)

            if type == "1":
                calc = 1 * price[2]
                count = count + calc
                salad1(type, calc)

            if type == "2":
                calc = 2 * price[2]
                count = count + calc
                salad1(type, calc)

            if type == "3":
                calc = 3 * price[2]
                count = count + calc
                salad1(type, calc)

            if type == "4":
                calc = 4 * price[2]
                count = count + calc
                salad1(type, calc)

            if type == "5":
                calc = 5 * price[2]
                count = count + calc
                salad1(type, calc)

        if request.form.getlist('roasted_papad'):
            r_papad = data4[3]
            type = request.form['type19']
            calc = 0

            def Roasted_papad(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO guest_accompaniments(U_name,Date,Accompaniments,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, r_papad, type, [cost]))
                db.commit()

            if type == "0":
                Roasted_papad(type, calc)

            if type == "1":
                calc = 1 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

            if type == "2":
                calc = 2 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

            if type == "3":
                calc = 3 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

            if type == "4":
                calc = 4 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

            if type == "5":
                calc = 5 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

        print(count)
        cur.execute("Select * from sign_up where U_name ='" + a + "'")
        data = cur.fetchone()
        #      print(data)
        userr = {'name': data[0], 'U_name': data[7]}

        return render_template("successful.html", userr=userr)

        # return render_template("stdform.html")
    return render_template("guestm.html",a=a,user=user, user1=user1, user2=user2, user3=user3, user4=user4)


@app.route('/fullm-<a>', methods=['GET', 'POST'])
def fullm(a):
    count = 0
    date = datetime.date.today()
    cur = db.cursor()

    cur.execute("SELECT * from admin_main where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user = {'name': [], 'price': []}
    # user1={'U_name':a}
    for row in data:
        user['name'].append(row[1])
        user['price'].append(row[2])

    cur.execute("SELECT * from admin_rotis where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user1 = {'name': [], 'price': []}
    for row in data:
        user1['name'].append(row[1])
        user1['price'].append(row[2])

    cur.execute("SELECT * from admin_rice where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user2 = {'name': [], 'price': []}
    for row in data:
        user2['name'].append(row[1])
        user2['price'].append(row[2])

    cur.execute("SELECT * from admin_sweets where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user3 = {'name': [], 'price': []}
    for row in data:
        user3['name'].append(row[1])
        user3['price'].append(row[2])

    cur.execute("SELECT * from admin_accompaniments where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user4 = {'name': [], 'price': []}
    for row in data:
        user4['name'].append(row[1])
        user4['price'].append(row[2])

    if request.method == 'POST':
        cur.execute("SELECT Main_Course from admin_main where Date=curdate()")
        data = cur.fetchall()
        # print(data)
        price = []
        cur.execute("SELECT price from admin_main where Date=curdate()")
        tejas = cur.fetchall()
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('bhendi_fry'):
            bhendi = data[0]
            cur = db.cursor()
            query = "INSERT INTO full_main(U_name,Main_Course,Date) VALUES(%s,%s,%s)"
            cur.execute(query, ([a], bhendi, date))
            db.commit()

        if request.form.getlist('palak_paneer'):
            paneer = data[1]
            cur = db.cursor()
            query = "INSERT INTO full_main(U_name,Main_Course,Date) VALUES(%s,%s,%s)"
            cur.execute(query, ([a], paneer, date))
            db.commit()

        if request.form.getlist('turai'):
            turai = data[2]
            cur = db.cursor()
            query = "INSERT INTO full_main(U_name,Main_Course,Date) VALUES(%s,%s,%s)"
            cur.execute(query, ([a], turai, date))
            db.commit()

        if request.form.getlist('aloo_lahsuni'):
            aloo = data[3]
            cur = db.cursor()
            query = "INSERT INTO full_main(U_name,Main_Course,Date) VALUES(%s,%s,%s)"
            cur.execute(query, ([a], aloo, date))
            db.commit()

        if request.form.getlist('jain_daal'):
            dal = data[4]
            cur = db.cursor()
            query = "INSERT INTO full_main(U_name,Main_Course,Date) VALUES(%s,%s,%s)"
            cur.execute(query, ([a], dal, date))
            db.commit()

        cur.execute("SELECT Rotis from admin_rotis where Date=curdate()")
        data1 = cur.fetchall()
        cur.execute("SELECT price from admin_rotis where Date=curdate()")
        tejas = cur.fetchall()
        price = []
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('masala_puri'):
            puri = data1[0]
            type = request.form['type5']
            calc = 0

            def masala_puri(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_rotis(U_name,Date,Rotis,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, puri, type, [cost]))
                db.commit()

            if type == "0":
                masala_puri(type, calc)

            if type == "1":
                calc = 1 * price[0]
                count = count + calc
                masala_puri(type, calc)

            if type == "2":
                calc = 2 * price[0]
                count = count + calc
                masala_puri(type, calc)

            if type == "3":
                calc = 3 * price[0]
                count = count + calc
                masala_puri(type, calc)

            if type == "4":
                calc = 4 * price[0]
                count = count + calc
                masala_puri(type, calc)

            if type == "5":
                calc = 5 * price[0]
                count = count + calc
                masala_puri(type, calc)

        if request.form.getlist('phulkaa'):
            phulkaa = data1[1]
            type = request.form['type6']
            calc = 0

            def phulkaa1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_rotis(U_name,Date,Rotis,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, phulkaa, type, [cost]))
                db.commit()

            if type == "0":
                phulkaa1(type, calc)

            if type == "1":
                calc = 1 * price[1]
                count = count + calc
                phulkaa1(type, calc)

            if type == "2":
                calc = 2 * price[1]
                count = count + calc
                phulkaa1(type, calc)

            if type == "3":
                calc = 3 * price[1]
                count = count + calc
                phulkaa1(type, calc)

            if type == "4":
                calc = 4 * price[1]
                count = count + calc
                phulkaa1(type, calc)

            if type == "5":
                calc = 5 * price[1]
                count = count + calc
                phulkaa1(type, calc)

        if request.form.getlist('phulkaa_ghee'):
            phulkaa = data1[2]
            type = request.form['type7']
            calc = 0

            def phulkaa_ghee(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_rotis(U_name,Date,Rotis,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, phulkaa, type, [cost]))
                db.commit()

            if type == "0":
                phulkaa_ghee(type, calc)

            if type == "1":
                calc = 1 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

            if type == "2":
                calc = 2 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

            if type == "3":
                calc = 3 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

            if type == "4":
                calc = 4 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

            if type == "5":
                calc = 5 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

        if request.form.getlist('multigrain_roti'):
            roti = data1[3]
            type = request.form['type8']
            calc = 0

            def multigrain_roti(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_rotis(U_name,Date,Rotis,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, roti, type, [cost]))
                db.commit()

            if type == "0":
                multigrain_roti(type, calc)

            if type == "1":
                count = count + calc
                calc = 1 * price[3]
                multigrain_roti(type, calc)

            if type == "2":
                calc = 2 * price[3]
                count = count + calc
                multigrain_roti(type, calc)

            if type == "3":
                calc = 3 * price[3]
                count = count + calc
                multigrain_roti(type, calc)

            if type == "4":
                calc = 4 * price[3]
                count = count + calc
                multigrain_roti(type, calc)

            if type == "5":
                calc = 5 * price[3]
                count = count + calc
                multigrain_roti(type, calc)

        cur.execute("SELECT Rice from admin_rice where Date=curdate()")
        data2 = cur.fetchall()
        price = []
        cur.execute("SELECT price from admin_rice where Date=curdate()")
        tejas = cur.fetchall()
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('fried_rice'):
            f_rice = data2[0]
            type = request.form['type9']
            calc = 0

            def fried_rice(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, f_rice, type, [cost]))
                db.commit()

            if type == "0":
                fried_rice(type, calc)

            if type == "1":
                calc = 1 * price[0]
                count = count + calc
                fried_rice(type, calc)

            if type == "2":
                calc = 2 * price[0]
                count = count + calc
                fried_rice(type, calc)

            if type == "3":
                calc = 3 * price[0]
                count = count + calc
                fried_rice(type, calc)

            if type == "4":
                calc = 4 * price[0]
                count = count + calc
                fried_rice(type, calc)

            if type == "5":
                calc = 5 * price[0]
                count = count + calc
                fried_rice(type, calc)

        if request.form.getlist('plain_rice'):
            p_rice = data2[1]
            type = request.form['type10']
            calc = 0

            def plain_rice(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, p_rice, type, [cost]))
                db.commit()

            if type == "0":
                plain_rice(type, calc)

            if type == "1":
                calc = 1 * price[1]
                count = count + calc
                plain_rice(type, calc)

            if type == "2":
                calc = 2 * price[1]
                count = count + calc
                plain_rice(type, calc)

            if type == "3":
                calc = 3 * price[1]
                count = count + calc
                plain_rice(type, calc)

            if type == "4":
                calc = 4 * price[1]
                count = count + calc
                plain_rice(type, calc)

            if type == "5":
                calc = 5 * price[1]
                count = count + calc
                plain_rice(type, calc)

        if request.form.getlist('veg_pulav'):
            v_pulav = data2[2]
            type = request.form['type11']
            calc = 0

            def veg_pulav(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, v_pulav, type, [cost]))
                db.commit()

            if type == "0":
                veg_pulav(type, calc)

            if type == "1":
                calc = 1 * price[2]
                count = count + calc
                veg_pulav(type, calc)

            if type == "2":
                calc = 2 * price[2]
                count = count + calc
                veg_pulav(type, calc)

            if type == "3":
                calc = 3 * price[2]
                count = count + calc
                veg_pulav(type, calc)

            if type == "4":
                calc = 4 * price[2]
                count = count + calc
                veg_pulav(type, calc)

            if type == "5":
                calc = 5 * price[2]
                count = count + calc
                veg_pulav(type, calc)

        if request.form.getlist('jira_rice'):
            j_rice = data2[3]
            type = request.form['type12']
            calc = 0

            def jira_rice(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, j_rice, type, [cost]))
                db.commit()

            if type == "0":
                jira_rice(type, calc)

            if type == "1":
                calc = 1 * price[3]
                count = count + calc
                jira_rice(type, calc)

            if type == "2":
                calc = 2 * price[3]
                count = count + calc
                jira_rice(type, calc)

            if type == "3":
                calc = 3 * price[3]
                count = count + calc
                jira_rice(type, calc)

            if type == "4":
                calc = 4 * price[3]
                count = count + calc
                jira_rice(type, calc)

            if type == "5":
                calc = 5 * price[3]
                count = count + calc
                jira_rice(type, calc)

        if request.form.getlist('paneer_pulav'):
            p_pulav = data2[4]
            type = request.form['type13']
            calc = 0

            def paneer_pulav(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, p_pulav, type, [cost]))
                db.commit()

            if type == "0":
                paneer_pulav(type, calc)

            if type == "1":
                calc = 1 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

            if type == "2":
                calc = 2 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

            if type == "3":
                calc = 3 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

            if type == "4":
                calc = 4 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

            if type == "5":
                calc = 5 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

        cur.execute("SELECT Sweets from admin_sweets where Date=curdate()")
        data3 = cur.fetchall()
        price = []
        cur.execute("SELECT price from admin_sweets where Date=curdate()")
        tejas = cur.fetchall()
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('gulab_jamun'):
            g_jamun = data3[0]
            type = request.form['type14']
            calc = 0

            def gulab_jamun(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_sweets(U_name,Date,Sweets,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, g_jamun, type, [cost]))
                db.commit()

            if type == "0":
                gulab_jamun(type, calc)

            if type == "1":
                calc = 1 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

            if type == "2":
                calc = 2 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

            if type == "3":
                calc = 3 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

            if type == "4":
                calc = 4 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

            if type == "5":
                calc = 5 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

        if request.form.getlist('shrikhand'):
            shrikhand = data3[1]
            type = request.form['typea']
            calc = 0

            def shrikhand1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_sweets(U_name,Date,Sweets,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, shrikhand, type, [cost]))
                db.commit()

            if type == "0":
                shrikhand1(type, calc)

            if type == "1":
                calc = 1 * price[1]
                count = count + calc
                shrikhand1(type, calc)

            if type == "2":
                calc = 2 * price[1]
                count = count + calc
                shrikhand1(type, calc)

            if type == "3":
                calc = 3 * price[1]
                count = count + calc
                shrikhand1(type, calc)

            if type == "4":
                calc = 4 * price[1]
                count = count + calc
                shrikhand1(type, calc)

            if type == "5":
                calc = 5 * price[1]
                count = count + calc
                shrikhand1(type, calc)

        if request.form.getlist('amrakhand'):
            Amrakhand = data3[2]
            type = request.form['typeb']
            calc = 0

            def Amrakhand1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_sweets(U_name,Date,Sweets,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, Amrakhand, type, [cost]))
                db.commit()

            if type == "0":
                Amrakhand1(type, calc)

            if type == "1":
                calc = 1 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

            if type == "2":
                calc = 2 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

            if type == "3":
                calc = 3 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

            if type == "4":
                calc = 4 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

            if type == "5":
                calc = 5 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

        if request.form.getlist('rabdi'):
            rabdi = data3[3]
            type = request.form['typec']
            calc = 0

            def rabdi1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_sweets(U_name,Date,Sweets,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, rabdi, type, [cost]))
                db.commit()

            if type == "0":
                rabdi1(type, calc)

            if type == "1":
                calc = 1 * price[3]
                count = count + calc
                rabdi1(type, calc)

            if type == "2":
                calc = 2 * price[3]
                count = count + calc
                rabdi1(type, calc)

            if type == "3":
                calc = 3 * price[3]
                count = count + calc
                rabdi1(type, calc)

            if type == "4":
                calc = 4 * price[3]
                count = count + calc
                rabdi1(type, calc)

            if type == "5":
                calc = 5 * price[3]
                count = count + calc
                rabdi1(type, calc)

        cur.execute("SELECT Accompaniments from admin_accompaniments where Date=curdate()")
        data4 = cur.fetchall()
        price = []
        cur.execute("SELECT price from admin_accompaniments where Date=curdate()")
        tejas = cur.fetchall()
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('masala_chaas'):
            chaas = data4[0]
            type = request.form['type16']
            calc = 0

            def Masala_chaas(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_accompaniments(U_name,Date,Accompaniments,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, chaas, type, [cost]))
                db.commit()

            if type == "0":
                Masala_chaas(type, calc)

            if type == "1":
                calc = 1 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

            if type == "2":
                calc = 2 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

            if type == "3":
                calc = 3 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

            if type == "4":
                calc = 4 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

            if type == "5":
                calc = 5 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

        if request.form.getlist('curd'):
            curd = data4[1]
            type = request.form['type17']
            calc = 0

            def curd1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_accompaniments(U_name,Date,Accompaniments,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, curd, type, [cost]))
                db.commit()

            if type == "0":
                curd1(type, calc)

            if type == "1":
                calc = 1 * price[1]
                count = count + calc
                curd1(type, calc)

            if type == "2":
                calc = 2 * price[1]
                count = count + calc
                curd1(type, calc)

            if type == "3":
                calc = 3 * price[1]
                count = count + calc
                curd1(type, calc)

            if type == "4":
                calc = 4 * price[1]
                count = count + calc
                curd1(type, calc)

            if type == "5":
                calc = 5 * price[1]
                count = count + calc
                curd1(type, calc)

        if request.form.getlist('salad'):
            salad = data4[2]
            type = request.form['type18']
            calc = 0

            def salad1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_accompaniments(U_name,Date,Accompaniments,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, salad, type, [cost]))
                db.commit()

            if type == "0":
                salad1(type, calc)

            if type == "1":
                calc = 1 * price[2]
                count = count + calc
                salad1(type, calc)

            if type == "2":
                calc = 2 * price[2]
                count = count + calc
                salad1(type, calc)

            if type == "3":
                calc = 3 * price[2]
                count = count + calc
                salad1(type, calc)

            if type == "4":
                calc = 4 * price[2]
                count = count + calc
                salad1(type, calc)

            if type == "5":
                calc = 5 * price[2]
                count = count + calc
                salad1(type, calc)

        if request.form.getlist('roasted_papad'):
            r_papad = data4[3]
            type = request.form['type19']
            calc = 0

            def Roasted_papad(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO full_extra_accompaniments(U_name,Date,Accompaniments,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, r_papad, type, [cost]))
                db.commit()

            if type == "0":
                Roasted_papad(type, calc)

            if type == "1":
                calc = 1 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

            if type == "2":
                calc = 2 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

            if type == "3":
                calc = 3 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

            if type == "4":
                calc = 4 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

            if type == "5":
                calc = 5 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

        cur.execute("Select * from sign_up where U_name ='" + a + "'")
        data = cur.fetchone()
        #      print(data)
        userr = {'name': data[0], 'U_name': data[7]}
        return render_template("successful1.html", userr=userr)

    return render_template("fullm.html", user=user, user1=user1, user2=user2, user3=user3, user4=user4)


@app.route('/halfm-<a>', methods=['GET', 'POST'])
def halfm(a):
    count = 0
    date = datetime.date.today()
    cur = db.cursor()

    cur.execute("SELECT * from admin_main where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user = {'name': [], 'price': []}
    # user1={'U_name':a}
    for row in data:
        user['name'].append(row[1])
        user['price'].append(row[2])

    cur.execute("SELECT * from admin_rotis where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user1 = {'name': [], 'price': []}
    for row in data:
        user1['name'].append(row[1])
        user1['price'].append(row[2])

    cur.execute("SELECT * from admin_rice where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user2 = {'name': [], 'price': []}
    for row in data:
        user2['name'].append(row[1])
        user2['price'].append(row[2])

    cur.execute("SELECT * from admin_sweets where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user3 = {'name': [], 'price': []}
    for row in data:
        user3['name'].append(row[1])
        user3['price'].append(row[2])

    cur.execute("SELECT * from admin_accompaniments where Date=curdate()")
    data = cur.fetchall()
    print(data)
    user4 = {'name': [], 'price': []}
    for row in data:
        user4['name'].append(row[1])
        user4['price'].append(row[2])

    if request.method == 'POST':
        cur.execute("SELECT Main_Course from admin_main where Date=curdate()")
        data = cur.fetchall()
        # print(data)
        price = []
        cur.execute("SELECT price from admin_main where Date=curdate()")
        tejas = cur.fetchall()
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('bhendi_fry'):
            bhendi = data[0]
            cur = db.cursor()
            query = "INSERT INTO half_main(U_name,Main_Course,Date) VALUES(%s,%s,%s)"
            cur.execute(query, ([a], bhendi, date))
            db.commit()

        if request.form.getlist('palak_paneer'):
            paneer = data[1]
            cur = db.cursor()
            query = "INSERT INTO half_main(U_name,Main_Course,Date) VALUES(%s,%s,%s)"
            cur.execute(query, ([a], paneer, date))
            db.commit()

        if request.form.getlist('turai'):
            turai = data[2]
            cur = db.cursor()
            query = "INSERT INTO half_main(U_name,Main_Course,Date) VALUES(%s,%s,%s)"
            cur.execute(query, ([a], turai, date))
            db.commit()

        if request.form.getlist('aloo_lahsuni'):
            aloo = data[3]
            cur = db.cursor()
            query = "INSERT INTO half_main(U_name,Main_Course,Date) VALUES(%s,%s,%s)"
            cur.execute(query, ([a], aloo, date))
            db.commit()

        if request.form.getlist('jain_daal'):
            dal = data[4]
            cur = db.cursor()
            query = "INSERT INTO half_main(U_name,Main_Course,Date) VALUES(%s,%s,%s)"
            cur.execute(query, ([a], dal, date))
            db.commit()

        cur.execute("SELECT Rotis from admin_rotis where Date=curdate()")
        data1 = cur.fetchall()
        cur.execute("SELECT price from admin_rotis where Date=curdate()")
        tejas = cur.fetchall()
        price = []
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('masala_puri'):
            puri = data1[0]
            type = request.form['type5']
            calc = 0

            def masala_puri(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_rotis(U_name,Date,Rotis,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, puri, type, [cost]))
                db.commit()

            if type == "0":
                masala_puri(type, calc)

            if type == "1":
                calc = 1 * price[0]
                count = count + calc
                masala_puri(type, calc)

            if type == "2":
                calc = 2 * price[0]
                count = count + calc
                masala_puri(type, calc)

            if type == "3":
                calc = 3 * price[0]
                count = count + calc
                masala_puri(type, calc)

            if type == "4":
                calc = 4 * price[0]
                count = count + calc
                masala_puri(type, calc)

            if type == "5":
                calc = 5 * price[0]
                count = count + calc
                masala_puri(type, calc)

        if request.form.getlist('phulkaa'):
            phulkaa = data1[1]
            type = request.form['type6']
            calc = 0

            def phulkaa1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_rotis(U_name,Date,Rotis,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, phulkaa, type, [cost]))
                db.commit()

            if type == "0":
                phulkaa1(type, calc)

            if type == "1":
                calc = 1 * price[1]
                count = count + calc
                phulkaa1(type, calc)

            if type == "2":
                calc = 2 * price[1]
                count = count + calc
                phulkaa1(type, calc)

            if type == "3":
                calc = 3 * price[1]
                count = count + calc
                phulkaa1(type, calc)

            if type == "4":
                calc = 4 * price[1]
                count = count + calc
                phulkaa1(type, calc)

            if type == "5":
                calc = 5 * price[1]
                count = count + calc
                phulkaa1(type, calc)

        if request.form.getlist('phulkaa_ghee'):
            phulkaa = data1[2]
            type = request.form['type7']
            calc = 0

            def phulkaa_ghee(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_rotis(U_name,Date,Rotis,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, phulkaa, type, [cost]))
                db.commit()

            if type == "0":
                phulkaa_ghee(type, calc)

            if type == "1":
                calc = 1 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

            if type == "2":
                calc = 2 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

            if type == "3":
                calc = 3 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

            if type == "4":
                calc = 4 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

            if type == "5":
                calc = 5 * price[2]
                count = count + calc
                phulkaa_ghee(type, calc)

        if request.form.getlist('multigrain_roti'):
            roti = data1[3]
            type = request.form['type8']
            calc = 0

            def multigrain_roti(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_rotis(U_name,Date,Rotis,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, roti, type, [cost]))
                db.commit()

            if type == "0":
                multigrain_roti(type, calc)

            if type == "1":
                count = count + calc
                calc = 1 * price[3]
                multigrain_roti(type, calc)

            if type == "2":
                calc = 2 * price[3]
                count = count + calc
                multigrain_roti(type, calc)

            if type == "3":
                calc = 3 * price[3]
                count = count + calc
                multigrain_roti(type, calc)

            if type == "4":
                calc = 4 * price[3]
                count = count + calc
                multigrain_roti(type, calc)

            if type == "5":
                calc = 5 * price[3]
                count = count + calc
                multigrain_roti(type, calc)

        cur.execute("SELECT Rice from admin_rice where Date=curdate()")
        data2 = cur.fetchall()
        price = []
        cur.execute("SELECT price from admin_rice where Date=curdate()")
        tejas = cur.fetchall()
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('fried_rice'):
            f_rice = data2[0]
            type = request.form['type9']
            calc = 0

            def fried_rice(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, f_rice, type, [cost]))
                db.commit()

            if type == "0":
                fried_rice(type, calc)

            if type == "1":
                calc = 1 * price[0]
                count = count + calc
                fried_rice(type, calc)

            if type == "2":
                calc = 2 * price[0]
                count = count + calc
                fried_rice(type, calc)

            if type == "3":
                calc = 3 * price[0]
                count = count + calc
                fried_rice(type, calc)

            if type == "4":
                calc = 4 * price[0]
                count = count + calc
                fried_rice(type, calc)

            if type == "5":
                calc = 5 * price[0]
                count = count + calc
                fried_rice(type, calc)

        if request.form.getlist('plain_rice'):
            p_rice = data2[1]
            type = request.form['type10']
            calc = 0

            def plain_rice(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, p_rice, type, [cost]))
                db.commit()

            if type == "0":
                plain_rice(type, calc)

            if type == "1":
                calc = 1 * price[1]
                count = count + calc
                plain_rice(type, calc)

            if type == "2":
                calc = 2 * price[1]
                count = count + calc
                plain_rice(type, calc)

            if type == "3":
                calc = 3 * price[1]
                count = count + calc
                plain_rice(type, calc)

            if type == "4":
                calc = 4 * price[1]
                count = count + calc
                plain_rice(type, calc)

            if type == "5":
                calc = 5 * price[1]
                count = count + calc
                plain_rice(type, calc)

        if request.form.getlist('veg_pulav'):
            v_pulav = data2[2]
            type = request.form['type11']
            calc = 0

            def veg_pulav(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, v_pulav, type, [cost]))
                db.commit()

            if type == "0":
                veg_pulav(type, calc)

            if type == "1":
                calc = 1 * price[2]
                count = count + calc
                veg_pulav(type, calc)

            if type == "2":
                calc = 2 * price[2]
                count = count + calc
                veg_pulav(type, calc)

            if type == "3":
                calc = 3 * price[2]
                count = count + calc
                veg_pulav(type, calc)

            if type == "4":
                calc = 4 * price[2]
                count = count + calc
                veg_pulav(type, calc)

            if type == "5":
                calc = 5 * price[2]
                count = count + calc
                veg_pulav(type, calc)

        if request.form.getlist('jira_rice'):
            j_rice = data2[3]
            type = request.form['type12']
            calc = 0

            def jira_rice(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, j_rice, type, [cost]))
                db.commit()

            if type == "0":
                jira_rice(type, calc)

            if type == "1":
                calc = 1 * price[3]
                count = count + calc
                jira_rice(type, calc)

            if type == "2":
                calc = 2 * price[3]
                count = count + calc
                jira_rice(type, calc)

            if type == "3":
                calc = 3 * price[3]
                count = count + calc
                jira_rice(type, calc)

            if type == "4":
                calc = 4 * price[3]
                count = count + calc
                jira_rice(type, calc)

            if type == "5":
                calc = 5 * price[3]
                count = count + calc
                jira_rice(type, calc)

        if request.form.getlist('paneer_pulav'):
            p_pulav = data2[4]
            type = request.form['type13']
            calc = 0

            def paneer_pulav(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_rice(U_name,Date,Rice,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, p_pulav, type, [cost]))
                db.commit()

            if type == "0":
                paneer_pulav(type, calc)

            if type == "1":
                calc = 1 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

            if type == "2":
                calc = 2 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

            if type == "3":
                calc = 3 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

            if type == "4":
                calc = 4 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

            if type == "5":
                calc = 5 * price[4]
                count = count + calc
                paneer_pulav(type, calc)

        cur.execute("SELECT Sweets from admin_sweets where Date=curdate()")
        data3 = cur.fetchall()
        price = []
        cur.execute("SELECT price from admin_sweets where Date=curdate()")
        tejas = cur.fetchall()
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('gulab_jamun'):
            g_jamun = data3[0]
            type = request.form['type14']
            calc = 0

            def gulab_jamun(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_sweets(U_name,Date,Sweets,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, g_jamun, type, [cost]))
                db.commit()

            if type == "0":
                gulab_jamun(type, calc)

            if type == "1":
                calc = 1 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

            if type == "2":
                calc = 2 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

            if type == "3":
                calc = 3 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

            if type == "4":
                calc = 4 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

            if type == "5":
                calc = 5 * price[0]
                count = count + calc
                gulab_jamun(type, calc)

        if request.form.getlist('shrikhand'):
            shrikhand = data3[1]
            type = request.form['typea']
            calc = 0

            def shrikhand1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_sweets(U_name,Date,Sweets,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, shrikhand, type, [cost]))
                db.commit()

            if type == "0":
                shrikhand1(type, calc)

            if type == "1":
                calc = 1 * price[1]
                count = count + calc
                shrikhand1(type, calc)

            if type == "2":
                calc = 2 * price[1]
                count = count + calc
                shrikhand1(type, calc)

            if type == "3":
                calc = 3 * price[1]
                count = count + calc
                shrikhand1(type, calc)

            if type == "4":
                calc = 4 * price[1]
                count = count + calc
                shrikhand1(type, calc)

            if type == "5":
                calc = 5 * price[1]
                count = count + calc
                shrikhand1(type, calc)

        if request.form.getlist('amrakhand'):
            Amrakhand = data3[2]
            type = request.form['typeb']
            calc = 0

            def Amrakhand1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_sweets(U_name,Date,Sweets,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, Amrakhand, type, [cost]))
                db.commit()

            if type == "0":
                Amrakhand1(type, calc)

            if type == "1":
                calc = 1 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

            if type == "2":
                calc = 2 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

            if type == "3":
                calc = 3 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

            if type == "4":
                calc = 4 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

            if type == "5":
                calc = 5 * price[2]
                count = count + calc
                Amrakhand1(type, calc)

        if request.form.getlist('rabdi'):
            rabdi = data3[3]
            type = request.form['typec']
            calc = 0

            def rabdi1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_sweets(U_name,Date,Sweets,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, rabdi, type, [cost]))
                db.commit()

            if type == "0":
                rabdi1(type, calc)

            if type == "1":
                calc = 1 * price[3]
                count = count + calc
                rabdi1(type, calc)

            if type == "2":
                calc = 2 * price[3]
                count = count + calc
                rabdi1(type, calc)

            if type == "3":
                calc = 3 * price[3]
                count = count + calc
                rabdi1(type, calc)

            if type == "4":
                calc = 4 * price[3]
                count = count + calc
                rabdi1(type, calc)

            if type == "5":
                calc = 5 * price[3]
                count = count + calc
                rabdi1(type, calc)

        cur.execute("SELECT Accompaniments from admin_accompaniments where Date=curdate()")
        data4 = cur.fetchall()
        price = []
        cur.execute("SELECT price from admin_accompaniments where Date=curdate()")
        tejas = cur.fetchall()
        for row in tejas:
            price.append(row[0])

        if request.form.getlist('masala_chaas'):
            chaas = data4[0]
            type = request.form['type16']
            calc = 0

            def Masala_chaas(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_accompaniments(U_name,Date,Accompaniments,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, chaas, type, [cost]))
                db.commit()

            if type == "0":
                Masala_chaas(type, calc)

            if type == "1":
                calc = 1 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

            if type == "2":
                calc = 2 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

            if type == "3":
                calc = 3 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

            if type == "4":
                calc = 4 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

            if type == "5":
                calc = 5 * price[0]
                count = count + calc
                Masala_chaas(type, calc)

        if request.form.getlist('curd'):
            curd = data4[1]
            type = request.form['type17']
            calc = 0

            def curd1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_accompaniments(U_name,Date,Accompaniments,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, curd, type, [cost]))
                db.commit()

            if type == "0":
                curd1(type, calc)

            if type == "1":
                calc = 1 * price[1]
                count = count + calc
                curd1(type, calc)

            if type == "2":
                calc = 2 * price[1]
                count = count + calc
                curd1(type, calc)

            if type == "3":
                calc = 3 * price[1]
                count = count + calc
                curd1(type, calc)

            if type == "4":
                calc = 4 * price[1]
                count = count + calc
                curd1(type, calc)

            if type == "5":
                calc = 5 * price[1]
                count = count + calc
                curd1(type, calc)

        if request.form.getlist('salad'):
            salad = data4[2]
            type = request.form['type18']
            calc = 0

            def salad1(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_accompaniments(U_name,Date,Accompaniments,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, salad, type, [cost]))
                db.commit()

            if type == "0":
                salad1(type, calc)

            if type == "1":
                calc = 1 * price[2]
                count = count + calc
                salad1(type, calc)

            if type == "2":
                calc = 2 * price[2]
                count = count + calc
                salad1(type, calc)

            if type == "3":
                calc = 3 * price[2]
                count = count + calc
                salad1(type, calc)

            if type == "4":
                calc = 4 * price[2]
                count = count + calc
                salad1(type, calc)

            if type == "5":
                calc = 5 * price[2]
                count = count + calc
                salad1(type, calc)

        if request.form.getlist('roasted_papad'):
            r_papad = data4[3]
            type = request.form['type19']
            calc = 0

            def Roasted_papad(type, calc):
                cur = db.cursor()
                cost = str(calc)
                query = "INSERT INTO half_extra_accompaniments(U_name,Date,Accompaniments,Quantity,Cost) VALUES(%s,%s,%s,%s,%s)"
                cur.execute(query, ([a], date, r_papad, type, [cost]))
                db.commit()

            if type == "0":
                Roasted_papad(type, calc)

            if type == "1":
                calc = 1 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

            if type == "2":
                calc = 2 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

            if type == "3":
                calc = 3 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

            if type == "4":
                calc = 4 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

            if type == "5":
                calc = 5 * price[3]
                count = count + calc
                Roasted_papad(type, calc)

        cur.execute("Select * from sign_up where U_name ='" + a + "'")
        data = cur.fetchone()
        #      print(data)
        userr = {'name': data[0], 'U_name': data[7]}
        return render_template("successful2.html", userr=userr)

    return render_template("halfm.html", user=user, user1=user1, user2=user2, user3=user3, user4=user4)


'''@app.route('/username', methods=['GET', 'POST'])
def username(a,password):
    return render_template("username.html")
'''


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    # global first_name, user
    global user
    if request.method == 'POST':
        date = datetime.date.today()
        first_name = request.form['fname']
        email = request.form['email']
        phone = request.form['phone']
        area = request.form['area']
        address = request.form['address']
        type = request.form['type']
        password = request.form['password']
        if type == "Guest":
            a = ("GU" + str(randint(100, 999)))
            cur = db.cursor()
            query = "INSERT INTO sign_up(first_name,email,phone,area,address,password,type,U_name) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query, (
                first_name, email, phone, area, address, sha256_crypt.encrypt(password), type, [a]))
            db.commit()

            user = {
                'name': a,
                'pass': password
            }
            return render_template("username1.html", user=user)

        if type == "Monthly full tiffin":
            a = ("MF" + str(randint(100, 999)))
            cur = db.cursor()
            query = "INSERT INTO sign_up(first_name,email,phone,area,address,password,type,U_name) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query, (
                first_name, email, phone, area, address, sha256_crypt.encrypt(password), type, [a]))
            db.commit()

            query = "INSERT INTO payment(first_name,pdate,amount,type) VALUES(%s,%s,%s,%s)"
            cur.execute(query, (first_name, date, 1300, type))
            db.commit()

            user = {
                'name': a,
                'pass': password
            }
            return render_template("username.html", user=user)

        if type == "Monthly half tiffin":
            a = ("MH" + str(randint(100, 999)))
            cur = db.cursor()
            query = "INSERT INTO sign_up(first_name,email,phone,area,address,password,type,U_name) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query, (
                first_name, email, phone, area, address, sha256_crypt.encrypt(password), type, [a]))
            db.commit()

            query = "INSERT INTO payment(first_name,pdate,amount,type) VALUES(%s,%s,%s,%s)"
            cur.execute(query, (first_name, date, 800, type))
            db.commit()

            user = {
                'name': a,
                'pass': password
            }
            return render_template("username2.html", user=user)

    return render_template("sign_up.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    global user
    global first_name
    # global a
    error = None
    if request.method == 'POST':
        first_name = request.form['fname']
        password = request.form['password']
        #  match=sha256_crypt.encrypt(password)
        cur = db.cursor()
        # cur.execute("SELECT * FROM sign_up WHERE U_name='" + first_name + "' AND password ='" + password + "'")

        cur.execute(
            "Select * from sign_up where U_name ='" + first_name + "'")
        data = cur.fetchone()
        user = {'password': data[5]}

        print(sha256_crypt.verify(password, user['password']))
        if (sha256_crypt.verify(password, user['password'])):

            if cur.execute(
                    "Select U_name from sign_up where U_name ='" + first_name + "' AND type like 'Guest'"):
                return redirect(url_for('guest_dash', a=first_name))

        else:
            return "<script>alert('Incorrect Username Or Password.Re-Enter it :)')</script>"
        if (sha256_crypt.verify(password, user['password'])):

            if cur.execute(
                    "Select * from sign_up where U_name ='" + first_name + "' AND type like 'Monthly full tiffin'"):
                return redirect(url_for('full_dash', a=first_name))

        if (sha256_crypt.verify(password, user['password'])):

            if cur.execute(
                    "Select U_name from sign_up where U_name ='" + first_name + "' AND type like 'Monthly half tiffin'"):
                return redirect(url_for('half_dash', a=first_name))

        if cur.execute(
                "Select U_name,password from sign_up where U_name ='" + first_name + "' AND U_name like 'admin'"):

            return redirect(url_for('admin_main', a=first_name))

        else:
            return render_template("login.html")
            # error = "Incorrect Username Or Password"

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
