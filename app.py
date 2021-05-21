##libraries
from flask import Flask, jsonify, request
import data
import utils

# Khởi tạo model.
global model 
model = []
count_matrix = []
cosine_sim = []
# Khởi tạo flask app
app = Flask(__name__)

# Khai báo các route 1 cho API
@app.route('/', methods=['GET','POST'])
# Khai báo hàm xử lý dữ liệu.
def _hello_world():
    if request.method == 'POST':
        id = request.form["id"]
        model = data.requre(id)
        if len(model) != 0:
            count_matrix,cosine_sim = utils.count(model)
            indices = []
            for i in range(0, len(model), 1):
                indices.append(model[i]['Title'])
        title = data.title(id)
        result = utils.recommend(title,cosine_sim, indices, model)
        return jsonify(result)
    else :
	    return "Hello, Flask!"

# @app.route('/getId', methods=['POST'])
# def getID():
#     id = request.form["id"]
#     model = data.requre(id)
#     if len(model) != 0:
#         count_matrix,cosine_sim = utils.count(model)
#         indices = []
#         for i in range(0, len(model), 1):
#             indices.append(model[i]['Title'])

#     return jsonify(utils.recommend('Phòng cho thuê mới 100% tại Cần Thơ',cosine_sim, indices, model))

if __name__ == '__main__':
    app.run(debug=True,threaded=True, port=3000)
    

