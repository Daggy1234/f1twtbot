import os

w = [w.strip() for w in open("accounts_to_scrape.txt").readlines() if not w.startswith("#")]
	
for u in w:
	os.system(f"poetry run twint -u {u} --timeline -o {u.lower()}.csv --csv")
