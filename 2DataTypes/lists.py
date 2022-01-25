def handler(result):
    Input = input().split()
    command = Input[0]
    Values = Input[1:]
    if command == 'print':
        print(result)
    else:
        execute = 'result.' + command + "("+",".join(Values) + ")"
        eval(execute)

result = []
for i in range(int(input())):
    handler(result)
"""Input = input().split()
command = Input[0]
print(command)
Values = Input[1:]
print(Input)

print(Values)"""