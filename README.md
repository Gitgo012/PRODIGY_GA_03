# Movie Line Generator through Markov chains

A fun web application that generates random movie-style lines using a Markov chain model trained on the Cornell Movie Dialogs Corpus. It was done as part of my internship at Prodigy Infotech

## Project Introduction

Movie Line Machine is a Flask-based web app that uses a Markov chain model to generate new, movie-like sentences. The model is trained on real movie dialogues, making the generated lines entertaining and often surprisingly realistic! The Markov model was specifically trained on the Cornell Movie Dialogs Corpus, which was obtained from Kaggle. The project demonstrates the use of Markov chains for text generation and provides a simple, interactive web interface.

## Features

- **Random Movie Line Generation:** Click a button to instantly generate a new, unique movie-style line.
- **Markov Chain Model:** Built using the `markovify` library and trained on the Cornell Movie Dialogs Corpus.
- **Simple Web Interface:** Clean, user-friendly frontend with a single button for interaction.
- **Flask Backend:** Lightweight Python backend serving the model and frontend.

## How to Run Locally

### 1. Clone the Repository

```bash
git clone <repo-url>
cd Prodigy-Infotech/PRODIGY_GA_03
```

### 2. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install required packages:

```bash
pip install flask markovify
```

### 3. Prepare the Markov Model

A pre-trained `markov_model.json` is included (large file). If you want to retrain or update the model:

- Open `model.ipynb` in Jupyter Notebook.
- Follow the steps to download the Cornell Movie Dialogs Corpus from Kaggle and train the model.
- Save the model as `markov_model.json` in the project directory.

### 4. Run the Application

```bash
python app.py
```

The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 5. Usage

- Open your browser and go to the app URL.
- Click the "Generate Movie Line" button to see a new line each time!

## 🛠️ Project Structure

- `app.py` - Flask backend serving the web app and API.
- `markov_model.json` - Pre-trained Markov model (large file).
- `templates/index.html` - Frontend HTML template.
- `model.ipynb` - Jupyter notebook for training the Markov model.

## Dependencies

- Flask
- markovify

## Credits

- [Cornell Movie Dialogs Corpus (Kaggle)](https://www.kaggle.com/datasets/Cornell-University/movie-dialog-corpus)
- [markovify](https://github.com/jsvine/markovify)
- Followed this amazing tutorial on Markovify and tweaked it a little for using my custom dataset (https://towardsdatascience.com/text-generation-with-markov-chains-an-introduction-to-using-markovify-742e6680dc33/)
- For understanding the math behind Markov chains used this resource from Brilliant (https://brilliant.org/wiki/markov-chains/)
---

## Output
---

#### Mobile view
---

<p align="center">
  <img src="images/Image%202%20task%203.jpg" height="250px"/>
</p>

---

#### PC view
---

<p align="center">
  <img src="images/Image%201%20task%203.png" height="250px"/>
</p>



