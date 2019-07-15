import time

true_password = '123'


def check_password(password):
    if password == true_password:
        print('unlock')
        return True
    else:
        time.sleep(0.1)


start = time.time()
for i in range(0, 999):
    if check_password(str(i)):
        break

print(str(time.time()-start) + 'seconds')
