text=input().strip()
k=int(input())
count={}
for i in range(len(text) - k + 1): 
  pattern=text[i:i+k]
  count[pattern]=count.get(pattern,0)+1
max_count=max(count.values()) 
result=[] 
for pattern in count: 
  if count [pattern]==max_count: 
    result.append(pattern) 
print(*result)     
