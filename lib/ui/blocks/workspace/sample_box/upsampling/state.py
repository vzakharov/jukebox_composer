from UI.general import project_name, project_name
from UI.navigation import picked_sample, picked_sample, picked_sample, picked_sample
from UI.preview import 
from UI.upsampling import upsampling_accordion, upsampling_level, upsampling_running, upsampling_status, upsampling_level, upsampling_running, upsampling_running, continue_upsampling_button, continue_upsampling_button, upsampling_status
from .init_args import upsample_button_click_args
from .manipulation import render_manipulation_column
from .refresher import render_refresher
from lib.upsampling.show_or_hide_continue_upsampling import show_or_hide_continue_upsampling
from lib.upsampling.show_or_hide_upsampling_elements import show_or_hide_upsampling_elements
from lib.ui.preview import default_preview_args

import gradio as gr

def render_upsampling_accordion():

  with upsampling_accordion.render():
    with gr.Row():
      
      with gr.Column():
        upsampling_level.render().change(
          **default_preview_args,
        )

        show_or_hide_upsampling_elements_args = dict(
          inputs = [ project_name, picked_sample, upsampling_running ],
          outputs = [ upsampling_status, upsampling_level ],
          fn = show_or_hide_upsampling_elements,
        )

        picked_sample.change( **show_or_hide_upsampling_elements_args )
        upsampling_running.change( **show_or_hide_upsampling_elements_args )

      render_manipulation_column()

    picked_sample.change(
      inputs = [ project_name, picked_sample, UI.project.total_audio_length, upsampling_running ],
      outputs = continue_upsampling_button,
      fn = show_or_hide_continue_upsampling,
    )

    continue_upsampling_button.render().click( **upsample_button_click_args )

    render_refresher(show_or_hide_upsampling_elements_args)

  upsampling_status.render()
  
  return show_or_hide_upsampling_elements_args, upsample_button_click_args

