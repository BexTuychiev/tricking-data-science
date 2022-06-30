from joblib import Parallel, delayed
import requests
from tqdm import tqdm
import time

def save_html(url):
    r = requests.get(url)
    assert r.status_code == 200, "Bad request"
    
    # Save HTML somewhere
    # ...
    
url = "https://quotes.toscrape.com/"


if __name__ == "__main__":
    
    start = time.time()
    
    Parallel(n_jobs=10, backend="multiprocessing")(
        delayed(save_html)(url) for i in tqdm(range(1000))
    )
    
    print(f"elapsed: {time.time() - start}")
