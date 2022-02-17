import twint

# Configure
c = twint.Config()

# Parameters
c.Lang = 'en'
c.Store_csv = True
c.Output = '../dataset/harassment-tweet2.csv'

# Keywords for search
c.Search = '#sexualcomments'

# Run
twint.run.Search(c)
