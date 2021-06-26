def multiple_table():
    row=1
    while row<=9:
        col=1
        while col<=row:
            print("%d * %d = %d" %(col, row, col*row), end=('\t'))
            col+=1
        print("")
        row+=1



def sum_2_sum(sum1,sum2):
  result=sum1+sum2
  #print("%d + %d = %d" %(sum1, sum2, result))
  return result

print(sum_2_sum(10,20))