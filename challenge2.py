#nro tnstj dltkdgka
# 모든 달은 28일까지 

# privacy에 저장된 애들을 가질고 

def solution(today, terms, privacies):
    answer = []
    to_year, to_month, to_day = map(int, today.split('.'))

    dic = {}
    for i in terms:
        dic[i.split()[0]] = int(i.split()[1])
        date, condition = privacies[i].split()
        year, month, day = map(int, date.split('.'))
        
        if day == 1:
            month -= 1
            day = 28
        if month + dic[condition] > 13:
            year += 1
            month -= 12
        
        if to_year < year:
            continue
        elif to_year == year:
            if month > to_month:
                answer.append(i + 1)
            elif month == to_month:
                if day > to_day:
                    answer.append(i + 1)
                else:
                    continue
            else:
                continue
        else:
            answer.append(i + 1)
        

   
        
                
    # 날짜가 1이면 month - 1 을 하고 날짜를 28로 변경
    # month를 더하는데 13을 넘어가면 year을 하나 더하고 month - 12를 함
    # year 은할거 없음
                
        
    return answer



        
        
        if month + dic[condition] < 13:
            print(' 13 보다 작음 ')
            if month + dic[condition] > to_month:
                print(' 더 한다 ')
                answer.append(i + 1)
                continue
            elif month + dic[condition] == to_month:
                if day > to_day:
                    answer.append(i + 1)
                    continue
                else:
                    continue
            else:
                continue

        else:
            if to_year - year < 1:
                continue
            else:
                if month + dic[condition] - 12 > to_month:
                    continue
                else:
                    if day > to_day:
                        answer.append(i + 1)
                        continue
                    else:
                        continue
                    
                        
    return answer
