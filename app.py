import gradio as gr
from inference import main

def run_app():
    return main()

with gr.Blocks() as demo:
    gr.Markdown("# 🚆 Railway Environment")

    output = gr.Textbox(label="Output")

    demo.load(fn=run_app, inputs=[], outputs=output)

demo.launch(server_name="0.0.0.0", server_port=7860)