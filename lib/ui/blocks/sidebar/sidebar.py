from .create_project import render_create_project
from .pick_project import render_pick_project
from .sampling_settings import render_sampling_settings

import gradio as gr

def render_sidebar():
  with gr.Column( scale = 1 ):
    render_pick_project()
    render_create_project()
    render_sampling_settings()