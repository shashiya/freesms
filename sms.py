from requests import post
url='https://sv2.ideamarthosting.dialog.lk/lakpriya1016Apps/wapp/otp2.php'
num=input('Enter Number: ')
msg=input('Enter Msg: ')
json={"id":num[1:],"apphash":msg}
req=post(url,json=json)
print(req.text)
