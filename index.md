<html lang="en">
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teboho Xaba - Python Developer</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(to bottom, #0a0f1a, #23022e);
            color: #e0e0f8;
            font-family: 'Poppins', sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            animation: fadeIn 1.5s ease-in;
            overflow-x: hidden;
        }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .background-animation {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('https://source.unsplash.com/random/1920x1080?technology') no-repeat center center/cover;
            opacity: 0.3;
            z-index: -1;
        }
        .navbar {
            display: flex;
            justify-content: center;
            padding: 15px;
            background: rgba(0, 0, 0, 0.7);
            animation: slideDown 1s ease-in-out;
        }
        @keyframes slideDown {
            from { transform: translateY(-50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        .navbar a {
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            font-weight: 600;
        }
        .navbar a:hover {
            color: #90ee90;
        }
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            padding: 20px;
            animation: fadeIn 2s ease-in;
        }
        .profile-img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            border: 3px solid white;
            object-fit: cover;
            margin-right: 20px;
            animation: zoomIn 1.5s ease-in-out;
        }
        @keyframes zoomIn {
            from { transform: scale(0.5); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }
        .header-text {
            text-align: left;
        }
        .content {
            background: rgba(30, 30, 60, 0.85);
            color: #f2f2f2;
            box-shadow: 0 0 12px rgba(255, 0, 255, 0.15);
            padding: 30px;
            border-radius: 12px;
            margin: 20px auto;
            max-width: 900px;
        }
        .projects {
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }
        .project-card {
            background: rgba(22, 27, 49, 0.95);
            color: #ccefff;
            box-shadow: 0 0 10px rgba(0, 255, 255, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        @keyframes scaleUp {
            from { transform: scale(0.8); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
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
            background-color: #00ffc8;
            color: #0a0f1a;
            border: none;
            padding: 10px 20px;
            margin: 5px;
            cursor: pointer;
            border-radius: 5px;
            font-size: 16px;
            box-shadow: 0 0 10px rgba(0, 255, 200, 0.6);
            transition: all 0.3s ease;
        }
        button:hover {
            background-color: #ff00c8;
            color: white;
            box-shadow: 0 0 20px rgba(255, 0, 200, 0.6);
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
            .background-animation::after {
                content: "";
                position: absolute;
                top: 0; left: 0;
                width: 100%;
                height: 100%;
                background-image: radial-gradient(circle, rgba(255,255,255,0.02) 1px, transparent 1px);
                background-size: 20px 20px;
                pointer-events: none;
            }
        }
    </style>
</head>
<body>
    <div class="background-animation"></div>
    <div class="navbar">
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#youtube">YouTube</a>
        <a href="#contact">Contact</a>
    </div>
    <div class="header-container">
        <img src="https://raw.githubusercontent.com/TebohoXaba/My-Profile/main/.github/Title.jpg" alt="Teboho Xaba" class="profile-img">
        <div class="header-text">
            <h1>🚀 Teboho Xaba - The Value Chain Programmer</h1>
            <h3>Python Developer | Data Science | Automation | Machine Learning | Supply Chain | Logistics</h3>
        </div>
    </div>
    <div class="content" id="about">
        <h2>About Me</h2>
        <p>👋 Hi there! I'm <strong>Teboho Xaba</strong>, a Python developer passionate about <strong>data analytics, automation, and machine learning</strong>.</p>
        <p>With a background in <strong>Logistics and Supply Chain Management</strong>, specializing in <strong>Road Transport</strong>, I strive to leverage <strong>technology for efficiency and innovation</strong>.</p>
        <p>🔹 <em>Looking to collaborate?</em> Feel free to explore my projects or get in touch!</p>
    </div>
    <div class="content" id="projects">
        <h2>🚀 Hall of Fame: Portfolio</h2>
        <div class="projects">
            <div class="project-card"><a href="https://zxfleet.co.za">Z X Fleet</a><br>  3P - Road Freight Logistics Partner site  </div>
            <div class="project-card"><a href="https://gcswarehouse.co.za">GCS Warehouse</a><br>  Smart Home Improvements E-Commerce site  </div>
            <div class="project-card"><a href="https://www.hyperiondev.com/portfolio/TX24110016723/"> Data Science Education </a><br>Portfolio of Evidence</div>
            <div class="project-card"><a href="">Dear Diary</a><br>Coming Soon...</div>
        </div>
    </div>
    <div class="content" id="youtube">
        <h2>🎥 My YouTube Channel: The Way to Transform</h2>
        <div class="video-container">
            <iframe id="youtube-video" src="https://www.youtube.com/embed/LWBLDtV5YGk" frameborder="0" allowfullscreen></iframe>
        </div>
        <button onclick="changeVideo('LWBLDtV5YGk')">Why Subscribe</button>
        <button onclick="changeVideo('9L8d_gwc7YQ')">Creating Data on MS Excel</button>
    </div>
    <div class="content" id="contact">
        <h2>📬 Get In Touch</h2>
        <p>
            <a href="https://www.linkedin.com/in/teboho-xaba-a142b617b/">LinkedIn</a> |
            <a href="https://github.com/TebohoXaba">GitHub</a> |
            <a href="https://www.youtube.com/@Real_Nonkosi">YouTube</a> |
            <a href="mailto:teboho.xaba@zxfleet.co.za">Email</a>
        </p>
    </div>
    <script>
        function changeVideo(videoId) {
            document.getElementById('youtube-video').src = "https://www.youtube.com/embed/" + videoId;
        }
    </script>
</body>
</html>
