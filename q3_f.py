import sys
import copy
import math
import collections
import timeit

def read_car(input_file):
  attribute_list = ["buying_vhigh", "buying_high", "buying_med", "buying_low", "maint_vhigh", "maint_high", "maint_med", "maint_low", "doors_2", "doors_3", "doors_4", "doors_5more", "persons_2", "persons_4", "persons_more", "lug_boot_small", "lug_boot_med", "lug_boot_big", "safty_low", "safty_med", "safty_high", "class_value_unacc", "class_value_acc", "class_value_good", "class_value_vgood"]
  attribute_num = len(attribute_list)
  fh = open(input_file, 'r')
  lines = fh.readlines()
  matrix = [[0 for x in range(25)]for x in range(len(lines))]
  j = 0
  for x in lines:
    line = x.strip()
    line.replace(" ", "")
    tmp = []
    tmp = line.split(',')

    if tmp[0] == "vhigh":
      matrix[j][0] = 1
    elif tmp[0] == "high":
      matrix[j][1] = 1
    elif tmp[0] == "med":
      matrix[j][2] = 1
    elif tmp[0] == "low":
      matrix[j][3] = 1
	 
    if tmp[1] == "vhigh":
      matrix[j][4] = 1
    elif tmp[1] == "high":
      matrix[j][5] = 1
    elif tmp[1] == "med":
      matrix[j][6] = 1
    elif tmp[1] == "low":
      matrix[j][7] = 1
	  
    if tmp[2] == "2":
      matrix[j][8] = 1
    elif tmp[2] == "3":
      matrix[j][9] = 1
    elif tmp[2] == "4":
      matrix[j][10] = 1
    elif tmp[2] == "5more":
      matrix[j][11] = 1
	  
    if tmp[3] == "2":
      matrix[j][12] = 1
    elif tmp[3] == "4":
      matrix[j][13] = 1
    elif tmp[3] == "more":
      matrix[j][14] = 1

    if tmp[4] == "small":
      matrix[j][15] = 1
    elif tmp[4] == "med":
      matrix[j][16] = 1
    elif tmp[4] == "big":
      matrix[j][17] = 1
	  
    if tmp[5] == "low":
      matrix[j][18] = 1
    elif tmp[5] == "med":
      matrix[j][19] = 1 
    elif tmp[5] == "high":
      matrix[j][20] = 1 

    if tmp[6] == "unacc":
      matrix[j][21] = 1 
    elif tmp[6] == "acc":
      matrix[j][22] = 1 
    elif tmp[6] == "good":
      matrix[j][23] = 1 
    elif tmp[6] == "vgood":
      matrix[j][24] = 1
    j += 1
  return matrix, attribute_list, attribute_num
  
def read_chess(input_file):
  attribute_list = ["White_King_File_a", "White_King_File_b", "White_King_File_c", "White_King_File_d", 
                    "White_King_Rank_1", "White_King_Rank_2", "White_King_Rank_3", "White_King_Rank_4", 
                    "White_Rook_File_a", "White_Rook_File_b", "White_Rook_File_c", "White_Rook_File_d", "White_Rook_File_e", "White_Rook_File_f", "White_Rook_File_g", "White_Rook_File_h", 
                    "White_Rook_Rank_1", "White_Rook_Rank_2", "White_Rook_Rank_3", "White_Rook_Rank_4", "White_Rook_Rank_5", "White_Rook_Rank_6", "White_Rook_Rank_7", "White_Rook_Rank_8", 
                    "Black_King_File_a", "Black_King_File_b", "Black_King_File_c", "Black_King_File_d", "Black_King_File_e", "Black_King_File_f", "Black_King_File_g", "Black_King_File_h", 
                    "Black_King_Rank_1", "Black_King_Rank_2", "Black_King_Rank_3", "Black_King_Rank_4", "Black_King_Rank_5", "Black_King_Rank_6", "Black_King_Rank_7", "Black_King_Rank_8", 
                    "draw", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen"]
  attribute_num = len(attribute_list)
  fh = open(input_file, 'r')
  lines = fh.readlines()
  matrix = [[0 for x in range(58)]for x in range(len(lines))]
  j = 0
  for x in lines:
    line = x.strip()
    line.replace(" ", "")
    tmp = []
    tmp = line.split(',')
	
    if tmp[0] == "a":
      matrix[j][0] = 1
    elif tmp[0] == "b":
      matrix[j][1] = 1
    elif tmp[0] == "c":
      matrix[j][2] = 1
    elif tmp[0] == "d":
      matrix[j][3] = 1
	
    if tmp[1] == "1":
      matrix[j][4] = 1
    elif tmp[1] == "2":
      matrix[j][5] = 1
    elif tmp[1] == "3":
      matrix[j][6] = 1
    elif tmp[1] == "4":
      matrix[j][7] = 1
	
    if tmp[2] == "a":
      matrix[j][8] = 1
    elif tmp[2] == "b":
      matrix[j][9] = 1
    elif tmp[2] == "c":
      matrix[j][10] = 1
    elif tmp[2] == "d":
      matrix[j][11] = 1
    elif tmp[2] == "e":
      matrix[j][12] = 1
    elif tmp[2] == "f":
      matrix[j][13] = 1
    elif tmp[2] == "g":
      matrix[j][14] = 1
    elif tmp[2] == "h":
      matrix[j][15] = 1
	  
    if tmp[3] == "1":
      matrix[j][16] = 1
    elif tmp[3] == "2":
      matrix[j][17] = 1
    elif tmp[3] == "3":
      matrix[j][18] = 1
    elif tmp[3] == "4":
      matrix[j][19] = 1
    elif tmp[3] == "5":
      matrix[j][20] = 1
    elif tmp[3] == "6":
      matrix[j][21] = 1
    elif tmp[3] == "7":
      matrix[j][22] = 1
    elif tmp[3] == "8":
      matrix[j][23] = 1
	
    if tmp[4] == "a":
      matrix[j][24] = 1
    elif tmp[4] == "b":
      matrix[j][25] = 1
    elif tmp[4] == "c":
      matrix[j][26] = 1
    elif tmp[4] == "d":
      matrix[j][27] = 1
    elif tmp[4] == "e":
      matrix[j][28] = 1
    elif tmp[4] == "f":
      matrix[j][29] = 1
    elif tmp[4] == "g":
      matrix[j][30] = 1
    elif tmp[4] == "h":
      matrix[j][31] = 1
	  
    if tmp[5] == "1":
      matrix[j][32] = 1
    elif tmp[5] == "2":
      matrix[j][33] = 1
    elif tmp[5] == "3":
      matrix[j][34] = 1
    elif tmp[5] == "4":
      matrix[j][35] = 1
    elif tmp[5] == "5":
      matrix[j][36] = 1
    elif tmp[5] == "6":
      matrix[j][37] = 1
    elif tmp[5] == "7":
      matrix[j][38] = 1
    elif tmp[5] == "8":
      matrix[j][39] = 1
	
    get_index = attribute_list.index(tmp[6])
    matrix[j][get_index] = 1
    j += 1
  return matrix, attribute_list, attribute_num

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

def apriori_1(matrix, min_sup, attribute_num):
  count_item_1 = [0 for x in range(attribute_num)]
  candidate = []
  candidate_f1 = []
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
  return freq_item

def apriori_2(matrix, min_sup, attribute_num):
  count_item_1 = [0 for x in range(attribute_num)]
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
  return freq_item

def is_subset(set1, set2):
  check = True
  for item in set1:
    if item not in set2:
      check = False
      break
  return check

def check_duplicate_element(aList):
  new_list = []
  for element in aList:
    if element not in new_list:
      new_list.append(element)
  return new_list
 
def sub(set1, set2):
  # return = set2 - set1
  result = []
  for each in set2:
    if not each[0] in set1:
      result.append(each[0])
  return result

def gen_candidate_1(itemset):
  # F1 * Fk-1
  candidates = []
  
  #generate F1
  f1 = []
  for each in itemset:
    for i in each:
      f1.append(i)
    f1 = check_duplicate_element(f1)
  f1.sort()
  #print f1
  
  for each in itemset:
    for i in f1:
      tmp = []
      if i not in each:
        tmp.append(i)
        for x in each:
          tmp.append(x)
        tmp.sort()
        candidates.append(tmp)
  candidates = check_duplicate_element(candidates)
  return candidates

def gen_candidate_2(itemsets):
  # Fk-1 * Fk-1
  candidates = []
  num = len(itemsets)
  
  # k=1 should be consider separately
  if len(itemsets[0]) == 1:
    for n in range(num-1):
      for m in range(n+1, num):
        candidates.append([itemsets[n][0], itemsets[m][0]])
  else:
    for n in range(num-1):
      for m in range(n+1, num):
        if(itemsets[n][:-1] == itemsets[m][:-1] and itemsets[n][1:] + [itemsets[m][-1]] in itemsets):
          candidates.append(itemsets[n] + [itemsets[m][-1]])
  return candidates
  
def generate_rules(freq_item, min_conf, method):
  result = {}
  for n in range(1, len(freq_item)):
    for itemset in freq_item[n]:
      h = []
      for each in itemset[0]:
        h.append([each])
      k_itemset = copy.deepcopy(h)
      count = len(k_itemset)
      for i in range(count-1):
        for each in k_itemset:
          div = sub(each, k_itemset)
          for l in freq_item[len(div)-1]:
           if sorted(div) == sorted(l[0]):
             sup = l[1]
             break
          conf = float(itemset[1])/sup
          if conf < min_conf:
            if each in h:
              h.remove(each)
          elif (result.has_key(conf) and [div, each] not in result[conf]):
            result[conf].append([div, each])
          else:
            result[conf] = [[div, each]]
        if h:
          if method == 1:
            h = gen_candidate_1(h)
          else:
            h = gen_candidate_2(h)
        else:
          break
  return result
  
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
  sup = float(count)/len(matrix)
  return sup

def cal_lift(associated_rules, matrix):
  associated_rules_w_lift = copy.deepcopy(associated_rules)
  lift_associated_rules = {}
  #print associated_rules
  #print associated_rules_w_lift
  for conf, rules in associated_rules.items():
    #print conf
    #print rules
    for i in range(len(rules)):
      #print rules[i][1]
      sup_consequent = cal_sup(matrix,rules[i][1])
      #print sup_consequent
      lift = conf / sup_consequent
      associated_rules_w_lift[conf][i].append(lift)
      if lift_associated_rules.has_key(lift):
        lift_associated_rules[lift].append(rules[i])
      else:
        lift_associated_rules[lift] = []
        lift_associated_rules[lift].append(rules[i])
  return associated_rules_w_lift, lift_associated_rules

def print_outcome(associated_rules_w_lift, attribute_list, output_file):
  f = open(output_file, 'w')
  f.write("Association Rule\tConfidence\tLift\n")
  for conf, rules in associated_rules_w_lift.items():
    for i in range(len(rules)):
      f.write("{")
      tmp = rules[i][0]
      f.write(attribute_list[tmp[0]-1])
      for j in range(1, len(rules[i][0])):
        f.write(", ")
        f.write(attribute_list[tmp[j]-1])
      f.write("}")
      f.write("->")
      f.write("{")
      tmp2 = rules[i][1]
      f.write(attribute_list[tmp2[0]-1])
      for k in range(1, len(rules[i][1])):
        f.write(", ")
        f.write(attribute_list[tmp2[k]-1])
      f.write("}")
      f.write("\t")
      f.write("%0.4f" %conf)
      f.write("\t")
      f.write("%0.4f" %rules[i][2])
      f.write("\n")

def print_top_10(top_10_by_conf, top_10_by_lift, attribute_list, output_file):
  f = open(output_file, 'w')
  f.write("Following identify top 10 rules by its lift (if same, then order by its support)\n")
  f.write("Association Rule: Lift/Support\n")
  for rules in top_10_by_lift:
      f.write("{")
      tmp = rules[2][0]
      f.write(attribute_list[tmp[0]-1])
      for j in range(1, len(rules[2][0])):
        f.write(", ")
        f.write(attribute_list[tmp[j]-1])
      f.write("}")
      f.write("->")
      f.write("{")
      tmp2 = rules[2][1]
      f.write(attribute_list[tmp2[0]-1])
      for k in range(1, len(rules[2][1])):
        f.write(", ")
        f.write(attribute_list[tmp2[k]-1])
      f.write("}")
      f.write(": ")
      f.write("%0.4f" %rules[0])
      f.write("/")
      f.write("%0.4f" %rules[1])
      f.write("\n")
  f.write("\nFollowing identify top 10 rules by its confidence (if same, then order by its support)\n")
  f.write("Association Rule: Confidence/Support\n")
  for rules in top_10_by_conf:
      f.write("{")
      tmp = rules[2][0]
      f.write(attribute_list[tmp[0]-1])
      for j in range(1, len(rules[2][0])):
        f.write(", ")
        f.write(attribute_list[tmp[j]-1])
      f.write("}")
      f.write("->")
      f.write("{")
      tmp2 = rules[2][1]
      f.write(attribute_list[tmp2[0]-1])
      for k in range(1, len(rules[2][1])):
        f.write(", ")
        f.write(attribute_list[tmp2[k]-1])
      f.write("}")
      f.write(": ")
      f.write("%0.4f" %rules[0])
      f.write("/")
      f.write("%0.4f" %rules[1])
      f.write("\n")

	  
def find_top_10(association_rules, matrix):
  top_10_rules = []
  arrange_rule = []
  for score, rules in association_rules.items():
    for i in range(len(rules)):
      new_list = []
      new_list.append(score)
      combine_item = rules[i][0] + rules[i][1]
      #print combine_item
      sup = cal_sup(matrix, combine_item)
      new_list.append(sup)
      new_list.append(rules[i])
      arrange_rule.append(new_list)
  #print arrange_rule
  arrange_rule.sort(key=lambda sl:(-sl[0], sl[1]))
  #print arrange_rule
  for i in range(10):
    top_10_rules.append(arrange_rule[i])
  return arrange_rule, top_10_rules

#Main function starts from here
if len(sys.argv) != 11:
		print "USAGE: q3_f.py -i [INPUT_FILE] -m [MIN_SUPPORT] -c [MIN_CONFIDENCE] -o [OUTPUT_FILE] -f [METHOD]"
		exit(-1)

if sys.argv[1] == "-i":
		input_file = sys.argv[2]
else:
		print "USAGE: q3_f.py -i [INPUT_FILE] -m [MIN_SUPPORT] -c [MIN_CONFIDENCE -o [OUTPUT_FILE] -f [METHOD]"
		exit(-1)

if sys.argv[3] == "-m":
		min_sup_freq = float(sys.argv[4])
else:
		print "USAGE: q3_f.py -i [INPUT_FILE] -m [MIN_SUPPORT] -c [MIN_CONFIDENCE -o [OUTPUT_FILE] -f [METHOD]"
		exit(-1)

if sys.argv[5] == "-c":
		min_conf = float(sys.argv[6])
else:
		print "USAGE: q3_f.py -i [INPUT_FILE] -m [MIN_SUPPORT] -c [MIN_CONFIDENCE -o [OUTPUT_FILE] -f [METHOD]"
		exit(-1)
		
if sys.argv[7] == "-o":
		output_file = sys.argv[8]
else:
		print "USAGE: q3_f.py -i [INPUT_FILE] -m [MIN_SUPPORT] -c [MIN_CONFIDENCE -o [OUTPUT_FILE] -f [METHOD]"
		exit(-1) 
		
if sys.argv[9] == "-f":
		method = int(sys.argv[10])
else:
		print "USAGE: q3_f.py -i [INPUT_FILE] -m [MIN_SUPPORT] -c [MIN_CONFIDENCE -o [OUTPUT_FILE] -f [METHOD]"
		exit(-1) 

start = timeit.default_timer()
if input_file == "item_1000.txt":
  detail = read_goods(input_file, "goods.txt")
  min_sup = math.ceil(len(detail) * min_sup_freq)
  name_list = read_name("goods.txt")
  attribute_num = len(name_list)
  if method == 1:
    freq_item = apriori_1(detail, min_sup, attribute_num)
  else:
    freq_item = apriori_2(detail, min_sup, attribute_num)
  associated_rules = generate_rules(freq_item, min_conf, method)
  associated_rules_w_lift, lift_associated_rules = cal_lift(associated_rules, detail)
  ordered_by_conf, top_10_by_conf = find_top_10(associated_rules, detail)
  ordered_by_lift, top_10_by_lift = find_top_10(lift_associated_rules, detail)
  print_top_10(top_10_by_conf, top_10_by_lift, name_list,output_file)
  print "The result is in the output file"
  
elif input_file == "car.txt":
  matrix, name_list, attribute_num = read_car(input_file)
  min_sup = math.ceil(len(matrix) * min_sup_freq)
  if method == 1:
    freq_item = apriori_1(matrix, min_sup, attribute_num)
  else:
    freq_item = apriori_2(matrix, min_sup, attribute_num)
  associated_rules = generate_rules(freq_item, min_conf, method)
  associated_rules_w_lift, lift_associated_rules = cal_lift(associated_rules, matrix)
  ordered_by_conf, top_10_by_conf = find_top_10(associated_rules, matrix)
  ordered_by_lift, top_10_by_lift = find_top_10(lift_associated_rules, matrix)
  print_top_10(top_10_by_conf, top_10_by_lift, name_list,output_file)
  print "The result is in the output file"

elif input_file == "chess.txt":
  matrix, name_list, attribute_num = read_chess(input_file)
  min_sup = math.ceil(len(matrix) * min_sup_freq)
  if method == 1:
    freq_item = apriori_1(matrix, min_sup, attribute_num)
  else:
    freq_item = apriori_2(matrix, min_sup, attribute_num)
  associated_rules = generate_rules(freq_item, min_conf, method)
  associated_rules_w_lift, lift_associated_rules = cal_lift(associated_rules, matrix)
  ordered_by_conf, top_10_by_conf = find_top_10(associated_rules, matrix)
  ordered_by_lift, top_10_by_lift = find_top_10(lift_associated_rules, matrix)
  print_top_10(top_10_by_conf, top_10_by_lift, name_list,output_file)
  print "The result is in the output file"
  
else:
  print "Input file should be item_1000.txt/car.txt/chess/txt"
  
  
  

#detail = read_goods("item_100.txt", "goods.txt")
#min_sup_freq = 0.015
#min_sup = math.ceil(len(detail) * min_sup_freq)
#print min_sup
#print detail
#name_list = read_name("goods.txt")
#print name_list
#freq_item = apriori_2(detail, min_sup) 
#associated_rules = generate_rules(freq_item, 0.6, 2)
#print associated_rules
#associated_rules_w_lift, lift_associated_rules = cal_lift(associated_rules, detail)
#print associated_rules_w_lift
#print lift_associated_rules
#ordered_by_conf, top_10_by_conf = find_top_10(associated_rules, detail)
#print top_10_by_conf
#ordered_by_lift, top_10_by_lift = find_top_10(lift_associated_rules, detail)
#print top_10_by_lift
#print_outcome(associated_rules_w_lift, name_list, "output_q3_f.txt")
#print_top_10(top_10_by_conf, top_10_by_lift, name_list,"output_q3_f_lift.txt")
stop = timeit.default_timer()
print "Runtime: %0.4f sec" %(stop-start) 