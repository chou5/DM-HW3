#!/usr/bin/python
# Importing libraries
import sys
import math
import timeit

def read_goods(input_file, goods_name):
  fh = open(input_file, 'r')
  f = open(goods_name, 'r')
  lines = fh.readlines()
  goods = f.readlines()
  matrix = [[0 for x in range(len(goods))]for x in range(len(lines))]
  for x in lines:
    line = x.strip()
    line.replace(" ", "")
    tmp = []
    tmp = line.split(', ')
    for i in range(1, len(tmp)):
      x = int(tmp[0])-1
      y = int(tmp[i])-1
      matrix[x][y] = 1
  return matrix

def cal_sup(matrix, aList):
  count = 0
  for transaction in matrix:
    check = True
    for i in aList:
      if transaction[i-1] != 1:
        check = False
    if check == True:
      count += 1
  #print count
  #sup = float(count)/len(matrix)
  return count

def check_duplicate_element(aList):
  new_list = []
  for element in aList:
    if element not in new_list:
      new_list.append(element)
  return new_list
  
def apriori(matrix, min_sup):
  count_item_1 = [0 for x in range(50)]
  candidate = []
  freq_item = []
  freq_item_1 = []  #F1
  f1 = []
  candidate_f1 = []
  for element in matrix:
    for i in range(len(element)):
      if element[i] == 1:
        count_item_1[i] = count_item_1[i] + 1
  for i in range(len(count_item_1)):
    if count_item_1[i] >= min_sup:
      candidate_f1.append([ [i+1], count_item_1[i] ])
      freq_item_1.append([ [i+1], count_item_1[i] ])   #i+1
      f1.append(i+1)
  #print f1
  candidate.append(candidate_f1)
  freq_item.append(freq_item_1)
  
  freq_item_2 = []
  candidate_f2 = []
  for i in range(len(f1)):
    for j in range(i, len(f1)):
      if i != j:
        count = 0
        for element in matrix:
          if element[f1[i]-1] == 1 and element[f1[j]-1]:
            count += 1
        tmp = []
        if count >= min_sup:
          tmp.append([f1[i], f1[j]])
          tmp.append(count)
          freq_item_2.append(tmp)
          candidate_f2.append(tmp)
  #print freq_item_2
  freq_item.append(freq_item_2)
  candidate.append(candidate_f2)
  
  notEmpty = True
  while notEmpty:
    k = len(freq_item)
    get_check_list = []
    for element in freq_item[k-1]:
      get_check_list.append(element[0])
    fk = []
    for i in range(len(get_check_list)):
      for j in range(i, len(get_check_list)):
        if i != j:
          check = True
          for x in range(k-1):
            if get_check_list[i][x] != get_check_list[j][x]:
              check = False
          tmp = []
          if check == True:
            for y in range(k-1):
              tmp.append(get_check_list[i][y])
            tmp.append(get_check_list[i][k-1])
            tmp.append(get_check_list[j][k-1])
            tmp.sort()
            fk.append(tmp)
    #print fk
    fk = check_duplicate_element(fk)
  
    freq_item_k = []
    candidate_fk = []
    for element in fk:
      count = cal_sup(matrix, element)
      candidate_fk.append([element, count])
      if count >= min_sup:
        freq_item_k.append([element, count])

    if len(freq_item_k) == 0:
      notEmpty = False
    else:
      freq_item.append(freq_item_k)
      candidate.append(candidate_fk)
  #print freq_item
  return freq_item, candidate

def read_name(input_file):
  fh = open(input_file, 'r')
  lines = fh.readlines()
  name_list = []
  for x in lines:
    tmp = x.strip().split(' \t')
    #print tmp
    i = tmp[1].replace("'", "")
    j = tmp[2].replace("'", "")
    name = i + " " + j
    name_list.append(name)
  return name_list
  
def print_outcome(freq_item, name_list, output_file):
  f = open(output_file, 'w')
  f.write("Candidate Itemsets -> Number of Frequent Itemsets\n")
  for element in freq_item:
    for info in element:
      f.write("{")
      i = info[0][0]
      f.write(name_list[i-1])
      if len(info[0]) > 1:
        for j in range(1, len(info[0])):
          f.write(", ")
          f.write(name_list[info[0][j]-1])
      f.write("}")
      f.write("->")
      f.write(str(info[1]))
      f.write("\n")

#Main function starts from here
if len(sys.argv) != 9:
		print "USAGE: q3_a-2.py -i [INPUT_FILE] -g [GOODS_NAME_FILE] -m [MIN_SUPPORT] -o [OUTPUT_FILE]"
		exit(-1)

if sys.argv[1] == "-i":
		input_file = sys.argv[2]
else:
		print "USAGE: q3_a-2.py -i [INPUT_FILE] -g [GOODS_NAME_FILE] -m [MIN_SUPPORT] -o [OUTPUT_FILE]"
		exit(-1)

if sys.argv[3] == "-g":
		goods_name = sys.argv[4]  
else:
		print "USAGE: q3_a-2.py -i [INPUT_FILE] -g [GOODS_NAME_FILE] -m [MIN_SUPPORT] -o [OUTPUT_FILE]"
		exit(-1)

if sys.argv[5] == "-m":
		min_sup_freq = float(sys.argv[6])
else:
		print "USAGE: q3_a-2.py -i [INPUT_FILE] -g [GOODS_NAME_FILE] -m [MIN_SUPPORT] -o [OUTPUT_FILE]"
		exit(-1)

if sys.argv[7] == "-o":
		output_file = sys.argv[8]
else:
		print "USAGE: q3_a-2.py -i [INPUT_FILE] -g [GOODS_NAME_FILE] -m [MIN_SUPPORT] -o [OUTPUT_FILE]"
		exit(-1)

start = timeit.default_timer()
detail = read_goods(input_file, goods_name)
name_list = read_name(goods_name)
min_sup = math.ceil(len(detail) * min_sup_freq)
freq_item, candidate = apriori(detail, min_sup)
#print candidate
print_outcome(candidate, name_list, output_file)
stop = timeit.default_timer()
print "Runtime: %0.4f sec" %(stop-start)
print "The Result which got from Fk-1 X Fk-1 method is in output file."