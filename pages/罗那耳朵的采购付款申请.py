from openai import OpenAI
import streamlit as st


st.title("💬让我们来探索一下汇联易AI吧")


st.caption("🚀财务中心AI探索，接入kimi的API")

def char_by_char_yield(text):
    for char in text:
        yield char

if "messages2" not in st.session_state:
    st.session_state["messages2"] = [{"role": "system", "content": "你是一个费用报销审核专家，你可以提取合同关键字，总结信息，提示异常点，你也可以回答其他任何问题。"}]


content = "公司的采购规定为：必须以人民币采购。现在是2024年11月，采购货品必须在3个月内到货。采购金额不能超过500000元。如果采购的是显卡，必须采购英伟达品牌的显卡，不能采购其他品牌的显卡。具体采购订单信息如下。采购人：罗那耳朵，收货方：罗那耳朵，采购日期：2024-11-01，到货时间：2025-9-30，交易地点：旧金山，付款方: 上海森马数据科技有限公司，银行账号：1234567890，采购内容：英特尔显卡一批，利润中心编码：P260000000，货币：美元。采购金额：699999元。"

st.header("公司采购规定（假设）")
st.write('''假设公司的采购规定为：''')
st.write('1. 必须以人民币采购。')
st.write('2. 现在是2024年11月，采购货品必须在3个月内到货。')
st.write('3. 采购金额不能超过500000元。')
st.write('4. 如果采购的是显卡，必须采购英伟达品牌的显卡，不能采购其他品牌的显卡。')

st.divider()

st.header("具体采购订单信息")
st.write("采购人：罗那耳朵")
st.write("收货方：罗那耳朵")
st.write("采购日期：2024-11-01")
st.write("到货时间：2025-9-30")
st.write("交易地点：旧金山")
st.write("付款方: 上海森马数据科技有限公司")
st.write("银行账号：1234567890")
st.write("采购内容：英特尔显卡一批")
st.write("利润中心编码：P260000000")
st.write("货币：美元")
st.write("采购金额：699999元")
st.divider()
st.write("👇🏻我可以提取合同关键字，总结信息，提示异常点，任何问题都可以问我")


for msg in st.session_state["messages2"] :
    if msg != st.session_state["messages2"][0]:
        if msg["role"] == "assistant":
            st.chat_message(msg["role"]).write(msg["content"])

if st.button("提示风险点"):
    client = OpenAI(
    api_key = "sk-gTjf6t2Hhopb2o1cVn42zbydKjt5oB0bNca9EftyjLmwVk8Q",
    base_url = "https://api.moonshot.cn/v1",
)
    st.session_state["messages2"] .append({"role": "user", "content": content+"就这份报采购订单而言，请提示风险点。"})
    # st.chat_message("user").write(prompt)
    

    # 流式输出
    stream = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state["messages2"] ,temperature=0.2,stream=True)

    full_stream=st.chat_message("assistant").write_stream(stream)
    
    # 保存流式传输结果

    st.session_state["messages2"] .append({"role": "assistant", "content": full_stream})

if st.button("请帮我总结"):
    client = OpenAI(
    api_key = "sk-gTjf6t2Hhopb2o1cVn42zbydKjt5oB0bNca9EftyjLmwVk8Q",
    base_url = "https://api.moonshot.cn/v1",
)
    st.session_state["messages2"].append({"role": "user", "content": content+"就这份采购订单而言，请总结收货方、采购内容、采购金额。"})
    # st.chat_message("user").write(prompt)
    

    # 流式输出
    stream = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state["messages2"] ,temperature=0.2,stream=True)

    full_stream=st.chat_message("assistant").write_stream(stream)
    
    # 保存流式传输结果

    st.session_state["messages2"] .append({"role": "assistant", "content": full_stream})

if st.button("请帮我决策"):
    client = OpenAI(
    api_key = "sk-gTjf6t2Hhopb2o1cVn42zbydKjt5oB0bNca9EftyjLmwVk8Q",
    base_url = "https://api.moonshot.cn/v1",
)
    st.session_state["messages2"] .append({"role": "user", "content": content+"就这份采购订单而言，根据公司规定允许采购吗？"})
    # st.chat_message("user").write(prompt)
    

    # 流式输出
    stream = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state["messages2"] ,temperature=0.2,stream=True)

    full_stream=st.chat_message("assistant").write_stream(stream)
    
    # 保存流式传输结果

    st.session_state["messages2"] .append({"role": "assistant", "content": full_stream})

if prompt := st.chat_input('有任何问题都可以在这里向Kimi提问'):

    client = OpenAI(
    api_key = "sk-gTjf6t2Hhopb2o1cVn42zbydKjt5oB0bNca9EftyjLmwVk8Q",
    base_url = "https://api.moonshot.cn/v1",
)
    st.session_state["messages2"] .append({"role": "user", "content": content+prompt})
    st.chat_message("user").write(prompt)
    

    # 流式输出
    stream = client.chat.completions.create(model="moonshot-v1-8k", messages=st.session_state["messages2"] ,temperature=0.2,stream=True)

    full_stream=st.chat_message("assistant").write_stream(stream)
    
    # 保存流式传输结果

    st.session_state["messages2"] .append({"role": "assistant", "content": full_stream})
