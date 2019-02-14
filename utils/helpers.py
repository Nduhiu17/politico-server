import json

party_to_post = {
    "name": "Democrat",
    "hqaddress": "New york",
    "logoUrl": "www.logo.com/logo"
}

party1_to_post = {
    "name": "K",
    "hqaddress": "New york",
    "logoUrl": "www.logo.com/logo"
}

party2_to_post = {
    "name": "democrat",
    "hqaddress": "1234",
    "logoUrl": "www.logo.com/logo"
}

party3_to_post = {
    "name": "democrat",
    "hqaddress": "New york",
    "logoUrl": "1234"
}

party4_to_post = {
    "hqaddress": "New york",
    "logoUrl": "www.photos/logo"
}

party5_to_post = {
    "name": "democrat",
    "logoUrl": "www.photos/logo"
}

party6_to_post = {
    "name": "Democrat",
    "hqaddress": "New york"
}

party7_to_post = {
    "name": 12345678,
    "hqaddress": 12345678,
    "logoUrl": 12344567
}

party8_to_post = {
    "name": "Democratedited",
    "hqaddress": "New yorkedited",
    "logoUrl": "www.logo.com/logo"
}

office_to_post = {
    "office_type": "federal",
    "name": "Democrat"
}

office1_to_post = {
    "office_type": "federal"
}

office2_to_post = {
    "name": "Democrat"
}

office3_to_post = {
    "office_type": 12345678,
    "name": "Democratic republic"
}

office4_to_post = {
    "office_type": "Federal",
    "name": 123456789
}

office5_to_post = {
    "office_type": "federal",
    "name": "demo"
}

office6_to_post = {
    "office_type": "federal",
    "name": "D"
}

office_to_post8 = {
    "office_type": 1223345,
    "name": "Democrat"
}

offices_allowed = ["federal", "legislative", "state", "local government"]

user = {
    "firstname": "Antony1",
    "lastname": "Nduhiu1",
    "othername": "Mundia1",
    "email": "nduhiu@gmail1.com",
    "phonenumber": "07221172641",
    "passporturl": "www.passport.com/ph1oto",
    "password": "Password2015"
}

user1 = {
    "lastname": "Nduhiu1",
    "othername": "Mundia1",
    "email": "nduhiu@gmail10.com",
    "phonenumber": "07221172641",
    "passporturl": "www.passport.com/ph1oto",
    "password": "Password2015"

}

user2 = {
    "firstname": "Antony1",
    "othername": "Mundia1",
    "email": "nduhiu@gmail100.com",
    "phonenumber": "07221172641",
    "passporturl": "www.passport.com/ph1oto",
    "password": "Password2015"

}
user3 = {
    "firstname": "Antony1",
    "lastname": "Nduhiu1",
    "email": "nduhiu@gmail1000.com",
    "phonenumber": "07221172641",
    "passporturl": "www.passport.com/ph1oto",
    "password": "Password2015"

}

user4 = {
    "firstname": "Antony1",
    "lastname": "Nduhiu1",
    "email": "nduhiu@gmail10000.com",
    "phonenumber": "07221172641",
    "passporturl": "www.passport.com/ph1oto",
    "password": "Password2015"

}

user5 = {
    "firstname": "Antony1",
    "lastname": "Nduhiu1",
    "phonenumber": "07221172641",
    "passporturl": "www.passport.com/ph1oto",
    "password": "Password2015"

}

user6 = {
    "firstname": "Antony1",
    "lastname": "Nduhiu1",
    "othername": "Mundia1",
    "email": "nduhiu@gmail1.com",
    "phonenumber": "07221172641",
    "password": "Password2015"
}

user7 = {
    "firstname": "Antony1",
    "lastname": "Nduhiu1",
    "othername": "Mundia1",
    "email": "nduhiu@gmccail1.com",
    "password": "Password2015"
}

user8 = {
    "firstname": "Antony1",
    "lastname": "Nduhiu1",
    "othername": "Mundia1",
    "phonenumber": "07221172641",
    "passporturl": "www.passport.com/ph1oto",
    "password": "Password2015"
}

user9 = {
    "firstname": "Antony1",
    "lastname": "Nduhiu1",
    "othername": "Mundia1",
    "email": "nduhiu@gmail1.com",
    "phonenumber": "07221172641",
    "passporturl": "www.passport.com/ph1oto"
}

user10 = {
    "firstname": 1245665665,
    "lastname": 465456456456,
    "othername": 4565464564654,
    "email": 14514361414,
    "phonenumber": 456444456346436,
    "passporturl": 336456465464654
}

user11 = {
    "firstname": "Antony1",
    "lastname": "Nduhiu1",
    "othername": "Mundia1",
    "email": "nduhiugmail1com",
    "phonenumber": "07221172641",
    "passporturl": "www.passport.com/ph1oto",
    "password": "Password2015"
}

user12 = {
    "email": "nduhiugmail1com"
}

user13 = {
    "email": 545645646545645465465,
    "password": 1654654564564564564564

}

user14 = {
    "email": "nduhiu@gmgfhfghfail10.com",
    "password": "Password2015"
}


def signup_user(self):
    """function that registers a user"""
    return self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(user),
        content_type='application/json'
    )
