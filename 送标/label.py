
with open('origindata') as f:
    for line in f.readlines():
        print(line)
        # l=json.loads(line)
        l=eval(line)
        print(l)