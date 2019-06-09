numbers = {'0': '', '00':'', '000':'', '1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', '10':'Ten', 
           '11':'Eleven', '12':'Twelve', '13':'Thirteen', '14':'Fourteen', '15':'Fifteen', '16':'Sixteen', '17':'Seventeen', '18':'Eighteen', '19':'Nineteen', 
           '20':'Twenty', '30':'Thirty', '40':'Forty', '50':'Fifty', '60':'Sixty', '70':'Seventy', '80':'Eighty', '90':'Ninety'}

orders_of_magnitude = {1: 'Thousand', 2: 'Million', 3: 'Billion'}

def two_digits_to_word(n):
    if (n[0] == '0'):
        return numbers[n[1]]
    return numbers[n] if (int(n) <= 20) else numbers[n[0] + '0'] + ' ' + numbers[n[1]]

def three_digits_to_word(n):
    if (n[0] == n[1] == n[2] == '0'):
        return ''
    if (n[0] != '0'):
        return numbers[n[0]] + ' Hundred ' + two_digits_to_word(n[1:])
    else:
        return two_digits_to_word(n[1:])

t = int(input())
for _ in range(t):
    n = input()
    word = ''
    if len(n) == 13:
        word = 'One Trillion'
    elif len(n) == 1:
        word = numbers[n[0]] if n[0] != '0' else 'Zero'
    elif len(n) == 2:
        word = two_digits_to_word(n)
    else:
        word = three_digits_to_word(n[-3:])
        n, order = n[:-3], 1
        while (len(n) != 0):
            word = (orders_of_magnitude[order] + ' ' + word) if int(n[-3:]) > 0 else word 
            if len(n) >= 3:
                word = three_digits_to_word(n[-3:]) + ' ' + word
                n = n[:-3]
                order += 1
            elif len(n) == 2:
                word = two_digits_to_word(n) + ' ' + word
                break
            elif len(n) == 1:
                word = numbers[n] + ' ' + word
                break
    print(word.replace('  ', ' ').replace('  ', ' '))
