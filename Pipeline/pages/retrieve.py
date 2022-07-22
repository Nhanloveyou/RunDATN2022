# df = px.data.tips()# Build App
# app = JupyterDash(__name__)
# ALLOWED_TYPES = (
#     "text", "number", "password", "email", "search",
#     "tel", "url", "range", "hidden",
# )
import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

layout = html.Div(
    [
        html.H1("Truy xuất"),
        dcc.Input(
            id="input_retrieve",
            type="text",
            placeholder="Nhập vào câu hỏi".format("text"),
            debounce=True,
            className="search-container",
        )
        # for _ in ALLOWED_TYPES
    ]
    + [html.P(id="output-retrieve", className="bar")]
    # + [html.Button("Download Text", id="btn-download-txt"),
    # dcc.Download(id="download-text")]

)
print()
@callback(
    Output(component_id="output-retrieve",  component_property="children"),
    Input(component_id="input_retrieve", component_property="value"),
)
def cb_rende(vals):
    # question = "Vào thời gian nào mà Hàn Quốc đã có những bước tiến triển tột bậc trong nền kinh tế?"
    question = vals
    # đường dẫn tới file chứa tất cả documents có thể retriever
    path_to_db = "./documents/all_documents_viquad.pickle"

    # khai báo retriever
    ranker = ViDR(path_to_db)

    # top_k là số lượng đoạn văn muốn retriver
    top_k = 5

    l_docs = ranker.ViDR_retriever(question, top_k)
    
    passage = ""
    dem = 1
    for doc in l_docs:
        passage += "Đoạn văn " + str(dem) + ":" + str(doc) + "\n"
        dem += 1
        # break
    # l_docs là list các đoạn văn với mỗi phần tử bao gồm (context, score)
    # trong đó context là đoạn văn, score là điểm khi retriever đoạn văn đó

    return passage