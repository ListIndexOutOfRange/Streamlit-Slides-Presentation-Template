# Template for Streamlit based Slides Presentation


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

### If the navigation arrow don't show up, refresh the page