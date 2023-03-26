from __future__ import annotations
import streamlit as st
from image_button import image_button
import slides
if slides.CONFIG["nested_layout"]:
    import streamlit_nested_layout  # noqa: F401


def init() -> None:
    """ The main function will display contents based on the index variable. This index will be
        computed by taking into account clicks on left/right buttons. The state variables to
        compute this index must be initialized on the first run.
    """
    if 'is_initialized' not in st.session_state:        # First session call to init() only.
        st.session_state.is_initialized       = True
        st.session_state.index                = 0
        st.session_state.previous_left_count  = 0
        st.session_state.previous_right_count = 0
        st.experimental_rerun()


def set_st_config() -> None:
    """ Basic streamlit layout config. """
    st.set_page_config(page_title=slides.CONFIG["page_title"], page_icon=None, layout='wide')


def resolve_index(current_left_count: int, current_right_count: int, max_index: int) -> None:
    """ This function is ran on every streamlit app run and will determine the content displayed.
        The index is calculated by computing the difference between the number of click of the last
        run on the current number of click. This difference is then clipped and the click count
        state is updated.

    Args:
        current_left_count (int): Number of clicks on the left button in the current run.
        current_right_count (int): Number of clicks on the right button in the current run.
        max_index (int): Number of pages. Will be used to clip the index value.
    """
    diff_left_count  = current_left_count  - int(st.session_state.previous_left_count)
    diff_right_count = current_right_count - int(st.session_state.previous_right_count)
    current_index    = int(st.session_state.index)
    new_index        = current_index + diff_right_count - diff_left_count
    new_index        = min(new_index, max_index - 1)
    new_index        = max(new_index, 0)  # 0 = min_index
    st.session_state.index = new_index
    st.session_state.previous_left_count  = current_left_count
    st.session_state.previous_right_count = current_right_count


def custom_footer():
    """ A hacky function to modify the streamlit footer content. """
    html = f'''
    <style>
    footer {{
        visibility: hidden;
    }}

    footer:after {{
        content:'{slides.CONFIG["footer"]}';
        visibility: visible;
        display: block;
        position: relative;
        #background-color: red;
        padding: 5px;
        top: 2px;
    }}
    </style>
    '''
    st.markdown(html, unsafe_allow_html=True)


def main(pages: tuple[str]) -> None:
    set_st_config()
    custom_footer()
    init()
    left, center, right = st.columns([1, 5, 1])
    with left:
        for _ in range(10):
            st.markdown('#')
        current_left_count = image_button('./image_button/img/gray_left_arrow.png')
    with right:
        for _ in range(10):
            st.markdown('#')
        current_right_count = image_button('./image_button/img/gray_right_arrow.png')
    resolve_index(current_left_count, current_right_count, max_index=len(pages))
    with center:
        eval(f"slides.{pages[st.session_state.index]}").main()


if __name__ == '__main__':
    main(slides.get_pages())
