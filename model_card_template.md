# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Xin He
4/7/2026
xhe2@wgu.edu
Model Version: 1.0.0
Model Type: Random Forest


## Intended Use
This intended use of this model is to predict if a person is earning $50,000 and less or earning over $50,000 based on their workclass, education, marital status, occupation, relationship, race, sex, and native country as listed in publicly available census data. 

The intended users for this model is for students and others in the educational field. 

Out-of-scope uses for this model include financial advisors and government policy makers as this model utlizes very limited data for training and does not paint a full picture for evolving trends in income. 


## Training Data
The training data for this model consists of census income data coming from the 1994 Census database. The original dataset consists of 32,561 rows, of which 80% was used for training (approximately 26,048). The categorical features used to train the model include workclass, education, marital status, occupation, relationship, race, sex, and native country and were transformed using OneHotEncoding. The target label is salary, which is binary and consists of "<=50K" or ">50K". 

## Evaluation Data
The evaluation data consists of 20% of the total Census data amounting to approximately 6,512 records. 

## Metrics
_Please include the metrics used and your model's performance on those metrics._

The metrics used to measure the model's performance include precision (.5684), recall (.8670), and F1-Score (.6867). 

The low precision and high recall values indicate that this model ensures that it is highly effective at identifying people who earn over $50,000. This, however does also lead to a higher amount of false positives, as indicated with the .5684 precision score.

## Ethical Considerations
Ethical considerations for this model include bias and age. Bias exists since this model utilizes features such as sex, race, and country of origin. These are sensitive features that could potentially sway the model due to historical prejudice based on these characteristics against members of society. 


## Caveats and Recommendations
A caveat is that the data used to train the model. The Census data was from 1994, income trends could have drastically changed in the past 30 years due to factors such as offshoring, automation, immigration, and emerging occupations. 
As such, this model should be strictly used for educational purposes and not for generating any meaningful insight into financial, governmental, or career oriented projects. 