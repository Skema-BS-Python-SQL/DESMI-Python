# A simple example with variable interpolation
# using the % string-format operator
print("""Dear %(recipient)s,
 
I wish you to leave Sunnydale and never return.
 
Not Quite Love,
%(sender)s
""" % {
    'sender': 'Buffy the Vampire Slayer',
    'recipient': 'Spike'
})
