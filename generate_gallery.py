from pathlib import Path
from bs4 import BeautifulSoup

def generage_html():
    with open('dst/gallery.html') as gallery_file:
        soup = BeautifulSoup(gallery_file.read())

    gallery_grid = soup.find(id="galleryGrid")
    gallery_grid.clear()

    files = Path('dst/resources/img/gallery/').glob('*.JPG')
    for file in sorted(files):
        category = file.name.split('_')[0]
        new_div = soup.new_tag('div', attrs={'class': f'gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter {category}'})
        new_img = soup.new_tag('img', attrs={'src': f'resources/img/gallery/{file.name}', 'class': 'img-responsive', 'data-target': '#lightboxModal', 'data-toggle': 'modal'})

        new_div.append(new_img)
        gallery_grid.append(new_div)

    with open('generate_gallery_output.txt', 'w') as output_file:
        output_file.write(soup.prettify())

if __name__ == '__main__':
    generage_html()