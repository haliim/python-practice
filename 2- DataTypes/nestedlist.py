if __name__ == '__main__':
    List = []
    Sorted_List = []
    Score_List = []
    Uniqe_Sorted_Score_List = []
    Students_List = []
    Sorted_Student_List = []
#===================================

    for _ in range(int(input())):
        Sub_List = []
        name = input()
        Sub_List.append(name)
        score = float(input())
        Sub_List.append(score)
        List.append(Sub_List)
#=======================================
#    List = [['ahmed', 1.0], ['rana', 2.0], ['rawan', 3.0], ['bassel', 2.0]]
    for name, score in List:
        Score_List.append(score)
    Uniqe_Sorted_Score_List = sorted(list(set(Score_List)))
    for name, score in List:
        if score == Uniqe_Sorted_Score_List[1]:
            Students_List.append(name)
    Sorted_Student_List = sorted(Students_List)
    for name in Sorted_Student_List:
        print(name)