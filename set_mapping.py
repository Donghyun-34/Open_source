import json

class Device_map:
    def __init__(self, name, sdid, dy_list):
        self.name = name
        self.sd_id = sdid
        self.dy_id = dict( {'c0' : dy_list[0], 'c1':dy_list[1], 's0':dy_list[2], 's1':dy_list[3]} )


'''
basic = {
    "name" = "device_name",
    "sd_id" = "111111",
    "dy_id" = {
        "c0":"",
        "c1":"",
        "s0":"",
        "s1":""
    }
}
'''

def options(input) -> bool:
    exit_comm = ['e', 'exit', 'Exit']
    update_comm = ['u', 'update', 'Update']
    delete_comm = ['d', 'delete', 'Delete']
    add_comm = ['a', 'add', 'Add']
    read_comm = ['r', 'read', 'Read']
    help_comm = ['h', 'help', 'Help']

    argv = input.split(' ')
    
    if argv[0] in help_comm:
        print("WIP")

    elif argv[0] in exit_comm:
        print("Exiting...")
        return False

    elif argv[0] in update_comm:
        if(len(argv == 2)):
            pass
        else:
            print("Wrong usage of 'update'!! Type 'h' or 'help' for more info.")

    elif argv[0] in delete_comm:
        if(len(argv == 2)):
            pass

    elif argv[0] in add_comm:
        pass

    elif argv[0] in read_comm:
        pass

    else:
        print("Unknown opiont \'", argv[0], "\' !!!" )

    return True
'''

metadata : [{sdit:name}]

st_id -> 이름, 
    htto:{주소}, dy_id -> http:[code] 
'''

#전처리
try:
    with open('./Data/mapping_table.json') as j_file:
        j_data = json.load(j_file)

except FileNotFoundError:
    print("There is no mapping table!!!")
    print("Creating New file...")
    #파일 읽어오기 / 없으면 빈 파일 생성
#수행 동작 선택

cont = True
while(cont):
    str = input("lestening[=]")
    cont = options(str)
    #추가 / 삭제 / 수정 / 종료 / 출력

