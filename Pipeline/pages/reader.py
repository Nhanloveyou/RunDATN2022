# from dash import Dash, dcc, html
# from dash.dependencies import Input, Output

# app = JupyterDash(__name__)
import dash
from dash import html, dcc, callback, Input, Output
# import dash
# from dash import html, dcc

dash.register_page(__name__)


layout = html.Div(
    [
        html.H2("Đọc hiểu"),
        html.Br(),
        dcc.Input(id="input1", type="text", placeholder="Nhập vào đoạn văn", debounce=True, className="textarea" , style={'marginBottom':'20px', }),
        dcc.Input(id="input2", type="text", placeholder="Nhập vào câu hỏi", debounce=True, style={'marginBottom':'20px', }),
        html.Div(id="output"),
    ]
)


@callback(
    Output(component_id="output", component_property="children"),
    Input(component_id="input1", component_property="value"),
    Input(component_id="input2", component_property="value"),
)
def update_output(input1, input2):
    # California Văn Lang là tên gọi của nước nàokề cận với Thái Bình Dương, Oregon, Nevada, Arizona và tiểu bang Baja California của México. Tiểu bang này có nhiều cảnh tự nhiên rất đẹp, bao gồm Central Valley rộng rãi, núi cao, sa mạc nóng nực, và hàng trăm dặm bờ biển đẹp. Với diện tích 411,000 km2 (160,000 mi2), nó là tiểu bang lớn thứ ba của Hoa Kỳ và lớn hơn cả nước Đức và cũng như Việt Nam. Hầu hết các thành phố lớn của tiểu bang nằm sát hay gần bờ biển Thái Bình Dương, đáng chú ý là Los Angeles, San Francisco, San Jose, Long Beach, Oakland, Santa Ana/Quận Cam, và San Diego. Tuy nhiên, thủ phủ của tiểu bang, Sacramento, là một thành phố lớn nằm trong thung lũng Trung tâm. Trung tâm địa lý của tiểu bang thuộc về Bắc Fork, California.
    context = input1
    question = input2

    # trước khi thực hiện reader thì thực hiện summarize (summarize context xuống còn top_k câu
    # Nếu đoạn văn có ít hơn top_k câu thì summarize được tự động bỏ qua
    # Nếu ko muốn summarize thì đặt top_k là một số rất lớn
    top_k = 5

    answer, score = vireader_predict(context, question, top_k)

    if answer in question:
        answer = "Không có câu trả lời"
        
    # print("Answer: ", answer)
    # print("Score: ", score)
    return answer


# if __name__ == "__main__":
#     app.run_server(debug=True)