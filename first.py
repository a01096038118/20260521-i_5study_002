'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1.회원가입  2.로그인   3.나의 회원 정보 출력  4.모든 회원 정보 출력  5. 회원 탈퇴 6. 회원정보 수정 99.종료
사용자가
'1.회원가입'을 선택하면 회원ID, 회원PW, 회원Email, 회원Phone 정보를 입력받아 회원가입 진행한다.
'2.로그인'을 선책하면 회원ID, 회원PW를 입력받아 로그인 '성공' 또는 '실패'를 출력한다.
'3.나의 회원 정보 출력'를 선택하면 회원ID와 회원PW를 입력받아 일치하는 회원 정보를 모두 출력한다.
'4.모든 회원 정보 출력'를 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'99.종료'를 선택하면 프로그램 종료 시킨다.
'''

flag = True
members = {}

import member

while flag:
    selectedMenuNum =member.getSelectedMenuNum()
    if selectedMenuNum == 1:
        
        uID = input('회원ID:  ')
        while True:
            uPW = input('회원PW는 특수문자 &를 사용하여 입력하세요:  ')

            if '&' not in uPW:  # True
                print('사용할 수 없는 비밀번호 입니다. 다시 작성해주세요.')
             
            else:
                break
        while True:    
            uEMAIL = input('회원EMAIL:  ')
            if '@' not in uEMAIL:  
                print('사용할 수 없는 이메일 입니다. 다시 작성해주세요.')

            else:
                break
        while True:
            uPHONE = input('회원PHONE:  ')
            if '-' not in uPHONE:  
                print('사용할 수 없는 번호입니다. 다시 작성해주세요.')
            else:    
                break

        members[uID] = {
            'uID': uID,
            'uPW': uPW,
            'uEMAIL': uEMAIL,
            'uPHONE': uPHONE
            }
        print('회원가입 성공')
            
    if selectedMenuNum == 2:
                while True:
                    uID = input('회원ID: ')
                    if uID not in members:
                        print('잘못입력 하셨습니다. 다시 입력하세요.')
                    else:
                        break

                while True:    
                    uPW = input('회원PW: ')
                    if uPW not in members:
                        print('잘못입력 하셨습니다. 다시 입력하세요.')
                    else:
                        print('로그인 성공')  
                   

    if selectedMenuNum == 3:
        uID = input('회원ID: ')
        uPW = input('회원PW: ')

        if uID in members:
             uInfo = members[uID]
             if uInfo ['uPW'] == uPW:
                  print('로그인 성공')

                  for key, value in uInfo.items():
                       print(f'{key}: {value}')

    if selectedMenuNum == 4:
        for key, value in members.items():
            print(f'{key}: {value}')

    if selectedMenuNum == 5:
        uID = input('삭제할 회원ID 입력: ')
        uPW = input('회원PW 입력: ')
         
        if uID in members:
            uInfo = members[uID]
            if uInfo ['uPW'] == uPW:
                del members[uID]
                print('회원탈퇴 되었습니다.')

    if selectedMenuNum == 6:
        uID = input('회원ID: ')
        uPW = input('회원PW: ')
        if uID in members:
            uInfo = members[uID]
            if uInfo ['uPW'] == uPW:
                print('인증 성공')

                updateKey = input('수정할 목록 입력: ')
                updateValue = input('새로운 값 입력: ')

                uInfo[updateKey] = updateValue
                for key, value in uInfo.items():
                    print(f'{key}: {value}') 
                    
    if selectedMenuNum == 7:
        selectedFindMenu = int(input('ID만 찾으실 분은 1번 , PW만 찾으실 분은: 2번 , 둘다 찾으실 분은 3번을 입력해주세요. '))
        if selectedFindMenu == 1:
            print('아이디 찾기를 하시려면 회원님의 이메일과 전화번호를 입력해주세요.')
            uEmail = input('회원 EMAIL: ')
            uPhone = input('회원 PHONE: ')
            found = False

            for key, value in members.items():
                if value['uEMAIL'] == uEmail and value['uPHONE'] == uPhone:
                    print(f'회원님의 아이디: {key} ')
                    found = True
                    break

                if found == False:
                    print('찾을 수 없는 회원 정보가 없습니다.')

        if selectedFindMenu == 2:
            print('비밀번호 찾기를 하시려면 회원님의 이메일과 전화번호를 입력해주세요.')
            uEmail = input('회원 EMAIL: ')
            uPhone = input('회원 PHONE: ')
            found = False
            for key, value in members.items():
                if value['uEMAIL'] == uEmail and value['uPHONE'] == uPhone:
                    print(f'회원님의 비밀번호: {value['uPW']} ')
                    found = True
                    break

            if found == False:
                print('찾을 수 없는 회원 정보가 없습니다.')            


        if selectedFindMenu == 3:
            print('아이디/비밀번호 찾기를 하시려면 회원님의 이메일과 전화번호를 입력해주세요.')
            uEmail = input('회원 EMAIL: ')
            uPhone = input('회원 PHONE: ')
            found = False
            for key, value in members.items():
                if value['uEMAIL'] == uEmail and value['uPHONE'] == uPhone:
                    print(f'회원님의 아이디: {key}, 회원님의 비밀번호: {value['uPW']} ')
                    found = True
                    break

            if found == False:
                print('찾을 수 없는 회원 정보가 없습니다.')

    if selectedMenuNum == 99:
        print('프로그램을 종료합니다. ')
        flag = False
        break