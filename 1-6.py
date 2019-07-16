with open('test_file.txt', 'w') as myfile:
    myfile.write('сетевое программирование\nсокет\nдекоратор\n')
print(myfile)
with open('test_file.txt') as myfile:
    for line in myfile:
        print(line.encode('cp1251').decode('utf-8','replace'))

# не уверен, правильно ли понял это задание, получилось вот так:

# <_io.TextIOWrapper name='test_file.txt' mode='w' encoding='cp1251'>
# ������� ����������������
#
# �����
#
# ���������