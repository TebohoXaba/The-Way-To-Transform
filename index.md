<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teboho Xaba - Python Developer</title>
    <style>
        body {
            background: linear-gradient(to bottom, #1b3c73, #28a745);
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            padding: 20px;
        }
        .profile-img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            border: 3px solid white;
            object-fit: cover;
            margin-right: 20px;
        }
        .header-text {
            text-align: left;
        }
        .content {
            max-width: 800px;
            margin: 20px auto;
            background: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
        }
        a {
            color: #90ee90;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
        .video-container {
            margin: 20px auto;
            width: 100%;
            max-width: 560px;
        }
        iframe {
            width: 100%;
            height: 315px;
            border-radius: 10px;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 5px;
            cursor: pointer;
            border-radius: 5px;
        }
        button:hover {
            background-color: #1b3c73;
        }
        @media (max-width: 768px) {
            .header-container {
                flex-direction: column;
                text-align: center;
            }
            .profile-img {
                margin: 0 auto 10px;
            }
            .header-text {
                text-align: center;
            }
        }
    </style>
</head>
<body>
    <div class="header-container">
        <img src="https://raw.githubusercontent.com/TebohoXaba/My-Profile/main/.github/Title.jpg" alt="Teboho Xaba" class="profile-img">
        <div class="header-text">
            <h1>🚀 Teboho Xaba - The Value Chain Programmer</h1>
            <h3>Python Developer | Data Science | Automation | Machine Learning | Supply Chain | Logistics</h3>
        </div>
    </div>
    <div class="content">
        <h2>About Me</h2>
        <p>👋 Hi there! I'm <strong>Teboho Xaba</strong>, a Python developer passionate about <strong>data analytics, automation, and machine learning</strong>.</p>
        <p>With a background in <strong>Logistics and Supply Chain Management</strong>, specializing in <strong>Road Transport</strong>, I strive to leverage <strong>technology for efficiency and innovation</strong>.</p>
        <p>🔹 <em>Looking to collaborate?</em> Feel free to explore my projects or get in touch!</p>
        
        <h2>🚀 Featured Projects</h2>
        <ul>
            <li><a href="https://zxfleet.co.za">Z X Fleet</a> - 3P - Road Freight Logistics Partner site</li>
            <li><a href="https://gcswarehouse.co.za">GCS Warehouse</a> - Smart Home Improvements E-Commerce site</li>
            <li><a href="#">Dear Diary</a> - Personal journal & AI insights App (*Coming Soon!*)</li>
        </ul>
        
        <h2>🎥 My YouTube Channel: The Way to Transform</h2>
        <div class="video-container">
            <iframe id="youtube-video" src="https://www.youtube.com/embed/LWBLDtV5YGk" frameborder="0" allowfullscreen></iframe>
        </div>
        <button onclick="changeVideo('LWBLDtV5YGk')">Why Subscribe</button>
        <button onclick="changeVideo('9L8d_gwc7YQ')">Creating Data on MS Excel</button>
        
        <script>
            function changeVideo(videoId) {
                document.getElementById('youtube-video').src = "https://www.youtube.com/embed/" + videoId;
            }
        </script>
        
        <h2>📬 Get In Touch</h2>
        <p>
            <a href="https://www.linkedin.com/in/teboho-xaba-a142b617b/">LinkedIn</a> |
            <a href="https://github.com/TebohoXaba">GitHub</a> |
            <a href="https://www.youtube.com/@Real_Nonkosi">YouTube</a> |
            <a href="mailto:teboho.xaba@zxfleet.co.za">Email</a>
        </p>
        <p>⭐ <em>Thanks for visiting! Feel free to check out my repositories and projects!</em></p>
    </div>
</body>
</html>
