#!/usr/bin/python
# Importing libraries
import sys
import math
import timeit

def read_goods(input_file,goods_name):
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
  candidate = []
  candidate_f1 = []
  count_item_1 = [0 for x in range(50)]
  freq_item = []
  freq_item_1 = []  #F1
  f1 = []
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
  
  notEmpty = True
  #Build item pairs from F1 
  while notEmpty:
    get_list_of_freq_item = freq_item[len(freq_item)-1]
    get_check_list = []
    for element in get_list_of_freq_item:
      for i in f1:
        tmp = []
        if i not in element[0]:
          tmp.append(i)
          for x in element[0]:
            tmp.append(x)
          tmp.sort()
          get_check_list.append(tmp)
    get_check_list = check_duplicate_element(get_check_list)
    candidate_fk = []
    fi = []
    for ele in get_check_list:
      count = cal_sup(matrix, ele)
      candidate_fk.append([ele, count])
    #print get_check_list
      if count >= min_sup:
        fi.append([ele, count])
    #print fi
    if len(fi) == 0:
      notEmpty = False
    else:
      freq_item.append(fi)
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
		print "USAGE: q3_a.py -i [INPUT_FILE] -g [GOODS_NAME_FILE] -m [MIN_SUPPORT] -o [OUTPUT_FILE]"
		exit(-1)

if sys.argv[1] == "-i":
		input_file = sys.argv[2]
else:
		print "USAGE: q3_a.py -i [INPUT_FILE] -g [GOODS_NAME_FILE] -m [MIN_SUPPORT] -o [OUTPUT_FILE]"
		exit(-1)

if sys.argv[3] == "-g":
		goods_name = sys.argv[4]  
else:
		print "USAGE: q3_a.py -i [INPUT_FILE] -g [GOODS_NAME_FILE] -m [MIN_SUPPORT] -o [OUTPUT_FILE"
		exit(-1)

if sys.argv[5] == "-m":
		min_sup_freq = float(sys.argv[6])
else:
		print "USAGE: q3_a.py -i [INPUT_FILE] -g [GOODS_NAME_FILE] -m [MIN_SUPPORT] -o [OUTPUT_FILE]"
		exit(-1)

if sys.argv[7] == "-o":
		output_file = sys.argv[8]
else:
		print "USAGE: q3_a.py -i [INPUT_FILE] -g [GOODS_NAME_FILE] -m [MIN_SUPPORT] -o [OUTPUT_FILE]"
		exit(-1)

start = timeit.default_timer()
detail = read_goods(input_file, goods_name)
#print detail
name_list = read_name(goods_name)
#print name_list
min_sup = math.ceil(len(detail) * min_sup_freq)
freq_item, candidate = apriori(detail, min_sup)
print_outcome(candidate, name_list, output_file)
#print candidate
stop = timeit.default_timer()
print "Runtime: %0.4f sec" %(stop-start)
print "The Result which got from F1 X Fk-1 method is in output file."