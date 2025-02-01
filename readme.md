Developing an API to Detect Local Languages Using FastAPI  

I am building an API that processes images containing handwritten text in local languages. The API will analyze the text, identify grammatical errors, and return a structured response with corrections and grading.  


Step 1: Setting Up My Workspace
To get started, I need to install a few essential tools on my computer:  
- Python – The core programming language for my API  
- FastAPI – The framework that helps me create the web service  
- Tesseract OCR– A tool that reads and extracts text from images  
- Image Processing Libraries – Such as OpenCV and PIL, which help clean and enhance images before processing  


Step 2: Setting Up the API Endpoint  
I will create an API endpoint that runs locally on `localhost:8000`. This serves as the entry point where users can upload images containing handwritten text.  

When I navigate to `localhost:8000/docs`, I can access an interactive interface that allows me to test and visualize how the API works.  

Step 3: Processing the Handwritten Image
Once an image is uploaded, my API follows a structured pipeline:  
1. Preprocessing – Enhancing the image by adjusting brightness and contrast for better readability  
2. Text Extraction – Using Tesseract OCR to read the handwritten text  
3. Language Identification – Recognizing the language of the extracted text  
4. Error Detection – Checking for grammatical mistakes  
5. Grading – Providing feedback on grammar, spelling, and structure  

Step 4: Running the API 
To start the service, I open my terminal and run the following command:  

`uvicorn main:app --reload`

This launches my API, making it accessible at `localhost:8000`.  


Step 5: Testing the API
I can test my API using different methods:  
1. Web Interface – By visiting `localhost:8000/docs` in my browser  
2. Postman – A tool for sending API requests and analyzing responses  
3. Terminal Command – Using `curl` to send an image for processing:  

`curl POST -F "image=@the-image.jpg" http://localhost:8000/analyze-text`
in my case, it would look something like this: `curl -v -X POST -F "image=@/Users/ishitha/Hard_Code/genai-apis/marwadi-lang.jpg" http://localhost:8000/analyze-text`

How the API Works
- It Supports Multiple Indian Languages – Recognizing and analyzing text in languages like Marwadi, Hindi, and Gujarati  
- Fast and Efficient – The response is quick with high accuracy  
- Detailed Feedback – The system provides an evaluation of grammar, spelling, and sentence structure  
- A Virtual Writing Assistant – It helps improve handwritten text quality  

Tech Stack 
- Python – Main programming language  
- FastAPI – Web framework for API development  
- Tesseract OCR – Reads handwritten text  
- OpenCV & PIL – Helps process and clean images  

System Architecture Overview 
- The FastAPI endpoint processes multipart/form-data** POST requests, handling JPEG image uploads** asynchronously at port `8000`.  
- The uploaded image undergoes binary conversion and preprocessing before text extraction using OCR.  
- The OCR engine, configured with a specific language pack (e.g., Gujarati: `lang='guj'`), extracts text accurately while maintaining Unicode encoding.  

Response Analysis 
The API returns a structured JSON response** with:  
- Confidence Score: 0.95 (95% recognition accuracy)  
- Text Analysis Metrics: 4 words, 14 characters extracted  
- Grading Breakdown: 
  - Grammar: 9.0/10  
  - Spelling: 8.5/10  
  - Sentence Structure: 8.0/10  
- File Validation: Ensuring correct MIME type (`image/jpeg`) and size verification  


Performance Insights
- Returns an HTTP/1.1 200 OK response  
- Efficient TCP connection handling at `127.0.0.1:8000`  
- Ensures a clean request-response cycle with **minimal latency**  

Final Thoughts
This API is designed to efficiently process handwritten text in local languages, analyze its structure, and provide meaningful feedback. So, next time I don't have to explain it to my north-indian friend about a sign board that says to not litter, I can just point her to this API.

