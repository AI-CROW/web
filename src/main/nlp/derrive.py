from nltk.corpus import stopwords
from nltk import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser
content = """Bitcoin (BTC) was higher, following through on the upside after Wednesday’s 7.4% jump to a new 2020 high. It was the biggest single-day increase in almost three months.  The surge past $12,000, with prices now around $13,000, came after the consumer payments giant PayPal (PYPL) announced it would allow its 346 million customers to hold bitcoin and other cryptocurrencies, and to use the digital assets to shop at the 26 million merchants on its network.  “Traders are now eyeing for BTC to test the $14,000 long-term resistance from 2019, which we believe should be breached in the coming months ahead,” Lennard Neo, head of research for the cryptocurrency-focused structured-products firm Stack Funds, wrote early Thursday in a report.  In traditional markets, European indexes slid and U.S. stock futures pointed to a lower open as lawmakers in Washington failed to agree on a new economic stimulus package as data showed a rising number of coronavirus cases.  Market Moves The official confirmation Wednesday that PayPal is pushing into cryptocurrencies (reported months ago by CoinDesk’s Ian Allison) ignited a fresh rally in prices for bitcoin, already seen as one of the world’s top-performing asset classes this year.  Subscribe to First Mover, our daily newsletter about markets."""
sentence = """"Bitcoin will moon at 1 million dollars", says John Doe"""

PS = PorterStemmer()

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(sentence)

filtered_content = [i for i in word_tokens if not i in stop_words]
stemmed_content = [PS.stem(i) for i in filtered_content]
pos_tagged = pos_tag(stemmed_content)
patterns = """mychunk:{<NN.?>*<VBP.?>*<CD>}"""
chunker = RegexpParser(patterns)
output = chunker.parse(pos_tagged)

print("Original Sentence", sentence)
print("Filtered Content", filtered_content)
print("Stemmed Content", stemmed_content)
print("POS Tagged", pos_tagged)
print("Chunker", chunker)
print("Output", output)