for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int(pow(10, i)*0.123456789)*pow(10, i-1) + (987654321 % ((987654321//pow(10, i-1))*pow(10, i-1))))

