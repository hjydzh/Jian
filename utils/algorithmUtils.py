#coding:utf-8

#最大子串
def lcs(str1, str2):
    str1 = '0' + str1
    str2 = '0' + str2
    matrix = gen_matrix(len(str1), len(str2))
    routine = gen_matrix(len(str1), len(str2))
    for i in range(len(str1)):
        for j in range(len(str2)):
            result = sub_str_lcs(matrix, i, j, str1, str2, routine)
            matrix = result[0]
            routine = result[1]
    return find_lcs(matrix, routine, len(str1)-1, len(str2)-1, str1)


def find_lcs(matrix, routine, row, col, str1):
    max_num = matrix[row][col]
    return find_routine(routine, row, col, str1)

def find_routine(routine, row, col,str1):
    positions = []
    positions = find_former_position(routine, (row, col), positions)
    lcs_str = ''
    for position in positions:
        if routine[position[0]][position[1]] == '↖':
            lcs_str = lcs_str + str1[position[0]]
    return lcs_str


def find_former_position(routine, position, positions):
    row = position[0]
    col = position[1]
    if row ==0 or col == 0:
        return positions
    #if positions[-1][0] ==0 or positions[-1][1] == 0:
        #return positions
    if routine[row][col] == '←':
        former_positione = (row, col - 1)
    elif  routine[row][col] == '↖':
        former_positione = (row - 1, col - 1)
    elif  routine[row][col] == '↑':
        former_positione = (row - 1, col )
    else:
        former_positione = (0, 0)
    former_routines = find_former_position(routine, former_positione, positions)
    positions.append(position)
    return positions


def sub_str_lcs(c, i, j, str_i, str_j, routine):
    if i < 0 or j < 0:
        return (c, routine)
    if i ==0 or j == 0:
        c[i][ j] = 0
        routine[0][0] = 0
    elif str_i[i] == str_j[j]:
        c[i ][j] = c[i-1][ j-1] + 1
        routine[i][j] = '↖'
    elif str_i[i] != str_j[j]:
        c[i ][j] = max(c[i-1 ][j], c[i ][j-1])
        if c[i][j] == c[i-1 ][j]:
            routine[i][j] = '↑'
        else:
            routine[i][j] = '←'
    return (c, routine)


def gen_matrix(rows,cols):
    return [[0 for col in range(cols)] for row in range(rows)]


def print_matrix(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print matrix[i][j],
        print '\n'


#判断两条日志是否一致
def msg_same(msg1, msg2):
    lcs_msg = lcs(msg1, msg2)
    max_len = max(len(msg1), len(msg2))
    a =  len(lcs_msg) / max_len
    if len(lcs_msg) / max_len > 0.75:
        return True
    return False

def RSHash(s):
    b = 378551
    a = 63689
    hash_num = 0
    for i in range(len(s)):
        hash_num = hash_num * a + ord(s[i])
        a = a * b
    return hash_num

def DEKHash(s):
    hash_num = len(s)
    for i in range(len(s)):
        hash_num = ((hash_num << 5) ^ (hash_num >> 27)) ^ + ord(s[i])
    return hash_num

def SDBMHash(s):
    hash_num = 0
    for i in range(len(s)):
        hash_num = ord(s[i]) + (hash_num << 6) + (hash_num << 16) - hash_num
    return hash_num

def BKDRHash(s):
    seed = 131
    hash_num = 0
    for i in range(len(s)):
        hash_num = (hash_num * seed) + ord(s[i])
    return hash_num

def bloom_filter_insert(seq,bit):
    index_1 = index(RSHash(seq) % 102400 )
    index_2 = index(DEKHash(seq)  % 102400)
    index_3 = index(SDBMHash(seq) % 102400 )
    index_4 = index(BKDRHash(seq) % 102400 )
    bit = bit | index_1 |index_2 |index_3 |index_4
    return bit

def index(hash_val):
    return (1 << hash_val)

#布隆过滤器
def bloom_filter_exist(seq,bit):
    index_1 = index(RSHash(seq)  % 102400)
    index_2 = index(DEKHash(seq) % 102400 )
    index_3 = index(SDBMHash(seq) % 102400 )
    index_4 = index(BKDRHash(seq)  % 102400)
    return (bit & index_1 > 0) and (bit & index_2> 0) and (bit & index_3> 0) and (bit & index_4> 0)
