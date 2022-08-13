e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f)  # 8.1

print(e2f["walrus"])  # 8.2

f2e = {}
for item in e2f.items():
    f2e[item[1]] = item[0]
print(f2e)  # 8.3

print(f2e["chien"])  # 8.4

print(set(e2f.keys()))  # 8.5
