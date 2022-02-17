import twint

# Configure
c = twint.Config()

# Parameterss
c.Lang = 'en'
c.Store_csv = True
c.Output = '../dataset/depress.csv'

# Keywords for search
c.Search = '#panickattacks'


# Run
twint.run.Search(c)
