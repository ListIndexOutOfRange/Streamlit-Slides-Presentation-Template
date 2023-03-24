# Template for Streamlit based Slides Presentation

[demo.webm](https://user-images.githubusercontent.com/49729757/227623886-7d85c8dd-efd0-4f29-8d2e-0e1619ea7b5f.webm)

This repo provides a minimal working example to create slides presentation using Streamlit.     
The example app contains basic instructions to create such a presentation.

## Install

```
git clone git@github.com:ListIndexOutOfRange/Streamlit-Slides-Presentation-Template.git
cd Streamlit-Slides-Presentation-Template/
pip install -r requirements.txt
```

## Instructions

You can launch the app like that:

```
streamlit run app.py
```

The app contains basics instructions.


The core idea is to create one python file per slide, inside the `slides/` folder.
This file **must** contain a `main() -> None` function that will be used to display the slide's content.


## Tips / Troobleshooting

- **If the navigation arrow don't show up, refresh the page**
- **You can change the theme to light or dark by using the burger menu on the top right of the app**



