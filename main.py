def answer():
  n = int(input("enter no of rows:"))
  rows = []
  name_set = {}
  
  for i in range(n):

    # we get id,name, score, updated_at in cur
    cur = input("enter row val:").split(',')
    cur_name = cur[0]
    if cur_name in name_set:
      cand = name_set[cur_name]
      if cand[3] >= cur[3]:
        continue
      else:
        name_set[cur_name] = cur

    else:
      name_set[cur_name] = cur

    # filtering based on score and appending
    if 0<=int(cur[2])<=100: 
      rows.append(cur)

  # deduplication logic!
  for i in range(len(rows)):
    if name_set[rows[i][0]][3] == rows[i][3]:
      out = ""
      
      #print(rows[i])
      #printing the correct records line by line
      print(",".join(rows[i]))
      
# basically calling the method when python3 main.py is executed
if __name__ == "__main__":
    answer()
  


  # 
    

    
    
