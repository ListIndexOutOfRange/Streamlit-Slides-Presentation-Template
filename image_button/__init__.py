import os
import base64
import streamlit.components.v1 as components


parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/build")
_component_func = components.declare_component("ImageButton", path=build_dir)


def image_button(image_path: str) -> int:
    """ Create a new instance of "image_button".

    Args:
        image_path (str): The path to the image used as a button.

    Returns:
        int: The number of times the component's image button has been clicked.
             (This is the value passed to `Streamlit.setComponentValue` on the frontend.)
    """
    # From the path param, the image needs to be loaded and prepared so that the resulting image
    # variable can be used in React code alike: <img src={image}></img>
    with open(image_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode()
    image = f'data:image/png;base64,{image_base64}'

    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(image=image, default=0)
    return component_value
