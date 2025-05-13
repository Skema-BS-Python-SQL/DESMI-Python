import sys
# get python version (x.x) for test if switch is available
major = sys.version_info[0]
sub = sys.version_info[1]

lang = input("What's the programming language you want to learn ?\n")

if sub >= 10:
    '''
  Following code only work in python 3.10
  '''
    from switch_example import switch

else:
    from no_switch_example import switch

print(switch(lang))
