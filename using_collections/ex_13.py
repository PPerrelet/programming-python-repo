# Without running the following code, determine what each print statement should print.

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)       # True
print('Butter' in cats)             # False     "string in list" must match a list element exactly.
print('Butter' in cats[3])          # True      cats[3] is 'Butterscotch' and 'Butter' is in 'Butterscotch'.
print('cheddar' in cats)            # False