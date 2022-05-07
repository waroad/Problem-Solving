def solution(survey, choices):
    arr= {"R":0,  "T":0,  "C":0,  "F":0,  "J":0,  "M":0,  "A":0,  "N":0} #R, T, C, F, J, M, A, N

    for i in range(len(choices)):
        if choices[i]>4:
            arr[survey[i][1]]+=choices[i]-4
        else:
            arr[survey[i][0]]+=4-choices[i]
    ans=""
    if arr["R"]>=arr["T"]:
        ans+="R"
    else:
        ans+="T"
    if arr["C"]>=arr["F"]:
        ans+="C"
    else:
        ans+="F"
    if arr["J"]>=arr["M"]:
        ans+="J"
    else:
        ans+="M"
    if arr["A"]>=arr["N"]:
        ans+="A"
    else:
        ans+="N"
    return ans



solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])