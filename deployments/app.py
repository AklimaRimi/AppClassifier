import gradio as gr
import onnxruntime 
from transformers import AutoTokenizer
import torch, json

token = AutoTokenizer.from_pretrained('pablocosta/bertabaporu-large-uncased')

with open("data.json", "r") as fp:
  types = json.load(fp)

types = list(types)


inf_session = onnxruntime.InferenceSession('classifier-quantized.onnx')
input_name = inf_session.get_inputs()[0].name
output_name = inf_session.get_outputs()[0].name

def classify(review):
    input_ids = token(review)['input_ids'][:512]
    logits = inf_session.run([output_name], {input_name: [input_ids]})[0]
    logits = torch.FloatTensor(logits)
    probs = torch.sigmoid(logits)[0]
    return dict(zip(types, map(float, probs))) 


label = gr.outputs.Label(num_top_classes=5)
iface = gr.Interface(fn=classify, inputs="text", outputs=label)
iface.launch(inline=False)