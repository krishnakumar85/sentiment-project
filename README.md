# PRISM
This is a project completed as part of the online course on AI and machine learning offered by CCE, IISc.
The project title is **PRISM: A Chrome Extension for AI-based Sentiment Analysis of Users' reviews**. Here, **PRISM** is acronym for **P**roduct **R**eview via **I**ntelligent **S**entiment **M**ining. The summary contains the following:
1. Introduction
2. Problem Statement
3. Proposed Solution
4. Development Process
5. Technical Highlights
6. Outcomes
7. Future Roadmap
## 1. Introduction

In the modern age of e-commerce and digital services, both consumers and businesses face significant challenges in sifting through countless online reviews to extract actionable insights. Reviews often contain critical information about customer satisfaction, product features, and service efficiency. However, due to the sheer volume of reviews and the complexity of human emotions embedded in text, manually processing this data is infeasible. 

**PRISM** (Product Review through via INtelligent Sentiment Mining) is a solution designed to address these challenges. It leverages artificial intelligence to classify reviews, analyze dominant emotions, highlight key features, and summarize insights that empower consumers to make informed purchasing decisions while enabling businesses to refine their operations effectively.


## 2. Problem Statement
1. **Volume Overload**: The massive number of online reviews makes manual analysis impossible.  
2. **Emotional Ambiguity**: The sentiments and emotions behind a review are often hidden within nuanced language.  
3. **Scattered Insights**: Reviews may provide critical insights, but these are buried in large datasets without proper structure.
---

## 3. Proposed Solution  

PRISM offers a scalable, AI-driven tool that:  
- Aggregates and analyzes the dominant emotions from large review datasets.  
- Uses natural language processing (NLP) to classify reviews by themes and emotions.  
- Summarizes actionable insights to help consumers and businesses.  

By providing clarity and focus, PRISM simplifies decision-making for both stakeholders. 

![image](https://github.com/user-attachments/assets/4c1e6ee8-4a05-4abf-99e0-6737d6f64dcc)

---

## 4. Development Phases

The development of PRISM was structured into three key phases:  

1. **Ideation Phase**:  
   - Data collection involved reviews from platforms like G2, Kaggle, and multiple e-commerce websites.  
   - Reviews were collected manually, providing a foundational dataset for initial experiments.  

2. **Intermediate Phase**:  
   - AI models like OpenAI’s GPT and tools like Claude.ai were employed for sentiment analysis.  
   - Experiments with parameters such as temperature and token limits were conducted to optimize response quality and cost efficiency.  

3. **Final Phase**:  
   - A Chrome extension, "Comment Scraper," was created to automate the collection of reviews from Amazon.in.  
   - The extension generates sentiment summaries, highlighting key product features and consumer sentiments in real-time.

---

## 5. Technical Highlights 
PRISM uses LLM models to identify dominant emotions and classify reviews based on recurring themes like customer service, product quality, or delivery experience.  
- **Temperature Control**: A low temperature value (T=0) was chosen to ensure deterministic and accurate results, avoiding the randomness that comes with higher temperature settings.  
- **Cost Optimization**: By setting a token limit of 800, PRISM ensures that summaries are concise yet detailed enough for actionable insights, making it cost-effective for large-scale analysis.  

# Developer Setup

## Setting up the server

### Environment setup
```bash
cd server
python3 -m venv venv
```

Now activate the virtual environment
```bash
source venv/bin/activate
```

### Install required packages
```bash
pip install -r requirements.txt
```

### Launch server
```bash
flask run
```

## Setting up chrome app
Load the chrome extension by visiting the chrome developer tools 
- Enable "Dev mode"
- Click on "Load Unpacked" to load the chrome extension


## Docker setup
The docker image is built using github actions and can be accessed from here -

```bash
docker pull abhishekdutta123/my-flask-api:latest
```

To run the docker container,

```bash
docker run -d -p 5000:5000 abhishekdutta123/my-flask-api:latest
```

## 6. Outcomes  

PRISM demonstrated the following capabilities:  
1. **For Consumers**: It provides clear and concise summaries of product features, enabling faster decision-making.  
2. **For Businesses**: Insights into customer sentiment and feedback can guide improvements in product design, customer support, and other areas.  

---

## 7. Future Roadmap  

To enhance PRISM's capabilities and usability, the following steps are planned: 

1. **Expand Dataset**: Increase the diversity and scale of datasets by incorporating reviews across a wider variety of platforms and industries.  
2. **Enhance Model Accuracy**: Improve model performance using different LLM models, algorithms and fine-tuning  
3. **User Feedback Integration**: Continuously gather feedback from users to refine the tool and align it with evolving needs.  
4. **Collaborations**: Partner with organizations for data sharing and collaborative insights to make PRISM a universal solution for review analysis.  
