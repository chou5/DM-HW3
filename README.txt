This README file is for all program might be used in question 3 in HW4
For question a, if you want to get the result by using f1*fk-1 method, you should execute "q3_a.py" and if the method is fk-1*fk-1, execute "q3_a-2.py"
USAGE: q3_a.py -i [INPUT_FILE] -g [GOODS_NAME_FILE] -m [MIN_SUPPORT] -o [OUTPUT_FILE]
Sample usage: q3_a.py -i item_1000.txt -g goods.txt -m 0.02 -o output.txt
USAGE: q3_a-2.py -i [INPUT_FILE] -g [GOODS_NAME_FILE] -m [MIN_SUPPORT] -o [OUTPUT_FILE]
Sample usage: q3_a-2.py -i item_1000.txt -g goods.txt -m 0.02 -o output.txt

For question b, c, d, e, f is basically the same as above, the only difference is specify the method (-f 1 => for using f1*fk-1, -f 2 => for using fk-1*fk-1 and -m for entering the minimum support and -c for entering the minimum confidence)
USAGE: q3_b.py -i [INPUT_FILE] -m [MIN_SUPPORT] -o [OUTPUT_FILE] -f [METHOD]
Sample usage: q3_b.py -i item_1000.txt -g goods.txt -m 0.02 -o output.txt -f 1
Sample usage: q3_f.py -i item_1000.txt -g goods.txt -m 0.02 -c 0.3 -o output.txt -f 1
***Don't forget to change the file name!!!
***It also tell you how to execute the program in the main file as well