# Vars exemple
number = 12.343562135
percentage_number = 0.33
high_number = 12349000212452

print(f'Printing without formatting: {number}'
      f'\nPrinting the var name: {number = }'
      f'\nShowing two decimal places: {number:.2f}' # You can choose any number 
      f'\nChanging characters wide: {number:30}' # The field will be 30 characters wide
      f'\nForces center alignment: {number:^30}' # For left-aligned use "<" and for right-aligned ">"
      f'\nFill white spaces: {number:=^30}' # You can fill white spaces with any characters
      f'\nPrinting percentages: {percentage_number:.2%}' # Multiply by 100 and add % symbol
      f'\nShowing two decimal places with comma: {high_number:,.2f}' 
      f'\nPrinting two decimal places with scientific notation: {high_number:.2e}'
     )
