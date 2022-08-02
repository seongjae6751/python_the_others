schedule_num = int(input('작업의 갯수:'))
schedule_dict = {} # 빈 딕셔너리
# 딕셔너리 입력 받아 만들기
while schedule_num > 0:
    schedule_num = schedule_num - 1
    Id = int(input('작업 ID: '))
    Rank = int(input('작업 우선 순위: '))
    s_time = int(input('작업 시간: '))
    schedule_dict[Id] = [Rank, s_time]
print('입력 받은 작업 딕셔너리 : ', schedule_dict)
dict_list = list(zip(schedule_dict.keys(), schedule_dict.values())) # 딕셔너리 리스트로 변환

# 리스트 우선순위 기준, 선택정렬
N = len(dict_list)
for i in range(0, N - 1): # 범위를 앞부터 뒤까지 좁혀감
    low_index = i # 가장 작은 것을 선별
    for j in range(i + 1, N):
        if dict_list[low_index][1][0] >  dict_list[j][1][0]:
            low_index = j
    dict_list[i], dict_list[low_index] = dict_list[low_index], dict_list[i] # 가장 작은 것과 맨 앞의 것 교환   

# 리스트 작업시간 기준, 선택정렬
N = len(dict_list)
for i in range(0, N - 1): # 범위를 앞부터 뒤까지 좁혀감
    low_index = i # 가장 작은 것을 선별
    for j in range(i + 1, N):
        if dict_list[low_index][1][0] ==  dict_list[j][1][0] and dict_list[low_index][1][1] >  dict_list[j][1][1]: # 우선순위가 같고 시간이 작은거 앞으로
            low_index = j
    dict_list[i], dict_list[low_index] = dict_list[low_index], dict_list[i]
print('정렬된 작업 리스트 : ', dict_list)


