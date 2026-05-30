import requests
# url="https://pixabay.com/api/?key=39964924-7c129c4a1eeb6e731fa1b2bf2&q=nature+wallpaper&image_type=photo&orientation=horizontal&editors_choice=true&order=latest&per_page=3"
res=requests.get(url,timeout=10)
if res.status_code==200:
    res_data=res.json()
    hits=res_data.get("hits",[])
    large_image_urls=[item["largeImageURL"] for item in hits if "largeImageURL" in item]
    # print(large_image_urls)
    for i,u in enumerate(large_image_urls):
        filename=f"{i+1}.jpg"
        print("Downloading Images...")
        img=requests.get(u).content
        with open(filename,'wb') as f:
            f.
