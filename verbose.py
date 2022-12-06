import re
charref = re.compile(r"""
 &[#]               # Start of a numeric entity reference
ce
 (
     0[0-7]+        # Octal form
   | [0-9]+         # Decimal form
   | x[0-9a-fA-F]+  # Hexadecimal form
  )
  ;                 # Trailing semicolon
""", re.VERBOSE)