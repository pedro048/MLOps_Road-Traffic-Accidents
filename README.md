# Projeto de MLOps: Road Traffic Accidents

**PROGRAMA DE PÓS-GRADUAÇÃO EM ENGENHARIA ELÉTRICA E DE COMPUTAÇÃO (PPgEEC) - UFRN**

**Disciplina:** Aprendizagem de Máquina **(EEC1509)**

**Grupo:** 

*   Beatriz Soares de Souza **(20211020152)**
*   Pedro Victor Andrade Alves **(20211027716)**

**Dataset:** [Road_Traffic_Accidents.csv](https://www.kaggle.com/datasets/saurabhshahane/road-traffic-accidents)

## Project's overview:

### Chose Dataset:

The dataset [Road_Traffic_Accidents.csv](https://www.kaggle.com/datasets/saurabhshahane/road-traffic-accidents), from Kaggle, was collected from Addis Ababa Sub city police departments for Masters research work and it has been prepared from manual records of road traffic accident of the year 2017-2020. All the sensitive information have been excluded during data encoding and finally it has 32 features and 12316 instances of the accident. Then it is preprocessed and for identification of major causes of the accident by analyzing it using different machine learning classification algorithms.

### Workflow and Deploy:

In this project you will find the steps necessary for building a classification model, such as setting up the environment, performing exploratory data analysis (EDA), processing, training and testing your model, and deploying a pipeline in production. All the code used on the project can be also found in this [Jupyter Notebook](https://github.com/pedro048/MLOps_Road-Traffic-Accidents/blob/main/Project_Road_Traffic_Accidents/Project_Road_Traffic_Accidents.ipynb), since we're gonna be using Python. The main goal here is to predict the severity of a road traffic accidents, based on variables available in the dataset, deploy it to Heroku and test it live, as [a Deliveried API ](https://road-traffic-accidents-app.herokuapp.com/docs). Decision tree was the classification method used and severity of road traffic accidents can reach three diffrent levels: 0, 1, 2.


## Workflow:

![Workflow](https://lh3.googleusercontent.com/pw/AM-JKLUCw27d6nW0YYrq-zIshMFLMSbCssGxQtNiQMwzxGu7W83kIgmfWlg75IKaNCCDuIB2Dk2ZTGLfEyvDt-AsW3F9m_MIVMlJoBPomkgBolc3WuSYvM2E3uFNDtcFgwhNE-dj1EcEMTtkhi8qmqBzvv9H=w1496-h948-no?authuser=0)

### **Project's workflow:** https://github.com/pedro048/MLOps_Road-Traffic-Accidents/blob/main/Project_Road_Traffic_Accidents/Project_Road_Traffic_Accidents.ipynb 

## Deploy:

![Deploy](https://lh3.googleusercontent.com/pw/AM-JKLXlXm09RhjF_hoHXWz4MhCFU9jF4VKlJr1OIcSinD0itYVclc8fJdRqTA6ECoBKcX7QLT8Ln8tRukszIyxMZIr_Y75nUxSp9DtY-xYXFHyVoDy6fSXCY_lU2mgjAqqdGL4lYrFOwsC22Eh9Tx55JgHz=w1598-h949-no?authuser=0)

### **API Deliveried with Heroku:** https://road-traffic-accidents-app.herokuapp.com/docs

## References:

- https://github.com/ivanovitchm/ppgeecmachinelearning

- https://github.com/ivanovitchm/colab2mlops

- https://www.kaggle.com/datasets/saurabhshahane/road-traffic-accidents

- https://wandb.ai/site

- https://id.heroku.com/login
