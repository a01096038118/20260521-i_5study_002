members = {}

def getSelectedMenuNum():
    selectedMenuNum = int(input('1.회원가입  2.로그인   3.나의 회원 정보 출력  4.모든 회원 정보 출력  5. 회원 탈퇴 6. 회원정보 수정 99.종료'))

    return selectedMenuNum

def inputUserData():
    uID = input('회원ID: ')
    uPW = input('회원PW (특수문자 &를 사용하여 입력하세요.): ')
    uEMAIL = input('회원EMAIL:  ')
    uPHONE = input('회원PHONE:  ')

    return uID, uPW, uEMAIL, uPHONE

def setNewMember(uID, uPW, uEMAIL, uPHONE):
    members[uID] = {
                'uID': uID,
                'uPW': uPW,
                'uEMAIL': uEMAIL,
                'uPHONE': uPHONE
                }

def checkLogin(uID, uPW):
    if uID in members:
        uInfo = members[uID]
        if uInfo ['uPW'] == uPW:
            return True

    return False

def printUserInfo(uInfo):
    for key, value in uInfo.items():
        print(f'{key}: {value}')

def printMembersInfo(members):
    for key, value in members.items():
            print(f'{key}: {value}')

