# Set the emails variable to be an empty dictionary
emails = {}

assert emails == {}, f"Expected `emails` to be {{}} but got: {repr(users)}"

# Add Ashley, Craig, and Elizabeth to the emails dictionary without reassigning the variable

emails['ashley'] = 'ashley@example.com'
emails['craig'] = 'craig@example.com'
emails['elizabeth'] = 'elizabeth@example.com'



assert emails == { 
    'ashley': 'ashley@example.com',
    'craig': 'craig@example.com',
    'elizabeth': 'elizabeth@example.com'
}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'craig': 'craig@example.com', 'elizabeth': 'elizabeth@example.com'}} but got: {repr(emails)}"

del emails [ 'craig']