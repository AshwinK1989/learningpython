import StringIO

s = 'My name is Ashwin'

f = StringIO.StringIO(s)

f.writelines(['I stay at Dadar ' 'I am a QA Automation Engineer'])

f.seek(0)
print(f.readlines())