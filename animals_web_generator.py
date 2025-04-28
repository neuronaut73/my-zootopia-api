import json
from search_images import fetch_image_url


def load_data(file_name):
    """ Loads a JSON file """
    with open(file_name, "r") as handle:
        return json.load(handle)


def load_html(file_name):
    """Loads the html file"""
    with open(file_name, "r") as handle:
        return handle.read()


def save_file(data: str, file_name: str):
    """Saves the animal html data to a html file"""
    with open(file_name, "w") as f:
        return f.write(data)


def generate_string_with_animals_data(animals_data):
    """Generates the animals cards plus an animal image from DuckDuckGo"""
    output = ''  # define an empty string
    for dict in animals_data:
        name = dict["name"]
        location = dict["locations"][0]
        diet = dict["characteristics"]["diet"]
        type_fox = dict["characteristics"].get("type")
        image_url = fetch_image_url(name)

        variables = [name, location, diet, type_fox]

        if all(var is not None for var in variables):
            output += f'<li class="cards__item">'
            output += f'<div class="card__content">'  # added content class
            output += f'  <div class="card__info">'    # added info class
            output += f'    <div class="card__title">{name}</div>'
            output += f'    <p class="card__text">'
            output += f'      <strong>Diet:</strong> {diet}<br/>'
            output += f'      <strong>Location:</strong> {location}<br/>'
            output += f'      <strong>Type:</strong> {type_fox}<br/>'
            output += f'    </p>'
            output += f'  </div>'
            output += f'  <figure class="card__image">'  # added card image class
            output += f'    <img src="{image_url}" alt="{name}">'
            output += f'  </figure>'
            output += f'</div>'
            output += f'</li>'
    return output


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
""" +
"""</style>
    </head>""")

    return html_data_new


def main():
    html_template = load_html("animals_template.html")
    animals_data = load_data('animals_data.json')
    animals_data_string = generate_string_with_animals_data(animals_data)
    html_template_new = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_data_string)
    html_template_new = insert_css_info(html_template_new)
    save_file(html_template_new, "animals.html")


if __name__ == "__main__":
    main()


