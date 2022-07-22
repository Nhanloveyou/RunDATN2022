

import dash
from dash import html, dcc, callback, Input, Output

# df = px.data.tips()# Build App
# app = JupyterDash(__name__)
dash.register_page(__name__, path='/')
# ALLOWED_TYPES = (
#     "text", "number", "password", "email", "search",
#     "tel", "url", "range", "hidden",
# )
layout = html.Div(
    [
        html.H1("Question Answering"),
        dcc.Input(
            id="input_{}".format("text"),
            type="text",
            placeholder="Nhập vào câu hỏi".format("text"),
            debounce=True,
            className="search-container",
        )
        # for _ in ALLOWED_TYPES
    ]
    + [html.H5(id="out-all-types", className="bar")]
    # + [html.Button("Download Text", id="btn-download-txt"),
    # dcc.Download(id="download-text")]

)
print()
@callback(
    Output(component_id="out-all-types", component_property="children"),
    [Input(component_id="input_{}".format("text"), component_property="value")],
)
def cb_rende(vals):
    # question = "Vào thời gian nào mà Hàn Quốc đã có những bước tiến triển tột bậc trong nền kinh tế?"
    question = vals
    answers = ViQAS_predict(question)
    List_answer = ""
    dem = 1
    for answer in answers:
        if answer in question:
            
            List_answer += "Câu trả lời " + str(dem) + ": " + "\n"
    #     # print("Answer: ", answer)
        else:
            List_answer += "Câu trả lời " + str(dem) + ": " + answer + "\n"
        dem += 1
    return List_answer

# app.run_server(mode='external')