members = {}

def getSelectedMenuNum():
    selectedMenuNum = int(input('1.회원가입  2.로그인   3.나의 회원 정보 출력  4.모든 회원 정보 출력  5. 회원 탈퇴 6. 회원정보 수정 99.종료'))

    return selectedMenuNum

def inputUserData():
    uId = input('회원ID: ')
    uPw = input('회원PW (특수문자 &를 사용하여 입력하세요.): ')
    uEmail = input('회원EMAIL:  ')
    uPhone = input('회원PHONE:  ')

    return uId, uPw, uEmail, uPhone

def setNewMember(uId, uPw, uEmail, uPhone):
    members[uId] = {
                'uId': uId,
                'uPw': uPw,
                'uEmail': uEmail,
                'uPhone': uPhone
                }

def checkLogin(uId, uPw):
    if uId in members:
        uInfo = members[uId]
        if uInfo ['uPw'] == uPw:
            return True

    return False

def printUserInfo(uInfo):
    for key, value in uInfo.items():
        print(f'{key}: {value}')

def printMembersInfo(members):
    for key, value in members.items():
            print(f'{key}: {value}')

def findMember(uEmail, uPhone):
    for key, value in members.items():

        if value['uEmail'] == uEmail and value['uPhone'] == uPhone:
            return key, value
    return None, None