# AppClassifier

## Motive

AppClassifier is a `multilabel` `NLP` project. Almost 600+ labels are used in this project.

## Data Collection

I collected data from : https://sourceforge.net/ <br>
Around 17000 pieces of data have been collected.

## Data Preprocessing

Because this project is based on 'MultiLabel,' each entity must have more than one label. I chose the most common labels because the least common labels can distract a model from detecting accurate labels.

Around 600+ labels are chosen and then Converted the string categories into numerical form.

## Training

For the rest of the work I use `PyTorch` WorkFrame. Also `Blurr` Api for training models. As a model I used two types of models, those are collected from the `HuggingFace` model library.

1. `distilroberta-base` and <br>
2. `bertabaporu-large`<br>

## Training Results

I used 2 models for comparison. But both models performed the same; they gave `99%` accuracy. Both model did great work.

## Deployment

I used `HuggingFace` to deploy this project. It is very easy to use and free. 
You can use this project as deployed : https://huggingface.co/spaces/Rimi98/AppClassifier

## Integration/ Render

I used `Flask` for rendering this project as an open website. I created a very basic GUI to build this website. 
Also I use the [Render](https://dashboard.render.com/) for integration.

Click this [link](appclassifier.onrender.com/)


## Future Work

Almost 50000+ data points can be found on [this](https://sourceforge.net/) website where I have collected 17000 data points. My future work will be to collect more data and develop this project. Anyone can join me. Feel free to knock on my door. 


