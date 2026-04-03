import gradio as gr
from inference import main

def run_app():
    return main()

iface = gr.Interface(
    fn=run_app,
    inputs=[],
    outputs="text",
    title="Railway Environment"
)

iface.launch()