![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FAklimaRimi%2FAppClassifier%2F&label=views&labelColor=%23697689&countColor=%23f47373)
# AppClassifier

## Motive

AppClassifier is a `multilabel` `NLP` project. Almost 360+ labels are used in this project which is deployed and rendered.

HuggingFace API           |  Rendered website
:-------------------------:|:-------------------------:
![](https://github.com/AklimaRimi/AppClassifier/blob/main/images/hugging.png)  |  ![](https://github.com/AklimaRimi/AppClassifier/blob/main/images/website.png)

## Data Collection

I collected data from : https://sourceforge.net/ <br>
Around 33634 pieces of data have been collected.

## Data Preprocessing

Because this project is based on `MultiLabel`, each entity must have more than one label. I chose the most common labels because the least common labels can distract a model from detecting accurate labels.

Around 360+ labels are chosen and then Converted the string categories into numerical form.

## Training

For the rest of the work I use `PyTorch` WorkFrame. Also `Blurr` Api for training models. For model choosing, I used two types of models, those are collected from the `HuggingFace` model library.

1. `distilroberta-base` and <br>
2. `bertabaporu-large`<br>

## Training Results

I used 2 models for comparison. But both models performed the same; they gave `99%` accuracy. Both model did great work.

1. **distilroberta-base** : As all the processes done in Pytorch so I had to use `dataloaders` for transform dataset for model. In that case I choose batch size `32`. This model is very faster than other models. **So I used this model for that project**  <br>
2. **bertabaporu-large** : For this model I had to choose the Batch size 2. Othewise `CUDA` Terminate the training process for crossing the limit of `CUDA`. This model is the most Slower.  <br>

## Models

All of the models can be found in [here](https://drive.google.com/drive/folders/1OB12YLmqM38qGf0AMWnXZoHfli6UJ-9j?usp=sharing).

## Deployment

I used `HuggingFace` to deploy this project. It is very easy to use and free. 
You can use this project as deployed : https://huggingface.co/spaces/Rimi98/AppClassifier <br>

![](https://github.com/AklimaRimi/AppClassifier/blob/main/images/hugging.png)

## Integration/ Render

I used `Flask` for rendering this project as an open website. I created a very basic GUI to build this website. 
Also I use the [Render](https://dashboard.render.com/) for integration.

Click this [link](appclassifier.onrender.com/)

![](https://github.com/AklimaRimi/AppClassifier/blob/main/images/website.png)


## Future Work

Almost 50000+ data points can be found on [this](https://sourceforge.net/) website where I have collected 33634 data points. My future work will be to collect more data and develop this project. Anyone can join me. Feel free to pull a request.


