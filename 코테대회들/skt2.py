def solution(periods, payments, estimates):
    customer_current=[0]*len(periods)
    customer_predict=[0]*len(periods)
    answer = [0]*2
    for ind, i in enumerate(periods):
        if i<23:
            continue
        else:
            customer_current[ind]=sum(payments[ind])
            customer_predict[ind]=sum(payments[ind][1:12])+estimates[ind]
    for i in range(len(periods)):
        if periods[i]<23:
            continue
        elif periods[i]==23:
            if customer_predict[i]>=900000:
                answer[0]+=1
        elif periods[i]<59:
            if customer_current[i] < 900000 <= customer_predict[i]:
                answer[0]+=1
            elif customer_predict[i] < 900000 <= customer_current[i]:
                answer[1]+=1
        elif periods[i]==59:
            if customer_current[i] < 900000 and customer_predict[i] >= 600000:
                answer[0] += 1
            elif customer_predict[i] < 600000 and customer_current[i] >= 900000:
                answer[1] += 1
        else:
            if customer_current[i] < 600000 <= customer_predict[i]:
                answer[0]+=1
            elif customer_predict[i] < 600000 <= customer_current[i]:
                answer[1]+=1

    return answer


print(solution([20, 23, 24], [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]], [100000, 100000, 100000]))