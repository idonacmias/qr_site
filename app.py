from flask import Flask, render_template, request
import qrcode


import base64
import io
from PIL import Image

app = Flask(__name__,
            template_folder='./templates',
            static_folder='./static')

@app.route('/', methods=["GET", "POST"])
def main():
    img = None
    if request.method == 'POST':
        in_memory_file = io.BytesIO()
       
        input_url = request.form.get('input_url')
        img = qrcode.make(input_url)
        
        img.save(in_memory_file, format="PNG")
        
        # raw_bytes = in_memory_file.getvalue()
        
        base64_encoded = base64.b64encode(in_memory_file.getvalue()).decode('utf-8')
            
        # 3. Construct the Data URI string
        image_data = f"data:image/png;base64,{base64_encoded}"

    return render_template('base.html', image_data=image_data)



if __name__ == '__main__':
    app.run(debug=True)
