def generate_html_template(filename="template.html"):
    # Define the basic HTML template
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Newsletter</title>
    <style>
        /* Font and Color Scheme */
        body {
            font-family: "Helvetica Neue", Arial, sans-serif;
            background-color: #e6f7ff; /* light baby blue */
            color: #333;
            margin: 0;
            padding: 0;
        }

        /* Header Styling */
        header {
            background-color: #007acc; /* deeper blue for contrast */
            color: white;
            text-align: center;
            padding: 1.5rem;
        }
        header h1 {
            font-size: 2rem;
            margin: 0;
        }

        /* Main Content Styling */
        main {
            max-width: 800px;
            margin: 2rem auto;
            padding: 1rem;
            background-color: #007acc; /* white background for content */
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }

        /* Paragraph and Image Styling */
        .content-section {
            display: flex;
            align-items: center;
            background-color: #e6f7ff; /* light baby blue */
            margin: 4rem auto;   
            margin-bottom: 1.5rem;
        }
        .content-left {
            flex-direction: row;
        }
        .content-right {
            flex-direction: row-reverse;
        }
        .content-section img {
            width: 150px;
            height: auto;
            margin: 0 1rem;
            border-radius: 8px;
        }
        .content-section img {
            width: 150px;
            height: auto;
            margin: 0 1rem;
            border-radius: 8px;
        }
        .content-section p {
            flex: 1;
            font-size: 1.1rem;
            line-height: 1.6;
            
        }
        .visit-button {
            display: block;
            width: fit-content;
            margin: 2rem auto 0;
            padding: 0.8rem 1.5rem;
            font-size: 1.1rem;
            color: white;
            background-color: #007acc;
            text-decoration: none;
            border-radius: 8px;
            transition: background-color 0.3s ease;
            text-align: center;
        }
        
        .visit-button:hover {
            background-color: #005fa3; /* darker shade on hover */
        }
    </style>
</head>
<body>

<header>
    <h1>Newsletter</h1>
</header>

<main>
    <div class="content-section content-left">
        <img src="image1.jpg" alt="Image 1">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus arcu est, ullamcorper non massa nec, venenatis rhoncus purus. Phasellus ornare vulputate orci, vel interdum turpis elementum at. Cras molestie finibus dolor, et posuere risus pretium ac. Integer ac ante vel nisi volutpat fringilla. Mauris bibendum, nunc vitae vehicula porta, nisi dui eleifend lacus, a consectetur eros sapien non nunc.</p>
    </div>
    <div class="content-section">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus arcu est, ullamcorper non massa nec, venenatis rhoncus purus. Phasellus ornare vulputate orci, vel interdum turpis elementum at. Cras molestie finibus dolor, et posuere risus pretium ac. Integer ac ante vel nisi volutpat fringilla. Mauris bibendum, nunc vitae vehicula porta, nisi dui eleifend lacus, a consectetur eros sapien non nunc.</p>
        <img src="image2.jpg" alt="Image 2">
    </div>
    <div class="content-section">
        <img src="image3.jpg" alt="Image 3">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus arcu est, ullamcorper non massa nec, venenatis rhoncus purus. Phasellus ornare vulputate orci, vel interdum turpis elementum at. Cras molestie finibus dolor, et posuere risus pretium ac. Integer ac ante vel nisi volutpat fringilla. Mauris bibendum, nunc vitae vehicula porta, nisi dui eleifend lacus, a consectetur eros sapien non nunc.</p>
    </div>
    <div class="content-section">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus arcu est, ullamcorper non massa nec, venenatis rhoncus purus. Phasellus ornare vulputate orci, vel interdum turpis elementum at. Cras molestie finibus dolor, et posuere risus pretium ac. Integer ac ante vel nisi volutpat fringilla. Mauris bibendum, nunc vitae vehicula porta, nisi dui eleifend lacus, a consectetur eros sapien non nunc.</p>
        <img src="image4.jpg" alt="Image 4">
    </div>
    <a href="https://google.com" class="visit-button">Visit us!</a>
</main>

</body>
</html>
"""
    with open(filename, "w") as file:
        file.write(html_content)

    print(f"HTML template '{filename}' created successfully.")
generate_html_template()