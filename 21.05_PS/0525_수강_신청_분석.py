def course_selection(course_list):
    # 시작 시간 순 정렬
    course_list.sort(key=lambda x:x[0])
    # 종료 시간 순 정렬
    course_list.sort(key=lambda x:x[1])
    course_select = [course_list[0]]
    j = 0
    for i in course_list:
        # (이후 수업의 시작 시간) > (이전 수업의 종료 시간)
        if (i[0] > course_select[j][1]):
            course_select.append(i)
            j += 1
    return course_select


print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
