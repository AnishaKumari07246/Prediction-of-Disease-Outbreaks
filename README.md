<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Disease Prediction Using Machine Learning</title>
  

  <h1>🧠 Disease Prediction Using Machine Learning</h1>
  <p>A machine learning-based system to predict <strong>Diabetes</strong>, <strong>Heart Disease</strong>, and <strong>Parkinson’s Disease</strong> using medical data and a Streamlit web app.</p>

  <hr/>

  <h2>📌 Table of Contents</h2>
  <ul>
    <li><a href="#overview">Overview</a></li>
    <li><a href="#problem">Problem Statement</a></li>
    <li><a href="#motivation">Motivation</a></li>
    <li><a href="#objectives">Objectives</a></li>
    <li><a href="#scope">Scope of the Project</a></li>
    <li><a href="#technologies">Technologies Used</a></li>
    <li><a href="#architecture">System Architecture</a></li>
    <li><a href="#evaluation">Model Evaluation</a></li>
    <li><a href="#webapp">Web Application</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#future">Future Work</a></li>
    <li><a href="#conclusion">Conclusion</a></li>
  </ul>

  <hr/>

  <h2 id="overview">🧾 Overview</h2>
  <p>This project applies machine learning to predict the likelihood of three major diseases based on user medical input:</p>
  <ul>
    <li>Diabetes</li>
    <li>Heart Disease</li>
    <li>Parkinson’s Disease</li>
  </ul>
  <p>It uses models like <strong>Support Vector Machine</strong>, <strong>Random Forest</strong>, <strong>Decision Tree</strong>, and <strong>Logistic Regression</strong>, optimized with <strong>Random Undersampling (RUS)</strong> for balanced classification. A <strong>Streamlit-based web app</strong> makes the system user-friendly and interactive.</p>

  <h2 id="problem">🩺 Problem Statement</h2>
  <p>Chronic diseases such as diabetes, heart disease, and Parkinson’s are widespread. Traditional diagnostic methods are often slow and manual.<br><strong>Goal:</strong> Develop an automated system for fast, reliable preliminary disease prediction using ML.</p>

  <h2 id="motivation">🔍 Motivation</h2>
  <ul>
    <li>Early disease detection</li>
    <li>Fast predictions</li>
    <li>Scalable deployment options</li>
  </ul>

  <h2 id="objectives">🎯 Objectives</h2>
  <ul>
    <li>Develop ML models for three diseases</li>
    <li>Improve accuracy using Random Undersampling</li>
    <li>Build a user interface using Streamlit</li>
    <li>Ensure the system is scalable, fast, and easy to use</li>
  </ul>

  <h2 id="scope">📈 Scope of the Project</h2>
  <ul>
    <li>Predicts probability of 3 diseases using ML</li>
    <li>Web app takes user input and displays predictions</li>
    <li>Does <strong>not</strong> replace professional medical advice — it's an assistive tool</li>
  </ul>

  <h2 id="technologies">🧰 Technologies Used</h2>
  <table>
    <tr><th>Category</th><th>Tools Used</th></tr>
    <tr><td>Programming</td><td>Python 3.x</td></tr>
    <tr><td>ML Libraries</td><td>scikit-learn, pandas, numpy, imbalanced-learn</td></tr>
    <tr><td>Web Framework</td><td>Streamlit</td></tr>
    <tr><td>Deployment</td><td>(Planned) AWS / Google Cloud</td></tr>
  </table>

  <h2 id="architecture">🏗️ System Architecture</h2>
  <pre><code>
[User Input] → [Data Preprocessing] → [Trained ML Model] → [Prediction] → [Streamlit Output]
  </code></pre>
  <ul>
    <li>Models trained separately for each disease</li>
    <li>Each model outputs predictions with probabilities</li>
    <li>Streamlit handles real-time input and output display</li>
  </ul>

  <h2 id="evaluation">📊 Model Evaluation</h2>
  <table>
    <tr><th>Algorithm</th><th>Metrics Used</th></tr>
    <tr><td>SVM, Random Forest, Decision Tree, Logistic Regression</td><td>Accuracy, Precision, Recall, F1-score</td></tr>
  </table>
  <p>Balanced dataset using <strong>Random Undersampling (RUS)</strong></p>

  <h2 id="webapp">🌐 Web Application</h2>
  <ul>
    <li>Built with Streamlit</li>
    <li>Accepts patient data via form</li>
    <li>Real-time prediction on button click</li>
    <li>Displays result with disease status</li>
    <li>Clean, minimal interface for accessibility</li>
  </ul>

  <div class="image-section">
    <h3>📷 Streamlit Dashboard Preview</h3>
    <img src="prediction dashboard.png" alt="Disease Prediction Streamlit App Preview"/>
    <img src="prediction dashboard1.png" alt="Disease Prediction Streamlit App Preview"/>
    <img src="prediction dashboard2.png" alt="Disease Prediction Streamlit App Preview"/>
  </div>

  <h2 id="results">✅ Results</h2>
  <ul>
    <li>High prediction accuracy on all three diseases</li>
    <li>System performs well on balanced test datasets</li>
    <li>User testing confirms ease-of-use and speed</li>
  </ul>

  <h2 id="future">🚀 Future Work</h2>
  <ul>
    <li>Integrate Deep Learning (Neural Networks)</li>
    <li>Collect real-time patient data via APIs</li>
    <li>Deploy system on cloud platforms (AWS, GCP)</li>
    <li>Add more diseases to prediction model</li>
  </ul>

  <h2 id="conclusion">🧾 Conclusion</h2>
  <p>This project demonstrates the potential of machine learning in healthcare. By building accurate models and wrapping them in an easy-to-use web app, we offer a strong proof-of-concept for assistive disease prediction.</p>
  <blockquote><strong>Disclaimer:</strong> This system is for preliminary predictions only and is not a substitute for professional medical diagnosis.</blockquote>

  <h2>🙋‍♀️ Author & Credits</h2>
  <ul>
    <li><strong>Author:</strong> Anisha Kumari</li>
    <li><strong>Email:</strong> anishakr9090@gmail.com</li>
    <li><strong>Organization:</strong> TechSaksham (AICTE Internship on AI)</li>
  </ul>

</body>
</html>
