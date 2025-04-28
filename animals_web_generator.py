import requests
import json
from search_images import fetch_image_url


def load_html(file_name):
    """Loads the html file"""
    with open(file_name, "r") as handle:
        return handle.read()


def save_file(data: str, file_name: str):
    """Saves the animal html data to a html file"""
    with open(file_name, "w") as f:
        f.write(data)





def generate_string_with_animals_data(animals_data):
    """Generates the animals cards plus an animal image from DuckDuckGo"""
    output = []  # define an empty string
    for animal in animals_data:
        name = animal.get("name")
        location = animal.get("locations")[0]
        diet = animal.get("characteristics").get("diet")
        type_fox = animal.get("characteristics").get("type")
        try:
            image_url = fetch_image_url(name)
        except:
            image_url = "https://demofree.sirv.com/nope-not-here.jpg"

        variables = [name, location, diet, type_fox]

        if all(var is not None for var in variables):
            output.append(f'<li class="cards__item">')
            output.append(f'<div class="card__content">')  # added content class
            output.append(f'  <div class="card__info">')    # added info class
            output.append(f'    <div class="card__title">{name}</div>')
            output.append(f'    <p class="card__text">')
            output.append(f'      <strong>Diet:</strong> {diet}<br/>')
            output.append(f'      <strong>Location:</strong> {location}<br/>')
            output.append(f'      <strong>Type:</strong> {type_fox}<br/>')
            output.append(f'    </p>')
            output.append(f'  </div>')
            output.append(f'  <figure class="card__image">')  # added card image class
            output.append(f'    <img src="{image_url}" alt="{name}">')
            output.append(f'  </figure>')
            output.append(f'</div>')
            output.append(f'</li>')
    return ''.join(output)


def insert_css_info(html_data: str):
    """Replaces the closing head tag with additional css info"""
    html_data_new = html_data.replace(
        """</style>
    </head>""",

"""
    .card__content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.card__info {
  flex: 2;
}

.card__image img {
  max-width: 150px;
  height: auto;
  border-radius: 8px;
}
h2 {
  text-align: center

}
""" +
"""</style>
    </head>""")

    return html_data_new


def main():
    html_template = load_html("animals_template.html")


    if len(animals_data) == 0:
        not_exist_string = f"<h2>The animal '{animal_name}' doesn't exist.</h2>"
        html_template_new = html_template.replace("__REPLACE_ANIMALS_INFO__", not_exist_string)
        html_template_new = insert_css_info(html_template_new)
        save_file(html_template_new, "animals.html")
    else:
        animals_data = raw.json()
        animals_data_string = generate_string_with_animals_data(animals_data)
        html_template_new = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_data_string)
        html_template_new = insert_css_info(html_template_new)
        save_file(html_template_new, "animals.html")

    print(f"{animal_name}-Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
