# 🎬 Movie Recommendation System

A content-based Movie Recommendation System that recommends similar movies based on their features using **TF-IDF Vectorization** and **Cosine Similarity**. The system analyzes movie metadata and suggests movies that are most similar to the selected movie.

## 🚀 Features

- Content-based movie recommendations
- TF-IDF vectorization for feature extraction
- Cosine Similarity for finding similar movies
- Fast and accurate recommendations
- User-friendly interface

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit / Flask (if applicable)

## 📂 Dataset

The project uses a movie dataset containing information such as:
- Movie Title
- Genres
- Keywords
- Cast
- Crew
- Overview

These features are combined to generate recommendations.

## ⚙️ Working

1. Load and preprocess the movie dataset.
2. Combine relevant movie features into a single text field.
3. Apply **TF-IDF Vectorization** to convert text into numerical vectors.
4. Compute **Cosine Similarity** between movie vectors.
5. Recommend the top similar movies based on similarity scores.

## ▶️ Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/movie-recommendation-system.git
```

2. Navigate to the project directory:
```bash
cd movie-recommendation-system
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

or (if using Streamlit):

```bash
streamlit run app.py
```

## 📸 Output

- Select or search for a movie.
- The system displays a list of similar recommended movies.

## 📌 Future Enhancements

- Improve recommendations using hybrid models.
- Deploy the application on Streamlit Cloud or Render.

## 👨‍💻 Author

Jiya Shah
